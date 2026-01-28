+++
title = '高二学生自制火箭'
date = 2026-01-28T18:50:09+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
+++

推荐[查看原文](https://www.kechuang.org/t/89400)，原文中有视频。

本文是一枚小型火箭从设计到制造再到发射的全部过程。  

大家好，我是一名高一升高二的学生，我利用暑假来制作这枚火箭。

  
# 一、设计理念及整箭设计图  

该枚火箭，计划采用32mm*150mm一次性固体发动机，箭体使用45mm*39mm*400mm牛皮纸桶，无飞控，使用延时开伞，预计飞行最大高度500m。  

![image.png](https://img.kechuang.org:81/r/344768?c=resource)

这是用open rocket画出的设计图，箭体内的四个舱室从左到右分别装的是：降落伞；隔热层和开伞药；开伞控制系统；发动机。

# 二、发动机的制作  

发动机的壳体是一段长15cm，外/内直径分别为32.5/24.5毫米的PPR冷水管，喷口和堵头均为堵漏王，并打入螺丝钉来保证喷口和堵头不飞出。

![QQ图片20230729220812.jpg](https://img.kechuang.org:81/r/344772?c=resource)

上图是发动机尺寸图（发动机中固定堵头和喷口的八颗螺丝钉未在图上标出）

下图是内弹道模拟

![image.png](https://img.kechuang.org:81/r/344774?c=resource)

  
发动机的装配顺序为

a：在发动机底部灌装堵漏王作为堵头，并在凝固前打入四颗螺丝钉固定

b：熬制燃料，并灌装燃料进发动机

c：使用四氟乙烯棒通出燃料内孔

d：等待燃料冷却，在燃料径面上覆盖一块形状与ppr管内圆形状相同的圆形硬纸板，防止在灌装喷口时堵漏王下渗。

e：在发动机顶端灌装堵漏王，并用四氟乙烯棒通出喷口，在堵漏王凝固前打入四颗螺丝固定

f：待堵漏王凝固，用一根合适尺寸的十字螺丝刀将燃料与喷口之间夹着的硬纸板捅破。

g：在燃料内孔中加入少量红磷，作为点火药

h：用保鲜膜和皮筋密封，待用  

燃料的熬制我参考的是论坛中的这篇文章《标准化的KNSB工艺》（目前被禁了）。

在此不对燃料的制作做过多展示。

![WIFI0s0-1218053167IMG_20230429_021716.jpg](https://img.kechuang.org:81/r/344769?c=resource)

下图为融化过后的knsb燃料

![WIFI0s0367557099IMG_20230429_023753.jpg](https://img.kechuang.org:81/r/344770?c=resource)

和文章“标准化的knsb工艺”不同的是，我在燃料熔化后，加入了燃料质量的千分之三的月桂醇醚硫酸钠作为表面活性剂使燃料的流动性增强，以便于稍后的燃料装填。  

![WIFI0s030858882IMG_20230429_020429.jpg](https://img.kechuang.org:81/r/344771?c=resource)

燃料装填完毕  

![WIFI0s0307908132IMG_20230429_034752.jpg](https://img.kechuang.org:81/r/344773?c=resource)

这是完工后的照片，质量为162g。

【视频】

这个发动机是我之前制作的一个规格相同的发动机，唯一区别是这个发动机没有加装点火药，所以可以看到当点火头点燃后，发动机延迟了较长时间才开始输出推力。

由于是垂直测量推力，所以推力的测量结果会因发动机重力的改变而不准，但其推力数据仍有利用价值。

选取几个时间点对应的推力值，可绘制出该发动机的推力-时间函数图，求出曲线与x轴围成的面积，进而推算出总冲。

很抱歉，我在整理电脑时将此推力-时间函数图搞丢了，所以不能呈现推力曲线了。

该发动机总冲约为73Ns，最大推力约为62N，可以看出73Ns的总冲和内弹道模拟的72Ns总冲基本一致。



# 三、开伞系统的制作

关于火箭的开伞动力，我使用火药爆炸作为降落伞弹出的动力来源，因为相较于其他开伞方式（弹簧弹射，壳体分裂释放降落伞等），火药弹射使用的机械零部件少，对零件制作工艺要求低，且材料易制得，对于我这种既要省钱又制作经验不足的初学者很是适用。

开伞药采用的是“绯红之粉”，由硝酸钾，抗坏血酸，氧化铁为原料制作，这个开伞药的制作方法可以在论坛中找到，详情见[绯红之粉(一种开伞剂)](https://www.kechuang.org/t/87751 "绯红之粉(一种开伞剂)")。

关于火箭的开伞控制，我使用一个简单的延时电路用来控制，它的部件全部可以在淘宝买到，且电路简单，不需要进行编程。![_745423504__894a0c488dfd7631c817798035873462_1889925808_Screenshot_20230729_235158_com.taobao_0_wifi_0.jpg](https://img.kechuang.org:81/r/344775?c=resource)

核心是一个这样的延时模块，它本质上就是一个会延时的继电器，当有电流流进控制端时，继电器会延时相应的时间再产生闭合。

由于这个模块需要5v的电压控制，我计划使用的锂电池电压在3.7v左右，所以还需要一个升压模块来为锂电池升压。![_323763490__e9bbd1292d25a84683e83cfdf84cc9ba_-1231027757_Screenshot_20230729_235227_com.taobao_0_wifi_0.jpg](https://img.kechuang.org:81/r/344776?c=resource)

但是光有延时还不够，为了让火箭精准的在最高点开伞，我希望开伞系统能在火箭升空的一瞬间开始通电计时，所以，我在电路中加装了一个常闭的继电器，当火箭处于待发射阶段时，继电器的电磁铁处于通电状态，电路断开。当火箭起飞，控制继电器的一根导线由于连接在地面上而被拉断，使继电器闭合进而开始计时。

这是电路图![无标题.png](https://img.kechuang.org:81/r/344777?c=resource)

  

  

  

  

  

  

来自：[航空航天](https://www.kechuang.org/f/74) / [喷气推进](https://www.kechuang.org/f/89)

7

 

 

 分享

 

![](https://img.kechuang.org:81/a/66ac3de59eafc7ef8ee9f10d?c=userAvatar)

[小叮当0312](https://www.kechuang.org/u/98137) ![](https://www.kechuang.org/statics/grade_icon/v3l.png "十步芳草")作者

2年6个月前 IP:河南

923496

 

[1楼](https://www.kechuang.org/p/923496) 

不好意思，我还没写完，本想存草稿没想到点成发布了，怎么才能删除稿件呢

引用

 

 

 

 

![](https://img.kechuang.org:81/a/6378f9310d85f5553caf04b0?c=userAvatar)

[CIT](https://www.kechuang.org/u/96650)

2年6个月前 IP:山西

923861

 

[2楼](https://www.kechuang.org/p/923861) 

不知道为什么，kc论坛里面所有的火箭飞行高度都是大概500m，他们貌似不知道500的飞行高度的难度有多少，我的C2max发动机100N的峰值推力也只能飞到300m高，而我的发动机300多克，而很多新人小小个的发动机也是预计飞行高度500m，飞行高度是可以算的，而不是简单的预估，不要看到别人随便报高度，自己也胡乱猜测高度，火箭飞行高度就算不用非常精确，也可以用高中物理加速度简单的进行计算的，因为这个涉及到你的开伞延时，如果提前开伞或者过后，你的伞绳大概率会被扯断，火箭不是模棱两可的，一定要有真实客观的数据作为支持，是要通过计算，除非你是姿态控制开伞，那你飞行时间就不用太注意

引用

 

 

 

 

![](https://img.kechuang.org:81/a/66ac3de59eafc7ef8ee9f10d?c=userAvatar)

[小叮当0312](https://www.kechuang.org/u/98137)![](https://www.kechuang.org/statics/grade_icon/v3l.png "十步芳草")作者

2年4个月前 IP:河南

925361

 

[3楼](https://www.kechuang.org/p/925361) 

很抱歉让这个帖子空在这里这么久，我来补一下发射视频

  

Play

00:00

00:00

Mute

Settings

PIPEnter fullscreen

Play

仅供内部学术交流或培训使用，请先保存到本地。本内容不代表科创观点，未经原作者同意，请勿转载。

 点击下载  预览

petal_20230818_134005.mp4  点击下载 ‎

我没有回收到火箭，搜索了周围的好几块玉米地都没有找到。

点火药应该被激发了，因为我听到了爆炸的声音，但是我没有看到降落伞。

这次发射的天气实在是不佳，云层的背景阻碍了我观察火箭轨迹。

很抱歉，这次火箭发射没有进行测高，也没有搭载任何仪器，只能算是对发动机的一次实际可行性验证。

未来我将在此火箭的基础下改进开伞系统，增加地面试验，以保证下一次发射的成功开伞。同时搭载航电系统，功能包括气压传感器，GPS模块以及图传模块。

此贴结束，欢迎各路大佬前来批评指正。

  

  

  

  

引用

 

 

 

 

![](https://img.kechuang.org:81/a/636654a0630cea3944a6409d?c=userAvatar)

[篝火旁](https://www.kechuang.org/u/98032)![](https://www.kechuang.org/statics/grade_icon/v0l.png "实习会员")

1年7个月前 IP:江苏

933602

 

[4楼](https://www.kechuang.org/p/933602) 

不知道楼主还在吗？能否告知继电器型号

  

引用

 

 

 

 

![](https://img.kechuang.org:81/a/65a412e247fe9b7fc40261c3?c=userAvatar)

[月光](https://www.kechuang.org/u/100243)![](https://www.kechuang.org/statics/grade_icon/v1l.png "浪迹天涯")

1年7个月前 修改于 1年7个月前 IP:江苏

933603

 

[5楼](https://www.kechuang.org/p/933603) 

> 引用[篝火旁](https://www.kechuang.org/u/98032)发表于[4](https://www.kechuang.org/p/933602?redirect=true)楼的内容
> 
> 不知道楼主还在吗？能否告知继电器型号

图上有写 [SRD-05VDC-SL-C](https://www.kechuang.org/l?t=aHR0cHM6Ly9pdGVtLnN6bGNzYy5jb20vMzY0MjIuaHRtbD9mcm9tWm9uZT1zX3NfXyUyNTIyU1JELTA1ViUyNTIy "SRD-05VDC-SL-C")  

![image.png](https://img.kechuang.org:81/r/355312?c=resource)

 **加载全文**

 

引用

 

 

 

 

![](https://img.kechuang.org:81/a/66ac3de59eafc7ef8ee9f10d?c=userAvatar)

[小叮当0312](https://www.kechuang.org/u/98137)![](https://www.kechuang.org/statics/grade_icon/v3l.png "十步芳草")作者

1年7个月前 IP:河南

933631

 

[6楼](https://www.kechuang.org/p/933631) 

嗯是的.....其实可以用mos管代替的......这枚一年前的窜天猴技术含量太低了，发动机也太辣鸡了，我现在在逐步向科创主流的火箭设计靠拢 ![sticker](https://img.kechuang.org:81/sticker/310082)

引用

 

 

 

 

![](https://img.kechuang.org:81/a/67782b1ff2e57372eefada9e?c=userAvatar)

[Log锦霖03](https://www.kechuang.org/u/106037)![](https://www.kechuang.org/statics/grade_icon/v0l.png "实习会员")

1年0个月前 IP:广东

940962

 

[7楼](https://www.kechuang.org/p/940962) 

Lz，不对啊，我怎么没有复刻出“绯红之粉”出来的东西，燃的太难了，火苗也很小