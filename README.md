## W O R K B E N C H

#### Kernels

###### aur-rebased

[aur-rebased](https://github.com/sirlucjan/workbench/tree/master/aur-rebased) / [aur-rebased](https://gitlab.com/sirlucjan/workbench/tree/master/aur-rebased) - linux-zen-git

###### linux-zen-git incorporates:

* [zen-kernel](https://github.com/zen-kernel/zen-kernel/tree/5.7/master) - specific patchset authored by ZEN Kernel Team

###### juliagoda-kernels

[juliagoda-kernels](https://github.com/sirlucjan/workbench/tree/master/juliagoda-kernels) / [juliagoda-kernels](https://gitlab.com/sirlucjan/workbench/tree/master/juliagoda-kernels) - linux-juliagoda-git (stable and stable-rc)

###### linux-juliagoda-git incorporates:

* [bfq improvements](https://groups.google.com/forum/#!forum/bfq-iosched) - latest fixes authored by Paolo Valente and BFQ Team

* [bfq-dev](https://github.com/Algodev-github/bfq-mq/tree/dev-bfq-on-5.6) - latest fixes authored by Paolo Valente and BFQ Team

* [bfq-lucjan-dev](https://github.com/sirlucjan/bfq-mq-lucjan/tree/dev-bfq-on-5.6-lucjan) - latest fixes authored by Paolo Valente and BFQ Team and forked by Piotr Gorski
 
* [graysky's GCC patch](https://github.com/graysky2/kernel_gcc_patch) - version for gcc 10.1

* [BMQ](https://gitlab.com/alfredchen/linux-bmq/tree/linux-5.6.y-bmq) / [BMQ blog](http://cchalpha.blogspot.com) - contains the newest vesion with latest fixes

* [random fixes from zen-kernel](https://github.com/zen-kernel/zen-kernel/tree/5.6/master) - specific patches authored by Jan Alexander Steffens and ZEN Kernel Team

* [random fixes from pfkernel](https://github.com/pfactum/pf-kernel/tree/pf-5.6) / [random fixes from pfkernel](https://gitlab.com/post-factum/pf-kernel/tree/pf-5.6) - for example patches from Arch Linux or specific patches authored by Oleksandr Natalenko

* [fixes from ClearLinux](https://github.com/clearlinux-pkgs/linux) - specific patches authored by ClearLinux Team

* [UKSM (sources)](https://github.com/dolohow/uksm) / [UKSM (info)](https://www.usenix.org/sites/default/files/conference/protected-files/fast18_slides_xia.pdf) - resync from dolohow’s github

* [LL-patches](https://github.com/sirlucjan/kernel-patches/tree/master/5.6/ll-patches) / [LL-patches](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.6/ll-patches) - specific patches authored by Piotr Gorski

* [LL-branding](https://github.com/sirlucjan/kernel-patches/tree/master/5.6/ll-branding) / [LL-branding](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.6/ll-branding) - specific patches authored by Piotr Gorski

###### Some patches for BFQ conflict with patches for BFQ-dev.

###### To use juliagoda-kernels smoothly apply bfq-reverts before linux-lucjan patch. Otherwise the kernel will not compile.

* [bfq-reverts](https://github.com/sirlucjan/kernel-patches/tree/master/5.6/bfq-reverts) / [bfq-reverts](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.6/bfq-reverts) - specific patches authored by Piotr Gorski

######  linux-5.7rc

[linux-5.7rc](https://github.com/sirlucjan/workbench/tree/master/linux-5.7rc) / [linux-5.7rc](https://gitlab.com/sirlucjan/workbench/tree/master/linux-5.7rc) - linux-aufs/linux-aufs-git && linux-bfq/linux-bfq-git && linux-uksm/linux-uksm-git

###### linux-aufs/linux-aufs-git incorporates:

* [AUFS](https://github.com/sfjro/aufs5-standalone/tree/aufs5.x-rcN) / [AUFS](http://aufs.sourceforge.net) - advanced multi-layered unification filesystem

###### linux-bfq/linux-bfq-git incorporates:

* [bfq improvements](https://groups.google.com/forum/#!forum/bfq-iosched) - latest fixes authored by Paolo Valente and BFQ Team

* [bfq-dev](https://github.com/Algodev-github/bfq-mq/tree/dev-bfq-on-5.6) - latest fixes authored by Paolo Valente and BFQ Team

* [bfq-lucjan-dev](https://github.com/sirlucjan/bfq-mq-lucjan/tree/dev-bfq-on-5.6-lucjan) - latest fixes authored by Paolo Valente and BFQ Team and forked by Piotr Gorski

* [bfq-dev-rc](https://github.com/sirlucjan/kernel-patches/tree/master/5.7-rc/bfq-dev-lucjan-sep-v6) / [bfq-dev-rc](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.7-rc/bfq-dev-lucjan-sep-v6) - specific patches authored by Paolo Valente and Piotr Gorski

* [LL-patches](https://github.com/sirlucjan/kernel-patches/tree/master/5.7-rc/ll-patches) / [LL-patches](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.7-rc/ll-patches) - specific patches authored by Piotr Gorski

[![latest packaged version(s)](https://repology.org/badge/latest-versions/linux-bfq.svg)](https://repology.org/project/linux-bfq/versions)

###### Some patches for BFQ conflict with patches for BFQ-dev.

###### To use linux-bfq/linux-bfq-git smoothly apply bfq-reverts before bfq-dev patch. Otherwise the kernel will not compile.

* [bfq-reverts](https://github.com/sirlucjan/kernel-patches/tree/master/5.7-rc/bfq-reverts-all) / [bfq-reverts](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.7-rc/bfq-reverts-all) - specific patches authored by Piotr Gorski

###### linux-uksm/linux-uksm-git incorporates:

* [UKSM (sources)](https://github.com/dolohow/uksm) / [UKSM (info)](https://www.usenix.org/sites/default/files/conference/protected-files/fast18_slides_xia.pdf) - resync from dolohow’s github

######  linux-5.7

[linux-5.7](https://github.com/sirlucjan/workbench/tree/master/linux-5.7) / [linux-5.7](https://gitlab.com/sirlucjan/workbench/tree/master/linux-5.7) - linux-aufs/linux-aufs-git && linux-bfq/linux-bfq-git && linux-uksm/linux-uksm-git

###### linux-aufs/linux-aufs-git incorporates:

* [AUFS](https://github.com/sfjro/aufs5-standalone/tree/aufs5.x-rcN) / [AUFS](http://aufs.sourceforge.net) - advanced multi-layered unification filesystem

###### linux-bfq/linux-bfq-git incorporates:

* [bfq improvements](https://groups.google.com/forum/#!forum/bfq-iosched) - latest fixes authored by Paolo Valente and BFQ Team

* [bfq-dev](https://github.com/Algodev-github/bfq-mq/tree/dev-bfq-on-5.6) - latest fixes authored by Paolo Valente and BFQ Team

* [bfq-lucjan-dev](https://github.com/sirlucjan/bfq-mq-lucjan/tree/dev-bfq-on-5.6-lucjan) - latest fixes authored by Paolo Valente and BFQ Team and forked by Piotr Gorski

* [bfq-dev-rc](https://github.com/sirlucjan/kernel-patches/tree/master/5.7/bfq-dev-lucjan-sep-v2) / [bfq-dev-rc](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.7/bfq-dev-lucjan-sep-v2) - specific patches authored by Paolo Valente and Piotr Gorski

* [LL-patches](https://github.com/sirlucjan/kernel-patches/tree/master/5.7/ll-patches) / [LL-patches](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.7/ll-patches) - specific patches authored by Piotr Gorski

[![latest packaged version(s)](https://repology.org/badge/latest-versions/linux-bfq.svg)](https://repology.org/project/linux-bfq/versions)

###### Some patches for BFQ conflict with patches for BFQ-dev.

###### To use linux-bfq/linux-bfq-git smoothly apply bfq-reverts before bfq-dev patch. Otherwise the kernel will not compile.

* [bfq-reverts](https://github.com/sirlucjan/kernel-patches/tree/master/5.7/bfq-reverts-all-v2) / [bfq-reverts](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.7/bfq-reverts-all-v2) - specific patches authored by Piotr Gorski

###### linux-uksm/linux-uksm-git incorporates:

* [UKSM (sources)](https://github.com/dolohow/uksm) / [UKSM (info)](https://www.usenix.org/sites/default/files/conference/protected-files/fast18_slides_xia.pdf) - resync from dolohow’s github

######  linux-lqx-rebranded

[linux-lqx-rebranded](https://github.com/sirlucjan/workbench/tree/master/linux-lqx-rebranded) / [linux-lqx-rebranded](https://gitlab.com/sirlucjan/workbench/tree/master/linux-lqx-rebranded) - linux-lqx-git/linux-lqx-tag/linux-lqx-tag-git

###### linux-lqx-git/linux-lqx-tag/linux-lqx-tag-git incorporates:

* [liquorix patchset](https://github.com/damentz/liquorix-package/tree/5.6) - authored by Steven Barrett

[![latest packaged version(s)](https://repology.org/badge/latest-versions/linux-lqx.svg)](https://repology.org/project/linux-lqx/versions)

###### linux-zen-rebranded

[linux-zen-rebranded](https://github.com/sirlucjan/workbench/tree/master/linux-zen-rebranded) / [linux-zen-rebranded](https://gitlab.com/sirlucjan/workbench/tree/master/linux-zen-rebranded) - linux-zen-tag

###### linux-zen-tag incorporates:

* [zen-kernel](https://github.com/zen-kernel/zen-kernel/tree/5.7/master) - specific patchset authored by ZEN Kernel Team

#### DOTS

gitconfig based on [pksunkara](https://gist.github.com/pksunkara/988716)
