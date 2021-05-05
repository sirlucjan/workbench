# Kernels and modules:

- linux-aufs

- linux-aufs-git

- linux-bfq-dev
 
- linux-bfq-dev-git

[![Packaging status](https://repology.org/badge/vertical-allrepos/linux-bfq-dev.svg)](https://repology.org/project/linux-bfq-dev/versions)

- linux-uksm

- linux-uksm-git

[![Packaging status](https://repology.org/badge/vertical-allrepos/linux-uksm.svg)](https://repology.org/project/linux-uksm/versions)

###### linux-aufs/linux-aufs-git incorporates:

* [AUFS](https://github.com/sfjro/aufs5-standalone/tree/aufs5.x-rcN) / [AUFS](http://aufs.sourceforge.net) - advanced multi-layered unification filesystem

###### linux-bfq-dev/linux-bfq-dev-git incorporates:

* [bfq improvements](https://groups.google.com/forum/#!forum/bfq-iosched) - latest fixes authored by Paolo Valente and BFQ Team

* ~~[bfq-dev](https://github.com/Algodev-github/bfq-mq/tree/dev-bfq-on-5.6) - latest fixes authored by Paolo Valente and BFQ Team~~

* ~~[bfq-dev-lucjan](https://github.com/sirlucjan/bfq-mq-lucjan/tree/dev-bfq-on-5.6-lucjan) - latest fixes authored by Paolo Valente and BFQ Team and forked by Piotr Gorski~~

* ~~[bfq-dev-lucjan-rc](https://github.com/sirlucjan/kernel-patches/tree/master/5.11/bfq-dev-lucjan) / [bfq-dev-lucjan-rc](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.11/bfq-dev-lucjan) - specific patches authored by Paolo Valente and Piotr Gorski~~

* [bfq-lucjan](https://github.com/sirlucjan/kernel-patches/tree/master/5.12/bfq-lucjan) / [bfq-lucjan](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.12/bfq-lucjan) - specific patches authored by Paolo Valente and Piotr Gorski

* [LL-patches](https://github.com/sirlucjan/kernel-patches/tree/master/5.12/ll-patches) / [LL-patches](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.12/ll-patches) - specific patches authored by Piotr Gorski

[![latest packaged version(s)](https://repology.org/badge/latest-versions/linux-bfq-dev.svg)](https://repology.org/project/linux-bfq-dev/versions)

###### Some patches for BFQ conflict with patches for BFQ-dev.

###### To use linux-bfq-dev/linux-bfq-dev-git smoothly apply bfq-reverts before bfq-dev patch. Otherwise the kernel will not compile.

* ~~[bfq-reverts](https://github.com/sirlucjan/kernel-patches/tree/master/5.11/bfq-reverts-all) / [bfq-reverts](https://gitlab.com/sirlucjan/kernel-patches/tree/master/5.11/bfq-reverts-all) - specific patches authored by Piotr Gorski~~

###### linux-uksm incorporates:

* [UKSM (sources)](https://github.com/dolohow/uksm) / [UKSM (info)](https://www.usenix.org/sites/default/files/conference/protected-files/fast18_slides_xia.pdf) - resync from dolohow’s github

[![latest packaged version(s)](https://repology.org/badge/latest-versions/linux-uksm.svg)](https://repology.org/project/linux-uksm/versions)

***

# Download:

```
git clone https://github.com/sirlucjan/workbench.git

```
or

```
git clone https://gitlab.com/sirlucjan/workbench.git

```

# Install:

```
cd /some_path/workbench/package_name
makepkg -srci

```

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