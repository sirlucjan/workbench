# Fork of linux-lucjan. Use at your own risk.
###### HP G62 with AMD Athlon II P340 optimized.
###### linux-lucjan/linux-juliagoda varies considerably from stock kernel. 
***
###### linux-lucjan/linux-juliagoda incorporates:

* [bfq improvements](https://groups.google.com/forum/#!forum/bfq-iosched) - latest fixes authored by Paolo Valente and BFQ Team

* [graysky's GCC patch](https://github.com/graysky2/kernel_gcc_patch) - version for gcc 8.1

* [UKSM (sources)](https://github.com/dolohow/uksm) / [UKSM (info)](https://www.usenix.org/sites/default/files/conference/protected-files/fast18_slides_xia.pdf) - resync from dolohow’s github

* [PDS-mq](https://github.com/cchalpha/PDS-mq) / [PDS-mq blog](http://cchalpha.blogspot.com) - contains the newest vesion with latest fixes

* [random fixes from zen-kernel](https://github.com/zen-kernel/zen-kernel) - specific patches authored by Jan Alexander Steffens and ZEN Kernel Team

* [random fixes from pfkernel](https://github.com/pfactum/pf-kernel) - for example patches from Arch Linux or specific patches authored by Oleksandr Natalenko

* [LL-patches](https://github.com/sirlucjan/kernel-patches/tree/master/4.20/ll-patches) / [LL-patches](https://gitlab.com/sirlucjan/kernel-patches/tree/master/4.20/ll-patches) - specific patches authored by Piotr Gorski

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


### Experimental

```
cd /some_path/workbench/linux-juliagoda/stable/package_name
makepkg -srci

```

### Trunk

```
cd /some_path/workbench/linux-juliagoda/stable-rc/package_name
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

For now, bfq-mq is enabled by default! [(since 5.0-lucjan-ll1-rc1.patch and LL-elevator-set-default-scheduler-to-bfq-for-blk-mq.patch)](https://github.com/sirlucjan/kernel-patches/blob/master/5.0/ll-patches/0003-LL-Add-.ll-version.patch)


***
# You've been warned.
