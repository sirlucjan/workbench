%define _disable_source_fetch 0
%define _version 0.13.0
%define _rpmrel 1

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

# Build against the chroot's LLVM, with the matching llvm-NN feature.
# The feature must match the LLVM linked in: bpf-linker built with llvm-21
# or llvm-22 ignores the memset()/memcpy() errors those versions' BPF
# backend reports for libcalls the runtime supplies, and one built with
# llvm-23 does not, so llvm-23 on LLVM 22 (Fedora 44) breaks Rust BPF
# schedulers with "A call to built-in function 'memset' is not supported".
export LLVM_CONFIG=llvm-config
LLVM_MAJOR=$(llvm-config --version | cut -d. -f1)
case "${LLVM_MAJOR}" in
    21|22|23) ;;
    *) echo "bpf-linker %{version} supports LLVM 21-23, found ${LLVM_MAJOR}" >&2; exit 1 ;;
esac
echo "Building bpf-linker with --features llvm-${LLVM_MAJOR}"

cargo build \
    --release \
    --locked \
    --no-default-features \
    --features llvm-${LLVM_MAJOR}

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
* Wed Nov 04 2026 Piotr Gorski <lucjan.lucjanov@gmail.com> - 0.12.0-5
- Pick the llvm-NN feature from the chroot's LLVM instead of llvm-23

* Mon Nov 02 2026 OdzioM - 0.12.0-1
- Initial package
