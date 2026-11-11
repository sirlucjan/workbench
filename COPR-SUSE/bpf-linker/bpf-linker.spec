%define _version 0.13.0
%define _rpmrel 1
%define llvm_major 23

%global _description %{expand:
bpf-linker is a BPF static linker. It links multiple BPF object
files and LLVM bitcode files together, with optional optimizations
for targeting older and more restrictive kernels.
}

Name:           bpf-linker
Version:        %{_version}
Release:        %{_rpmrel}%{?dist}
Summary:        Static linker for BPF programs

License:        Apache-2.0 OR MIT
URL:            https://github.com/aya-rs/bpf-linker
Source0:        https://github.com/aya-rs/bpf-linker/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  chrpath
BuildRequires:  clang%{llvm_major}
BuildRequires:  curl
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libzstd-devel
BuildRequires:  llvm%{llvm_major}-devel
BuildRequires:  make
BuildRequires:  tar
BuildRequires:  zlib-devel

%description
%{_description}

%prep
%autosetup -n %{name}-%{version}

%build
# Install an isolated Rust toolchain for the build
# (requires "Enable internet access during builds" in COPR).
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

# bpf-linker's .cargo/config.toml sets linker = "clang", but openSUSE's
# clang%{llvm_major} only ships versioned binaries (clang-%{llvm_major}).
# Provide unversioned shims pointing at the requested LLVM version.
mkdir -p .shims
for tool in clang clang++; do
    ln -sf "$(command -v ${tool}-%{llvm_major})" .shims/${tool}
done
export PATH="${PWD}/.shims:${PATH}"
clang --version

# openSUSE ships versioned LLVM; prefer llvm-config-<major>.
export LLVM_CONFIG="$(command -v llvm-config-%{llvm_major} || command -v llvm-config)"

cargo build \
    --release \
    --locked \
    --no-default-features \
    --features llvm-%{llvm_major}

%install
install -Dpm0755 target/release/%{name} \
    %{buildroot}%{_bindir}/%{name}

# Remove the redundant standard RUNPATH, if any.
chrpath -d %{buildroot}%{_bindir}/%{name} || :

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{_bindir}/%{name}

%changelog
* Mon Nov 02 2026 Piotr Gorski <lucjan.lucjanov@gmail.com> - 0.12.0-2
- Provide unversioned clang/clang++ shims for the hardcoded cargo linker

* Mon Nov 02 2026 Piotr Gorski <lucjan.lucjanov@gmail.com> - 0.12.0-1
- Initial openSUSE package for COPR
