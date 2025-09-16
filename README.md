# 🛠️ Workbench

A collection of useful tools, configurations, and Linux-related packages.

---

## 📂 DOTS

**gitconfig** inspired by [pksunkara](https://gist.github.com/pksunkara/988716).
Available versions for **nano**, **vim**, **VS Code**, and **Codium** (also in Flatpak builds).

---

## 🧩 Kernels & Modules

### 🔹 linux-lqx

* Kernel variant based on the **Liquorix patchset** authored by [Steven Barrett](https://github.com/damentz/liquorix-package/tree/6.16/master).
* Packaging status:
  [![Packaging status](https://repology.org/badge/vertical-allrepos/linux-lqx.svg)](https://repology.org/project/linux-lqx/versions)
  [![Latest packaged version(s)](https://repology.org/badge/latest-versions/linux-lqx.svg)](https://repology.org/project/linux-lqx/versions)

---

### 🔹 linux-rolling-stable

These sources are not fundamentally different from **archlinux-lucjan** \[1] and **POLAUR** \[2].
The main difference: when upgrading the kernel version, there is **no need to switch branches manually** — the build process will handle it automatically.

* \[1] **archlinux-lucjan** [GitHub](https://github.com/archlinux-lucjan) · [GitLab](https://gitlab.com/archlinux-lucjan) · [Codeberg](https://codeberg.org/archlinux-lucjan)
* \[2] **POLAUR** [GitHub](https://github.com/polaur) · [GitLab](https://gitlab.com/polaur)

---

## 📦 COPR (Fedora 42 / Silverblue / Kinoite)

The **scx-scheds** project will soon [switch](https://github.com/sched-ext/scx/discussions/2731) from **Meson** to **Cargo**.
Here you can find test builds compiled in **Rust (cargo)** for **Fedora 42**.

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

📖 Usage guide available in the [CachyOS wiki](https://wiki.cachyos.org/configuration/sched-ext/).

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
sudo zypper install scx scx-manager
```

You can also install -git version of scx:

```bash
sudo zypper refresh
sudo zypper install scx-git
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
