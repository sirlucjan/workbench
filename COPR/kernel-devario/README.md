# Devario Linux Kernel for Fedora

Devario Linux kernel packages for Fedora, built from the [Seafoam Labs Linux tree](https://github.com/Seafoam-Labs/linux).

Devario provides both a current kernel based on the Linux 7.2 stable series and an LTS kernel based on Linux 6.18. Both carry a curated Devario patch set focused on predictable behavior, hardware support, regression fixes, and sched-ext compatibility rather than a large experimental performance patch stack.

## Features

- Current kernel based on the Linux 7.2 stable series.
- LTS kernel based on the Linux 6.18 long-term series.
- Curated Devario kernel patch set.
- Official builds target **x86-64-v3**.
- sched-ext support.
- Selected hardware and regression fixes.
- ACS Override support.
- Additional timer-frequency options.
- Intel P-State controls.
- VHBA support.
- ADIOS I/O scheduler updates.
- TSC synchronization work.
- x86-64 ISA-level support.
- ZSTD-compressed kernel modules.

For the exact patch set included in a release, see the [Devario Linux releases](https://github.com/Seafoam-Labs/linux/releases).

## CPU requirements

Official Fedora builds target **x86-64-v3**.

Before installing, verify that your CPU supports the v3 baseline:

```bash
/lib64/ld-linux-x86-64.so.2 --help | grep "(supported, searched)"
```

A kernel built for x86-64-v3 may use instructions unavailable on older CPUs and therefore requires compatible hardware.

## Installation

### Fedora Workstation

Enable the COPR repository hosting the Devario kernel:

```bash
sudo dnf copr enable sirlucjan/kernel-devario
```

Then install either the current kernel:

```bash
sudo dnf install kernel-devario kernel-devario-devel-matched
```

or the Linux 6.18 LTS kernel:

```bash
sudo dnf install kernel-devario-lts kernel-devario-lts-devel-matched
```

Keeping Fedora's stock kernel installed as a fallback is recommended.

If SELinux prevents kernel modules from being loaded, enable the required policy:

```bash
sudo setsebool -P domain_kernel_load_modules on
```

### Fedora Silverblue / Kinoite

Enable the repository first, then replace the Fedora kernel packages with the Devario kernel:

```bash
cd /etc/yum.repos.d/
sudo wget "https://copr.fedorainfracloud.org/coprs/sirlucjan/kernel-devario/repo/fedora-$(rpm -E %fedora)/sirlucjan-kernel-devario-fedora-$(rpm -E %fedora).repo"

sudo rpm-ostree override remove \
  kernel \
  kernel-core \
  kernel-modules \
  kernel-modules-core \
  kernel-modules-extra \
  --install kernel-devario

sudo systemctl reboot
```

For the Linux 6.18 LTS kernel, use:

```bash
sudo rpm-ostree override remove \
  kernel \
  kernel-core \
  kernel-modules \
  kernel-modules-core \
  kernel-modules-extra \
  --install kernel-devario-lts

sudo systemctl reboot
```

## Setting Devario as the default kernel

Fedora normally boots the most recently updated kernel. If both the Fedora and Devario kernels are installed, a Fedora kernel update may become the default again.

You can explicitly select the latest Devario kernel with `grubby`:

```bash
sudo grubby --set-default="$(ls /boot/vmlinuz-*devario* | sort -V | tail -1)"
```

Keeping the Fedora kernel installed provides a convenient fallback if a Devario update causes problems.

## sched-ext

The kernel supports sched-ext userspace schedulers.

Seafoam/Devario-compatible sched-ext packages for Fedora are available from the dedicated COPR repository:

https://copr.fedorainfracloud.org/coprs/sirlucjan/scx-scheds-cargo/

Enable the repository and install the schedulers and loader tools with:

```bash
sudo dnf copr enable sirlucjan/scx-scheds-cargo
sudo dnf install scx-scheds scx-tools
```

`scxctl` can then be used to start, stop, and switch schedulers and profiles.

Upstream sched-ext:

https://github.com/sched-ext/scx

## Sources

- Devario Linux kernel tree: https://github.com/Seafoam-Labs/linux
- Linux 7.2 base branch: https://github.com/Seafoam-Labs/linux/tree/7.2/base
- Linux 6.18 LTS base branch: https://github.com/Seafoam-Labs/linux/tree/6.18/base
- Devario Linux releases: https://github.com/Seafoam-Labs/linux/releases
- Devario packaging: https://github.com/Seafoam-Labs/devario-custom-packagbuilds
- Fedora kernel COPR: https://copr.fedorainfracloud.org/coprs/sirlucjan/kernel-devario/
- Fedora sched-ext COPR: https://copr.fedorainfracloud.org/coprs/sirlucjan/scx-scheds-cargo/
- Seafoam Labs: https://github.com/Seafoam-Labs

## License

The Linux kernel is licensed under `GPL-2.0-only`.
