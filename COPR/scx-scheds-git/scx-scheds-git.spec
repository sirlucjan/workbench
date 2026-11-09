%global _default_patch_fuzz 2
%global commitdate 20261109
%global commit 9344d26331bbdfbeec0e44d3cc444aed54b6a1a0
%global revision 1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define _disable_source_fetch 0
# Available profiles: “release”, “release-tiny”, “release-fast“
# See: https://github.com/sched-ext/scx/blob/main/Cargo.toml
%global mode release

Name:           scx-scheds-git
Version:        1.1.4.%{commitdate}.%{revision}.git.%{shortcommit}
Release:        1%{?dist}
Summary:        Sched_ext Schedulers and Tools

License:        GPL=2.0
URL:            https://github.com/sched-ext/scx
Source0:        %{URL}/archive/%{commit}/scx-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  python
# The workspace's rust-version (MSRV).
BuildRequires:  cargo >= 1.91
BuildRequires:  rust >= 1.91
BuildRequires:  rust-src
BuildRequires:  clang >= 21
BuildRequires:  llvm >= 21
BuildRequires:  lld >= 21
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
# Exactly one scx-scheds variant can be installed.
Conflicts: scx-scheds
Conflicts: scx-scheds-dev-git
Provides: scx-scheds = %{version}-%{release}
# The schedulers these once separate packages shipped are in this one.
Provides: scx_layered = %{version}-%{release}
Obsoletes: scx_layered < %{version}-%{release}
Provides: scx_rustland = %{version}-%{release}
Obsoletes: scx_rustland < %{version}-%{release}
Provides: scx_rusty = %{version}-%{release}
Obsoletes: scx_rusty < %{version}-%{release}
# scx-tools cannot work alongside this package: never install them together.
Conflicts: scx-tools
Conflicts: scx-tools-git
Conflicts: scx-tools-dev-git
# Upgrade path: the matching scx-tools variant, up to scx-loader 1.1.3, is
# replaced by this package. The other two only conflict, so that an upgrade
# never picks a variant for them.
Obsoletes: scx-tools-git < 1.1.4

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
