# Fork of linux-lucjan. Use at your own risk.
###### HP G62 with AMD Athlon II P340 optimized.
###### linux-lucjan/linux-juliagoda varies considerably from stock kernel. 
***
###### linux-lucjan/linux-juliagoda incorporates:

* [bfq improvements](https://groups.google.com/forum/#!forum/bfq-iosched) - latest fixes authored by Paolo Valente and BFQ Team

* ~~[bfq-dev](https://github.com/Algodev-github/bfq-mq/tree/dev-bfq-on-5.6) - latest fixes authored by Paolo Valente and BFQ Team~~

* ~~[bfq-dev-lucjan](https://github.com/sirlucjan/bfq-mq-lucjan/tree/dev-bfq-on-5.6-lucjan) - latest fixes authored by Paolo Valente and BFQ Team and forked by Piotr Gorski~~

* ~~[bfq-dev-lucjan-rc](https://github.com/sirlucjan/kernel-patches/tree/master/5.11/bfq-dev-lucjan) / [bfq-dev-lucjan-rc](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.11/bfq-dev-lucjan) - specific patches authored by Paolo Valente and Piotr Gorski~~

* [bfq-lucjan](https://github.com/sirlucjan/kernel-patches/tree/master/5.15/bfq-lucjan) / [bfq-lucjan](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.15/bfq-lucjan) - specific patches authored by Paolo Valente and Piotr Gorski

* [graysky's GCC/Clang patch](https://github.com/graysky2/kernel_compiler_patch) - version for gcc v11/clang v12

* [Project C](https://gitlab.com/alfredchen/linux-prjc/tree/linux-5.15.y-prjc) / [Project C blog](http://cchalpha.blogspot.com) - contains the newest vesion with latest fixes

* [random fixes from zen-kernel](https://github.com/zen-kernel/zen-kernel/tree/5.15/master) - specific patches authored by Jan Alexander Steffens and ZEN Kernel Team

* [random fixes from xanmod-linux](https://github.com/xanmod/linux/tree/5.15) - specific patches authored by Alexandre Frade

* [random fixes from pfkernel](https://github.com/pfactum/pf-kernel/tree/pf-5.15) / [random fixes from pfkernel](https://gitlab.com/post-factum/pf-kernel/tree/pf-5.15) - for example patches from Arch Linux or specific patches authored by Oleksandr Natalenko

* [fixes from ClearLinux](https://github.com/clearlinux-pkgs/linux) - specific patches authored by ClearLinux Team

* [UKSM (sources)](https://github.com/dolohow/uksm) / [UKSM (info)](https://www.usenix.org/sites/default/files/conference/protected-files/fast18_slides_xia.pdf) - resync from dolohow’s github

* [LL-patches](https://github.com/sirlucjan/kernel-patches/tree/master/5.15/ll-patches) / [LL-patches](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.15/ll-patches) - specific patches authored by Piotr Gorski

* [LL-branding](https://github.com/sirlucjan/kernel-patches/tree/master/5.15/ll-branding) / [LL-branding](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.15/ll-branding) - specific patches authored by Piotr Gorski

###### Some patches for BFQ/block-stable conflict with patches for BFQ-dev/block-mainline.

###### To use juliagoda-kernels smoothly apply ll-reverts before linux-lucjan patch. Otherwise the kernel will not compile.

* ~~[ll-reverts](https://github.com/sirlucjan/kernel-patches/tree/master/5.11-dev/ll-reverts) / [ll-reverts](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.11-dev/ll-reverts) - specific patches authored by Piotr Gorski~~

***
# Download:

```
git clone https://github.com/sirlucjan/worbench.git

```

or

```
git clone https://gitlab.com/sirlucjan/workbench.git

```

# Install:


### Stable

```
cd /some_path/workbench/juliagoda-kernels/stable/package_name
makepkg -srci

```

### Stable RC

```
cd /some_path/workbench/juliagoda-kernels/stable-rc/package_name
makepkg -srci

```
### Rolling

```
cd /some_path/workbench/juliagoda-kernels/rolling/package_name
makepkg -srci

```

***
# Enable bfq

~~For now, you can use `sudo tee /sys/block/sda/queue/scheduler <<< bfq` to enable "bfq".~~

~~You can also add this to file `60-schedulers.rules`:~~

```
# Non-rotational disks
ACTION=="add|change", KERNEL=="sd[a-z]", ATTR{queue/rotational}=="0", ATTR{queue/scheduler}="bfq"
# Rotational disks
ACTION=="add|change", KERNEL=="sd[a-z]", ATTR{queue/rotational}=="1", ATTR{queue/scheduler}="bfq"
```

~~and run a command `sudo udevadm control --reload && sudo udevadm trigger`~~

For now, bfq is enabled by default! [(since 5.0-lucjan-ll1-rc1.patch and LL-elevator-set-default-scheduler-to-bfq-for-blk-mq.patch)](https://github.com/sirlucjan/kernel-patches/blob/master/5.0/ll-patches/0002-LL-elevator-set-default-scheduler-to-bfq-for-blk-mq.patch)


***

# You've been warned.
