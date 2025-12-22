---
title: Enable ZRAM on Raspberry pi 4 and up
date: 2025-12-21
author: Nick Buraglio
layout: page
categories:
    - configuration
tags:
    - linux
    - raspberypi
---

Full details from [here](https://teejeetech.com/2022/06/04/tweaks-for-ubuntu-22-04-on-raspberry-pi-4/)

tl:dr - Works on Raspberry pi 4 and above, Ubuntu 22. I was able to cobble it to sorta work on an Rpi3. Rpi2 is a no-go. It does seem to help performance. 

`sudo apt install -y linux-modules-extra-raspi`
`sudo apt install -y zram-tools`
`sudo apt autoremove --purge -y zram-config`
`sudo vi /etc/default/zramswap`
`sudo sed -i -e 's/zswap.enabled=1/zswap.enabled=0/' /boot/firmware/cmdline.txt`
`sudo reboot`

in `/etc/default/zramswap` change:

```
`ALGO=zstd
`PERCENT=50
`PRIORITY=100
```

`zramctl` to check status


