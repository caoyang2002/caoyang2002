+++
title = '极简 RP2040 推力采集系统'
date = 2026-02-01T10:14:17+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
cover = "https://circuitstate.com/wp-content/uploads/2021/05/Raspberry-Pi-Pico-RP2040-Microcontroller-Development-Board-Vishnu-Mohanan-2500px-1.jpg"
+++

[查看原文](https://www.kechuang.org/t/91248)

RP2040单片机功能强大，用在发动机推力采集上，人机界面得以简化，新手友好。尝试按以下步骤搭建：

# 一、让RP2040单片机运行

注意，这一步不需要懂单片机，不需要单片机开发程序，只需要拷个文件。拿到RP2040后，按住单片机板上左边BOOT键，通过USB线插到电脑上，然后把附件的二进制文件拷到新出现的U盘上，单片机就运行起来啦！


附RP2040单片机tb图，这个程序要16M那种

![Screenshot_20250613_074909.jpg](https://img.kechuang.org:81/r/372147?c=resource)

怎么知道它是不是真的在运行呢？两个办法，一是看电脑上会出现一个新的U盘，15MB 左右，这是程序创建的单片机板载U盘。另一个办法就是接着完成第二步，接个 OLED，来个实时显示。

# 二、扩展附件1，连OLED显示屏

买一个SH1106的OLED，拔下单片机（断电）焊4根线：VCC接单片机5V、GND接单片机GND、SDA接单片机GP2、SCL接单片机GP3。单片机插回电脑（这时候不按BOOT键了），应该能看到OLED亮了，完成第二步！

附tb OLED图片，这两种都行

![Screenshot_20250610_115153.jpg](https://img.kechuang.org:81/r/372025?c=resource)

# 三、扩展附件2，连HX711

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

1. 每次上电系统会自动去皮归零，然后进入定时采样，20ms一次。连续3个采样点推力大于50g会启动点火，然后连续采集10s后停止采样，计算并显示推力曲线及总冲量。

2. 连接单片机到电脑或手机，会出现一个新U盘，里面有3个数据文件，一是校准文件Clb，二是运行计数Cnt，三是推力数据Run001。以后每次重新上电采集，会生成一个新的数据文件，文件名序号增Run00x。数据文件可以直接拷贝到电脑或手机上。不删除的情况下，这几个文件可以一直掉电保存，存到5000次试车数据后，文件名回到Run001覆盖之前数据。连电脑试车的情况下，也可以通过串口调试软件，实时传输推力数据至电脑。

3. 校准，上电后（自动去皮后），拿一个已知重量的物体放推力台上（试车台竖直向下），如果物体重1000g，测得推力数值是210g，就把Clb文本文件里的1000000改成210000。再次重新上电测量，推力值就会变成1000g左右，这个值也会掉电保存，除非手动修改或删除。



# 系统的工作原理简介

（供爱好者研究、并提改进建议，仅关心使用的可忽略）

1. 单片机软件，使用 Ardunio IDE 编程，主要参考 RP2040 C/C++ SDK 手册及 https://github.com/earlephilhower/arduino-pico ，代码有点长 290 行，编译为二进制文件后使用。

> RP2040 支持直接拷贝二进制程序，按住BOOT插USB的情况下，板载flash程序段会在电脑上显示为一个U盘，把arduino等单片机开发软件编译好的二进制文件拷到U盘里，单片机马上就会运行程序。所以不需要使用者懂单片机，不需要开发软件及准备各种库，拷完文件单片机马上就运行起来了。

2. 单片机内部程序流程

每次重新上电后，会自动运行一次去皮程序，测推力100次，取后50次平均值作去皮值，后续测量值都会减去这个值；

启动每 20ms 一次的定时中断，指向一个推力采集程序 F_Smp；

初始化 OLED 显示；

生成或读取校准文件 Clb.txt；

板载文件系统FATFSUSB程序，自动生成或打开一个电脑能访问的新U盘，对应板载flash的数据段，用于数据存储。

进入主循环loop程序，就是不停刷新OLED，实时显示推力值display.print(F);

每20ms定时中断会打断一下loop的OLED显示，跳转至推力采集程序F_Smp，每次只采集一个数据点；

推力采集程序包含点火启动判断，连续3个采样点推力大于50g为点火开始，数据点依次存入数组`F0[500]`。

记录点达到498也就是接近10s之后，停止中断程序，也就停止了推力采集，还设置了一个循环存储以保存点火前一小段数据点到F0数组。

最后一个采集点后，计算总冲，也就是从点火启动到最末大于50g（连续3个）的推力值 x 0.02秒累加。

最后一个采集点内还包含数据文件生成程序，第一次运行会建立计数文件Cnt.txt，从1开始以后每次加1，生成数据文件名从Run001开始，根据Cnt生成新文件名每次累加1。

最后loop主循环中OLED显示推力曲线，程序会自动调整XY显示范围。以及

```ino
FatFS.begin();
FatFS.end();
FatFSUSB.begin();
```

再次允许运行电脑或手机访问程序创建的板载U盘，以拷走数据或修改校准系数等。


# 查看源代码

{{<details summary="源代码：">}}

```ino
#include <Arduino.h> // 引入 Arduino 核心头文件
#include <stdio.h>
#include <pico/stdlib.h>
#include <hardware/divider.h>
#include <hardware/timer.h>
#include <hardware/clocks.h>
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SH110X.h>
#include <hardware/i2c.h>
#include <FatFS.h>
#include <FatFSUSB.h>

#define i2c_Address 0x3C //initialize with the I2C addr 0x3C Typically eBay OLED's
#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels
#define OLED_RESET -1   //   QT-PY / XIAO

Adafruit_SH1106G display = Adafruit_SH1106G(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire1, OLED_RESET);

int F;                  //推力测量值
float FSum;               //总冲量
long offset=0;          //推力计零点测量
long ret2;
int F0[500]={0};        //各时间点的推力值，总时长500/50Hz=10秒；
uint8_t dT = 20;           //采样周期20ms(50Hz)

int i=0;
int j=0;
int Tmi=9;              //点火后采样点计数，从第11点开始，前面有10个点预留给了点火前的数据
uint8_t FrON=0;            //正在采样标志，此版本为自动检测推力模式
uint8_t Frd=0;             //已点火标志
int Thr=50;            //大于50g判断为点火
int Tm0=500;                //工作总时长
int clb = 1000000;             //传感器校准系数1kg=1000000mg
char buff[32];

struct repeating_timer timer;

void setup() {
  Serial.begin(115200);
  pinMode(4, INPUT);
  pinMode(5, OUTPUT);
  digitalWrite(5, HIGH);
  digitalWrite(5, LOW); 
  for (i=0;i<100;i++)
  {
    F=F_Measure();
    if(i>49)
    {
      offset=offset+F/50;                        //推力计去皮测量
    }
  }
  add_repeating_timer_ms(-20, F_Smp, NULL, &timer); 
  Wire1.setSDA(2);  //参考自Example for Ardunio Nano P2040 Connect的Wire例程TalkToMyself!!!
  Wire1.setSCL(3);
  Wire1.begin();
  display.begin(i2c_Address, true); // Address 0x3C default
  display.display();
  FatFS.begin();
  //校准文件
  File fc = FatFS.open("Clb.txt", "r");
  if(fc){                            //文件存在且位数大于2则读出新校准值
    bzero(buff, 32);//将内存块(字符串)的前32个字节清零
    fc.read((uint8_t *)buff, 31);
    if(strlen(buff)>2){
      sscanf(buff, "%d", &clb);
    }
    fc.close();
  }
  File fc2 = FatFS.open("Clb.txt", "r");
  if(!fc2){                            //文件不存在则新建
    sprintf(buff, "%d\n", clb);
    fc2 = FatFS.open("Clb.txt", "w");
    fc2.write(buff, strlen(buff));
    fc2.close();
  }

  FatFS.end();
  // Start FatFS USB drive mode
  FatFSUSB.begin(); 
}

void loop() 
{ 
  //等待点火，传前一轮推力数据至串口，OLED实时显示推力值
  if(Frd==0)    
  {
    delay(10);    
    display.clearDisplay();
    display.setTextSize(2);
    display.setTextColor(SH110X_WHITE);
    display.setCursor(0,0);
    display.println("?? Fire ??"); 
    display.setTextSize(3);                        
    display.setCursor(5,30);    
    display.print(F);  
    display.print(" g");     
    display.display();
  }
  //点火后，OLED显示推力值
  if(FrON==1)
  {
    delay(10);    
    display.clearDisplay();
    display.setTextSize(2);
    display.setTextColor(SH110X_WHITE);
    display.setCursor(0,0);
    display.println("FireON -->");      
    display.setTextSize(3);
    display.setTextColor(SH110X_WHITE);
    display.setCursor(5,30);
    display.print(F);display.print(" g");                       
    display.display(); 
  }
  //采样结束，OLED显示结果
  if(FrON==0&Frd==1)     
  {
    delay(10);    
    display.clearDisplay();

    for(i=1;i<500;i++)
    {
      Tm0 = 500-i;
      if(F0[Tm0]>Thr&F0[Tm0-1]>Thr&F0[Tm0-2]>Thr)
      {   
        break;            
      }
    }

    int MaxF=0;   
    for(i=0;i<498;i++)
    {    
      if(F0[i]>MaxF)
      {
        MaxF = F0[i];
      }
    }
    for(i=0;i<128;i++)
    {   
      if(Tm0<128)
      {
        j=64-F0[i]/(MaxF/45);
      }
      if(Tm0>127&Tm0<256)
      {
        j=64-(F0[i*2-1]+F0[i*2-0])/2/(MaxF/45);
      }  
      if(Tm0>255&Tm0<384)
      {
        j=64-(F0[i*3-2]+F0[i*3-1]+F0[i*3-0])/3/(MaxF/45);
      } 
      if(Tm0>383)
      {   
        j=64-(F0[i*4-3]+F0[i*4-2]+F0[i*4-1]+F0[i*4-0])/4/(MaxF/45);
      }
      display.drawFastVLine(i,j,63,SH110X_WHITE);
    } 
    display.setTextSize(2);
    display.setTextColor(SH110X_WHITE);
    display.setCursor(2,0);
    display.print(FSum,0);
    display.setTextSize(1);
    display.print("gs "); 
    display.setTextSize(2);
    display.print((Tm0-5)/50.0,1);   
    display.setTextSize(1);
    display.print("s"); 
    display.display(); 
        FatFS.begin();
        FatFS.end();
        FatFSUSB.begin(); 
    delay(200);    
  }    
}

bool F_Smp(struct repeating_timer *t)
{  
  F = (F_Measure()-offset)*1.0*10000/clb;///MyScale.readWeight();  //单点的推力值g
  //点火前的数据段。循环转移至数组F0的前10个  
  if(Frd==0)
  {
    for(j=0;j<9;j++)
    {
      F0[j]=F0[j+1];
    }  
    F0[9]=F;
  }

  if(Frd==0&F0[9]>Thr&F0[8]>Thr&F0[7]>Thr)
  { 
    Frd = 1;                  //推力超过Thr(50g)判断为点火 
    FrON = 1;  
    Serial.println("*****Fire*****");//串口发送数据                 
  }
  
  if(FrON==1)                 //采集数据顺序存放到F0数组
  {
    Tmi = Tmi+1;              //从10开始计数至498，时长10s控制，
    F0[Tmi]=F;                //推力值存至数组F0[500]，前面10个为点火前数据
  }
  
  Serial.println(F);//串口发送实时推力数据
    
  if(Tmi>498)                 //点火Fire 10s后
  {
    //停止Tmi计数，停止顺序存数。计算总冲量，存储数据，显示结果
    FrON = 0;                 
    bool cancelled = cancel_repeating_timer(&timer); 
    delay(10);    
    FSum=0;
    
    //判断推力结束点Tm0
    for(i=1;i<500;i++)
    {
      Tm0 = 501-i;
      if(F0[Tm0-1]>Thr&F0[Tm0-2]>Thr&F0[Tm0-3]>Thr)
      {   
        Serial.print("N = ");//串口发送数据 
        Serial.println(Tm0-7);//串口发送数据 
        break;            
      }
    }

    //计算总冲量并发送至串口
    for(j=5;j<Tm0;j++)
    {
      FSum = FSum+F0[j]*1.0*dT/1000;               //总冲量g*s
    }
    Serial.print("FSum = ");
    Serial.print(FSum);//串口发送数据 
    Serial.print("(gs);  ");
    Serial.print("Tm0 = ");//串口发送数据 
    Serial.print((Tm0-5)/50.0);//串口发送数据 
    Serial.println("(s)");
    
    //存储数据至数据文件，最多静态存储9.9s数据

    FatFSUSB.end();
    FatFS.begin();  
    //文件序号增1
    int cnt = 0;
    File f2 = FatFS.open("Cnt.txt", "r");
    if (f2) {
      bzero(buff, 32);//将内存块(字符串)的前32个字节清零
      f2.read((uint8_t *)buff, 31);
      sscanf(buff, "%d", &cnt);
    }
    f2.close();
    cnt++;
    if(cnt>500){
      cnt=1;
    }
    sprintf(buff, "%d\n", cnt);
    f2 = FatFS.open("Cnt.txt", "w");
    f2.write(buff, strlen(buff));
    f2.close();

    char filename[32]; 
    sprintf(filename, "Run%d.txt", cnt); // 生成文件名

    File f = FatFS.open(filename, "a");
    for(j=0;j<498;j++){
      sprintf(buff, "%d\n", F0[j]);    
      f.write(buff, strlen(buff));
    }
    f.close();
    FatFS.end();
  }
  return true; 
}

long F_Measure()
{
  uint8_t data[3];
  long ret=0;
  while (digitalRead(4));
  for (uint8_t j = 0; j < 3; j++)
  {
    for (uint8_t i = 0; i < 8; i++)
    {
      digitalWrite(5, HIGH);
      bitWrite(data[2 - j], 7 - i, digitalRead(4));
      digitalWrite(5, LOW); 
    }
  }
  ret = (((long) data[2] << 16) | ((long) data[1] << 8) | (long) data[0])^0x800000;
  digitalWrite(5, HIGH);
  digitalWrite(5, LOW); 
  return ret;
}
```
{{</details>}}

另外还测试了低成本版，RP2040 2M flash单片机只要7.5元！OLED也是只要9多块钱

![Screenshot_20250615_192017.jpg](https://img.kechuang.org:81/r/372244?c=resource)


试车台可以参考以前帖子，也是结构简单，就3个零件加几颗螺丝，大L型材底座、小L型材连接、U型槽用于绑发动机。

![IMG_20250512_191031.jpg](https://img.kechuang.org:81/r/372049?c=resource)

![IMG_20250509_210039.jpg](https://img.kechuang.org:81/r/372050?c=resource)

![IMG_20250415_170852.jpg](https://img.kechuang.org:81/r/372052?c=resource)

最后这个是炸机的后果，以警醒大家要千万小心，要躲在掩体后面试车，祝大家玩得安全开心！
