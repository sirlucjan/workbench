%global _default_patch_fuzz 2
%global commitdate 20261103
%global commit 7ce3c310ed390d583ed1e3cf25c1ede818b75c60
%global revision 4
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define _disable_source_fetch 0
# Available profiles: “release”, “release-tiny”, “release-fast“
# See: https://github.com/sched-ext/scx/blob/main/Cargo.toml
%global mode release

Name:           scx-scheds-dev-git
Version:        1.1.4.%{commitdate}.%{revision}.git.%{shortcommit}
Release:        1%{?dist}
Summary:        Sched_ext Schedulers and Tools

License:        GPL=2.0
URL:            https://github.com/sched-ext/scx
Source0:        %{URL}/archive/%{commit}/scx-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  python
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  rust-src
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
# Not in Fedora; built in this COPR project (needed for Rust BPF schedulers)
BuildRequires:  bpf-linker
BuildRequires:  protobuf-compiler
BuildRequires:  libseccomp-devel
BuildRequires: openssl-devel
Requires:  elfutils-libelf
Requires:  libseccomp
Requires:  protobuf
Requires:  zlib
Requires:  jq
Recommends: polkit
Conflicts: scx-scheds
Conflicts: scx-scheds-git
Conflicts: scx_layered
Conflicts: scx_rustland
Conflicts: scx_rusty
Conflicts: rust-scx_utils-devel
Provides: scx-scheds = %{version}
Provides: scx_layered
Provides: scx_rustland
Provides: scx_rusty
Provides: rust-scx_utils-devel

%description
sched_ext is a Linux kernel feature which enables implementing kernel thread schedulers in BPF and dynamically loading them. This repository contains various scheduler implementations and support utilities.

%prep
%autosetup -p1 -n scx-%{commit}

%build
export CARGO_HOME=%{_builddir}/.cargo
# Rust BPF schedulers: bpfel-unknown-none has no linker in its target spec,
# so rustc may fall back to its default linker. Force bpf-linker;
# scx_rustsched_build's inner cargo inherits these.
export CARGO_TARGET_BPFEL_UNKNOWN_NONE_LINKER=bpf-linker
export CARGO_TARGET_BPFEB_UNKNOWN_NONE_LINKER=bpf-linker
cargo fetch --locked

# Toolchain versions, for the build log.
rustc -vV
bpf-linker --version

# Rust BPF schedulers (those built through scx_rustsched_build) need the
# BPF backend of LLVM >= 23: LLVM 22 (Fedora 44) rejects the memset() LLVM
# emits for zeroed structs. Leave them out there instead of failing.
# rustc and bpf-linker both use the system LLVM; llvm-config is not in the
# buildroot (llvm-devel), so take the version from rustc.
LLVM_MAJOR=$(rustc -vV | sed -n 's/^LLVM version: \([0-9]*\).*/\1/p')
RUST_BPF_EXCLUDE=""
if [ "${LLVM_MAJOR:-0}" -lt 23 ]; then
    for toml in $(grep -rl --include=Cargo.toml 'scx_rustsched_build' scheds); do
        pkg=$(sed -n 's/^name *= *"\(.*\)"/\1/p' "$toml" | head -n1)
        [ -n "$pkg" ] && RUST_BPF_EXCLUDE="$RUST_BPF_EXCLUDE --exclude $pkg"
    done
    echo "LLVM ${LLVM_MAJOR} < 23, skipping Rust BPF schedulers:$RUST_BPF_EXCLUDE"
fi

cargo build \
     --profile=%{mode} \
     --frozen \
     --workspace \
     --exclude scx_rlfifo \
     --exclude scx_characterize \
     --exclude vmlinux_docify \
     --exclude scx_arena_selftests \
     --exclude scx_arena_libarena_selftests \
     $RUST_BPF_EXCLUDE

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
