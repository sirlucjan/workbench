%define _disable_source_fetch 0
%define _lto_cflags %{nil}
%define libbpf_min_ver 1.4
%define llvm_min_ver 17

Name:           scx-tools
Version:        1.0.18
Release:        1
Summary:        Sched_ext Tools
License:        GPL-2.0-only
URL:            https://github.com/sched-ext/scx-loader
Source0:        %{URL}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  bpftool >= 7.5.0
BuildRequires:  clang >= %{llvm_min_ver}
BuildRequires:  libbpf-devel >= %{libbpf_min_ver}
BuildRequires:  lld
BuildRequires:  llvm >= %{llvm_min_ver}
BuildRequires:  pkgconfig
BuildRequires:  rust+cargo >= 1.82
BuildRequires:  zstd
BuildRequires:  pkgconfig(libbpf) >= %{libbpf_min_ver}
BuildRequires:  pkgconfig(systemd)
Requires:  scx

%description
scx_loader: A DBUS Interface for Managing sched_ext Schedulers

%prep
%autosetup -n scx-%{version}

%build
export CARGO_HOME=%{_builddir}/.cargo
cargo fetch --locked
cargo build --release --frozen --all-features --workspace

%install

# Install all built executables (skip .so and .d files)
find target/release \
    -maxdepth 1 -type f -executable ! -name '*.so' ! -name 'xtask' \
    -exec install -Dm755 -t %{buildroot}%{_bindir} {} +

# Install runtime assets via xtask
# (systemd units, D-Bus services, configs, sample files)
./target/release/xtask install --destdir %{buildroot}

%files

# Binaries
%{_bindir}/*

# Systemd service
%{_unitdir}/scx_loader.service

# DBus service and configuration
%{_datadir}/dbus-1/system-services/org.scx.Loader.service
%{_datadir}/dbus-1/system.d/org.scx.Loader.conf

# Polkit authorization policy for scx-loader
%{_datadir}/polkit-1/actions/org.scx.Loader.policy

# Configuration files
%{_datadir}/scx_loader/config.toml
