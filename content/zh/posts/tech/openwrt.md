+++
date = '2023-10-29T09:31:37+08:00'
draft = false
title = 'OpenWRT 教程'
tags = ["运维","openwrt"]
toc = true
+++

[OpenWRT下载地址](https://lidrive.vip/)
# 下载
![版本](https://www.caoyang2002.top/usr/uploads/2023/12/3668705269.png)

# 制作启动盘
将PE系统写入到U盘，window：rufus，macOS：balenaEtcher
将OpenWRT镜像、rufus（在PE系统上写盘会需要）拷贝到写完的U盘里（也可以用另一个U盘）

# 进入BIOS
将U盘插入至路由器，根据硬件选择启动顺序为U盘，笔者的路由器是F12
# 删除设备的磁盘分区
进入PE系统之后，打开rufus（按Ctrl-Alt-F开启内部磁盘的识别），选择OpenWRT镜像并将其写入到内置的磁盘
# 写入镜像 (IMG写盘工具)
打开IMG写盘工具, 选择设备的物理盘, 选择OpenWrt镜像
# 重启
写入完成之后，就可以拔掉U盘，重启后进入OpenWRT了

# 其他信息
ip: 一般是: 192.168.5.1, 可以自己改
账号密码: 账号是 root, 密码不填, 直接登录即可
