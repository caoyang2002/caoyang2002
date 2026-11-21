+++
title = 'VPN不求人！教你自搭建ClashVPN节点'
date = 2026-11-22T06:31:05+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "<no value>"
+++

查看原文: https://www.xianyuwang.top/archives/203

## **自建多个协议节点教程很简单，整个教程分三步**：

- **第一步：购买VPS服务器**
- **第二步：一键部署VPS服务器**
- **第三步：一键加速VPS服务器 （五合一的TCP网络加速脚本）**

## **前言：**

可以无需域名。按照提示操作安装，全程回车即可。搭建好后默认有4个节点，1个vless-reality-vision节点，1个vmess-ws节点，1个Hysteria-2节点，1个Tuic-v5节点。鼠标往上翻，可以看到节点的一键导入链接和二维码。支持v2rayn、v2rayng、nekobox、小火箭shadowrocket客户端。

![成功示范](https://esaimg.cdn1.vip/i/6a7f366cb5125_1786721900.jpg)



## **第一步：购买VPS服务器**

VPS服务器需要选择国外的，这里我推荐雨云([rainyun.com](https://www.xianyuwang.top/dinterception?a=ddJzqT3Qr0BncOTZ_1795300062))，速度不错、稳定且性价比高。

RackNerd 量大管饱：https://racknerd.com

### **一、购买云服务器：**

来到[雨云官网](https://www.xianyuwang.top/dinterception?a=pUlXkSUYmP1Sj4EW_1795300062)点击云产品，按提示操作注册账号。优惠码：**xywlkj**

![20251002213903686-1bbda1fd0fecd29cf37a62d6870171b3_20231219154825_57ee1160d5d4da81afd2ee61ab1ae718](https://esaimg.cdn1.vip/i/6a7f366f3e665_1786721903.webp)

### 二、选择服务器配置

点击进入购买界面后可按需求按需购买，如果不知道如何选择可以看雨云的[选购指南](https://www.xianyuwang.top/dinterception?a=Si3TA5hiWVGRkV3s_1795300062)。

**选择云服务器：**

![20251002214247505-image](https://esaimg.cdn1.vip/i/6a7f36726c1d6_1786721906.webp)

### 三、测试访问

购买成功后，页面会自动跳转到管理页面，等待服务器运行状态变为`运行中`后，我们可以使用页面各处的远程连接信息，连接到服务器。

![20251002214346491-88c05394d4b8f576821843f6baa6d62e_img_1702016773_4ea0ec3a30e90fa7677c9ce983e77e35](https://esaimg.cdn1.vip/i/6a7f36746b74b_1786721908.webp)

## **第二步：部署服务器脚本**

### **连接服务器：**

使用电脑ssh命令【ssh root@你的服务器IP】来连接你的服务器。也可以使用最近很火的[**GMSSH 来连接服务器**](https://www.xianyuwang.top/dinterception?a=aEPd4xjroIBTihzG_1795300062)

![20251002214712733-5ebcf2b9bb80a179584cca82f10f9843_68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f416c76696e393939392f5041432f73732f787368656c6c322e706e67](https://esaimg.cdn1.vip/i/6a7f367541a48_1786721909.png)

连接成功后，会出现如上图所示，之后就可以复制粘贴代码部署了。（如果下面脚本无法正常安装，教程末尾还有一个备用脚本）

### 脚本安装命令：

```bash
bash <(wget -qO- https://raw.githubusercontent.com/yonggekkk/sing-box-yg/main/sb.sh)
```

> **安装完成后，输入sb可进入管理页面。脚本来自[yonggekkk](https://www.xianyuwang.top/dinterception?a=v0pIldTq7f1gyKVZ_1795300062)**

------

### 脚本演示：

复制上面安装命令代码到VPS服务器里，复制代码用鼠标右键的复制，然后在vps里面右键粘贴进去，因为ctrl+c和ctrl+v无效。接着输入数字1来安装。

首次安装需要 Yes 确认。

安装完成后，如果想修改、查看配置等，可以输入sb进行管理页面，不用重复安装脚本。

![20251002214919348-7f80b12d0157b16ea0d3db50b729d2a4_68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f416c76696e393939392f706163322f736f6674696d61672f7967312e6a7067](https://esaimg.cdn1.vip/i/6a7f367709726_1786721911.webp)

输入数字1进行安装

![20251002214938870-6e20cd30da71b104f71ba41284f8b8f2_68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f416c76696e393939392f706163322f736f6674696d61672f7967322e6a7067](https://esaimg.cdn1.vip/i/6a7f3679e43c6_1786721913.webp)

之后的设置全程回车即可

![20251002215010708-image](https://esaimg.cdn1.vip/i/6a7f367c3eb5e_1786721916.webp)

搭建好后默认有4个节点，1个vless节点，1个vmess节点，1个hysteria2节点，1个tuic节点。

鼠标往上翻，可以看到节点的一键导入链接和二维码。支持v2rayn、v2rayng、nekobox、小火箭shadowrocket客户端。

### **特殊情况：**

**如果选择的是CentOS系统，还需要关闭vps防火墙来开放端口，相关命令如下：**

**查看防火墙状态命令**：

```
firewall-cmd --state
```

**停止firewall命令**：

```
systemctl stop firewalld.service
```

**禁止firewall开机启动命令**：

```
systemctl disable firewalld.service
```

## **第三步：一键加速VPS服务器**

五合一的TCP网络加速脚本，包括了BBR原版、BBR魔改版、暴力BBR魔改版、BBR plus（首选）、Lotsever(锐速)安装脚本。可用于KVMXen架构，不兼容OpenVZ（OVZ）。支持Centos 6+ / Debian 7+ / Ubuntu 14+，BBR魔改版不支持Debian 8。

```
wget -N --no-check-certificate "https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh"

chmod +x tcp.sh

./tcp.sh
```

> **如果提示 wget: command not found 的错误，这是你的系统精简的太干净了，wget都没有安装，所以需要安装wget。CentOS系统安装wget命令： yum install -y wget   Debian/Ubuntu系统安装wget命令：apt-get install -y wget**

安装完成后，脚本管理命令为：./tcp.sh

![20251002215259655-1b19fe2afecd35678decd00bc3571d34_68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f416c76696e393939392f706163322f76756c74722f6e6577626272312e6a7067](https://esaimg.cdn1.vip/i/6a7f367fc678c_1786721919.webp)

操作方法：先安装内核，重启vps让内核生效，再启动对应的加速即可。数字1的BBR/BBR魔改内核对应数字4、5、6的BBR加速、BBR魔改加速和暴力BBR魔改版加速。数字2的BBRplus内核对应数字7的BBRplus加速。数字3的锐速加速内核对应数字8的锐速加速。

>  如果服务器系统是Debian或Ubuntu系统，可不用安装内核，直接输入数字4启动bbr原版加速。

以安装暴力BBR魔改版加速为例：

我们先安装对应的内核，输入数字 `1`

![20251002215318185-646d165338145d8320e89aada0edf31e_68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f416c76696e393939392f706163322f76756c74722f6e6577626272322e6a7067](https://esaimg.cdn1.vip/i/6a7f36819cc37_1786721921.webp)

内核安装完成后，输入 `y` 进行重启，重启才能让内核生效

![20251002215334879-3d111c6dc6a5a9511b38edd36aff05d8_68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f416c76696e393939392f706163322f76756c74722f6e6577626272332e6a7067](https://esaimg.cdn1.vip/i/6a7f368381098_1786721923.webp)

重启完成后，输入数字 `6` 来启动暴力BBR魔改版加速

![20251002215346791-3e08a874dd63e7dad8ae362b19670dae_68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f416c76696e393939392f706163322f76756c74722f6e6577626272342e6a7067](https://esaimg.cdn1.vip/i/6a7f3684cc119_1786721924.webp)

![20251002215352432-1501f86739c4b07f099924b84bf4ce46_68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f416c76696e393939392f706163322f76756c74722f6e6577626272352e6a7067](https://esaimg.cdn1.vip/i/6a7f3685eb8b9_1786721925.jpg)

输入 `./tcp.sh`查看最终是否启动成功。

如果想换一个加速，输入数字9进行卸载加速，然后进行同样的操作，安装内核再安装对应内核的加速即可。

**注意：如果在安装内核环节出现这样一张图，注意选择NO**

![20251002215422727-d15ad3a8dea410f3f0735fee2de621b0_68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f416c76696e393939392f706163322f76756c74722f6e6577626272362e6a7067](https://esaimg.cdn1.vip/i/6a7f36878376e_1786721927.webp)

## **客户端下载及使用方法：**

windows电脑系统推荐使用v2rayN客户端，最好用v2rayN最新版。

**注意**：第一次使用v2rayN客户端时，需要安装最新版NET Framework ，不然无法正常运行，[微软官网](https://www.xianyuwang.top/dinterception?a=7hFaWusnqm8XuBGA_1795300062)下载。

windows v2rayN 客户端：[github最新版下载](https://www.xianyuwang.top/dinterception?a=qCdSsULSedyXO9TR_1795300062) (下载带core的文件) [github镜像下载](https://www.xianyuwang.top/dinterception?a=6WAWXWaqQAuKCgDS_1795300062) (下载带core的文件)

Mac客户端 v2rayU 客户端：[github最新版下载](https://www.xianyuwang.top/dinterception?a=a7bSOdk27YmgG2U6_1795300062) [github镜像下载](https://www.xianyuwang.top/dinterception?a=Fak7V1p9WD6rXc42_1795300062)

Linux客户端 Qv2ray 客户端：[github最新版下载](https://www.xianyuwang.top/dinterception?a=vwHFyynf8ct0McF7_1795300062) [github镜像下载](https://www.xianyuwang.top/dinterception?a=KoEi1XpEvGWGjCPw_1795300062)

安卓v2rayNG 客户端：[github最新版下载](https://www.xianyuwang.top/dinterception?a=cMgWLG2WqL43KMyV_1795300062) [github镜像下载](https://www.xianyuwang.top/dinterception?a=xCggv6EZxrldlZ6U_1795300062)

iOS：[没有美区AppleID的翻墙教程](https://www.xianyuwang.top/dinterception?a=g88C2vYaCWfjq3xb_1795300062) [iOS注册美区Apple ID教程](https://www.xianyuwang.top/dinterception?a=dU3Usf8kxJL00QQD_1795300062)

## **软件代理设置：**

![20251002215536147-1631dce0b897aaad8a69a815a6942a24_68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f416c76696e393939392f706163322f736f6674696d61672f76327261796e3030312e6a7067](https://esaimg.cdn1.vip/i/6a7f3688546fc_1786721928.jpg)

Windows系统打开v2rayN软件，在软件的底部，选择“自动配置系统代理”，路由可选择“全局(Global)”。全局(Global)模式：所有网站通过节点服务器代理上网。

## **注意事项**：

1、电脑如果使用V2rayN客户端，最好用v2rayN最新版，至少使用6.43及以上版本，不然节点可能无法使用。因为脚本搭建的时候服务器用的是最新版的服务端,所以客户端的版本太老的话可能就不兼容。其它操作系统的客户端也一样,也最好用最新版。v2rayN最新版下载地址：[https://github.com/2dust/v2rayN/releases](https://www.xianyuwang.top/dinterception?a=bzy11yY1LrIozgV6_1795300062)

2、**备用脚本：**

```
bash <(wget -qO- https://raw.githubusercontent.com/fscarmen/sing-box/main/sing-box.sh)
```

搭建好后有9个节点，包括vmess、vless、ss、hysteria2、trojan节点。

3、请勿用于违法用途！本教程仅供网络技术学习交流使用，请不要用于黑灰产等。