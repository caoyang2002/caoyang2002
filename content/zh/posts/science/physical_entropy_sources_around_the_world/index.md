+++
title = "世界上的物理熵源"
date = 2026-11-24T07:24:45+08:00
draft = false
author = "simons"
categories = ["科学"]
tags = ["随机", "熵", "科学"]
+++

计算机天生是确定性的，算法无法凭空创造出真正的随机性。因此，当需要最高级别的安全随机数时，系统必须向物理世界“借取”不可预测性——这就是**物理熵源**。

它捕捉的是自然界中那些原则上无法被预测和复现的现象，将其转化为数字世界中的随机“种子”。

# 第一类：Cloudflare的“熵墙”——工程创意与象征

查看原文：https://blog.cloudflare.com/zh-cn/harnessing-office-chaos/

网络安全公司 Cloudflare 将这一理念做成了引人注目的实体装置。这些装置部署在其全球各地办公室，统称为“熵墙”，采集的数据通过 **LavaRand** 系统汇入其加密基础设施。

## 旧金山：熔岩灯墙 (Lava Lamp Wall)

![Lava Lamp Wall](https://blog.cloudflare.com/content/images/2017/11/lava-lamps.jpg)

这是 LavaRand 的起点，一面由约 **100 盏**熔岩灯组成的墙。灯内蜡质的流动形态永不重复，一台摄像机持续拍摄图像，每一个像素都被转化为数值。环境的细微变化——光线闪烁、路人走过——都会改变最终图像，使其无法被复制



## 伦敦：双摆墙 (Wall of Double Pendulums)

![Wall of Double Pendulums](https://www.ianvisits.co.uk/articles/wp-content/uploads/sites/2/2024/03/cloudflare-swining-pendulum-01.jpg)

双摆是混沌系统的经典范例，对初始条件极度敏感。哪怕最轻微的气流扰动，都会让后续的摆动轨迹变得完全不同。摄像机追踪这些“优雅的混沌”，将摆动中投下的变幻阴影转化为随机数据。

## 里斯本：波浪机墙 (Wall of Wave Machines)

原文：https://blog.cloudflare.com/chaos-in-cloudflare-lisbon-office-securing-the-internet-with-wave-motion/

![Wall of Wave Machines](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44CJEYQF3K0YD2JCZ8V555.JPG&w=715&h=475&f=webp&fit=cover&position=center)

2025年3月投入使用，由 **50 台**波浪机组成，每台装有约 **500 毫升**液体，每分钟产生约 **15 次**波浪。其设计致敬了葡萄牙的海洋探索历史。摄像头捕捉不断变化的波浪形态、光影乃至传感器噪声，将每一帧图像哈希后作为随机种子。

## 奥斯汀：悬浮彩虹 (Suspended Rainbows)

![Hanging rainbow mobiles in Cloudflare’s Austin office.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47PHR0FF2CKBGVBTENQDTX.png&w=715&h=703&f=webp&fit=cover&position=center)

一个半透明的彩虹色动态雕塑装置。它的运动受环境气流等因素影响，产生不可预测的形态变化，从而贡献熵源。

# 第二类：TRNG中的物理熵源——技术谱系

在芯片和硬件安全模块中，物理熵源的选择范围要广阔得多，核心目标是在微观尺度上捕捉不可预测的物理噪声。

## 热噪声 (Thermal Noise)

![img](https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f6/JohnsonNoiseEquivalentCircuits.svg/250px-JohnsonNoiseEquivalentCircuits.svg.png?utm_source=zh.wikipedia.org&utm_campaign=parser&utm_content=thumbnail)导体中电子的热运动会产生微小的电压波动，即约翰逊-奈奎斯特噪声。这种波动源于热力学定律，无法被建模或预测。TRNG 通过放大这种模拟噪声，再将其转换为数字比特流来提取随机性。



## 环形振荡器抖动 (Ring Oscillator Jitter)

由奇数个反相器构成的环形振荡器，其振荡周期并非绝对稳定。温度、电压的微观涨落和电磁干扰会导致每次翻转的时机产生微小的“抖动”。通过在高频下采样这种时序漂移，就能捕获硬件层面的随机性。



## 量子光子源 (Quantum Photonic Source)

量子随机数发生器利用的是亚原子层面根本的概率性。例如，将一个单光子射向一个**50/50 分束器**，它会以完全相等的概率选择两条路径之一。这个选择在量子力学框架下是绝对随机的，无法被任何“更深的”理论所预测，从而产生一个“无懈可击”的随机比特。



## 其他经典物理熵源
此外，**放射性衰变**本身作为一种量子过程，也常被独立用作熵源（如 HotBits 系统）；而**大气噪声**——源于全球范围内不可预测的雷电活动——则是 Random.org 等服务的数据基础。

