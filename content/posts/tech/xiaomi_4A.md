[查看原文](https://blog.csdn.net/yilovexing/article/details/129688708)

# 一、获取原厂固件的 ssh 登录权限

有些厂商的路由器会提供原厂固件的 ssh 登录权限，有些则需要通过原厂固件漏洞等方式来获取路由器后台登录权限，比如：小米路由器就需要先通过 OpenWRTInvasion 破解路由登录权限。

小米路由器4A千兆版是利用 2.28.62 版本固件的一个 Shell 命令注入的漏洞，所以要想刷机成功就必须得降级到这个版本（2.28.62 之后的新版本应该是将这个漏洞修复了，我再次通过 OpenWRTInvasion 没获取到 ssh 登录权，所有刷的时候尽量在 2.28.62 这个固件版本下刷机）。

## 克隆破解程序到电脑 并 执行破解
```shell
git clone https://github.com/acecilia/OpenWRTInvasion.git  # 克隆
cd OpenWRTInvasion/ # 进入目录
pip install -r requirements.txt # 下载配置
python remote_command_execution_vulnerability.py # 执行脚本
```


# 二、在命令行登陆路由器后台

## telnet 连接 （也可以使用 ssh ）
1. 按 `win + R` 打开运行窗口。
2. 输入 `OptionalFeatures` 打开 `windows功能` 窗口（也可以在设置里面搜索 `windows功能` ）
3. 下滑找到 `Telnet Client` 勾选后点击确定。
```shell
telnet 192.168.31.1
```
4. 密码是 `root`

显示 "are u ok" 表示登陆成功

## 使用 ssh 连接（也可以使用 telnet ）

```shell
ssh root@192.168.31.1
```

密码是 `root`

显示 "are u ok" 表示登陆成功

# 刷入 Breed

> 对于路由器这类的嵌入式设备刷机有很大的可能会变砖。为了防止我们的路由器有变砖的风险，一般会在刷入第三方路由器固件之前先刷入 Breed。Breed 是国内个人 hackpascal 开发的闭源 Bootloader，也被称为“不死鸟”。
> 因为有些官方升级固件自带 bootloader，如果从官方固件升级，会导致现有 bootloader 被覆盖。而当 Breed 更新固件时，它会自动删除固件附带的引导加载程序，因此可以防止 Breed 被覆盖。
> Breed 拥有以下特性：
> 实时刷机进度，进度条能准确反映刷机进度
> Web 页面快速响应
> 最大固件备份速度，依 Flash 而定，一般能达到 1MB/s
> 免按复位键进入 Web 刷机模式
> Telnet 功能，免 TTL 进入 Breed 命令控制台
> 复位键定义测试功能
> 固件启动失败自动进入 Web 刷机模式
> 可自定义位置和大小的环境变量块
> 由于是闭源，无法进行二次开发，所有支持的设备均由 hackpascal 一人完成。在 2020-10-09 后已经停止版本更新，但官网目前
> 然开放所有的 Breed 下载。
> 一句话概括就是：Breed 是操作系统，第三方路由器固件是应用软件，软件频繁更换和安装不会影响操作系统。

## 备份分区数据

```shell
cat /proc/mtd
dd if=/dev/mtd0 of=/tmp/all.bin
dd if=/dev/mtd1 of=/tmp/Bootloader.bin
dd if=/dev/mtd3 of=/tmp/eeprom.bin
```

下载 Breed：
Breed 下载地址：https://breed.hackpascal.net/
在 `文件资源管理器` 中输入 `ftp://192.168.31.1` 打开路由器的文件系统

刷入 Breed：
```shell
cd /tmp
mtd -r write breed-mt7621-pbr-m1.bin Bootloader
```


# 刷入第三方路由器固件


OpenWRT下载地址：https://downloads.openwrt.org/releases/21.02.3/targets/ramips/mt7621/

找到对应型号：openwrt-21.02.3-ramips-mt7621-xiaomi_mi-router-4a-gigabit-squashfs-sysupgrade.bin。
```shell
cd /tmp
mtd -e OS1 -r write openwrt-21.02.3-ramips-mt7621-xiaomi_mi-router-4a-gigabit-squashfs-sysupgrade.bin OS1
```

## 通过 Breed Web 恢复控制台刷入第三方路由器固件

当我们刷入 Breed 后就相当于是给路由器装了个操作系统，可以在上面随意刷入第三方路由器固件，一般情况下不会出现变砖的风险。
### OpenWrt
一般情况都安装 OpenWRT 或者是魔改后的 OpenWRT，小米路由器本身也是魔改的 OpenWRT。
OpenWRT官网下载地址：https://downloads.openwrt.org/releases/21.02.3/targets/ramips/mt7621/
默认账户：root
OpenWRT魔改下载地址：https://download.csdn.net/download/yilovexing/87600550
默认账户：root
默认密码：coolxiaomi

### Padavan
据说小米路由器使用老毛子固件更稳定，我也没有具体去考证，也不知道是不是真的。反正我是比较喜欢用 Padavan，无论是界面还是稳定性都不错（还有个使用老毛子的原因是 2022-07-24 Breed 进行了重大更新，OpenWrt 不再支持直接用底包刷固件了。）！

Padavan官网源码：https://bitbucket.org/padavan/rt-n56u/src/master/
Padavan下载地址：https://opt.cn2qq.com/padavan/
默认账户：admin
默认密码：admin


---
[原文](https://blog.csdn.net/xingman510/article/details/127174713)

介绍一下配置：
- wifi 全程不用连网
- win系统电脑刷机，需要下载一个刷机包
- windows 有 python 程序，查看方法：在命令提示符窗口输入 `python --version`，会输出版本号

Breed也被称为“不死鸟”，顾名思义刷入Breed后即使后续为路由器刷固件失败，也不至于让路由器变砖，并且对于以后更换固件非常友好，强烈建议刷Breed。

> 首先下载刷机所需要用到的工具
> 链接：https://pan.baidu.com/s/1kGnIe2T8Ul1XvWobdyxDbQ
> 提取码：iaxp


提示：小米路由器后管理地址，一般为192.168.31.1

# 打开小米路由器的 Telnet 和 FTP
1. 打开下载工具包中的 `R3GV2 patches` 文件夹
2. 运行文件夹中的 0.start_main.bat 批处理文件，此文件实际上是运行了一个 python 脚本，向路由器上传了一个开启 Telnet 和 FTP 的文件。

# 用 MobaXterm 连接小米路由器
（也可以在终端连接，我在小米4a路由器的刷机过程中就是用的终端）
1. 打开下载的工具包中的 `MobaXterm_Personal_21.1.exe` 程序，
2. 依次点击 `Sessions` -> `New session` -> `Telnet` ，
  - 在 `Remote host`  中输入`192.168.31.1`
  - `Username` 中输入 `root`
  - 最后点击 `OK`，回到主界面后会发现生成了一个新的session

3. 双击运行新的 session（这一步可能会提示无法连接，从头开始按照以上步骤多试几次就行了），如果需要输入密码，尝试输入 `root` 或者 `password` 或者你的 wifi 密码。

界面显示 “are u ok”，表示连接成功。

# 备份文件
1. 在 `MobaXterm` 命令行中分别输入以下命令

`dd if=/dev/mtd0 of=/tmp/all.bin` 将整个磁盘分区命名为all.bin备份到tmp路径

`dd if=/dev/mtd1 of=/tmp/bootloader.bin` 将Bootloader分区命名为bootloader.bin备份到tmp路径

`dd if=/dev/mtd2 of=/tmp/eeprom.bin` 将Eeprom分区命名为eeprom.bin备份到tmp路径


2. 备份完成后打开 `文件资源管理器`，在地址栏输入 `ftp://192.168.31.1`，打开 `tmp` 文件夹，并将刚刚备份的 `3个bin文件` 复制到 `自己的电脑` 中(注意：务必检查eeprom.bin文文件大小，通常为64kb，若文件只有几百字节则须重新备份)

# 刷入Breed
1. 打开工具包中的 `Breed` 文件夹复制 `breed.bin` 文件，然后上传到 `tmp` 目录内

2. 回到 `MobaXterm` 中输入 `mtd write /tmp/breed.bin Bootloader` 刷入Breed。

3. 刷入完成后将小米路由器4C断电，按住复位键的同时通电，可以看到电源灯与网络灯闪烁几下后即可松开复位键，此时就进入了Breed模式。

4. 在浏览器输入 `192.168.1.1` 进入 Breed 页面。

# 刷入OpenWrt

{bs-font color="#080000"}注意：一定要先刷入`eeprom.bin`再刷入`OpenWrt固件`{/bs-font}

1. 在 `Breed Web` 恢复控制台中依次刷入备份好的 `eeprom.bin` 与 `OpenWrt固件` 即可

OpenWrt固件在工具包文件夹OpenWrt固件中

# 其他
刷好OpenWrt后输入 `192.168.5.1` 进入路由器管理界面，默认密码为 `password`
