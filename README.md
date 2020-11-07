## W O R K B E N C H

#### Kernels

###### aur-rebased

[aur-rebased](https://github.com/sirlucjan/workbench/tree/master/aur-rebased) / [aur-rebased](https://gitlab.com/sirlucjan/workbench/tree/master/aur-rebased) - linux-zen-git

###### linux-zen-git incorporates:

* [zen-kernel](https://github.com/zen-kernel/zen-kernel/tree/5.9/master) - specific patchset authored by ZEN Kernel Team

###### juliagoda-kernels

[juliagoda-kernels](https://github.com/sirlucjan/workbench/tree/master/juliagoda-kernels) / [juliagoda-kernels](https://gitlab.com/sirlucjan/workbench/tree/master/juliagoda-kernels) - linux-juliagoda-git (stable and stable-rc)

###### linux-juliagoda-git incorporates:

* [bfq improvements](https://groups.google.com/forum/#!forum/bfq-iosched) - latest fixes authored by Paolo Valente and BFQ Team

* [bfq-dev](https://github.com/Algodev-github/bfq-mq/tree/dev-bfq-on-5.6) - latest fixes authored by Paolo Valente and BFQ Team

* [bfq-dev-lucjan](https://github.com/sirlucjan/bfq-mq-lucjan/tree/dev-bfq-on-5.6-lucjan) - latest fixes authored by Paolo Valente and BFQ Team and forked by Piotr Gorski

* [bfq-dev-lucjan-rc](https://github.com/sirlucjan/kernel-patches/tree/master/5.9/bfq-dev-lucjan) / [bfq-dev-lucjan-rc](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.9/bfq-dev-lucjan) - specific patches authored by Paolo Valente and Piotr Gorski
 
* [graysky's GCC patch](https://github.com/graysky2/kernel_gcc_patch) - version for gcc 10.1

* [Project C](https://gitlab.com/alfredchen/linux-prjc/tree/linux-5.9.y-prjc) / [Project C blog](http://cchalpha.blogspot.com) - contains the newest vesion with latest fixes

* [random fixes from zen-kernel](https://github.com/zen-kernel/zen-kernel/tree/5.9/master) - specific patches authored by Jan Alexander Steffens and ZEN Kernel Team

* [random fixes from pfkernel](https://github.com/pfactum/pf-kernel/tree/pf-5.9) / [random fixes from pfkernel](https://gitlab.com/post-factum/pf-kernel/tree/pf-5.9) - for example patches from Arch Linux or specific patches authored by Oleksandr Natalenko

* [fixes from ClearLinux](https://github.com/clearlinux-pkgs/linux) - specific patches authored by ClearLinux Team

* [UKSM (sources)](https://github.com/dolohow/uksm) / [UKSM (info)](https://www.usenix.org/sites/default/files/conference/protected-files/fast18_slides_xia.pdf) - resync from dolohow’s github

* [LL-patches](https://github.com/sirlucjan/kernel-patches/tree/master/5.9/ll-patches) / [LL-patches](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.9/ll-patches) - specific patches authored by Piotr Gorski

* [LL-branding](https://github.com/sirlucjan/kernel-patches/tree/master/5.9/ll-branding) / [LL-branding](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.9/ll-branding) - specific patches authored by Piotr Gorski

###### Some patches for BFQ/block-stable conflict with patches for BFQ-dev/block-mainline.

###### To use juliagoda-kernels smoothly apply ll-reverts before linux-lucjan patch. Otherwise the kernel will not compile.

* [ll-reverts](https://github.com/sirlucjan/kernel-patches/tree/master/5.9-dev/ll-reverts) / [ll-reverts](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.9-dev/ll-reverts) - specific patches authored by Piotr Gorski

######  linux-lqx-rebranded

[linux-lqx-rebranded](https://github.com/sirlucjan/workbench/tree/master/linux-lqx-rebranded) / [linux-lqx-rebranded](https://gitlab.com/sirlucjan/workbench/tree/master/linux-lqx-rebranded) - linux-lqx-git/linux-lqx-tag/linux-lqx-tag-git

###### linux-lqx-git/linux-lqx-tag/linux-lqx-tag-git incorporates:

* [liquorix patchset](https://github.com/damentz/liquorix-package/tree/5.9/master) - authored by Steven Barrett

[![latest packaged version(s)](https://repology.org/badge/latest-versions/linux-lqx.svg)](https://repology.org/project/linux-lqx/versions)

###### linux-zen-rebranded

[linux-zen-rebranded](https://github.com/sirlucjan/workbench/tree/master/linux-zen-rebranded) / [linux-zen-rebranded](https://gitlab.com/sirlucjan/workbench/tree/master/linux-zen-rebranded) - linux-zen-tag

###### linux-zen-tag incorporates:

* [zen-kernel](https://github.com/zen-kernel/zen-kernel/tree/5.9/master) - specific patchset authored by ZEN Kernel Team

#### DOTS

gitconfig based on [pksunkara](https://gist.github.com/pksunkara/988716)
