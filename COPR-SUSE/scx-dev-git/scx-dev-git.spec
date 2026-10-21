%define _disable_source_fetch 0
%define _lto_cflags %{nil}
%define libbpf_min_ver 1.4
%define llvm_min_ver 17
%global _default_patch_fuzz 2
%global commitdate 20261021
%global commit c9b0ee0bfe8973e0120e7ffb87afc645ad866177
%global revision 2
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Available profiles: “release”, “release-tiny”, “release-fast“
# See: https://github.com/sched-ext/scx/blob/main/Cargo.toml
%global mode release

Name:           scx-dev-git
Version:        1.1.4.%{commitdate}.%{revision}.git.%{shortcommit}
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
BuildRequires: pkgconfig(openssl)
BuildRequires: openssl-devel
Conflicts: scx
Conflicts: scx-git
Provides: scx = %{version}

%description
sched_ext is a Linux kernel feature which enables implementing kernel thread schedulers in BPF and dynamically loading them. This package contains various scheduler implementations and support utilities.

%prep
%autosetup -p1 -n scx-%{commit}

%build
export CARGO_HOME=%{_builddir}/.cargo
cargo fetch --locked
cargo build \
     --profile=%{mode} \
     --frozen \
     --workspace \
     --exclude scx_rlfifo \
     --exclude xtask \
     --exclude scx_characterize \
     --exclude vmlinux_docify \
     --exclude scx_arena_selftests \
     --exclude scx_arena_libarena_selftests

%install

# Install all built executables (skip .so and .d files)
find target/%{mode} \
    -maxdepth 1 -type f -executable ! -name '*.so' \
    -exec install -Dm755 -t %{buildroot}%{_bindir} {} +

# Install the upstream systemd service and default configuration
install -Dm644 services/scx.service %{buildroot}%{_unitdir}/scx.service
install -Dm644 services/scx %{buildroot}%{_sysconfdir}/default/scx

%files

# Binaries
%{_bindir}/*

# systemd service and configuration
%{_unitdir}/scx.service
%config(noreplace) %{_sysconfdir}/default/scx
