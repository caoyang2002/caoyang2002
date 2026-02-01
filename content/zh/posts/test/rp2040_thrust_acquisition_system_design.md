+++
title = '极简 RP2040 推力采集系统'
date = 2026-02-01T10:14:17+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
+++

[查看原文](https://www.kechuang.org/t/91248)

RP2040单片机功能强大，用在发动机推力采集上，人机界面得以简化，新手友好。尝试按以下步骤搭建：

# 一、让RP2040单片机运行

注意，这一步不需要懂单片机，不需要单片机开发程序，只需要拷个文件。拿到RP2040后，按住单片机板上左边BOOT键，通过USB线插到电脑上，然后把附件的二进制文件拷到新出现的U盘上，单片机就运行起来啦！

![attachment icon](https://www.kechuang.org/attachIcon/uf2)**1_F711_RP2040.ino.uf2**253.00KBUF264次下载

附RP2040单片机tb图，这个程序要16M那种

![Screenshot_20250613_074909.jpg](https://img.kechuang.org:81/r/372147?c=resource)

怎么知道它是不是真的在运行呢？两个办法，一是看电脑上会出现一个新的U盘，15MB 左右，这是程序创建的单片机板载U盘。另一个办法就是接着完成第二步，接个 OLED，来个实时显示。

# 二、扩展附件1，连OLED显示屏

买一个SH1106的OLED，拔下单片机（断电）焊4根线：VCC接单片机5V、GND接单片机GND、SDA接单片机GP2、SCL接单片机GP3。单片机插回电脑（这时候不按BOOT键了），应该能看到OLED亮了，完成第二步！

附tb OLED图片，这两种都行

![Screenshot_20250610_115153.jpg](https://img.kechuang.org:81/r/372025?c=resource)

3，扩展附件2，连HX711

单片机断电再焊另4根线，VCC接单片机5V、GND接GND、DAT接GP4、CLK接GP5。推力传感器也按线的颜色焊到HX711板上。为了达到80Hz采样率，需要用小刀片断开HX711背后那个RATE中间细细的连接处。这样整个系统软硬件就都完成啦！重新插回电脑，手压传感器能看到OLED显示的推力变化。

附tb HX711及传感器图片，这种紫色板比较好，设置采样率rate也容易些：

![Screenshot_20250610_115335.jpg](https://img.kechuang.org:81/r/372026?c=resource)

![Screenshot_20250610_115543.jpg](https://img.kechuang.org:81/r/372027?c=resource)

完成的系统如图

![IMG_20250609_212946.jpg](https://img.kechuang.org:81/r/372020?c=resource)

可以装到一个聚碳酸酯盒子里，装上电池使用（这个照片里单片机还不是RP2040，仅供参考）。电池正极接到OLED的Vcc就行啦，正极线串入一个肖特基二极管（热缩管鼓起那里），以免忘了取出电池就插电脑，以及电池装反（有次黑灯瞎火搞就装反过！），我一般都是抠掉电池再插电脑或手机，勤快的可以给装上个开关。

![IMG_20250712_195025_edit_178769100061262.jpg](https://img.kechuang.org:81/r/373384?c=resource)

照片中接的是30MPa压力传感器，用来测试燃烧室压力、测量燃速压力系数都很合适，这个采集盒也是兼容的，直接接上4根线就能用，校准需要找个带表头的空压机。

气压传感器型号见图，4条线的颜色跟HX711接口都是对应上的，直接兼容。

![Screenshot_20250829_160830.jpg](https://img.kechuang.org:81/r/376292?c=resource)![Screenshot_20250829_160724.jpg](https://img.kechuang.org:81/r/376291?c=resource)

盒子的tb图片，下方10cm大的那种，聚碳酸酯材质的，盖子炸飞了都没坏！

![Screenshot_20250610_120740.jpg](https://img.kechuang.org:81/r/372028?c=resource)

再看看使用说明，是不是也很简单呢：

1，每次上电系统会自动去皮归零，然后进入定时采样，20ms一次。连续3个采样点推力大于50g会启动点火，然后连续采集10s后停止采样，计算并显示推力曲线及总冲量。

2，连接单片机到电脑或手机，会出现一个新U盘，里面有3个数据文件，一是校准文件Clb，二是运行计数Cnt，三是推力数据Run001。以后每次重新上电采集，会生成一个新的数据文件，文件名序号增Run00x。数据文件可以直接拷贝到电脑或手机上。不删除的情况下，这几个文件可以一直掉电保存，存到5000次试车数据后，文件名回到Run001覆盖之前数据。连电脑试车的情况下，也可以通过串口调试软件，实时传输推力数据至电脑。

3，校准，上电后（自动去皮后），拿一个已知重量的物体放推力台上（试车台竖直向下），如果物体重1000g，测得推力数值是210g，就把Clb文本文件里的1000000改成210000。再次重新上电测量，推力值就会变成1000g左右，这个值也会掉电保存，除非手动修改或删除。



系统的工作原理简介（供爱好者研究、并提改进建议，仅关心使用的可忽略）

1 单片机软件，使用Ardunio IDE编程，主要参考RP2040 C/C++ SDK手册及https://github.com/earlephilhower/arduino-pico，代码有点长290行，编译为二进制文件后使用。RP2040支持直接拷贝二进制程序，按住BOOT插USB的情况下，板载flash程序段会在电脑上显示为一个U盘，把arduino等单片机开发软件编译好的二进制文件拷到U盘里，单片机马上就会运行程序。所以不需要使用者懂单片机，不需要开发软件及准备各种库，拷完文件单片机马上就运行起来了。

2单片机内部程序流程

每次重新上电后，会自动运行一次去皮程序，测推力100次，取后50次平均值作去皮值，后续测量值都会减去这个值；

启动每20ms一次的定时中断，指向一个推力采集程序F_Smp；

初始化OLED显示；

生成或读取校准文件Clb.txt；

板载文件系统FATFSUSB程序，自动生成或打开一个电脑能访问的新U盘，对应板载flash的数据段，用于数据存储。

进入主循环loop程序，就是不停刷新OLED，实时显示推力值display.print(F);

每20ms定时中断会打断一下loop的OLED显示，跳转至推力采集程序F_Smp，每次只采集一个数据点；

推力采集程序包含点火启动判断，连续3个采样点推力大于50g为点火开始，数据点依次存入数组F0[500]。记录点达到498也就是接近10s之后，停止中断程序，也就停止了推力采集，还设置了一个循环存储以保存点火前一小段数据点到F0数组。最后一个采集点后，计算总冲，也就是从点火启动到最末大于50g（连续3个）的推力值 x 0.02秒累加。

最后一个采集点内还包含数据文件生成程序，第一次运行会建立计数文件Cnt.txt，从1开始以后每次加1，生成数据文件名从Run001开始，根据Cnt生成新文件名每次累加1。

最后loop主循环中OLED显示推力曲线，程序会自动调整XY显示范围。以及

FatFS.begin();
FatFS.end();
FatFSUSB.begin();

再次允许运行电脑或手机访问程序创建的板载U盘，以拷走数据或修改校准系数等。

源代码以文本文件附上：



![attachment icon](https://www.kechuang.org/attachIcon/txt)**1_F711_RP2040.txt**7.87KBTXT31次下载

另外还测试了低成本版，RP2040 2M flash单片机只要7.5元！OLED也是只要9多块钱

![Screenshot_20250615_192017.jpg](https://img.kechuang.org:81/r/372244?c=resource)

程序需要这个2M flash的

![attachment icon](https://www.kechuang.org/attachIcon/uf2)**F711_RP2040_2M.ino.uf2**252.50KBUF215次下载

试车台可以参考以前帖子，也是结构简单，就3个零件加几颗螺丝，大L型材底座、小L型材连接、U型槽用于绑发动机。

![IMG_20250512_191031.jpg](https://img.kechuang.org:81/r/372049?c=resource)![IMG_20250509_210039.jpg](https://img.kechuang.org:81/r/372050?c=resource)![IMG_20250415_170852.jpg](https://img.kechuang.org:81/r/372052?c=resource)

最后这个是炸机的后果，以警醒大家要千万小心，要躲在掩体后面试车，祝大家玩得安全开心！













[修改于 5个月5天前 - 2025/08/29 16:11:54]

来自：[电子信息](https://www.kechuang.org/f/222) / [电子技术](https://www.kechuang.org/f/37)，[航空航天](https://www.kechuang.org/f/74) / [喷气推进](https://www.kechuang.org/f/89)动手实践：实验报导严肃内容：教程/课程

36

 

 

 

 

 分享

 

![img](https://img.kechuang.org:81/a/678f6a97df4d46d73064a707?c=userAvatar)

[ZZCjas](https://www.kechuang.org/u/106216) ![浪迹天涯](https://www.kechuang.org/statics/grade_icon/v1l.png)

7个月25天前 IP:湖北

944778

 

[1楼](https://www.kechuang.org/p/944778) 

好教程![😆](https://www.kechuang.org/statics/fluentui-emoji/1f606.png)，感谢大佬分享！



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/6902178b82ff939ddb258bdd?c=userAvatar)

[柠檬酸hp](https://www.kechuang.org/u/106613)![一表人才](https://www.kechuang.org/statics/grade_icon/v2l.png)

7个月25天前 IP:江苏

944785

 

[2楼](https://www.kechuang.org/p/944785) 

厉害



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)作者

7个月23天前 IP:北京

944840

 

[3楼](https://www.kechuang.org/p/944840) 

更正了一个小bug：![Screenshot_20250613_094031_edit_489800961236198.jpg](https://img.kechuang.org:81/r/372149?c=resource)

这里x1.0先转换成浮点数。



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67fbde9573e858be0314a327?c=userAvatar)

[TK_2410](https://www.kechuang.org/u/107430)![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)

7个月14天前 IP:江苏

944992

 

[4楼](https://www.kechuang.org/p/944992) 



感谢！很喜欢楼主的OLED板子，很方便且直观。

我还不懂编程，只是个普通高中生，不过楼主提供了很好的可供实践的方法，过几天暑假时来尝试一下![☺️](https://www.kechuang.org/statics/fluentui-emoji/263a-fe0f.png)



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)作者

7个月13天前 IP:北京

944998

 

[5楼](https://www.kechuang.org/p/944998) 

是啊先买一套连起来看看，能亮起来再说，买上面回复里说那两个便宜的就行。RP2040的好处是可以直接拷执行文件运行，先运行起来再试着去编代码。我有个工程实践课，其中有个6小时单片机教程（动手能力强的3小时就够），教生物专业本科生新手的，或许可以整理一下暑假发到KC上



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67fbde9573e858be0314a327?c=userAvatar)

[TK_2410](https://www.kechuang.org/u/107430)![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)

7个月8天前 IP:江苏

945104

 

[6楼](https://www.kechuang.org/p/945104) 



小白的一个疑问![Screenshot_20250627_211513.jpg](https://img.kechuang.org:81/r/372674?c=resource)单片机上的GP2、GP3是右边从上往下第三个和第四个排母吗？![IMG_20250627_210229.jpg]()

还有OLED显示屏上排针有SCK而非SCL，是楼主字打错了吗？![IMG_20250627_210322.jpg]()

![🤔](https://www.kechuang.org/statics/fluentui-emoji/1f914.png)



 **加载全文**

 

引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)作者

7个月8天前 IP:北京

945106

 

[7楼](https://www.kechuang.org/p/945106) 

> 引用[TK_2410](https://www.kechuang.org/u/107430)发表于[6](https://www.kechuang.org/p/945104?redirect=true)楼的内容
>
> 小白的一个疑问单片机上的GP2、GP3是右边从上往下第三个和第四个排母吗？还有OLED显示屏上排针有



对的，印的那个数字就是GP0-

![Screenshot_20250627_224130.jpg](https://img.kechuang.org:81/r/372678?c=resource)



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)作者

7个月8天前 IP:北京

945107

 

[8楼](https://www.kechuang.org/p/945107) 

> 引用[TK_2410](https://www.kechuang.org/u/107430)发表于[6](https://www.kechuang.org/p/945104?redirect=true)楼的内容
>
> 小白的一个疑问单片机上的GP2、GP3是右边从上往下第三个和第四个排母吗？还有OLED显示屏上排针有

这个板子也一样![Screenshot_20250627_224428.jpg](https://img.kechuang.org:81/r/372679?c=resource)



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)作者

7个月7天前 IP:北京

945122

 

[9楼](https://www.kechuang.org/p/945122) 

> 引用[TK_2410](https://www.kechuang.org/u/107430)发表于[6](https://www.kechuang.org/p/945104?redirect=true)楼的内容
>
> 小白的一个疑问单片机上的GP2、GP3是右边从上往下第三个和第四个排母吗？还有OLED显示屏上排针有

亮了吗？![😊](https://www.kechuang.org/statics/fluentui-emoji/1f60a.png)



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67fbde9573e858be0314a327?c=userAvatar)

[TK_2410](https://www.kechuang.org/u/107430)![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)

7个月7天前 IP:江苏

945131

 

[10楼](https://www.kechuang.org/p/945131) 

![IMG_20250628_215250.jpg](https://img.kechuang.org:81/r/372695?c=resource)

这样，还差那些传感器板子杜邦线之类的，在等快递



 **加载全文**

 

引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)作者

7个月7天前 IP:北京

945132

 

[11楼](https://www.kechuang.org/p/945132) 

> 引用[TK_2410](https://www.kechuang.org/u/107430)发表于[10](https://www.kechuang.org/p/945131?redirect=true)楼的内容
>
> 这样，还差那些传感器板子杜邦线之类的，在等快递

哦哦，用杜邦线也行，我都喜欢直接焊高温导线，杜邦线爱掉



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67fbde9573e858be0314a327?c=userAvatar)

[TK_2410](https://www.kechuang.org/u/107430)![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)

7个月6天前 IP:江苏

945149

 

[12楼](https://www.kechuang.org/p/945149) 

对了，还有一个问题![Screenshot_20250629_112917.jpg](https://img.kechuang.org:81/r/372708?c=resource)

楼主用的传感器是20千克的应变压力模块，如果觉得量程小，换成其他量程的模块，能够适配现有的程序吗



 **加载全文**

 

引用

 

 

 

 

![img](https://img.kechuang.org:81/a/685bcf65c21f2c26ebf96150?c=userAvatar)

[暮羽要摸鱼](https://www.kechuang.org/u/84430)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)

7个月6天前 IP:美国

945155

 

[13楼](https://www.kechuang.org/p/945155) 

> 引用[TK_2410](https://www.kechuang.org/u/107430)发表于[12](https://www.kechuang.org/p/945149?redirect=true)楼的内容
>
> 对了，还有一个问题楼主用的传感器是20千克的应变压力模块，如果觉得量程小，换成其他量程的模块，能够适

能的，重新校准一下就可以了



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)作者

7个月6天前 IP:河北

945158

 

[14楼](https://www.kechuang.org/p/945158) 

> 引用[暮羽要摸鱼](https://www.kechuang.org/u/84430)发表于[13](https://www.kechuang.org/p/945155?redirect=true)楼的内容
>
> 能的，重新校准一下就可以了

对的，测拿个1kg重物测一下，然后把校准文档中的数改成读数克数加000



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67fbde9573e858be0314a327?c=userAvatar)

[TK_2410](https://www.kechuang.org/u/107430)![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)

7个月5天前 修改于 7个月5天前 IP:江苏

945195

 

[15楼](https://www.kechuang.org/p/945195) 



![Screenshot_20250630_230555.jpg](https://img.kechuang.org:81/r/372784?c=resource)

![IMG_20250630_225423.jpg]()![IMG_20250630_230827.jpg]()

小刀操作起来有点不顺手，效果不够美观。成品是指这样吗？

![😶](https://www.kechuang.org/statics/fluentui-emoji/1f636.png)![💦](https://www.kechuang.org/statics/fluentui-emoji/1f4a6.png)

科创上有到处找过，似乎作者是唯一一个使用紫色板HX711的



 **加载全文**

 

引用

 

 

 

 

![img](https://img.kechuang.org:81/a/602a5f1271a5a9425c194c5c?c=userAvatar)

[bs170](https://www.kechuang.org/u/90364)![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)

7个月5天前 IP:浙江

945196

 

[16楼](https://www.kechuang.org/p/945196) 

**RP2040好像说是能直接连个小屏装专用定制系统的，有试过的吗，有什么好的用处**



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)作者

7个月5天前 IP:北京

945197

 

[17楼](https://www.kechuang.org/p/945197) 

> 引用[TK_2410](https://www.kechuang.org/u/107430)发表于[15](https://www.kechuang.org/p/945195?redirect=true)楼的内容
>
> 小刀操作起来有点不顺手，效果不够美观。成品是指这样吗？😶💦科创上有到处找过，似乎作者是唯一一个使

竖着划



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)作者

7个月5天前 IP:北京

945198

 

[18楼](https://www.kechuang.org/p/945198) 

> 引用[TK_2410](https://www.kechuang.org/u/107430)发表于[15](https://www.kechuang.org/p/945195?redirect=true)楼的内容
>
> 小刀操作起来有点不顺手，效果不够美观。成品是指这样吗？😶💦科创上有到处找过，似乎作者是唯一一个使

这样也是能用的，不过只需要竖着刻两小道，把中间那一点点0.2mm的连线抠掉就行



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)作者

7个月5天前 IP:北京

945201

 

[19楼](https://www.kechuang.org/p/945201) 

> 引用[bs170](https://www.kechuang.org/u/90364)发表于[16](https://www.kechuang.org/p/945196?redirect=true)楼的内容
>
> RP2040好像说是能直接连个小屏装专用定制系统的，有试过的吗，有什么好的用处

没试过，看上去应该就是硬件集成了一下，软件应该还是独立的，可能有例程以及一段预装的显示代码。用起来估计跟自己买个屏接线差不多，就是屏幕贴得更紧



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67fbde9573e858be0314a327?c=userAvatar)

[TK_2410](https://www.kechuang.org/u/107430)![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)

7个月3天前 IP:江苏

945239

 

[20楼](https://www.kechuang.org/p/945239) 

哭笑不得，白天接电路的时候，给RP2040

不小心电源装反了一会儿，晚上再插电脑的，已经没有反应了

又要来买，还得再等两三天



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/697e043430cf98270ac18879?c=userAvatar)

[御坂18650](https://www.kechuang.org/u/79849)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)

6个月29天前 IP:北京

945385

 

[21楼](https://www.kechuang.org/p/945385) 

最近试用了楼主设计的采集装置，用起来非常方便。个人觉得美中不足的一个问题是，采集数据中没有时间，711输出速率又不够稳定，导致还需要根据视频校准发动机工作时间。即使如此处理，最后得到的总冲也是精度一般的，如果数据文件加一列时间就解决了





引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)作者

6个月28天前 IP:北京

945396

 

[22楼](https://www.kechuang.org/p/945396) 

> 引用[御坂18650](https://www.kechuang.org/u/79849)发表于[21](https://www.kechuang.org/p/945385?redirect=true)楼的内容
>
> 最近试用了楼主设计的采集装置，用起来非常方便。个人觉得美中不足的一个问题是，采集数据中没有时间，71

不对哦，这个方案用的叫定时中断，它采集的时间是准准的20ms间隔，你别看它那个串口时间，那个不准的。你就按均匀的20ms采样时间点来用就好了。实在想看看时间的话，加一列时间输出肯定也是可以的啦，有空我看看代码再说哈



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)作者

6个月28天前 IP:北京

945401

 

[23楼](https://www.kechuang.org/p/945401) 

![IMG_20250707_223728.jpg](https://img.kechuang.org:81/r/373162?c=resource)

测试了，就是不用加时间戳，加了也是齐刷刷的20ms间隔



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)作者

6个月28天前 IP:北京

945403

 

[24楼](https://www.kechuang.org/p/945403) 

![IMG_20250707_231353_edit_692178991020422.jpg](https://img.kechuang.org:81/r/373174?c=resource)

用了另一个读时间函数看，精确到微秒！



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/666d50ea3785d827685bb9d3?c=userAvatar)

[bmte](https://www.kechuang.org/u/104296)![浪迹天涯](https://www.kechuang.org/statics/grade_icon/v1l.png)

6个月0天前 IP:辽宁

946053

 

[25楼](https://www.kechuang.org/p/946053) 



这里问一下用的电池型号，是18650吗



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)作者

6个月0天前 IP:北京

946062

 

[26楼](https://www.kechuang.org/p/946062) 

对的，其他类型锂电也可以



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/69586c4b5f1ee2b17dd28424?c=userAvatar)

[风铃FL](https://www.kechuang.org/u/108695)![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)

5个月15天前 IP:山东

946475

 

[27楼](https://www.kechuang.org/p/946475) 

有大佬可以帮助我一下吗？

按照作者的步骤思路，将文件拖拽至单片机中，并按下boot键。之后再打开是有一个文件里面显示10000。

但是当我用面包板连接OLED事儿，并没有成功点亮

**求帮助**![Screenshot_20250819_134438_com.taobao.taobao.jpg](https://img.kechuang.org:81/r/375704?c=resource)![IMG_20250818_212118.jpg]()





 **加载全文**

 

引用

 

 

 

 

![img](https://img.kechuang.org:81/a/6742c3f7ad8914b7610d4f37?c=userAvatar)

[黑土](https://www.kechuang.org/u/105427)![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)

5个月15天前 IP:广东

946487

 

[28楼](https://www.kechuang.org/p/946487) 

当我好不容易仿老帖搓出试车台，灌入程序后。看到你的预制菜程序有多绝望吗？



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)作者

5个月14天前 IP:北京

946509

 

[29楼](https://www.kechuang.org/p/946509) 

> 引用[风铃FL](https://www.kechuang.org/u/108695)发表于[27](https://www.kechuang.org/p/946475?redirect=true)楼的内容
>
> 有大佬可以帮助我一下吗？按照作者的步骤思路，将文件拖拽至单片机中，并按下boot键。之后再打开是有一

不对啊，你用的是7线OLED。需要4线的（I2C接口），而且内置驱动芯片也有不同型号。



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67782b1ff2e57372eefada9e?c=userAvatar)

[Log锦霖03](https://www.kechuang.org/u/106037)![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)

1个月6天前 修改于 1个月5天前 IP:广东

948216

 

[30楼](https://www.kechuang.org/p/948216) 

挺好



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67782b1ff2e57372eefada9e?c=userAvatar)

[Log锦霖03](https://www.kechuang.org/u/106037)![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)

1个月0天前 IP:广东

948351

 

[31楼](https://www.kechuang.org/p/948351) 

有个问题，我按你的方法制作算是成功了。但前几次插上电脑都没有问题，可以正常通电和打开文件。现在换个电脑，显示器显示四个问号。我再拔了重新插上，现在显示屏直接没反应了，是哪儿坏了啊？不能是被烧了吧，但就是电脑的usb借口啊，怎么会坏呢



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)作者

29天1时前 IP:北京

948399

 

[32楼](https://www.kechuang.org/p/948399) 

> 引用[Log锦霖03](https://www.kechuang.org/u/106037)发表于[31](https://www.kechuang.org/p/948351?redirect=true)楼的内容
>
> 有个问题，我按你的方法制作算是成功了。但前几次插上电脑都没有问题，可以正常通电和打开文件。现在换个电

显示器4个问号，显示屏还是显示器？也许是按到重置键啦？你按住重置按钮再插USB，插好后放开按钮，应该可以完全重新来，电脑上应该能看见它系统初始U盘。如果看不到，就是坏了，只能换一个板试试



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67782b1ff2e57372eefada9e?c=userAvatar)

[Log锦霖03](https://www.kechuang.org/u/106037)![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)

28天23时前 IP:广东

948402

 

[33楼](https://www.kechuang.org/p/948402) 

> 引用[Tangshm](https://www.kechuang.org/u/105684)发表于[32](https://www.kechuang.org/p/948399?redirect=true)楼的内容
>
> 显示器4个问号，显示屏还是显示器？也许是按到重置键啦？你按住重置按钮再插USB，插好后放开按钮，应该

就是连接的那个小的液晶屏显示四个问号，现在按你说的方法还是没反应。我就是好奇，如果真是坏了。这咋坏的，太玄学了



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)作者

28天22时前 IP:北京

948404

 

[34楼](https://www.kechuang.org/p/948404) 

> 引用[Log锦霖03](https://www.kechuang.org/u/106037)发表于[33](https://www.kechuang.org/p/948402?redirect=true)楼的内容
>
> 就是连接的那个小的液晶屏显示四个问号，现在按你说的方法还是没反应。我就是好奇，如果真是坏了。这咋坏的

至少重置后，电脑上要能看见它的U盘



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67782b1ff2e57372eefada9e?c=userAvatar)

[Log锦霖03](https://www.kechuang.org/u/106037)![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)

28天9时前 IP:广东

948414

 

[35楼](https://www.kechuang.org/p/948414) 

> 引用[Tangshm](https://www.kechuang.org/u/105684)发表于[34](https://www.kechuang.org/p/948404?redirect=true)楼的内容
>
> 至少重置后，电脑上要能看见它的U盘

已放弃，重买个试试。为啥那么容易坏。我想它没有收到过暴力的放置等



引用

 

 

 

 

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)作者

28天2时前 IP:北京

948418

 

[36楼](https://www.kechuang.org/p/948418) 

> 引用[Log锦霖03](https://www.kechuang.org/u/106037)发表于[35](https://www.kechuang.org/p/948414?redirect=true)楼的内容
>
> 已放弃，重买个试试。为啥那么容易坏。我想它没有收到过暴力的放置等

只有电池装反烧过一次，其他没坏过～



引用

 

 

 

 

想参与大家的讨论？现在就 登录 或者 注册。

所属专业

[电子技术](https://www.kechuang.org/f/37)[喷气推进](https://www.kechuang.org/f/89)

上级专业

[电子信息](https://www.kechuang.org/f/222)[航空航天](https://www.kechuang.org/f/74)

同级专业

[航空技术](https://www.kechuang.org/f/165)[无线电](https://www.kechuang.org/f/163)[航天技术](https://www.kechuang.org/f/366)

![img](https://img.kechuang.org:81/a/67386ec3e2de9318d7e08efe?c=userAvatar)

[Tangshm](https://www.kechuang.org/u/105684)

![百炼成钢](https://www.kechuang.org/statics/grade_icon/v4l.png)学者 机友

文章

 

15

 

回复

 

180

 

学术分

 

1

2024/11/16注册，39分48秒前活动

研究神经科学的火箭工程师

主体类型：个人

所属领域：无

认证方式：手机号

IP归属地：北京

[名片](https://www.kechuang.org/u/105684)私信

作者最新文章

[简化制作感应炮](https://www.kechuang.org/t/91605)

[电磁炮](https://www.kechuang.org/f/367)[Tangshm](https://www.kechuang.org/u/105684) 1个月6天前

[低成本的RP2040产生高频时序脉冲](https://www.kechuang.org/t/91539)

[电子技术](https://www.kechuang.org/f/37)[Tangshm](https://www.kechuang.org/u/105684) 2个月21天前

[高压桥丝装置制作与改进](https://www.kechuang.org/t/91422)

[起爆药与火工品](https://www.kechuang.org/f/358)[Tangshm](https://www.kechuang.org/u/105684) 5个月14天前

[开源RP2040飞控主板](https://www.kechuang.org/t/91298)

[喷气推进](https://www.kechuang.org/f/89)[Tangshm](https://www.kechuang.org/u/105684) 7个月2天前

[极简RP2040推力采集系统](https://www.kechuang.org/t/91248)

[电子技术](https://www.kechuang.org/f/37)[Tangshm](https://www.kechuang.org/u/105684) 7个月25天前

[用RP2040升级替代arduino单片机](https://www.kechuang.org/t/91241)

[航天技术](https://www.kechuang.org/f/366)[Tangshm](https://www.kechuang.org/u/105684) 8个月1天前

[钛金属端燃发动机最终版](https://www.kechuang.org/t/91189)

[喷气推进](https://www.kechuang.org/f/89)[Tangshm](https://www.kechuang.org/u/105684) 8个月24天前

[极简推力测量](https://www.kechuang.org/t/90965)

[喷气推进](https://www.kechuang.org/f/89)[Tangshm](https://www.kechuang.org/u/105684) 11个月25天前

[固体发动机的简化设计](https://www.kechuang.org/t/90947)

[喷气推进](https://www.kechuang.org/f/89)[Tangshm](https://www.kechuang.org/u/105684) 1年0个月前

[解码高速GPS](https://www.kechuang.org/t/90933)

[航天技术](https://www.kechuang.org/f/366)[Tangshm](https://www.kechuang.org/u/105684) 1年0个月前

相似文章推荐

[开源一个没什么卵用的320HZ采集卡](https://www.kechuang.org/t/91296)

[电子技术](https://www.kechuang.org/f/37)[bbbbmmdddd](https://www.kechuang.org/u/102911) 7个月2天前

[极简RP2040推力采集系统](https://www.kechuang.org/t/91248)

[电子技术](https://www.kechuang.org/f/37)[Tangshm](https://www.kechuang.org/u/105684) 7个月25天前

关于

- [关于科创](https://www.kechuang.org/t/25436)
-  
- [提问须知](https://www.kechuang.org/t/36782)
-  
- [禁止事项](https://www.kechuang.org/t/66350)
-  
- [建设指南](https://www.kechuang.org/t/79481)
-  
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
-  
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

##### 科创研究院 (c)2001-2024[蜀ICP备11004945号-2](https://beian.miit.gov.cn/)[川公网安备51010802000058号](https://www.beian.gov.cn/)·
