%define _disable_source_fetch 0
%define _lto_cflags %{nil}
%define libbpf_min_ver 1.4
%define llvm_min_ver 17
%global _default_patch_fuzz 2
%global commitdate 20251112
%global commit 9540243d9d95570f5c7e56bf0fc8d456cc0cb585
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           scx-tools-git
Version:        1.0.18.%{commitdate}.git.%{shortcommit}
Release:        1
Summary:        Sched_ext Tools
License:        GPL-2.0-only
URL:            https://github.com/sched-ext/scx-loader
Source0:        %{URL}/archive/%{commit}/scx-loader-%{commit}.tar.gz

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
Requires:  scx-git

%description
scx_loader: A DBUS Interface for Managing sched_ext Schedulers

%prep
%autosetup -p1 -n scx-loader-%{commit}

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
