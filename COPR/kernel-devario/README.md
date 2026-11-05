# Devario Linux Kernel for Fedora

Fedora packages of the **Devario Linux kernel**, maintained by
[Seafoam Labs](https://github.com/Seafoam-Labs/linux). These packages provide
an alternative regular kernel and an LTS kernel for Fedora systems.

- **Regular:** Linux **7.3** series in the current Devario packaging tree.
- **LTS:** Linux **6.18** long-term series.

The kernel is maintained as a separate source tree with a curated selection
of fixes and optimizations, including patches originating from CachyOS.
Its priority is predictable behavior, hardware support, regression fixes,
and `sched_ext` compatibility rather than a broad experimental performance
patch stack. Actual RPM versions and Fedora release availability depend on
the latest successful COPR builds.

## Features and policy

- An EEVDF-based Linux kernel with `sched_ext` support.
- Official builds target **x86-64-v3**.
- Selected hardware enablement, compatibility and regression fixes.
- Curated kernel patches, including selected work from CachyOS.
- Alternative timer-frequency and build-time configuration options, where
  supported by the corresponding Devario source branch.
- ZSTD-compressed modules in the Devario kernel packaging.

Features are **branch-specific**. Not every out-of-tree patch is carried by
both the regular and LTS kernels, and no benchmark gain alone guarantees that
an upstream release-candidate patch is safe to backport. Riskier changes
should be tested separately before inclusion in stable builds.

See the [Devario Linux releases](https://github.com/Seafoam-Labs/linux/releases)
for the source corresponding to a particular build.

## CPU requirements

The published Devario Fedora builds described here target **x86-64-v3**.
Check that your processor supports it before installing:

```bash
/lib64/ld-linux-x86-64.so.2 --help | grep 'x86-64-v3'
```

Look for a `supported` indication. The requirement applies to the kernel
binary itself; older x86-64 CPUs may not boot these builds.

## Installation

### Fedora Workstation and other DNF-based editions

Enable the repository:

```bash
sudo dnf copr enable sirlucjan/kernel-devario
```

Install the regular kernel and matching development package:

```bash
sudo dnf install kernel-devario kernel-devario-devel-matched
```

Or install the 6.18 LTS track:

```bash
sudo dnf install kernel-devario-lts kernel-devario-lts-devel-matched
```

The commands above use the package names from this COPR's documented
installation scheme; verify availability for your Fedora release. **Keep at
least one stock Fedora kernel** as a fallback, and test a new kernel before
removing a previously working boot option.

### Fedora Silverblue / Kinoite (rpm-ostree)

Download the repository definition for your Fedora release:

```bash
sudo curl -fL -o /etc/yum.repos.d/sirlucjan-kernel-devario.repo \
  "https://copr.fedorainfracloud.org/coprs/sirlucjan/kernel-devario/repo/fedora-$(rpm -E %fedora)/sirlucjan-kernel-devario-fedora-$(rpm -E %fedora).repo"
```

For the regular kernel, create a new deployment with an override:

```bash
sudo rpm-ostree override remove \
  kernel kernel-core kernel-modules kernel-modules-core kernel-modules-extra \
  --install kernel-devario
sudo systemctl reboot
```

For the LTS track, use `--install kernel-devario-lts` instead. These are
alternative commands, not steps to perform one after the other. Keep a
working previous deployment and consult `rpm-ostree status` before changing
or rolling back the kernel.

## Choosing the default kernel

On classic Fedora editions where `grubby` manages the boot entries, inspect
the available entries first:

```bash
sudo grubby --info=ALL
```

Select the **specific** Devario kernel image you want, rather than blindly
assuming the newest kernel is on the desired regular or LTS track:

```bash
sudo grubby --set-default /boot/vmlinuz-<selected-devario-kernel-version>
```

This `grubby` example is not intended for rpm-ostree systems.

## sched-ext

These kernels support the `sched_ext` framework for userspace CPU
schedulers. The separately maintained Fedora COPR for sched-ext is:

https://copr.fedorainfracloud.org/coprs/sirlucjan/scx-scheds-cargo/

```bash
sudo dnf copr enable sirlucjan/scx-scheds-cargo
sudo dnf install scx-scheds
```

The newer sched-ext integration uses **`scx.service`** and, in builds that
include it, **`scxtui`**. It does not require the old `scx_loader`/`scxctl`
workflow. Check the installed package contents and its version before
using these commands:

```bash
scxtui --cli list
scxtui --cli get
systemctl status scx.service
```

A discovered scheduler is not necessarily compatible with every kernel;
failed launches should be checked with `journalctl -u scx.service`.

Upstream: https://github.com/sched-ext/scx

## Sources

- Kernel source: https://github.com/Seafoam-Labs/linux
- Regular source branch: https://github.com/Seafoam-Labs/linux/tree/7.3/base
- LTS source branch: https://github.com/Seafoam-Labs/linux/tree/6.18/base
- Kernel source releases: https://github.com/Seafoam-Labs/linux/releases
- Arch/Devario packaging: https://github.com/Seafoam-Labs/devario-custom-packagbuilds
- Fedora kernel COPR: https://copr.fedorainfracloud.org/coprs/sirlucjan/kernel-devario/
- Fedora sched-ext COPR: https://copr.fedorainfracloud.org/coprs/sirlucjan/scx-scheds-cargo/

## Credits and provenance

The Devario kernel incorporates selected patches and optimizations from the
[CachyOS kernel](https://github.com/CachyOS/linux-cachyos). We acknowledge
**Peter Jung (ptr1337), Eric Naim, Vasiliy Stelmachenok**, and other CachyOS
contributors, as well as the upstream Linux kernel developers. Devario
maintains its own kernel tree, source releases and distribution packages.

## License

The Linux kernel is licensed under `GPL-2.0-only`, subject to the licenses
of the individual components included in its source tree.
