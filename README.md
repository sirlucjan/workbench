# 🛠️ Workbench

A collection of useful tools, configurations, and Linux-related packages.

---

## 📂 DOTS

**gitconfig** inspired by [pksunkara](https://gist.github.com/pksunkara/988716).
Available versions for **nano**, **vim**, **VS Code**, and **Codium** (also in Flatpak builds).

---

## 🧩 Kernels & Modules

### 🔹 linux-lqx

* Kernel variant based on the **Liquorix patchset** authored by [Steven Barrett](https://github.com/damentz/liquorix-package/tree/6.17/master).
* Packaging status:
  [![Packaging status](https://repology.org/badge/vertical-allrepos/linux-lqx.svg)](https://repology.org/project/linux-lqx/versions)
  [![Latest packaged version(s)](https://repology.org/badge/latest-versions/linux-lqx.svg)](https://repology.org/project/linux-lqx/versions)

---

### 🔹 linux-rolling-stable

These sources are not fundamentally different from **archlinux-lucjan** [1] and **POLAUR** [2].
The main difference: when upgrading the kernel version, there is **no need to switch branches manually** — the build process will handle it automatically.

* [1] **archlinux-lucjan** [GitHub](https://github.com/archlinux-lucjan) · [GitLab](https://gitlab.com/archlinux-lucjan) · [Codeberg](https://codeberg.org/archlinux-lucjan)
* [2] **POLAUR** [GitHub](https://github.com/polaur) · [GitLab](https://gitlab.com/polaur)

---

## 📦 COPR (openSUSE Tumbleweed)

Packages are also available for **openSUSE** via COPR:
👉 [sirlucjan/scx-scheds-suse](https://copr.fedorainfracloud.org/coprs/sirlucjan/scx-scheds-suse/packages/)

These packages differ from openSUSE builds:

* fully compiled with **Cargo** (instead of Meson used in openSUSE specs),
* include **[scx-manager](https://github.com/CachyOS/scx-manager)** — a tool for managing schedulers in GUI.
* provides full support for scx_loader and scxctl

To add the repository manually (example for openSUSE Tumbleweed):

```bash
cd /etc/zypp/repos.d/
sudo wget https://copr.fedorainfracloud.org/coprs/sirlucjan/scx-scheds-suse/repo/opensuse-tumbleweed/sirlucjan-scx-scheds-suse-opensuse-tumbleweed.repo
```

Then install the packages:

```bash
sudo zypper refresh
sudo zypper install scx scx-manager scx-tools
```

You can also install -git version of scx:

```bash
sudo zypper refresh
sudo zypper install scx-git scx-tools-git
```

📖 Usage guide available in the [CachyOS wiki](https://wiki.cachyos.org/configuration/sched-ext/).

---

## ⬇️ Download

```bash
git clone https://github.com/sirlucjan/workbench.git
```

or:

```bash
git clone https://gitlab.com/sirlucjan/workbench.git
```

or:

```bash
git clone https://codeberg.org/sirlucjan/workbench.git
```

---

## ⚙️ Installation

```bash
cd /path/to/workbench/package_name
makepkg -srci
```

---
