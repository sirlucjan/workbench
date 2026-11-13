%define _disable_source_fetch 0

Name:           helicoprion
Version:        0.2.0
Release:        2
Summary:        Scheduler-focused CPU benchmark for EEVDF and sched-ext

License:        MIT OR Apache-2.0
URL:            https://github.com/Seafoam-Labs/helicoprion
Source0:        %{URL}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  rust+cargo >= 1.91

%description
Scheduler-focused CPU benchmark: detects whether EEVDF or a sched-ext
scheduler is running, runs wake-up latency workloads and charts the
difference between schedulers in a self-contained HTML report.

%prep
%autosetup -n helicoprion-%{version}


%build
export CARGO_HOME=%{_builddir}/.cargo
cargo fetch --locked
cargo build --release --frozen -p helicoprion

%install
install -Dm755 target/release/helicoprion %{buildroot}%{_bindir}/helicoprion

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md

# Binaries
%{_bindir}/helicoprion
