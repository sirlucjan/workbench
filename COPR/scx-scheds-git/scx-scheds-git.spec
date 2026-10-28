%global _default_patch_fuzz 2
%global commitdate 20261029
%global commit 5b0795a4d63b3c1ff2d4e8b401c5544c1a4652a1
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
BuildRequires:  cargo
BuildRequires:  rust
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
