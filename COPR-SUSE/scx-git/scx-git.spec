%define _disable_source_fetch 0
%define _lto_cflags %{nil}
%define libbpf_min_ver 1.4
%define llvm_min_ver 17
%global _default_patch_fuzz 2
%global commitdate 20250929
%global commit 969cd35e252c9f09b32b0bea699f7c4c88773f49
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           scx-git
Version:        1.0.16.%{commitdate}.git.%{shortcommit}
Release:        1
Summary:        Sched_ext CPU schedulers
License:        GPL-2.0-only
URL:            https://github.com/sched-ext/scx
Source0:        %{URL}/archive/%{commit}/scx-%{commit}.tar.gz

BuildRequires:  bpftool >= 7.5.0
BuildRequires:  clang >= %{llvm_min_ver}
BuildRequires:  jq
BuildRequires:  libbpf-devel >= %{libbpf_min_ver}
BuildRequires:  lld
BuildRequires:  llvm >= %{llvm_min_ver}
BuildRequires:  pkgconfig
BuildRequires:  rust+cargo >= 1.82
BuildRequires:  zstd
BuildRequires:  pkgconfig(libbpf) >= %{libbpf_min_ver}
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(systemd)
Conflicts: scx
Provides: scx = %{version}

%description
sched_ext is a Linux kernel feature which enables implementing kernel thread schedulers in BPF and dynamically loading them. This package contains various scheduler implementations and support utilities.

%prep
%autosetup -p1 -n scx-%{commit}

%build
export CARGO_HOME=%{_builddir}/.cargo
cargo fetch --locked
cargo build --release --frozen --locked

%install

# Install all built executables (skip .so and .d files)
find target/release \
    -maxdepth 1 -type f -executable ! -name '*.so' \
    -exec install -Dm755 -t %{buildroot}%{_bindir} {} +

# Install systemd service file
install -Dm644 services/systemd/scx_loader.service \
    %{buildroot}%{_unitdir}/scx_loader.service

# Install DBus service file
install -Dm644 services/systemd/org.scx.Loader.service \
    %{buildroot}%{_datadir}/dbus-1/system-services/org.scx.Loader.service

# Install DBus configuration
install -Dm644 tools/scx_loader/org.scx.Loader.conf \
    %{buildroot}%{_datadir}/dbus-1/system.d/org.scx.Loader.conf

# Install scx_loader configuration
install -Dm644 services/scx_loader.toml \
    %{buildroot}%{_datadir}/scx_loader/config.toml

%files

# Binaries
%{_bindir}/*

# Systemd service
%{_unitdir}/scx_loader.service

# DBus service and configuration
%{_datadir}/dbus-1/system-services/org.scx.Loader.service
%{_datadir}/dbus-1/system.d/org.scx.Loader.conf

# Configuration files
%{_datadir}/scx_loader/config.toml
