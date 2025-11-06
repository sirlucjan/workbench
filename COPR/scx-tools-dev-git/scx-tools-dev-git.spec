%global _default_patch_fuzz 2
%global commitdate 20251106
%global commit 3946e99c17e1241b3b958ac715ea60aa560cd3a7
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define _disable_source_fetch 0

Name:           scx-tools-dev-git
Version:        1.0.17.%{commitdate}.git.%{shortcommit}
Release:        2%{?dist}
Summary:        Sched_ext Tools

License:        GPL=2.0
URL:            https://github.com/sched-ext/scx-loader
Source0:        %{URL}/archive/%{commit}/scx-loader-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  python
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  clang >= 17
BuildRequires:  llvm >= 17
BuildRequires:  lld >= 17
BuildRequires:  systemd
BuildRequires:  bpftool
BuildRequires:  libseccomp-devel
Requires:  scx-scheds-git
Obsoletes: scxctl = 0.3.4
Provides: scxctl = %{version}

%description
scx_loader: A DBUS Interface for Managing sched_ext Schedulers

%prep
%autosetup -p1 -n scx-loader-%{commit}

%build
export CARGO_HOME=%{_builddir}/.cargo
cargo fetch --locked
cargo build \
     --release \
     --frozen \
     --all-features \
     --workspace \
     --exclude xtask

%install

# Install all built executables (skip .so and .d files)
find target/release \
    -maxdepth 1 -type f -executable ! -name '*.so' \
    -exec install -Dm755 -t %{buildroot}%{_bindir} {} +

# Install runtime assets via xtask
# (systemd units, D-Bus services, configs, sample files)
cargo xtask install --destdir %{buildroot}

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
