%define _disable_source_fetch 0
%define _lto_cflags %{nil}
%define libbpf_min_ver 1.4
%define llvm_min_ver 17
# Packaged as upstream 1.1.4; the sources are the Seafoam Labs tag below.
%global tagver 1.1.5-devario4
# Available profiles: “release”, “release-tiny”, “release-fast“
# See: https://github.com/sched-ext/scx/blob/main/Cargo.toml
%global mode release

Name:           scx
Version:        1.1.4
Release:        2
Summary:        Sched_ext CPU schedulers
License:        GPL-2.0-only
URL:            https://github.com/sched-ext/scx
Source0:        https://github.com/Seafoam-Labs/scx/archive/refs/tags/v%{tagver}/scx-%{tagver}.tar.gz

# Not in openSUSE; built in this COPR project (needed for Rust BPF schedulers)
BuildRequires:  bpf-linker
BuildRequires:  bpftool >= 7.5.0
BuildRequires:  clang >= %{llvm_min_ver}
BuildRequires:  jq
BuildRequires:  libbpf-devel >= %{libbpf_min_ver}
BuildRequires:  lld
BuildRequires:  llvm >= %{llvm_min_ver}
BuildRequires:  pkgconfig
BuildRequires:  rust+cargo >= 1.82
BuildRequires:  rust-src
BuildRequires:  zstd
BuildRequires:  pkgconfig(libbpf) >= %{libbpf_min_ver}
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(systemd)
BuildRequires: pkgconfig(openssl)
BuildRequires: openssl-devel
Recommends: polkit
Conflicts: scx-git
Conflicts: scx-dev-git

%description
sched_ext is a Linux kernel feature which enables implementing kernel thread schedulers in BPF and dynamically loading them. This package contains various scheduler implementations and support utilities.

%prep
%autosetup -p1 -n scx-%{tagver}

%build
export CARGO_HOME=%{_builddir}/.cargo
# Rust BPF schedulers: bpfel-unknown-none has no linker in its target spec,
# so openSUSE's rustc falls back to its default linker (clang). Force
# bpf-linker; scx_rustsched_build's inner cargo inherits these.
export CARGO_TARGET_BPFEL_UNKNOWN_NONE_LINKER=bpf-linker
export CARGO_TARGET_BPFEB_UNKNOWN_NONE_LINKER=bpf-linker
cargo fetch --locked

# Toolchain versions, for the build log.
rustc -vV
bpf-linker --version

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
