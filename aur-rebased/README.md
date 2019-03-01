## Fork off linux-bfq-mq-git

- linux-bfq-mq-lucjan-git

###### linux-bfq-mq-lucjan-git incorporates:

* [BFQ-SQ and BFQ-MQ Scheduler](https://github.com/sirlucjan/bfq-mq-lucjan) - bfq-sq and bfq-mq from Algodev-github, forked by sirlucjan

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
cd /some_path/workbench/aur-rebased/package_name
makepkg -srci

```


~~For now, you can use `sudo tee /sys/block/sda/queue/scheduler <<< bfq-mq` to enable "bfq-mq".~~

~~You can also add this to file `60-schedulers.rules`:~~

```
# Non-rotational disks
ACTION=="add|change", KERNEL=="sd[a-z]", ATTR{queue/rotational}=="0", ATTR{queue/scheduler}="bfq-mq"
# Rotational disks
ACTION=="add|change", KERNEL=="sd[a-z]", ATTR{queue/rotational}=="1", ATTR{queue/scheduler}="bfq-mq"
```

~~and run a command `sudo udevadm control --reload && sudo udevadm trigger`~~

For now, bfq-mq is enabled by default! [(since elevator-set-default-scheduler-to-bfq-mq-for-blk-mq.patch)](https://github.com/sirlucjan/bfq-mq-lucjan/commit/64c139894fb8f521c75e8f28acb2d59163e6c393)
