## W O R K B E N C H

#### DOTS

gitconfig based on [pksunkara](https://gist.github.com/pksunkara/988716)
Versions for nano/vim/code/codium (code and codium also in flatpak version)

# Kernels and modules:

- linux-lqx

[![Packaging status](https://repology.org/badge/vertical-allrepos/linux-lqx.svg)](https://repology.org/project/linux-lqx/versions)

#### linux-lqx incorporates:

* [liquorix patchset](https://github.com/damentz/liquorix-package/tree/6.16/master) - authored by Steven Barrett

[![latest packaged version(s)](https://repology.org/badge/latest-versions/linux-lqx.svg)](https://repology.org/project/linux-lqx/versions)

#### linux-rolling-stable

###### These sources are not fundamentally different from those available in the archlinux-lucjan [1] and POLAUR repository [2]. 

###### The only difference is that if you change the kernel version to a higher one, there will be no need to change the branch in the sources section - the new version will compile automatically.

[1] * [archlinux-lucjan](https://github.com/archlinux-lucjan) / [archlinux-lucjan](https://gitlab.com/archlinux-lucjan) / [archlinux-lucjan](https://codeberg.org/archlinux-lucjan)

[2] * [POLAUR](https://github.com/polaur) / [POLAUR](https://gitlab.com/polaur)

#### COPR

###### scx-scheds will soon drop meson. Here you will find a test version compiled in cargo.

First, enable the [COPR](https://copr.fedorainfracloud.org/coprs/sirlucjan/scx-scheds-cargo/) repository hosting addon package.

```
sudo dnf copr enable sirlucjan/scx-scheds-cargo
```

or for Fedora Silverblue/Kinoite

```
cd /etc/yum.repos.d/
sudo wget https://copr.fedorainfracloud.org/coprs/sirlucjan/scx-scheds-cargo/repo/fedora-$(rpm -E %fedora)/sirlucjan-scx-scheds-cargo-$(rpm -E %fedora).repo
```

Then you can install scx-scheds:

```
sudo dnf install scx-scheds
```

or for Fedora Silverblue/Kinoite

```
sudo rpm-ostree install scx-scheds
sudo systemctl reboot

```

You can also use -git version:

```
sudo dnf install scx-scheds-git
```

or for Fedora Silverblue/Kinoite

```
sudo rpm-ostree install scx-scheds-git
sudo systemctl reboot

```


You can learn how to use scx-scheds from [this](https://wiki.cachyos.org/configuration/sched-ext/) wiki.

***
# Download:

```
git clone https://github.com/sirlucjan/workbench.git

```

or

```
git clone https://gitlab.com/sirlucjan/workbench.git

```
or

```
git clone https://codeberg.org/sirlucjan/workbench.git

```

# Install:


```
cd /some_path/workbench/package_name
makepkg -srci

```
