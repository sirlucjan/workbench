## Fork off linux-bfq-mq-git

- switch sources

- sync with linux-bfq-mq

###### linux-bfq/linux-bfq-git incorporates:

* [BFQ-SQ and BFQ-MQ Scheduler](https://github.com/Algodev-github/bfq-mq) - bfq-sq and bfq-mq from Algodev-github

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
cd /some_path/workbench/fork-off-linux-bfq-mq-git/package_name
makepkg -srci

```

# Enable bfq-mq

For now, you can use `sudo tee /sys/block/sda/queue/scheduler <<< bfq-mq` to enable "bfq-mq".

You can also add this to file `60-schedulers.rules`:

```
# Non-rotational disks
ACTION=="add|change", KERNEL=="sd[a-z]", ATTR{queue/rotational}=="0", ATTR{queue/scheduler}="bfq-mq"
# Rotational disks
ACTION=="add|change", KERNEL=="sd[a-z]", ATTR{queue/rotational}=="1", ATTR{queue/scheduler}="bfq-mq"
```

and run a command `sudo udevadm control --reload && sudo udevadm trigger`
