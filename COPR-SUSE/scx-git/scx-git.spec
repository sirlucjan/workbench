%define _disable_source_fetch 0
%define _lto_cflags %{nil}
%define libbpf_min_ver 1.4
%define llvm_min_ver 17
%global _default_patch_fuzz 2
%global commitdate 20251103
%global commit 6889f4a1e249ec84ab2e15f2429cd81919a28366
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           scx-git
Version:        1.0.17.%{commitdate}.git.%{shortcommit}
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
cargo build \
     --release \
     --frozen \
     --all-features \
     --workspace \
     --exclude scx_rlfifo \
     --exclude scx_mitosis \
     --exclude scx_wd40 \
     --exclude xtask \
     --exclude scxcash \
     --exclude vmlinux_docify \
     --exclude scx_arena_selftests

%install

# Install all built executables (skip .so and .d files)
find target/release \
    -maxdepth 1 -type f -executable ! -name '*.so' \
    -exec install -Dm755 -t %{buildroot}%{_bindir} {} +

%files

# Binaries
%{_bindir}/*
