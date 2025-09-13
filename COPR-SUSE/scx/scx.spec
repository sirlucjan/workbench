%define _disable_source_fetch 0
%define _lto_cflags %{nil}
%define libbpf_min_ver 1.4
%define llvm_min_ver 17
Name:           scx
Version:        1.0.16
Release:        3
Summary:        Sched_ext CPU schedulers
License:        GPL-2.0-only
URL:            https://github.com/sched-ext/scx
Source0:        %{URL}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  bpftool >= 7.5.0
BuildRequires:  clang >= %{llvm_min_ver}
BuildRequires:  jq
BuildRequires:  libbpf-devel >= %{libbpf_min_ver}
BuildRequires:  lld
BuildRequires:  llvm >= %{llvm_min_ver}
BuildRequires:  meson >= 1.2.0
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  rust+cargo >= 1.82
BuildRequires:  zstd
BuildRequires:  pkgconfig(libbpf) >= %{libbpf_min_ver}
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(systemd)

%description
sched_ext is a Linux kernel feature which enables implementing kernel thread schedulers in BPF and dynamically loading them. This package contains various scheduler implementations and support utilities.

%prep
%autosetup -n scx-%{version}

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
