# 🛠️ Workbench

A collection of useful tools, configurations, and Linux-related packages.

## Contents

- [DOTS](#dots)
- [Kernels & Modules](#kernels--modules)
  - [Devario Linux Kernel for Fedora](#devario-linux-kernel-for-fedora-regular-and-lts)
- [COPR repositories](#copr-repositories)
  - [Fedora: scx-scheds](#fedora-scx-scheds-fedora-4445rawhide-including-silverblue-and-kinoite)
  - [openSUSE Tumbleweed: scx](#opensuse-tumbleweed-scx)
- [Download](#download)
- [Installation](#installation)
- [Cargo build profiles](#cargo-build-profiles-fedora--opensuse)

---

## DOTS

**gitconfig** inspired by [pksunkara](https://gist.github.com/pksunkara/988716).
Available versions for **Codium** and **Codium Insiders**

---

## Kernels & Modules

### linux-lqx (PDS and BMQ versions)

* Kernel variant based on the **Liquorix patchset** authored by [Steven Barrett](https://github.com/damentz/liquorix-package/tree/7.3/master).
* Packaging status:
  [![Packaging status](https://repology.org/badge/vertical-allrepos/linux-lqx.svg)](https://repology.org/project/linux-lqx/versions)
  [![Latest packaged version(s)](https://repology.org/badge/latest-versions/linux-lqx.svg)](https://repology.org/project/linux-lqx/versions)

### Devario Linux Kernel for Fedora (regular and LTS)

Fedora packages of the **Devario Linux kernel**, maintained by
[Seafoam Labs](https://github.com/Seafoam-Labs/linux), are available as
regular and LTS kernel tracks.

- **Regular:** Linux **7.3** series in the documented packaging tree.
- **LTS:** Linux **6.18** long-term series.

The kernel is maintained as a separate source tree with a curated selection
of fixes and optimizations, including patches originating from CachyOS.
Its priority is predictable behavior, hardware support, regression fixes,
and `sched_ext` compatibility rather than a broad experimental performance
patch stack. Actual RPM versions and Fedora release availability depend on
the latest successful COPR builds.

#### Features and policy

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

#### CPU requirements

The published Devario Fedora builds described here target **x86-64-v3**.
Check that your processor supports it before installing:

```bash
/lib64/ld-linux-x86-64.so.2 --help | grep 'x86-64-v3'
```

Look for a `supported` indication. The requirement applies to the kernel
binary itself; older x86-64 CPUs may not boot these builds.

#### Installation

##### Fedora Workstation and other DNF-based editions

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

##### Fedora Silverblue / Kinoite (rpm-ostree)

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

#### Choosing the default kernel

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

#### sched-ext compatibility

Devario kernels support the `sched_ext` framework. Scheduler packages and
installation instructions are documented in [Fedora: scx-scheds](#fedora-scx-scheds).
The current workflow uses `scx.service`, `scxcli`, and `scxtui` instead of
`scx_loader`/`scxctl`:

```bash
scxcli list
scxcli get
systemctl status scx.service
```

A discovered scheduler is not necessarily compatible with every kernel. If
launching one fails, inspect `journalctl -u scx.service`.

#### Sources, credits and license

- Kernel source: https://github.com/Seafoam-Labs/linux
- Regular source branch: https://github.com/Seafoam-Labs/linux/tree/7.3/base
- LTS source branch: https://github.com/Seafoam-Labs/linux/tree/6.18/base
- Kernel source releases: https://github.com/Seafoam-Labs/linux/releases
- Arch/Devario packaging: https://github.com/Seafoam-Labs/devario-custom-packagbuilds
- Fedora kernel COPR: https://copr.fedorainfracloud.org/coprs/sirlucjan/kernel-devario/

The Devario kernel incorporates selected patches and optimizations from the
[CachyOS kernel](https://github.com/CachyOS/linux-cachyos). Credit goes to
**Peter Jung (ptr1337), Eric Naim, Vasiliy Stelmachenok**, other CachyOS
contributors, and the upstream Linux kernel developers. Devario maintains its
own kernel tree, source releases, and distribution packages.

The Linux kernel is licensed under `GPL-2.0-only`, subject to the licenses
of the individual components in its source tree.

---

## COPR repositories

### Fedora: scx-scheds (Fedora 44/45/Rawhide, including Silverblue and Kinoite)

The **scx-scheds** packages in this Fedora COPR are built with **Cargo** from
[Seafoam Labs internal releases](https://github.com/Seafoam-Labs/scx/tags).
These releases (`v1.1.5-devarioN` tags) are snapshots taken directly from the
upstream [`sched-ext/scx` `main` branch](https://github.com/sched-ext/scx),
without additional downstream commits or patches. They provide fixed integration
points for Devario's desktop environment, rather than a separate development fork
or a guarantee of stability.

**Note:** `scx_loader` is no longer provided by this COPR. For scheduler
management, use `scx.service`, `scxcli`, or `scxtui` instead.

1. Enable the [COPR](https://copr.fedorainfracloud.org/coprs/sirlucjan/scx-scheds-cargo/) repository:

   ```bash
   sudo dnf copr enable sirlucjan/scx-scheds-cargo
   ```

   **For Fedora Silverblue / Kinoite:**

   ```bash
   cd /etc/yum.repos.d/
   sudo wget https://copr.fedorainfracloud.org/coprs/sirlucjan/scx-scheds-cargo/repo/fedora-$(rpm -E %fedora)/sirlucjan-scx-scheds-cargo-$(rpm -E %fedora).repo
   ```

2. Install `scx-scheds`:

   ```bash
   sudo dnf install scx-scheds
   ```

   **For Fedora Silverblue / Kinoite:**

   ```bash
   sudo rpm-ostree install scx-scheds
   sudo systemctl reboot
   ```

3. Install the `scx-scheds-git` version:

   ```bash
   sudo dnf install scx-scheds-git
   ```

   **For Fedora Silverblue / Kinoite:**

   ```bash
   sudo rpm-ostree install scx-scheds-git
   sudo systemctl reboot
   ```
   
Additional sched-ext background: [CachyOS wiki](https://wiki.cachyos.org/configuration/sched-ext/).

---

### openSUSE Tumbleweed: scx

The **scx** packages are built with **Cargo** from the same
[Seafoam Labs internal release snapshots](https://github.com/Seafoam-Labs/scx/tags)
used for Fedora. They are unmodified upstream `main` checkpoints for Devario
integration, not independently guaranteed stable releases.

**Note:** `scx_loader` is no longer provided by this COPR. For scheduler
management, use `scx.service`, `scxcli`, or `scxtui` instead.

Packages are available via COPR:
👉 [sirlucjan/scx-scheds-suse](https://copr.fedorainfracloud.org/coprs/sirlucjan/scx-scheds-suse/packages/)

To add the repository manually (example for openSUSE Tumbleweed):

```bash
cd /etc/zypp/repos.d/
sudo wget https://copr.fedorainfracloud.org/coprs/sirlucjan/scx-scheds-suse/repo/opensuse-tumbleweed/sirlucjan-scx-scheds-suse-opensuse-tumbleweed.repo
```

Then install the packages:

```bash
sudo zypper refresh
sudo zypper install scx
```

You can also install -git version of scx:

```bash
sudo zypper refresh
sudo zypper install scx-git
```

Additional sched-ext background: [CachyOS wiki](https://wiki.cachyos.org/configuration/sched-ext/).

---

## Download

```bash
git clone https://github.com/sirlucjan/workbench.git
```

---

## Installation

```bash
cd /path/to/workbench/package_name
makepkg -srci
```

---

## Cargo build profiles (Fedora & openSUSE)

Both the Fedora and openSUSE builds support selecting one of three Cargo build profiles, defined upstream in:

- **scx-scheds:** [upstream Cargo.toml](https://github.com/sched-ext/scx/blob/main/Cargo.toml)

Available profiles:

- **release** – default optimized profile  
- **release-tiny** – minimized binary size, no LTO, stripped symbols
- **release-fast** – faster builds, no LTO, more codegen units

Select one of the appropriate options here

```bash
%global mode release
```
The default option is `release`

---

### Profile definitions

```toml
[profile.release]
lto = "thin"

[profile.release-tiny]
inherits = "release"
opt-level = "z"
lto = false
codegen-units = 1
strip = true
panic = "abort"

[profile.release-fast]
inherits = "release"
lto = false
codegen-units = 32
panic = "abort"
```

---

### Explanation of each option

- **lto = "thin"**  
  Enables LLVM ThinLTO — lightweight LTO with good performance‑to‑size ratio.

- **lto = false**  
  Disables LTO for the fastest possible builds.

- **strip = true**  
  Strips symbols to reduce binary size.

- **codegen-units = 32**
  Allows more parallel code generation, usually trading optimization for build speed.

- **inherits = "release"**  
  Inherits all settings from the main release profile.

---

### Summary

The table reflects the definitions shown above; none of these profiles sets
`incremental = true` (release profiles default to non-incremental builds).

| Profile          | LTO        | Stripping | Incremental | Use case |
|------------------|-----------|-----------|-------------|----------|
| **release**       | thin      | no        | no          | Standard optimized build |
| **release-tiny**  | disabled  | yes       | no          | Smallest binary size |
| **release-fast**  | disabled  | no        | no          | Faster builds |

