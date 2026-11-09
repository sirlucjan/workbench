%define _disable_source_fetch 0
%define _lto_cflags %{nil}
%define libbpf_min_ver 1.4
%define llvm_min_ver 21
%global _default_patch_fuzz 2
%global commitdate 20261109
%global commit b0fb03e7289835cf66459210c372bc421d48768b
%global revision 3
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

# Not in openSUSE; built in this COPR project (needed for Rust BPF schedulers)
BuildRequires:  bpf-linker
BuildRequires:  bpftool >= 7.5.0
BuildRequires:  clang >= %{llvm_min_ver}
BuildRequires:  jq
BuildRequires:  libbpf-devel >= %{libbpf_min_ver}
BuildRequires:  lld
BuildRequires:  llvm >= %{llvm_min_ver}
BuildRequires:  pkgconfig
# The workspace's rust-version (MSRV).
BuildRequires:  rust+cargo >= 1.91
BuildRequires:  rust-src
BuildRequires:  zstd
BuildRequires:  pkgconfig(libbpf) >= %{libbpf_min_ver}
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(systemd)
BuildRequires: pkgconfig(openssl)
BuildRequires: openssl-devel
Recommends: polkit
# Exactly one scx variant can be installed.
Conflicts: scx
Conflicts: scx-git
Provides: scx = %{version}-%{release}
# scx-tools cannot work alongside this package: never install them together.
Conflicts: scx-tools
Conflicts: scx-tools-git
Conflicts: scx-tools-dev-git
# Upgrade path: the matching scx-tools variant, up to scx-loader 1.1.3, is
# replaced by this package. The other two only conflict, so that an upgrade
# never picks a variant for them.
Obsoletes: scx-tools-dev-git < 1.1.4

%description
sched_ext is a Linux kernel feature which enables implementing kernel thread schedulers in BPF and dynamically loading them. This package contains various scheduler implementations and support utilities.

%prep
%autosetup -p1 -n scx-%{commit}

%build
export CARGO_HOME=%{_builddir}/.cargo
# Rust BPF schedulers: bpfel-unknown-none has no linker in its target spec,
# so openSUSE's rustc falls back to its default linker (clang). Force
# bpf-linker; scx_rustsched_build's inner cargo inherits these.
export CARGO_TARGET_BPFEL_UNKNOWN_NONE_LINKER=bpf-linker
export CARGO_TARGET_BPFEB_UNKNOWN_NONE_LINKER=bpf-linker
cargo fetch --locked
cargo build \
     --profile=%{mode} \
     --frozen \
     --workspace \
     --exclude scx_rlfifo \
     --exclude scx_characterize \
     --exclude vmlinux_docify \
     --exclude scx_arena_selftests \
     --exclude scx_arena_libarena_selftests

%install

# Install all built executables (skip .so and .d files)
find target/%{mode} \
    -maxdepth 1 -type f -executable ! -name '*.so' ! -name 'xtask' \
    -exec install -Dm755 -t %{buildroot}%{_bindir} {} +

# Runtime data via xtask: scx.service, /etc/default/scx,
# /usr/share/scx/catalog.json, the scxcli polkit policy.
# --source-dir keeps cargo out of %%install.
./target/%{mode}/xtask install \
    --source-dir . \
    --destdir %{buildroot} \
    --unitdir %{_unitdir} \
    --polkitdir %{_datadir}/polkit-1/actions

%files

# Binaries
%{_bindir}/*

# systemd service and configuration
%{_unitdir}/scx.service
%config(noreplace) %{_sysconfdir}/default/scx

# Scheduler catalog and the scxcli polkit policy
%dir %{_datadir}/scx
%{_datadir}/scx/catalog.json
%{_datadir}/polkit-1/actions/org.sched_ext.scxcli.policy
