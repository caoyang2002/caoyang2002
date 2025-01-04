+++
date = '2024-12-29T09:31:37+08:00'
draft = true
title = 'Go'
toc = true
+++

[原文链接](https://blog.csdn.net/christmans/article/details/129641264)

# 查看 CPU 架构
```shell
uname -m：该命令会输出当前系统的CPU架构，如x86_64、i386、armv7l等。
arch：该命令可以查看Linux系统的CPU架构。
cat /proc/version：该命令可以查看系统内核的版本信息。
cat /proc/cpuinfo：该命令可以查看CPU信息，如每个物理CPU中core的个数、逻辑CPU的个数、CPU型号等。
```
> [脚本目录](http://ipkg.nslu2-linux.org/optware-ng/bootstrap/)

# X86_64 架构安装
## 切换到root账号
```shell
sudo -i
```

## 下载脚本
```shell
wget http://ipkg.nslu2-linux.org/optware-ng/bootstrap/buildroot-x86_64-bootstrap.sh
```

## 添加可执行权限
```shell
chmod +x buildroot-x86_64-bootstrap.sh
```
## 执行脚本
```shell
./buildroot-x86_64-bootstrap.sh
```

## 升级ipkg

```shell
/opt/bin/ipkg update
```

## 安装gcc

```shell
/opt/bin/ipkg install gcc
```

# ARM 架构安装


## 切换到root账号

```shell
sudo -i
```

## 安装脚本

> 切换到临时目录，下载一个脚本 buildroot-armeabihf-bootstrap.sh，并添加可执行权限
```shell
cd /volume1/@tmp
wget http://ipkg.nslu2-linux.org/optware-ng/bootstrap/buildroot-armeabihf-bootstrap.sh .
chmod +x buildroot-armeabihf-bootstrap.sh
```

## 执行脚本

```shell
./buildroot-armeabihf-bootstrap.sh
```

## 升级ipkg

```shell
/opt/bin/ipkg update
```

## 安装gcc

```shell
/opt/bin/ipkg install gcc
```

# 可选

设置别名
```shell
alias ipkg=/opt/bin/ipkg
```
