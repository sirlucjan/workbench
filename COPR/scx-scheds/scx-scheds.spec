%define _disable_source_fetch 0

Name:           scx-scheds
Version:        1.0.16
Release:        12%{?dist}
Summary:        Sched_ext Schedulers and Tools

License:        GPL=2.0
URL:            https://github.com/sched-ext/scx
Source0:        %{URL}/archive/refs/tags/v%{version}.tar.gz

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
Conflicts: scx-scheds-git
Conflicts: scx_layered
Conflicts: scx_rustland
Conflicts: scx_rusty
Conflicts: rust-scx_utils-devel
Obsoletes: scxctl = 0.3.4
Provides: scx_layered
Provides: scx_rustland
Provides: scx_rusty
Provides: rust-scx_utils-devel
Provides: scxctl = %{version}

%description
sched_ext is a Linux kernel feature which enables implementing kernel thread schedulers in BPF and dynamically loading them. This repository contains various scheduler implementations and support utilities.

%prep
%autosetup -n scx-%{version}

%build
export CARGO_HOME=%{_builddir}/.cargo
cargo fetch --locked
cargo build \
     --release \
     --locked \
     --frozen \
     --workspace \
     --exclude scx_rlfifo \
     --exclude scx_mitosis \
     --exclude scx_wd40 \
     --exclude scxcash \
     --exclude vmlinux_docify \
     --exclude scx_lib_selftests

%install

# Install all built executables (skip .so and .d files)
find target/release \
    -maxdepth 1 -type f -executable ! -name '*.so' \
    -exec install -Dm755 -t %{buildroot}%{_bindir} {} +

# Install systemd service files
install -Dm644 services/systemd/scx_loader.service \
   -t %{buildroot}%{_unitdir}/

install -Dm644 services/systemd/scx.service \
   -t %{buildroot}%{_unitdir}/

# Install DBus service file
install -Dm644 services/systemd/org.scx.Loader.service \
   -t %{buildroot}%{_datadir}/dbus-1/system-services/

# Install DBus configuration
install -Dm644 tools/scx_loader/org.scx.Loader.conf \
   -t %{buildroot}%{_datadir}/dbus-1/system.d/

# Install scx_loader configuration
install -Dm644 services/scx_loader.toml \
    %{buildroot}%{_datadir}/scx_loader/config.toml

# Install scx configuration
install -Dm644 services/scx \
   -t %{buildroot}%{_sysconfdir}/default/

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

