+++
title = '发动机系统设计与仿真'
date = 2026-02-01T11:01:18+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
cover = "https://p.cgmol.com/20240813/b_689892_14615430252152303.png"
+++

[查看原文](https://www.kechuang.org/t/88458)

计划利用一定的时间和篇幅，对现有工业界常用的液体、固体、固液混合等主流火箭发动机的设计仿真工具进行梳理总结，给出适用于初学者的中文版用户手册。理论综述与软件总结主要面向系统设计仿真，轻微涉及三维部组件设计仿真，至于较新的基于模型的系统工程方法（MBSE），则由于其需要较扎实的理论和工程基础，后续计划进行简要的入门介绍。

主要目的有两个：
一是尽可能使得现有火箭航模爱好者的理论和技术工具更为扎实，尽快脱离看火听响、盲目试错的层次水平；二是激发爱好者专业研究的兴趣，引到有意识地阅读专业文献，使用专业工具，吸引更多新生力量加入航空航天专业研究。

本文会在后续持续更新，将结合笔者自身的代码、软件经验，并尽可能充分梳理论坛前期的各种工具、国外流行的软件方法，适度开源源码和用户手册，争取形成一个成熟可用的设计与仿真体系。


引言：在KC群里看到很多同学在做一些固体、液体甚至是固液混合的火箭发动机的研究。但可能由于主要是本科及以下的爱好者，大家在理论、工具等方面均有较大欠缺，重复造轮子的情况还比较严重，以至于相当一部分同学还没有达到学校航模队的门槛。火箭爱好是一个较为宽泛的范畴，最初步的理解可能就是做一个火箭，这是典型的系统研究。当然，也有喜欢做精、做细分单元的同学，这也很值得鼓励，实质上每个单机、甚至于一个小电路都是很有价值的，科学研究不会只看大而全，一个看似漂亮的吸人眼球的模型火箭，其实际价值和意义可能还不如一个精巧的电路设计、一次完善新颖的单机测试（例如具备一定的专利或者论文潜力）。各种爱好都应该得到尊重，并且更加鼓励爱好者深入细分领域做研究，而不是人人都要当“总师”，追逐“一人全能”这种虚假的荣誉。

回到我们所关心的问题本身。事实上，大多数刚入门的爱好者都还是喜欢做总体，那么我们就需要知道：系统设计与仿真技术是一个综合程度较高的学科，一定要认识到，一个人的能力是有限的，真正的总体并不是现下火热吸睛的“一个人搞全套，一人把火箭全做完”的噱头，而是对所研究对象的数理模型有深入了解，具备系统工程概念，善于分配指标并能有力统筹各细分专业。鼓励大家合作研究，既能互相取长补短、分工协作、又能集中力量办大事。当然，兴趣爱好能为大家带来成就感，并激发进一步探索的热情，这是非常值得肯定的，但更为深入的研究需要进一步地学习深造，例如进入相关机构和单位开展学术性或工程性的研究。否则只能是不了了之，纸上谈兵了。

本文结合笔者工作学习实际，计划以研究中所涉及的一些公开试验以及国内外典型公开资料为例，对现在业余/工业界常用的液体、固体、固液混合等主流火箭发动机的设计理论、仿真工具进行综述，并尽可能提供中文用户手册。一些详细的内容如果较长，将直接提供推荐权威教材名称或相关学术论文，内容以经典教材为主，笔者本人的部分研究论文为辅。后续帖子中所涉及的理论与软件工具案例主要面向系统设计仿真，少部分涉及三维部组件设计仿真，最后对基于模型的系统工程方法（MBSE）进行介绍，以期能够抛砖引玉，为同学们未来的深入研究提供帮助。

内容：

1. 系统设计理论（以文献和学生作业算例为主）

1.1 火箭发动机原理基础

1.2 喷管设计理论

1.3 热力学计算方法

1.4 系统设计平衡计算与指标分配

1.5 组件设计与参数确认

1.6 总装与工艺

1.7 试验与校准

1.8 航空航天项目与质量管理

2. 热力学计算工具

2.1 KC常用热力学软件及其汉化版本

  2.1.1 PROPEP（汉化后KCPEP2）

  2.2.2 cpropep（汉化后CpropepShell_cn）

2.2 教学与自编软件工具

  2.2.1 课题自行开发的matlab程序

  2.2.2 学生教学程序（Access to TPEQUIL,HPFLAME and UVFLAME Software）

  THU热能工程系自用碳氢化合物-空气燃烧产物平衡产物计算机编码，与Stephen R. Turns的《燃烧学导论:概念与应用》（第2版）配套使用。

  2.2.3 自用某型俄罗斯热力学计算程序（俄文）

2.3 NASA CEA程序及二次开发

![demo3.png](https://img.kechuang.org:81/r/336852?c=resource)

3. 液体火箭发动机系统设计方法及软件工具应用

3.1 科创论坛设计软件

  3.1.1 Rocket Designer/Rocket Designer System V2.0 （RD.exe）

  3.1.2 液机内弹道V1.0/V2.0

  3.1.3 简单matlab案例

3.2 半专业RPA液体火箭发动机设计工具及二次开发

![demo2_1.png](https://img.kechuang.org:81/r/336851?c=resource)

![demo2.png](https://img.kechuang.org:81/r/336850?c=resource)

3.3 工程专业系统设计工具案例与论文复现

  3.3.1 火箭发动机静特性工程求解器

  3.3.2 火箭发动机系统动/静特性通用代码

​    matlab.m/C++/Fortran

  3.3.3 基于simulink的火箭发动机系统动态特性仿真

  3.3.4 火箭发动机多学科系统仿真商业平台应用实例

![demo4_1.png](https://img.kechuang.org:81/r/336855?c=resource)

3.4 组件设计案例方法



  3.4.1 阀门设计与仿真

​    几何/强度/流场设计工具实例（step by step）

​    Auto CAD/Caxa/Solidworks/NX

​    Ansys mechanical/Fluent/Star CCM/Comsol

  3.4.2 涡轮泵设计与仿真

​    CF Turbo/Simerics Pumplinx/Fluent/Star CCM

  3.4.3 管路系统设计与仿真

​    Flowmaster/Amesim

  3.4.4 热力组件设计与仿真

​    Ansys Fluent/Star CCM

3.5 总装与工艺设计方法

​    Auto CAD/Caxa/Solidworks/NX Simcenter 3D/Catia

3.6 试验设计与发动机性能校准方法

  3.6.1 试验台设计与硬件选型方法

​    PLC自动控制试车台设计/Labview专业控制试车台设计与实施/FPGA、单片机定制化控制电路设计方法

​    阀门选型/压力容器设计与选型/过程安全控制标准/传感器、仪器仪表使用及选取

![demo10.png](https://img.kechuang.org:81/r/336863?c=resource)

  3.6.2 冷流试验设计与参数分析

  3.6.3 缩尺试验设计与参数分析

![1.png](https://img.kechuang.org:81/r/325164?c=resource)

  3.6.4 半系统试验设计与数据判读

  3.6.5 全系统试验设计与故障分析

4. 固体火箭发动机设计方法及软件工具应用



4.1 科创论坛设计软件

  4.1.1 Rocket Designer/Rocket Designer System V2.0 （RD.exe）

  4.1.2 简单Excel/matlab案例

4.2 工程专业系统设计工具案例与论文复现

  4.2.1 零维内弹道求解器

​    matlab.m/C++/Fortran

![固发仿真——1.png](https://img.kechuang.org:81/r/336854?c=resource)

  4.2.2 固体火箭发动机高维内弹道仿真

​     Ansys Fluent/Rocstar

  4.2.3 固体火箭发发动机整机仿真商业平台实例

4.3 组件设计方法

   4.3.1 喷管设计与仿真

   4.3.2 壳体结构设计与仿真

   4.3.3 绝热层设计

​    Ansys Fluent/Star CCM

4.4 总装与工艺设计方法

​    Auto CAD/Caxa/Solidworks/NX Simcenter 3D/Catia

4.5. 试验设计与发动机性能校准方法

  4.5.1 固发试验台设计与硬件选型方法

  4.5.2 缩尺试验设计与参数分析

![20211030164555.png](https://img.kechuang.org:81/r/325162?c=resource)

  4.5.3 整机试验设计与故障分析

5. 固液混合火箭发动机工程设计方法及实用代码



6. 冲压发动机工程设计方法及实用程序
7. 基于MBSE的系统工程理论与应用
8. 国内外民营航空航天公司推介
9. 业余模型火箭的进展与案例



9.1 航模火箭设计工具

   9.1.1 发动机设计工具（同上并适当简化）

   9.1.2 简易火箭弹道设计工具

​    Open Rocket的使用及二次开发

![demo9.png](https://img.kechuang.org:81/r/336862?c=resource)

   9.1.3 自编火箭弹道设计工具

​    matlab.m/matlab simulink工具

9.2 航模火箭的试验与新颖玩法

   9.2.1 典型模型火箭制作与试验

​    模型制图与激光切割机的使用

​    模型装配、胶粘工艺

​    蒙皮制作

​    航模发动机的使用与发控设计

![demo8.jpg](https://img.kechuang.org:81/r/336861?c=resource)

![demo6.png](https://img.kechuang.org:81/r/336860?c=resource)

![demo7.jpg](https://img.kechuang.org:81/r/336858?c=resource)

   9.2.2 带控制的模型火箭与试验

​    受限于航模本身的特性，这里的外形与控制主要是学生概念小创造，培养兴趣爱好，锻炼动手能力。并不是真正意义上的科研研究，深入研究需要转入专业领域并从基础理论和专业试验着手。

​    另外，随着3D打印的普及，各种外形的火箭得以以较低的成本制造，上色装饰可使其具有一定的观赏性。

​    一种简易的可实施的带姿态控制的火箭控制方法如下：

![demo5.png](https://img.kechuang.org:81/r/336856?c=resource)

10. 总结展望





除经典文献外，部分仿真设计、试验来源于作者的一些公开发表的论文、多年前的一些小案例和项目，各部分内容将在后续逐渐补充，有兴趣的同学也可以参与补充与完善。





来自：[航空航天](https://www.kechuang.org/f/74) / [喷气推进](https://www.kechuang.org/f/89)严肃内容：教程/课程

1

 

 

21

 

 

 鼓励 

 

 分享

 

![img](https://img.kechuang.org:81/a/64118dae2680e8488c2f67c1?c=userAvatar)

[wchx0121](https://www.kechuang.org/u/93147) ![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)

2年11个月前 IP:陕西

918115

 

[1楼](https://www.kechuang.org/p/918115) 

您好，读了您的帖子，我受益匪浅，进一步了解了发动机设计仿真领域，想找您咨询如下两个问题，请不吝赐教：
（1）我想用simulink编写一个液体火箭发动机的动态仿真代码，目前代码编写好了，但由于很多参数不知道在什么地方找，导致求解一直无法收敛，在液体火箭发动机系统建模和仿真的学习和编程方面（什么编程语言都可以），请问能不能给点学习和编程实现的建议？
（2）您在文章说的发动机静特性工程模拟器、通用代码等，我在网上没有搜到，请问在什么地方可以查到吗？

希望得到您的回复，谢谢！！！

引用

 

评论

 

 

2

 

 

 

 

##### 请完成以下任务，获取完整发表权限。



通过入学培训



发表3条电文















































0/100000

专栏

##### 目前还不能开设专栏，通常是因为你参与讨论较少或没有文章被列入精选。

我已阅读并同意遵守与本次发表相关的全部协议。[查看协议](https://www.kechuang.org/protocol)

 

所属专业

[喷气推进](https://www.kechuang.org/f/89)

上级专业

[航空航天](https://www.kechuang.org/f/74)

同级专业

[航空技术](https://www.kechuang.org/f/165)[航天技术](https://www.kechuang.org/f/366)[火箭燃料](https://www.kechuang.org/f/368)

关注

![img](https://img.kechuang.org:81/a/5f0d65a1351a5f14687982f8?c=userAvatar)

[RD270](https://www.kechuang.org/u/79377)

![浪迹天涯](https://www.kechuang.org/statics/grade_icon/v1l.png)机友 笔友

文章

 

1

 

回复

 

29

 

学术分

 

0

2019/03/12注册，1年4个月前活动

火箭发动机发烧友

主体类型：个人

所属领域：无

认证方式：手机号

IP归属地：陕西

[名片](https://www.kechuang.org/u/79377)私信

作者最新文章

[开一个发动机系统设计与仿真的帖](https://www.kechuang.org/t/88458)

[喷气推进](https://www.kechuang.org/f/89)[RD270](https://www.kechuang.org/u/79377) 3年2个月前

相似文章推荐

[导弹控制系统 飞行控制系统](https://www.kechuang.org/t/34139)

[喷气推进](https://www.kechuang.org/f/89)[qq154884863](https://www.kechuang.org/u/20514) 14年10个月前

[详解固体火箭发动机（转帖）](https://www.kechuang.org/t/12724)

[喷气推进](https://www.kechuang.org/f/89)[空中米格](https://www.kechuang.org/u/2997) 17年2个月前

[“迷”火箭发射成功](https://www.kechuang.org/t/73717)

[喷气推进](https://www.kechuang.org/f/89)[京-t](https://www.kechuang.org/u/40075) 10年6个月前

[标准化拉瓦尔喷口的制造【理论+实践】](https://www.kechuang.org/t/19894)

[喷气推进](https://www.kechuang.org/f/89)[black](https://www.kechuang.org/u/4513) 16年6个月前

[【廣局神作】RNX噴燃比對比裝機測試](https://www.kechuang.org/t/46237)

[喷气推进](https://www.kechuang.org/f/89)[焓熵`](https://www.kechuang.org/u/8089) 13年10个月前

[液机历程](https://www.kechuang.org/t/38472)

[喷气推进](https://www.kechuang.org/f/89)[乖雪狼](https://www.kechuang.org/u/15987) 14年4个月前

[中国最高的硝糖火箭----远征2号探空火箭 最终报告版](https://www.kechuang.org/t/80846)

[喷气推进](https://www.kechuang.org/f/89)[1703115](https://www.kechuang.org/u/50827) 9年5个月前

[【QHarryQ Studio】征途一号（75mm小型气象火箭）成功发射](https://www.kechuang.org/t/58923)

[喷气推进](https://www.kechuang.org/f/89)[qharryq](https://www.kechuang.org/u/15291) 12年8个月前

[简单地说说火箭发动机的基础理论（一）（喷管原理及其热力学计算，不同发动机之间的](https://www.kechuang.org/t/58783)

[喷气推进](https://www.kechuang.org/f/89)[猎鹰](https://www.kechuang.org/u/19313) 12年8个月前

[【重磅发布】汉化版open Motor](https://www.kechuang.org/t/91566)

[喷气推进](https://www.kechuang.org/f/89)[就是氧化铁喽](https://www.kechuang.org/u/101243) 2个月6天前

关于

- [关于科创](https://www.kechuang.org/t/25436)
-  
- [提问须知](https://www.kechuang.org/t/36782)
-  
- [禁止事项](https://www.kechuang.org/t/66350)
-  
- [建设指南](https://www.kechuang.org/t/79481)
- [FAQ](https://www.kechuang.org/page/faq)

应用

- [计算工具](https://www.kechuang.org/tools)
-  
- [科创基金](https://www.kechuang.org/fund)
-  
- [考试系统](https://www.kechuang.org/exam)
-  
- [活动](https://www.kechuang.org/activity)

其他

- [ 上报问题](https://www.kechuang.org/problem/add)
-  
-  028-86691700
- [ Github](https://github.com/kccd/nkc)









关于

- [关于科创](https://www.kechuang.org/t/25436)
- [提问须知](https://www.kechuang.org/t/36782)
- [禁止事项](https://www.kechuang.org/t/66350)
- [建设指南](https://www.kechuang.org/t/79481)
- [FAQ](https://www.kechuang.org/page/faq)

应用

- [计算工具](https://www.kechuang.org/tools)
- [科创基金](https://www.kechuang.org/fund)
- [考试系统](https://www.kechuang.org/exam)
- [活动](https://www.kechuang.org/activity)

友情链接

- [故园艺术](https://ngy.kexinshe.com/)
- [哈罗CQ火腿社区](https://www.hellocq.net/forum/)
- [模友之吧](https://www.moz8.com/)

其他

- [ 报告问题 / 投诉](https://www.kechuang.org/problem/add)
-  028-86691700
- [ GitHub](https://github.com/kccd/nkc)

手机访问

- 

安卓客户端

- [点击下载](https://www.kechuang.org/app)

##### 本站所有内容由网友发布，不代表本站观点。如涉嫌侵犯您的权利，请通过举报或报告问题/投诉功能发送通知。

##### 科创研究院 (c)2001-2024[蜀ICP备11004945号-2](https://beian.miit.gov.cn/)[川公网安备51010802000058号](https://www.beian.gov.cn/)
