%global _default_patch_fuzz 2
%global commitdate 20250909
%global commit 0a66117570bda64d903a76e6bc1e84549be9c966
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define _disable_source_fetch 0

Name:           scx-scheds-git
Version:        1.0.16.%{commitdate}.git.%{shortcommit}
Release:        5%{?dist}
Summary:        Sched_ext Schedulers and Tools

License:        GPL=2.0
URL:            https://github.com/sched-ext/scx
Source0:        %{URL}/archive/%{commit}/scx-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  python
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  clang >= 17
BuildRequires:  llvm >= 17
BuildRequires:  lld >= 17
BuildRequires:  elfutils-libelf
BuildRequires:  elfutils-libelf-devel
BuildRequires:  zlib
BuildRequires:  jq
BuildRequires:  jq-devel
BuildRequires:  systemd
BuildRequires:  bpftool
BuildRequires:  protobuf-compiler
BuildRequires:  libseccomp-devel
Requires:  elfutils-libelf
Requires:  libseccomp
Requires:  protobuf
Requires:  zlib
Requires:  jq
Obsoletes: scxctl = 0.3.4
Conflicts: scx-scheds
Conflicts: scx_layered
Conflicts: scx_rustland
Conflicts: scx_rusty
Conflicts: rust-scx_utils-devel
Provides: scx-scheds = %{version}
Provides: scxctl = %{version}
Provides: scx_layered
Provides: scx_rustland
Provides: scx_rusty
Provides: rust-scx_utils-devel

%description
sched_ext is a Linux kernel feature which enables implementing kernel thread schedulers in BPF and dynamically loading them. This repository contains various scheduler implementations and support utilities.

%prep
%autosetup -p1 -n scx-%{commit}

%build
export CARGO_HOME=%{_builddir}/.cargo
cargo fetch --locked
cargo build --release --frozen --locked

%install

# Install binary files (all executables except *.so)
find target/release -maxdepth 1 -type f -executable ! -name '*.so' \
    -exec install -Dm755 -t %{buildroot}/usr/bin {} +

# Install systemd service files
install -Dm644 services/systemd/scx_loader.service \
    %{buildroot}/usr/lib/systemd/system/scx_loader.service

install -Dm644 services/systemd/scx.service \
    %{buildroot}/usr/lib/systemd/system/scx.service

# Install DBus service file
install -Dm644 services/systemd/org.scx.Loader.service \
    %{buildroot}/usr/share/dbus-1/system-services/org.scx.Loader.service

# Install DBus configuration
install -Dm644 tools/scx_loader/org.scx.Loader.conf \
    %{buildroot}/usr/share/dbus-1/system.d/org.scx.Loader.conf

# Install scx_loader configuration
install -Dm644 services/scx_loader.toml \
    %{buildroot}/usr/share/scx_loader/config.toml

# Install scx configuration
install -Dm644 services/scx \
    %{buildroot}/etc/default/scx

%files

# Binaries
%{_bindir}/*

# Systemd services
%{_unitdir}/scx_loader.service
%{_unitdir}/scx.service

# DBus service and configuration
%{_datadir}/dbus-1/system-services/org.scx.Loader.service
%{_datadir}/dbus-1/system.d/org.scx.Loader.conf

# Configuration files
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/default/scx
%{_datadir}/scx_loader/config.toml
