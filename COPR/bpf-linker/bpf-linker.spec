%define _disable_source_fetch 0
%define _version 0.12.0
%define _rpmrel 4

%global _description %{expand:
bpf-linker is a BPF static linker. It links multiple BPF object
files and LLVM bitcode files together, with optional optimizations
for targeting older and more restrictive kernels.
}

Name:           bpf-linker
Version:        %{_version}
Release:        %{_rpmrel}%{?dist}
Summary:        Static linker for BPF programs

License:        MIT OR Apache-2.0
URL:            https://github.com/aya-rs/bpf-linker
Source0:        https://github.com/aya-rs/bpf-linker/archive/refs/tags/v%{version}/bpf-linker-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  curl
BuildRequires:  tar
BuildRequires:  llvm-devel
BuildRequires:  llvm-libs
BuildRequires:  zlib-devel
BuildRequires:  clang
BuildRequires:  chrpath

%description
%{_description}

%prep
%autosetup -n bpf-linker-%{version}

%build
# Install an isolated Rust toolchain for the build.
export RUSTUP_HOME="%{_builddir}/.rustup"
export CARGO_HOME="%{_builddir}/.cargo"
export PATH="${CARGO_HOME}/bin:${PATH}"

curl --retry 5 --retry-delay 5 -sSf \
    https://static.rust-lang.org/rustup/dist/%{_arch}-unknown-linux-gnu/rustup-init \
    -o rustup-init

chmod +x rustup-init

./rustup-init -y \
    --profile minimal \
    --default-toolchain stable \
    --no-modify-path

# Use Fedora's LLVM 23.
export LLVM_CONFIG=llvm-config

cargo build \
    --release \
    --locked \
    --no-default-features \
    --features llvm-23

%install
install -Dpm0755 target/release/bpf-linker \
    %{buildroot}%{_bindir}/bpf-linker

# Remove the redundant standard RUNPATH.
chrpath -d %{buildroot}%{_bindir}/bpf-linker

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{_bindir}/bpf-linker

%changelog
* Mon Nov 02 2026 OdzioM - 0.12.0-1
- Initial package
