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
