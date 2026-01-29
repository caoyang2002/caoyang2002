+++
title = '如何在Ubuntu系统下搭建ESP32开发环境：从零开始配置与测试'
date = 2025-04-06T17:09:20+08:00
draft = false
author = "simons"
categories = ["物联网", "嵌入式开发", "Ubuntu"]
tags = ["ESP32", "ESP-IDF", "环境搭建", "Ubuntu 22.04", "物联网开发", "乐鑫", "烧录调试"]
description = "本文提供了一份详细的、从零开始的教程，指导开发者如何在Ubuntu 22.04系统上搭建完整的ESP32开发环境。内容涵盖安装依赖、配置ESP-IDF框架、设置工具链、编译烧写Hello World示例程序，并附带了CMake版本、编译器缺失等常见问题的解决方案，帮助物联网和嵌入式新手快速上手。"

+++

### 引言

在物联网（IoT）领域，ESP32因其强大的功能和灵活性而广受欢迎。无论是智能家居、工业自动化还是个人项目，ESP32都能提供可靠的解决方案。然而，要充分利用这一强大的微控制器，首先需要搭建一个稳定的开发环境。本文将详细介绍如何在Ubuntu系统下搭建ESP32开发环境，帮助新手和有一定经验的开发者顺利入门。

### 一、准备工作

#### 1. 硬件要求

- **ESP32开发板**：如乐鑫ESP32模块或安信可WIFI开发板。
- **电脑**：运行Ubuntu 22.04操作系统。

#### 2. 软件要求

- **Ubuntu 22.04**：确保系统更新到最新版本。
- **Git**：用于克隆源代码。
- **Python**：建议使用Python 3.8及以上版本。

### 二、安装依赖

首先，打开终端并执行以下命令以更新系统并安装必要的依赖项：

```bash
sudo apt update
sudo apt upgrade
sudo apt install git wget python3 python3-pip
```

### 三、下载和配置ESP-IDF

#### 1. 克隆ESP-IDF源代码

在`home`目录下创建一个名为`esp`的文件夹，并进入该文件夹：

```bash
mkdir ~/esp
cd ~/esp
```

使用Git克隆ESP-IDF源代码：

```bash
git clone -b v4.4 --recursive https://github.com/espressif/esp-idf.git
```

#### 2. 下载编译工具链

从乐鑫官网下载编译工具链：

```bash
wget https://dl.espressif.com/dl/xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz
```

下载完成后，解压工具链：

```bash
tar -xzf xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz
```

#### 3. 设置环境变量

在`~/.bashrc`文件中添加以下内容：

```bash
export IDF_PATH=~/esp/esp-idf
export PATH=$PATH:$HOME/xtensa-esp32-elf/bin
```

保存并关闭文件，然后执行以下命令使环境变量生效：

```bash
source ~/.bashrc
```

### 四、安装Python依赖

进入ESP-IDF目录并安装所需的Python包：

```bash
cd $IDF_PATH
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

### 五、编译和烧写示例程序

#### 1. 编译示例程序

进入ESP-IDF的示例目录并编译`helloworld`示例：

```bash
cd $IDF_PATH/examples/get-started/helloworld
idf.py set-target esp32
idf.py build
```

#### 2. 烧写程序到ESP32

在烧写程序之前，需要给USB设备增加读写权限：

```bash
sudo usermod -a -G dialout $USER
sudo reboot
```

重启系统后，连接ESP32开发板，长按`BOOT`键，然后执行以下命令烧写程序：

```bash
idf.py flash
```

### 六、验证环境

使用串口终端工具（如`minicom`）查看ESP32的打印信息：

```bash
sudo apt install minicom
minicom -b 115200 -o -D /dev/ttyUSB0
```

如果一切顺利，你应该能看到`Hello world!`的打印信息。

### 七、常见问题及解决方法

#### 1. CMake版本过低

如果编译时提示CMake版本过低，可以安装最新版本的CMake：

```bash
sudo apt remove cmake
sudo apt install software-properties-common
sudo add-apt-repository ppa:kitware/cmake
sudo apt update
sudo apt install cmake
```

#### 2. 编译时提示无g++编译器

安装g++编译器：

```bash
sudo apt install build-essential
```

### 八、总结

通过以上步骤，你应该能够在Ubuntu系统下成功搭建ESP32开发环境。虽然过程中可能会遇到一些问题，但只要按照步骤逐一解决，最终一定能顺利搭建完成。希望本文能帮助你快速入门ESP32开发，开启物联网项目的精彩旅程。

### 参考文献

- 乐鑫官网：Espressif Systems
- ESP-IDF文档：ESP-IDF Programming Guide

### 结语

搭建开发环境只是第一步，接下来你可以探索更多ESP32的功能和应用场景。无论是智能家居、数据采集还是其他创新项目，ESP32都能为你提供强大的支持。祝你在物联网开发的道路上越走越远！

用户名

评论内容

提交评论 重置

相关链接

- [如何在Ubuntu系统上配置并优化SSR服务端实现高效代理服务](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-shang-pei-zhi-bing-you-hua-ssr-fu-wu-duan-shi-xian-gao-xiao-dai-li-fu-wu.html)
- [如何在Ubuntu系统中通过Python脚本修改Hosts文件以配置主机名解析](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-zhong-tong-guo-python-jiao-ben-xiu-gai-hosts-wen-jian-yi-pei-zhi-zhu-ji-min.html)
- [解决Ubuntu安装后开机找不到系统盘的常见问题及解决方案](https://www.oryoy.com/news/jie-jue-ubuntu-an-zhuang-hou-kai-ji-zhao-bu-dao-xi-tong-pan-de-chang-jian-wen-ti-ji-jie-jue-fang-an.html)
- [如何在Ubuntu系统中通过编程调整屏幕分辨率的方法详解](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-zhong-tong-guo-bian-cheng-diao-zheng-ping-mu-fen-bian-lv-de-fang-fa-xiang-j.html)
- [如何在Ubuntu系统中使用Python脚本查看和管理运行内存使用情况](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-zhong-shi-yong-python-jiao-ben-cha-kan-he-guan-li-yun-xing-nei-cun-shi-yong.html)
- [如何在Ubuntu 14.04中关闭防火墙以优化编程环境配置](https://www.oryoy.com/news/ru-he-zai-ubuntu-14-04-zhong-guan-bi-fang-huo-qiang-yi-you-hua-bian-cheng-huan-jing-pei-zhi.html)
- [解决Ubuntu 14到18版本升级后系统卡顿的编程优化技巧](https://www.oryoy.com/news/jie-jue-ubuntu-14-dao-18-ban-ben-sheng-ji-hou-xi-tong-ka-dun-de-bian-cheng-you-hua-ji-qiao.html)
- [如何在Ubuntu系统下安装和配置Oracle数据库：详细步骤指南](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-an-zhuang-he-pei-zhi-oracle-shu-ju-ku-xiang-xi-bu-zhou-zhi-nan.html)
- [如何在Ubuntu 16.04中使用Vim进行高效的Python代码编辑与调试](https://www.oryoy.com/news/ru-he-zai-ubuntu-16-04-zhong-shi-yong-vim-jin-xing-gao-xiao-de-python-dai-ma-bian-ji-yu-diao-shi.html)
- [如何在Ubuntu中使用Python脚本查看和管理网络连接状态](https://www.oryoy.com/news/ru-he-zai-ubuntu-zhong-shi-yong-python-jiao-ben-cha-kan-he-guan-li-wang-luo-lian-jie-zhuang-tai.html)
- [Ubuntu系统下高效清理垃圾文件的Python脚本实现方法](https://www.oryoy.com/news/ubuntu-xi-tong-xia-gao-xiao-qing-li-la-ji-wen-jian-de-python-jiao-ben-shi-xian-fang-fa.html)
- [Ubuntu系统进入紧急模式：排查与修复指南，快速恢复编程环境](https://www.oryoy.com/news/ubuntu-xi-tong-jin-ru-jin-ji-mo-shi-pai-cha-yu-xiu-fu-zhi-nan-kuai-su-hui-fu-bian-cheng-huan-jing.html)
- [如何在Windows上安装双系统Ubuntu 16.04 LTS：详细步骤指南](https://www.oryoy.com/news/ru-he-zai-windows-shang-an-zhuang-shuang-xi-tong-ubuntu-16-04-lts-xiang-xi-bu-zhou-zhi-nan.html)
- [如何在Ubuntu 2K分辨率下编程实现自动下载高清壁纸](https://www.oryoy.com/news/ru-he-zai-ubuntu-2k-fen-bian-lv-xia-bian-cheng-shi-xian-zi-dong-xia-zai-gao-qing-bi-zhi.html)
- [如何在非双系统环境下安装Ubuntu并配置Python开发环境](https://www.oryoy.com/news/ru-he-zai-fei-shuang-xi-tong-huan-jing-xia-an-zhuang-ubuntu-bing-pei-zhi-python-kai-fa-huan-jing.html)
- [如何在Ubuntu中使用Python脚本实现无需重启获取root权限](https://www.oryoy.com/news/ru-he-zai-ubuntu-zhong-shi-yong-python-jiao-ben-shi-xian-wu-xu-zhong-qi-huo-qu-root-quan-xian.html)
- [Ubuntu系统下实现Python脚本开机自启动的详细教程与实践](https://www.oryoy.com/news/ubuntu-xi-tong-xia-shi-xian-python-jiao-ben-kai-ji-zi-qi-dong-de-xiang-xi-jiao-cheng-yu-shi-jian.html)
- [解决Ubuntu安装显卡驱动后频繁重启问题：NVIDIA驱动调试指南](https://www.oryoy.com/news/jie-jue-ubuntu-an-zhuang-xian-ka-qu-dong-hou-pin-fan-zhong-qi-wen-ti-nvidia-qu-dong-diao-shi-zhi-nan.html)
- [解决Ubuntu中Vim编辑器代码不对齐问题：配置技巧与实战](https://www.oryoy.com/news/jie-jue-ubuntu-zhong-vim-bian-ji-qi-dai-ma-bu-dui-qi-wen-ti-pei-zhi-ji-qiao-yu-shi-zhan.html)
- [Ubuntu 18.04下NVIDIA 1080显卡驱动安装与配置指南](https://www.oryoy.com/news/ubuntu-18-04-xia-nvidia-1080-xian-ka-qu-dong-an-zhuang-yu-pei-zhi-zhi-nan.html)
- [解决Ubuntu系统中编程时打字无输入法候选框的问题方法详解](https://www.oryoy.com/news/jie-jue-ubuntu-xi-tong-zhong-bian-cheng-shi-da-zi-wu-shu-ru-fa-hou-xuan-kuang-de-wen-ti-fang-fa-xian.html)
- [如何在Ubuntu系统中使用Python脚本删除新增用户账户](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-zhong-shi-yong-python-jiao-ben-shan-chu-xin-zeng-yong-hu-zhang-hu.html)
- [Ubuntu系统下使用Python脚本高效修改网络配置的详细教程](https://www.oryoy.com/news/ubuntu-xi-tong-xia-shi-yong-python-jiao-ben-gao-xiao-xiu-gai-wang-luo-pei-zhi-de-xiang-xi-jiao-cheng.html)
- [如何在Ubuntu 16.04上下载并安装AMD显卡驱动程序以优化编程环境](https://www.oryoy.com/news/ru-he-zai-ubuntu-16-04-shang-xia-zai-bing-an-zhuang-amd-xian-ka-qu-dong-cheng-xu-yi-you-hua-bian-che.html)
- [Ubuntu强制关机后如何安全重启系统以恢复编程环境](https://www.oryoy.com/news/ubuntu-qiang-zhi-guan-ji-hou-ru-he-an-quan-zhong-qi-xi-tong-yi-hui-fu-bian-cheng-huan-jing.html)
- [如何在Ubuntu系统中配置并使用dos2unix工具转换文件格式](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-zhong-pei-zhi-bing-shi-yong-dos2unix-gong-ju-zhuan-huan-wen-jian-ge-shi.html)
- [如何在Ubuntu系统中通过SSH进行远程连接与管理详解](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-zhong-tong-guo-ssh-jin-xing-yuan-cheng-lian-jie-yu-guan-li-xiang-jie.html)
- [解决Ubuntu编程环境中文乱码：Python/C++/Java开发者必看指南](https://www.oryoy.com/news/jie-jue-ubuntu-bian-cheng-huan-jing-zhong-wen-luan-ma-python-c-java-kai-fa-zhe-bi-kan-zhi-nan.html)
- [Ubuntu环境下Anaconda安装与运行指南：Python开发者必备技巧](https://www.oryoy.com/news/ubuntu-huan-jing-xia-anaconda-an-zhuang-yu-yun-xing-zhi-nan-python-kai-fa-zhe-bi-bei-ji-qiao.html)
- [Ubuntu环境下使用Shell脚本实现硬盘完全格式化及分区重建教程](https://www.oryoy.com/news/ubuntu-huan-jing-xia-shi-yong-shell-jiao-ben-shi-xian-ying-pan-wan-quan-ge-shi-hua-ji-fen-qu-zhong-j.html)
- [掌握Python技巧：在Ubuntu系统上轻松更新内核版本的完整指南](https://www.oryoy.com/news/zhang-wo-python-ji-qiao-zai-ubuntu-xi-tong-shang-qing-song-geng-xin-nei-he-ban-ben-de-wan-zheng-zhi.html)
- [如何在Ubuntu系统损坏后通过命令行重新安装编程环境与工具](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-sun-huai-hou-tong-guo-ming-ling-xing-zhong-xin-an-zhuang-bian-cheng-huan-ji.html)
- [解决Ubuntu 12.04启动卡顿：排查与优化系统启动流程的编程技巧](https://www.oryoy.com/news/jie-jue-ubuntu-12-04-qi-dong-ka-dun-pai-cha-yu-you-hua-xi-tong-qi-dong-liu-cheng-de-bian-cheng-ji-qi.html)
- [如何在Ubuntu系统中配置和使用SSR链接进行安全编程和网络访问](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-zhong-pei-zhi-he-shi-yong-ssr-lian-jie-jin-xing-an-quan-bian-cheng-he-wang.html)
- [如何在Ubuntu系统上高效安装和使用Anaconda进行Python开发](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-shang-gao-xiao-an-zhuang-he-shi-yong-anaconda-jin-xing-python-kai-fa.html)
- [如何在Ubuntu系统中使用Python脚本快速获取当前IP地址](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-zhong-shi-yong-python-jiao-ben-kuai-su-huo-qu-dang-qian-ip-di-zhi.html)
- [使用Python在Ubuntu系统下开启Wi-Fi热点：n1模块实现指南](https://www.oryoy.com/news/shi-yong-python-zai-ubuntu-xi-tong-xia-kai-qi-wi-fi-re-dian-n1-mo-kuai-shi-xian-zhi-nan.html)
- [如何在Ubuntu 18.04中使用Python脚本高效复制文件夹及其内容](https://www.oryoy.com/news/ru-he-zai-ubuntu-18-04-zhong-shi-yong-python-jiao-ben-gao-xiao-fu-zhi-wen-jian-jia-ji-qi-nei-rong.html)
- [如何在Ubuntu中使用GCC编译器创建C++动态链接库（.so文件）](https://www.oryoy.com/news/ru-he-zai-ubuntu-zhong-shi-yong-gcc-bian-yi-qi-chuang-jian-c-dong-tai-lian-jie-ku-so-wen-jian.html)
- [如何在Ubuntu 18.04双硬盘环境下优化Python开发环境配置与数据存储](https://www.oryoy.com/news/ru-he-zai-ubuntu-18-04-shuang-ying-pan-huan-jing-xia-you-hua-python-kai-fa-huan-jing-pei-zhi-yu-shu.html)
- [在Ubuntu系统中安装与配置Telegram：程序员必备的即时通讯工具指南](https://www.oryoy.com/news/zai-ubuntu-xi-tong-zhong-an-zhuang-yu-pei-zhi-telegram-cheng-xu-yuan-bi-bei-de-ji-shi-tong-xun-gong.html)
- [Ubuntu系统下彻底更换用户：命令行操作指南及注意事项](https://www.oryoy.com/news/ubuntu-xi-tong-xia-che-di-geng-huan-yong-hu-ming-ling-xing-cao-zuo-zhi-nan-ji-zhu-yi-shi-xiang.html)
- [如何在Ubuntu系统中使用命令行高效搜索特定后缀名的文件](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-zhong-shi-yong-ming-ling-xing-gao-xiao-sou-suo-te-ding-hou-zhui-ming-de-wen.html)
- [如何在Ubuntu 18.04下配置多显示器以提高Python开发效率](https://www.oryoy.com/news/ru-he-zai-ubuntu-18-04-xia-pei-zhi-duo-xian-shi-qi-yi-ti-gao-python-kai-fa-xiao-lv.html)
- [如何在Ubuntu系统中查看C/C++预处理后的源代码文件](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-zhong-cha-kan-c-c-yu-chu-li-hou-de-yuan-dai-ma-wen-jian.html)
- [解决Ubuntu中文显示乱码：Python脚本一键配置语言环境](https://www.oryoy.com/news/jie-jue-ubuntu-zhong-wen-xian-shi-luan-ma-python-jiao-ben-yi-jian-pei-zhi-yu-yan-huan-jing.html)
- [解决Ubuntu 18.10编程环境不稳定问题：优化配置与常见故障排除](https://www.oryoy.com/news/jie-jue-ubuntu-18-10-bian-cheng-huan-jing-bu-wen-ding-wen-ti-you-hua-pei-zhi-yu-chang-jian-gu-zhang.html)
- [解决Ubuntu系统网络已连接但无法上网的编程调试技巧](https://www.oryoy.com/news/jie-jue-ubuntu-xi-tong-wang-luo-yi-lian-jie-dan-wu-fa-shang-wang-de-bian-cheng-diao-shi-ji-qiao.html)
- [如何在Ubuntu 16.04中配置编程项目的开机自启动服务：完整指南](https://www.oryoy.com/news/ru-he-zai-ubuntu-16-04-zhong-pei-zhi-bian-cheng-xiang-mu-de-kai-ji-zi-qi-dong-fu-wu-wan-zheng-zhi-na.html)
- [解决安装CUDA后Ubuntu无法进入的问题：详细排查与修复步骤](https://www.oryoy.com/news/jie-jue-an-zhuang-cuda-hou-ubuntu-wu-fa-jin-ru-de-wen-ti-xiang-xi-pai-cha-yu-xiu-fu-bu-zhou.html)

![云原生实践](https://www.oryoy.com/uploads/202312/05/3495ff32eef34d5b.webp)

云原生实践

- [Home](https://www.oryoy.com/)
- 搜索

最新文档

[掌握Ubuntu系统，轻松下载安装软件：新手必看教程！](https://www.oryoy.com/news/zhang-wo-ubuntu-xi-tong-qing-song-xia-zai-an-zhuang-ruan-jian-xin-shou-bi-kan-jiao-cheng.html)

发表于 2025-04-06

[Ubuntu音视频播放全攻略：轻松解决播放难题，享受视听盛宴！](https://www.oryoy.com/news/ubuntu-yin-shi-pin-bo-fang-quan-gong-lve-qing-song-jie-jue-bo-fang-nan-ti-xiang-shou-shi-ting-sheng.html)

发表于 2025-04-06

[Ubuntu一键安装：轻松开启编程之旅，热门软件一网打尽！](https://www.oryoy.com/news/ubuntu-yi-jian-an-zhuang-qing-song-kai-qi-bian-cheng-zhi-lv-re-men-ruan-jian-yi-wang-da-jin.html)

发表于 2025-04-06

[揭秘Ubuntu系统在企业级应用中的优势与挑战](https://www.oryoy.com/news/jie-mi-ubuntu-xi-tong-zai-qi-ye-ji-ying-yong-zhong-de-you-shi-yu-tiao-zhan.html)

发表于 2025-04-06

[解锁教育新可能：Ubuntu系统打造专属学习平台](https://www.oryoy.com/news/jie-suo-jiao-yu-xin-ke-neng-ubuntu-xi-tong-da-zao-zhuan-shu-xue-xi-ping-tai.html)

发表于 2025-04-06

[揭秘Ubuntu系统：开源项目的魅力与挑战](https://www.oryoy.com/news/jie-mi-ubuntu-xi-tong-kai-yuan-xiang-mu-de-mei-li-yu-tiao-zhan.html)

发表于 2025-04-06

[探索Ubuntu与Linux家族：差异与特色全解析](https://www.oryoy.com/news/tan-suo-ubuntu-yu-linux-jia-zu-cha-yi-yu-te-se-quan-jie-xi.html)

发表于 2025-04-06

[深度探索：精选Ubuntu技术博客，助你成为Linux高手](https://www.oryoy.com/news/shen-du-tan-suo-jing-xuan-ubuntu-ji-shu-bo-ke-zhu-ni-cheng-wei-linux-gao-shou.html)

发表于 2025-04-06

1. [引言](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-0)
2. [一、准备工作](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-1)
3. [1. 硬件要求](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-2)
4. [2. 软件要求](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-3)
5. [二、安装依赖](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-4)
6. [三、下载和配置ESP-IDF](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-5)
7. [1. 克隆ESP-IDF源代码](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-6)
8. [2. 下载编译工具链](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-7)
9. [3. 设置环境变量](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-8)
10. [四、安装Python依赖](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-9)
11. [五、编译和烧写示例程序](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-10)
12. [1. 编译示例程序](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-11)
13. [2. 烧写程序到ESP32](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-12)
14. [六、验证环境](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-13)
15. [七、常见问题及解决方法](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-14)
16. [1. CMake版本过低](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-15)
17. [2. 编译时提示无g++编译器](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-16)
18. [八、总结](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-17)
19. [参考文献](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-18)
20. [结语](https://www.oryoy.com/news/ru-he-zai-ubuntu-xi-tong-xia-da-jian-esp32-kai-fa-huan-jing-cong-ling-kai-shi-pei-zhi-yu-ce-shi.html#toc-19)

© 2025 云原生实践 [闽ICP备2022018693号](https://beian.miit.gov.cn/)
