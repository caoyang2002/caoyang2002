+++
title = '星云科技矢量火箭制作流程'
date = 2026-01-31T01:04:19+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
+++

今天，我们实现了一个来自2021年的梦想——星云科技矢量火箭制作流程及开源计划

[查看原文](https://www.kechuang.org/t/89933)

[Github](https://github.com/baimo0001/vector_rocket2.0)

完成2021年提出的矢量火箭项目的具体过程，以及项目的开源计划，供各位爱好者批评交流。

> 2021年的时候，我刚刚进入高三，也刚刚开始接触火箭圈子，从那时起便想自己制作一枚搭载控制系统的火箭，在深思熟虑中，我们选择了一种叫做“矢量”的控制方法。本文中的代码和结构文档均已开源，供各位爱好者交流互鉴

# 第一阶段

最初我们刚刚进入高三，利用课余时间进行绘图、设计，由于彼时的我们不清楚SW、CAD等相对专业的建模软件，故采用了手工绘图的方法。最早的图纸就像下面这样，非常的业余：

![WeChat图片编辑_20240215202506.jpg](https://img.kechuang.org:81/r/350210?c=resource)

由于本人主要负责电控部分，所以我分享一下最开始的全部代码（代码已在Github开源，大家需要自取）。最初的控制系统采用了Arduino UNO和MPU6050姿态传感器，只有一个最简单的map映射，软件中没有控制开伞部分的程序，完整代码如下：

```cpp
C++
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
#include <Servo.h>

Adafruit_MPU6050 mpu;
int x = 0;
int y = 0;
int z = 0;

Servo servo1; 
Servo servo2;
Servo servo3;
Servo servo4;

int value  = 0;

void setup(void) {
  Serial.begin(115200);

  // 尝试初始化
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");

  // 将加速度计范围设置为 +-8G
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);

  // 将陀螺仪范围设置为 +- 500 度/秒
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);

  // 将滤波器带宽设置为 21 Hz
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

  delay(100);
  servo1.attach(8);
  //servo2.attach(6); 
  //servo3.attach(5); 
  servo4.attach(6); 

  servo1.write(90);
  servo2.write(0);
  servo3.write(0);
  servo4.write(90);
}

void loop() {
  /* 使用读数获取新的传感器事件 */
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  x = a.acceleration.x;
  y = a.acceleration.y;
  z = a.acceleration.z;
  
  Serial.print(x);Serial.print(" ");
  Serial.println(y);Serial.print(" ");
  Serial.println(z);Serial.print("\n");
  
if (x < 10 && x > 0 && y < 4 && y > -4){
  Serial.println("up");
   value = map(x,  0, 10, 0, 180);
   servo1.write(value);
   Serial.print(value);
  }
else if (x > -10 && x < 0 && y < 4 && y > -4){   //2
  Serial.println("down");
  value = map(x,  -10, 0, 180, 0);
  servo1.write(180-value);
  Serial.print(value);
  }

if (y < 10 && y > 0 && x < 4 && x > -4){      //3
  Serial.println("Right");
  value = map(y,  0, 10, 0, 180);
  servo4.write(180-value);
  Serial.print(value);
  }
else if (y > -10 && y < 0  && x < 4 && x > -4){
  Serial.println("left");
  value = map(y,  -10, 0, 180, 0);
  servo4.write(value);
  Serial.print(value);
  }
}
```

当然，这份代码只是在理论上实现了所谓的控制，实测的时候观察到6050传感器的抖动和舵机修正角度的过大，导致火箭呈现“S”形上升。修正效果并不理想，而且此时的火箭结构还仅限于纸筒，未形成完整的图纸。全部代码和开源图纸我也放在这里：

![attachment icon](https://www.kechuang.org/attachIcon/rar)**矢量火箭图纸23.6.10.rar**7.06MB RAR 290次下载

![attachment icon](https://www.kechuang.org/attachIcon/ino)**Vector.ino**1.95KB INO 112次下载

本文所有涉及到的火箭发动机燃料均为KNSB

**第二阶段：**

为了解决第一版的问题，于是在后面版本的程序迭代中，我引入了卡尔曼滤波算法以及简单的增量PID算法，代码我先放在下面：

```cpp
C++
#include <Adafruit_Sensor.h>
#include <Wire.h>
#include <I2Cdev.h>
#include <Servo.h>
#include <MPU6050.h>
#include <Math.h>

MPU6050 accelgyro;
unsigned long now, lastTime = 0;
float dt;                                   //微分时间

int16_t ax, ay, az, gx, gy, gz;             //加速度计陀螺仪原始数据
float aax=0, aay=0,aaz=0, agx=0, agy=0, agz=0;    //角度变量
long axo = 0, ayo = 0, azo = 0;             //加速度计偏移量
long gxo = 0, gyo = 0, gzo = 0;             //陀螺仪偏移量

float pi = 3.1415926;
float AcceRatio = 16384.0;                  //加速度计比例系数
float GyroRatio = 131.0;                    //陀螺仪比例系数

uint8_t n_sample = 8;                       //加速度计滤波算法采样个数
float aaxs[8] = {0}, aays[8] = {0}, aazs[8] = {0};         //x,y轴采样队列
long aax_sum, aay_sum,aaz_sum;                      //x,y轴采样和
 
float a_x[10]={0}, a_y[10]={0},a_z[10]={0} ,g_x[10]={0} ,g_y[10]={0},g_z[10]={0}; //加速度计协方差计算队列
float Px=1, Rx, Kx, Sx, Vx, Qx;             //x轴卡尔曼变量
float Py=1, Ry, Ky, Sy, Vy, Qy;             //y轴卡尔曼变量
float Pz=1, Rz, Kz, Sz, Vz, Qz;             //z轴卡尔曼变量

float num1=1;
float num2=1;
float num3=1;
float num4=1;

Servo servo1; 
Servo servo2;
Servo servo_pin_2;  //开伞舵机

/**
 * 矢量pid部分
 */
double kp = 0.3,ki = 0.15,kd = 0.1;

/*
Kp：比例增益，是调适参数；
Ki：积分增益，也是调适参数；
Kd：微分增益，也是调适参数；
取增量pid
采用恒定的采样周期 T，一旦确定Kp、Ki、Kd参数，只要使用前后三次测量的偏差值，就可以由增量式PID公式求出控制量。
现在设置的参数是我瞎蒙的，不一定准确
*/

double sumerror_x,sumerror_y;//x轴和y轴总计误差
double lasterror_x,lasterror_y;//上一时刻误差值
double output_x,output_y;//累加修正结果

void setup() {
    servo1.attach(8);
    servo2.attach(6); 
    servo_pin_2.attach(9);

    servo1.write(90);
    servo2.write(90);
    servo_pin_2.write( 180 );

    Wire.begin();
    Serial.begin(115200);
 
    accelgyro.initialize();                 //初始化
 
    unsigned short times = 200;             //采样次数
    for(int i=0;i<times;i++)
    {
        accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz); //读取六轴原始数值
        axo += ax; ayo += ay; azo += az;      //采样和
        gxo += gx; gyo += gy; gzo += gz;
    
    }
    
    axo /= times; ayo /= times; azo /= times; //计算加速度计偏移
    gxo /= times; gyo /= times; gzo /= times; //计算陀螺仪偏移

}

void loop() {
  unsigned long now = millis();             //当前时间(ms)
    dt = (now - lastTime) / 1000.0;           //微分时间(s)
    lastTime = now;                           //上一次采样时间(ms)
 
    accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz); //读取六轴原始数值
 
    float accx = ax / AcceRatio;              //x轴加速度
    float accy = ay / AcceRatio;              //y轴加速度
    float accz = az / AcceRatio;              //z轴加速度
 
    aax = atan(accy / accz) * (-180) / pi;    //y轴对于z轴的夹角
    aay = atan(accx / accz) * 180 / pi;       //x轴对于z轴的夹角
    aaz = atan(accz / accy) * 180 / pi;       //z轴对于y轴的夹角
 
    aax_sum = 0;                              // 对于加速度计原始数据的滑动加权滤波算法
    aay_sum = 0;
    aaz_sum = 0;
  
    for(int i=1;i<n_sample;i++)
    {
        aaxs[i-1] = aaxs[i];
        aax_sum += aaxs[i] * i;
        aays[i-1] = aays[i];
        aay_sum += aays[i] * i;
        aazs[i-1] = aazs[i];
        aaz_sum += aazs[i] * i;
    
    }
    
    aaxs[n_sample-1] = aax;
    aax_sum += aax * n_sample;
    aax = (aax_sum / (11*n_sample/2.0)) * 9 / 7.0; //角度调幅至0-90°
    aays[n_sample-1] = aay;                        //此处应用实验法取得合适的系数
    aay_sum += aay * n_sample;                     //本例系数为9/7
    aay = (aay_sum / (11*n_sample/2.0)) * 9 / 7.0;
    aazs[n_sample-1] = aaz; 
    aaz_sum += aaz * n_sample;
    aaz = (aaz_sum / (11*n_sample/2.0)) * 9 / 7.0;
 
    float gyrox = - (gx-gxo) / GyroRatio * dt; //x轴角速度
    float gyroy = - (gy-gyo) / GyroRatio * dt; //y轴角速度
    float gyroz = - (gz-gzo) / GyroRatio * dt; //z轴角速度
    agx += gyrox;                             //x轴角速度积分
    agy += gyroy;                             //y轴角速度积分
    agz += gyroz;
    
    /* 卡尔曼滤波算法部分 */
    Sx = 0; Rx = 0;
    Sy = 0; Ry = 0;
    Sz = 0; Rz = 0;
    
    for(int i=1;i<10;i++)
    {                 //测量值平均值运算
        a_x[i-1] = a_x[i];                      //即加速度平均值
        Sx += a_x[i];
        a_y[i-1] = a_y[i];
        Sy += a_y[i];
        a_z[i-1] = a_z[i];
        Sz += a_z[i];
    
    }
    
    a_x[9] = aax;
    Sx += aax;
    Sx /= 10;                                 //x轴加速度平均值
    a_y[9] = aay;
    Sy += aay;
    Sy /= 10;                                 //y轴加速度平均值
    a_z[9] = aaz;
    Sz += aaz;
    Sz /= 10;
 
    for(int i=0;i<10;i++)
    {
        Rx += sq(a_x[i] - Sx);
        Ry += sq(a_y[i] - Sy);
        Rz += sq(a_z[i] - Sz);
    
    }
    
    Rx = Rx / 9;                              //得到方差
    Ry = Ry / 9;                        
    Rz = Rz / 9;
  
    Px = Px + 0.0025;                         // 0.0025在下面有说明...
    Kx = Px / (Px + Rx);                      //计算卡尔曼增益
    agx = agx + Kx * (aax - agx);             //陀螺仪角度与加速度计速度叠加
    Px = (1 - Kx) * Px;                       //更新p值
 
    Py = Py + 0.0025;
    Ky = Py / (Py + Ry);
    agy = agy + Ky * (aay - agy); 
    Py = (1 - Ky) * Py;
  
    Pz = Pz + 0.0025;
    Kz = Pz / (Pz + Rz);
    agz = agz + Kz * (aaz - agz); 
    Pz = (1 - Kz) * Pz;


    /**
     * 矢量控制部分
     */

     if(agx > 0)
     {
      Serial.print("up ");
      Serial.print(agx);
      Serial.println("度");
      sumerror_x += agx;
      output_x = kp*agx + ki*sumerror_x + kd*(lasterror_x - agx);
      lasterror_x = agx;
      agx += output_x;
      servo1.write(agx);
      }

      if(agx < 0)
     {
      Serial.print("down ");
      Serial.print(agx);
      Serial.println("度");
      sumerror_x += agx;
      output_x = kp*agx + ki*sumerror_x + kd*(lasterror_x - agx);
      lasterror_x = agx;
      agx += output_x;
      servo1.write(agx);
      //servo1.write(num2*(90-agx));

      }

      if(agy > 0)
     {
      //servo2.write(num3*agy);
      Serial.print("left ");
      Serial.print(agy);
      Serial.println("度");
      sumerror_y += agy;
      output_y = kp*agy + ki*sumerror_y + kd*(lasterror_y - agy);
      lasterror_y = agy;
      agy += output_y;
      servo2.write(agy);
      }

      if(agy < 0)
     {
      //servo2.write(num4*(90-agy));
      Serial.print("right ");
      Serial.print(agy);
      Serial.println("度");
      sumerror_y += agy;
      output_y = kp*agy + ki*sumerror_y + kd*(lasterror_y - agy);
      lasterror_y = agy;
      agy += output_y;
      servo2.write(agy);
      }


      /**
       * 开伞部分
       */
       
    if(agx>70)//开伞角度
  {
    //digitalWrite(8,1);
    servo_pin_2.write( 0 );
    delay(2000);
    
  
Serial.print("开伞agx>70");
while(1)
 {
  }
    }
  if(agy>70)//开伞角度
  {
    //digitalWrite(8,1);
    servo_pin_2.write( 0 );
    delay(2000);
    
  
Serial.print("开伞agy>70");
while(1)
{
  }
    }

  if(agy<-70)//开伞角度
  {
    //digitalWrite(8,1);
    servo_pin_2.write( 0 );
    delay(2000);
    
  
Serial.print("开伞agy<-70");
while(1)
{
  }
    }

  if(agx<-70)//开伞角度
  {
    //digitalWrite(8,1);
    servo_pin_2.write( 0 );
    delay(2000);
    
  
Serial.print("开伞agx<-70");
while(1)
{
  }
    }
   // Serial.print(agx);Serial.print(",");
   // Serial.print(agy);Serial.print(",");
   // Serial.print(agz);Serial.println();
    
}
```

而针对滤波算法，当时我找到了一段描述，大致是这样的：卡尔曼滤波是一种高效的自回归滤波器，它能在存在诸多不确定性情况的组合信息中估计动态系统的状态，是一种强大的、通用性极强的工具。卡尔曼滤波算法采用递推方式实现实时在线计算，在目标跟踪、模式识别、导航等领域有着广泛应用。对于EKF，在一个动态系统中，将目标状态方程表示为：

𝑋(𝑡)=𝐹(𝑡)·𝑋(𝑡−1)+𝑤(𝑡)

量测方程表示为：

𝑍(𝑡)=𝐻(𝑡)·𝑋(𝑡)+𝑣(𝑡)

其中：X(t)为t时刻系统状态向量；F(t)为t时刻系统状态转移矩阵；Z(t)为t时刻系统量测向量；H(t)为t时刻系统量测转移矩阵；w(t)为过程噪声；v(t)为观测噪声。

对于火箭姿态解算问题，建立基于姿态四元数的状态向量：

𝑋(𝑡)=[𝑞0𝑞1𝑞2𝑞3𝑏𝑔𝑥𝑏𝑔𝑦𝑏𝑔𝑧]𝑇

其中，𝑞=[𝑞0𝑞1𝑞2𝑞3]𝑇为表示姿态信息的四元数，𝑏=[𝑏𝑔𝑥𝑏𝑔𝑦𝑏𝑔𝑧]𝑇为陀螺仪角速度测量偏差。

这枚火箭的控制逻辑如图所示：

![1111.jpg](https://img.kechuang.org:81/r/350212?c=resource)

PID算法部分在我之前的帖子中也有提及，在此不多赘述。此时的火箭结构部分我们换用了桁架蒙皮结构，发动机也从最开始的PPR机换成了碳纤维机，增强了稳定性的同时也易于装配。

（1）牵拉部分

我们使用了舵机原装的拉杆，并自己利用金属3D打印制作了一段特制的长拉杆，装配时，将舵机原装的拉杆和特制的长拉杆利用小螺丝进行安装，此时在螺丝孔位置，二者可以相对转动。长的拉杆再与固定在矢量喷口上的金属环以相同的方式相连，从而达到了传动的目的。舵机连杆和拉杆结构如下图所示。

![11.png](https://img.kechuang.org:81/r/350213?c=resource)

（2）开伞装置及原理

为保证降落伞能顺利打开，我们选择将火箭的头锥分为两半设计，一半是固定在头锥底座上的，另一半则可以分离，中间用连杆和舵机相连，头锥固定一侧的内部结构如下图所示。正常情况下，舵机会旋转到0度的地方，将可活动头锥固定住，当Seeeduino XIAO开发板解算出火箭的偏移角度超过了70度时，舵机会立刻旋转到180度的位置，将头锥中可活动的部分推出，此时放置在头锥内的降落伞会展开，完成开伞动作。



![头锥.jpg](https://img.kechuang.org:81/r/350215?c=resource)

（3）发动机装配细节

发动机部分外壳采用碳纤维管制作，内部用PVC管做隔热层，前后两个法兰盘、喷口、固定矢量喷管用的支架以及矢量喷管均采用金属3D打印制作，堵头部分则利用酚醛浇筑制成，并利用O型圈做密封处理，防止漏气发生爆炸。发动机内部药柱采用中空设计，从而增加燃烧的速率。发动机前后用法兰盘和螺杆夹紧，做进一步的固定，提高发动机的稳定性。发动机结构如下图所示（未安装螺杆时）

![发动机总装.png](https://img.kechuang.org:81/r/350216?c=resource)

（4）发动机舱结构设计

为确保发动机不会从舱内滑落，我们在火箭尾部设计了小卡扣，可以保证发动机在任何情况下都会固定在发动机舱内，发动机舱的上方隔板上有四个圆孔，便于特制的拉杆通过；相应的，法兰盘上也有孔位，以确保矢量系统的正常运行。发动机舱的外部有尾翼卡环，用来固定尾翼、优化火箭的气动外形。前后法兰盘结构、发动机舱上下部、尾翼卡环如下图所示。为确保发动机不会从舱内滑落，我们在火箭尾部设计了小卡扣，可以保证发动机在任何情况下都会固定在发动机舱内；发动机舱的上方隔板上有四个圆孔，便于特制的拉杆通过；相应的，法兰盘上也有孔位，以确保矢量系统的正常运行。发动机舱的外部有尾翼卡环，用来固定尾翼、优化火箭的气动外形。

![前法兰盘.jpg](https://img.kechuang.org:81/r/350217?c=resource)

前法兰盘结构

![后法兰盘.jpg](https://img.kechuang.org:81/r/350218?c=resource)

后法兰盘结构

![发动机舱上部.jpg](https://img.kechuang.org:81/r/350219?c=resource)

发动机舱上部

![发动机舱下部.jpg](https://img.kechuang.org:81/r/350220?c=resource)

发动机舱下部（内部用一圈卡扣卡住发动机，防止发动机滑落）

![尾翼卡环 （）.jpg](https://img.kechuang.org:81/r/350221?c=resource)

尾翼卡环（尾翼固定环）

（5）飞控支架设计

支架共分为四层，从下往上分别是：矢量舵机层、飞控电源层、飞控PCB层、惯导模块层。其中矢量舵机层用来存放控制矢量喷管的舵机；飞控电源层用来存放锂电池，锂电池同时给飞控和惯导模块供电，飞控PCB层用来存放PCB板，最上面的惯导模块层存放用来监控火箭姿态的IMU模块，该IMU模块加装无线串口后支持远程实时传输。飞控支架如图所示。

![飞控支架.jpg](https://img.kechuang.org:81/r/350222?c=resource)

（6）矢量喷口部分设计

喷口分为固定部分和可摆动部分，固定部分内部采取拉瓦尔喷管结构，具有扩张段结构，能有效增大推力。可摆动部分在拉杆的牵拉下旋转来改变尾焰喷射方向，从而实现矢量控制。喷口部分结构如图所示。

![固定喷口.jpg](https://img.kechuang.org:81/r/350224?c=resource)

固定喷口

![喷口可摆动部分.jpg](https://img.kechuang.org:81/r/350225?c=resource)

喷口可摆动部分

这时候我们也使用了3D打印的方法，制作了完整的火箭模型，并完成了组装和测试，火箭总装如下图所示

![zhuangpei.png](https://img.kechuang.org:81/r/350227?c=resource)

这时候火箭的雏形已经具备，在细节方面还有待优化，比如开伞部分和尾翼部分。

**第三阶段：**

在这个阶段，我基本重写了整个项目的软件部分，进一步优化控制流程和控制思路，除了像上一篇帖子提到的“利用switch case对飞行进行“分段处理”，分为：上电自检和初始化、等待发射、发射、发动机工作、下落开伞”以外，还学会了调整舵臂安装误差、软限位和地面站数据传输等。主体部分代码如下：

```cpp
C++
void setup() {
  #if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
        Wire.begin();
        Wire.setClock(400000); // 400kHz的I2C
    #elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
        Fastwire::setup(400, true);
    #endif

    Servo1.attach(8);
    Servo2.attach(6);
    Servo_KS.attach(9);

    Servo1.write(90);
    Servo2.write(90);
    Servo_KS.write(Servo_KS_ANGLE1);
 

   
    Serial.begin(115200);
    //while (!Serial); //当串口监视打开以后程序运行，方便调试，上箭之前记得注释掉

    Serial.println(F("加载I2C设备..."));
    mpu.initialize();
    pinMode(INTERRUPT_PIN, INPUT);

    Serial.println(F("测试设备连接中..."));
    Serial.println(mpu.testConnection() ? F("MPU6050连接成功") : F("MPU6050连接失败"));

    Serial.println(F("调用 DMP..."));
    devStatus = mpu.dmpInitialize();

    mpu.setXGyroOffset(220);
    mpu.setYGyroOffset(76);
    mpu.setZGyroOffset(-85);
    mpu.setZAccelOffset(1788);

    if (devStatus == 0) {
        mpu.CalibrateAccel(6);
        mpu.CalibrateGyro(6);
        mpu.PrintActiveOffsets();
        //打开DMP
        Serial.println(F("Enabling DMP..."));
        mpu.setDMPEnabled(true);

        Serial.print(F("Enabling interrupt detection (Arduino external interrupt "));
        Serial.print(digitalPinToInterrupt(INTERRUPT_PIN));
        Serial.println(F(")..."));
        attachInterrupt(digitalPinToInterrupt(INTERRUPT_PIN), dmpDataReady, RISING);
        mpuIntStatus = mpu.getIntStatus();

        Serial.println(F("DMP ready! Waiting for first interrupt..."));
        dmpReady = true;

        packetSize = mpu.dmpGetFIFOPacketSize();
    } else {
        // ERROR!
        // 1 = 初始内存加载失败
        // 2 = DMP 配置更新失败
        Serial.print(F("DMP配置失败 (代码 "));
        Serial.print(devStatus);
        Serial.println(F(")"));
    }
}

void loop() {
  // put your main code here, to run repeatedly:
    if (!dmpReady) return;
    // 从FIFO读取包
    if (mpu.dmpGetCurrentFIFOPacket(fifoBuffer)) {
     
        #ifdef OUTPUT_READABLE_YAWPITCHROLL
            mpu.dmpGetQuaternion(&q, fifoBuffer);
            mpu.dmpGetGravity(&gravity, &q);
            mpu.dmpGetYawPitchRoll(ypr, &q, &gravity);
           
            mpu.dmpGetQuaternion(&q, fifoBuffer);
            mpu.dmpGetAccel(&aa, fifoBuffer);
            mpu.dmpGetGravity(&gravity, &q);
            mpu.dmpGetLinearAccel(&aaReal, &aa, &gravity);

            acc_z=aaReal.z;
           
            angle_x=ypr[2] * 180/M_PI;
            angle_y=ypr[1] * 180/M_PI;
            angle_z=ypr[0] * 180/M_PI;
            angle_x_ano = ypr[2] * 180/M_PI;
            angle_y_ano = ypr[1] * 180/M_PI;
            angle_z_ano = ypr[0] * 180/M_PI;
            Send_Data_Attitude(angle_x_ano, angle_y_ano, angle_z_ano); //发送欧拉角
        #endif

        PID_control();

        sample_valid = 0;
        sample_ready = 1;
        sample_cnt = sample_cnt + 1;
    }
```

这一代的航电部分，我们选择自行绘制PCB板，主控芯片选择了Atmega328p，USB转TTL芯片选择的是CH340N（之前帖子中提到的无法识别设备的问题已经解决，原因就是Type-c接口焊接不牢固，后面我用烙铁挨个引脚上锡加焊就解决了，感谢各位大佬的帮助），供电板上面的电压转换芯片选择的是74HC244D，实测可以带动三个舵机，四个舵机稍有勉强。

在这一代的结构部分，我们进一步完善了开伞的机械结构和尾翼的外形，新的开伞结构如下图所示：

![ks.png](https://img.kechuang.org:81/r/350229?c=resource)

舵机触发后，会将滑块和头锥的活动部分向上推出，头锥就会打开，完成开伞动作，如下图所示：

![图片_20240215213230.png](https://img.kechuang.org:81/r/350230?c=resource)

火箭的总装效果如下图所示。

![图片_20240215213432.jpg](https://img.kechuang.org:81/r/350231?c=resource)

然后我们进行了发射测试，并顺利完成开伞回收（开伞瞬间被发动机喷出的烟给挡住了，这里用一张正在降落阶段的照片代替。发射场地是一个废弃的飞机场，面积足够大，可能是由于长焦的缘故好像离民房很近）。

![图片_20240215214403.jpg](https://img.kechuang.org:81/r/350239?c=resource)

总结一下，在这个项目中，我学到了很多知识，也了解了很多未曾涉猎的领域。在实现梦想的道路上，感谢所有团队成员的辛勤付出，也感谢所有朋友对我们的制导帮助。希望在未来的日子里，我们继续前行在追梦的道路上。以上便是我和我的团队成员探索、追梦的全过程，有些地方用到的术语可能不准确，也希望各位批评指正，再次感谢各位的帮助。

[修改于 1年11个月前 - 2024/02/15 23:03:59]

来自：[航空航天](https://www.kechuang.org/f/74) / [喷气推进](https://www.kechuang.org/f/89)

12

 

 

 

 

14

 

 

 鼓励 

 

 分享

 

![img](https://img.kechuang.org:81/a/6683fd8fae9e9bf5f39ffb7b?c=userAvatar)

[wxn](https://www.kechuang.org/u/98022) ![十步芳草](https://www.kechuang.org/statics/grade_icon/v3l.png)

1年11个月前 IP:上海

929543

 

[1楼](https://www.kechuang.org/p/929543) 

请问一下有发射视频吗，想看看

引用

 

评论

 

 

 

 

 

![img](https://img.kechuang.org:81/a/62d54658fd6d3e429c348682?c=userAvatar)

[XYSC](https://www.kechuang.org/u/90139)![一表人才](https://www.kechuang.org/statics/grade_icon/v2l.png)

1年11个月前 IP:辽宁

929576

 

[2楼](https://www.kechuang.org/p/929576) 

我补充一点图片和视频资料

发动机展示

![wx_camera_1690006465743.jpg](https://img.kechuang.org:81/r/344491?c=resource)

发动机药形

![mmexport1706437071012.jpg]()

试车





Play

00:00

00:00

Mute

Settings

PIPAirPlayEnter fullscreen

<video class="plyr-dom" preload="none" poster="https://img.kechuang.org:81/r/350246/cover" data-rid="350246" data-plyr-title="VID_20240128_161222.mp4" src="https://img.kechuang.org:81/r/350246?c=resource&amp;t=hd&amp;w=9eqbx9qm" style="box-sizing: inherit; --tw-border-spacing-x: 0; --tw-border-spacing-y: 0; --tw-translate-x: 0; --tw-translate-y: 0; --tw-rotate: 0; --tw-skew-x: 0; --tw-skew-y: 0; --tw-scale-x: 1; --tw-scale-y: 1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness: proximity; --tw-gradient-from-position: ; --tw-gradient-via-position: ; --tw-gradient-to-position: ; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width: 0px; --tw-ring-offset-color: #fff; --tw-ring-color: rgba(59,130,246,.5); --tw-ring-offset-shadow: 0 0 #0000; --tw-ring-shadow: 0 0 #0000; --tw-shadow: 0 0 #0000; --tw-shadow-colored: 0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; --tw-contain-size: ; --tw-contain-layout: ; --tw-contain-paint: ; --tw-contain-style: ; display: inline-block; vertical-align: middle; border-radius: inherit; height: 662.25px; width: 883px; border: 0px; left: 0px; top: 0px; -webkit-user-select: none; max-width: 100%;"></video>

Play

仅供内部学术交流或培训使用，请先保存到本地。本内容不代表科创观点，未经原作者同意，请勿转载。

 

VID_20240128_161222.mp4 点击下载‎



![mmexport1690128745805.jpg]()

矢量机构





Play

00:00

00:00

Mute

Settings

PIPAirPlayEnter fullscreen

<video class="plyr-dom" preload="none" poster="https://img.kechuang.org:81/r/350244/cover" data-rid="350244" data-plyr-title="mmexport1707991872975.mp4" src="https://img.kechuang.org:81/r/350244?c=resource&amp;t=hd&amp;w=rkjdia12" style="box-sizing: inherit; --tw-border-spacing-x: 0; --tw-border-spacing-y: 0; --tw-translate-x: 0; --tw-translate-y: 0; --tw-rotate: 0; --tw-skew-x: 0; --tw-skew-y: 0; --tw-scale-x: 1; --tw-scale-y: 1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness: proximity; --tw-gradient-from-position: ; --tw-gradient-via-position: ; --tw-gradient-to-position: ; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width: 0px; --tw-ring-offset-color: #fff; --tw-ring-color: rgba(59,130,246,.5); --tw-ring-offset-shadow: 0 0 #0000; --tw-ring-shadow: 0 0 #0000; --tw-shadow: 0 0 #0000; --tw-shadow-colored: 0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; --tw-contain-size: ; --tw-contain-layout: ; --tw-contain-paint: ; --tw-contain-style: ; display: inline-block; vertical-align: middle; border-radius: inherit; height: 662.25px; width: 883px; border: 0px; left: 0px; top: 0px; -webkit-user-select: none; max-width: 100%;"></video>

Play

仅供内部学术交流或培训使用，请先保存到本地。本内容不代表科创观点，未经原作者同意，请勿转载。

 

mmexport1707991872975.mp4 点击下载‎







Play

00:00

00:00

Mute

Settings

PIPAirPlayEnter fullscreen

<video class="plyr-dom" preload="none" poster="https://img.kechuang.org:81/r/350248/cover" data-rid="350248" data-plyr-title="VID_20240215_112316.mp4" src="https://img.kechuang.org:81/r/350248?c=resource&amp;t=hd&amp;w=hq1c3zbv" style="box-sizing: inherit; --tw-border-spacing-x: 0; --tw-border-spacing-y: 0; --tw-translate-x: 0; --tw-translate-y: 0; --tw-rotate: 0; --tw-skew-x: 0; --tw-skew-y: 0; --tw-scale-x: 1; --tw-scale-y: 1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness: proximity; --tw-gradient-from-position: ; --tw-gradient-via-position: ; --tw-gradient-to-position: ; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width: 0px; --tw-ring-offset-color: #fff; --tw-ring-color: rgba(59,130,246,.5); --tw-ring-offset-shadow: 0 0 #0000; --tw-ring-shadow: 0 0 #0000; --tw-shadow: 0 0 #0000; --tw-shadow-colored: 0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; --tw-contain-size: ; --tw-contain-layout: ; --tw-contain-paint: ; --tw-contain-style: ; display: inline-block; vertical-align: middle; border-radius: inherit; height: 662.25px; width: 883px; border: 0px; left: 0px; top: 0px; -webkit-user-select: none; max-width: 100%;"></video>

Play

仅供内部学术交流或培训使用，请先保存到本地。本内容不代表科创观点，未经原作者同意，请勿转载。

 

VID_20240215_112316.mp4 点击下载‎





 **加载全文**

 

引用

 

**评论(5)**

 

 

3

 

 

 

 

![img](https://img.kechuang.org:81/a/62d8c49bc8de9846c4afcad5?c=userAvatar)

[chenruixi](https://www.kechuang.org/u/96478)![十步芳草](https://www.kechuang.org/statics/grade_icon/v3l.png)

1年11个月前 IP:江苏

929735

 

[3楼](https://www.kechuang.org/p/929735) 

自己写卡尔曼，精度恐怕问题不小吧

线性化处理后的模型会存在较大的截断误差，感觉以328p这种小芯片的算力跑不了UT变换，所以性价比更高的是用自带滤波的陀螺仪。（记得捷特智能的jy61p精度不错，价格也还好。）

发动机的侧向推力有测么，视频看不清。

做做尾翼性价比更高，矢量发动机大可不必。

引用

 

评论

 

 

2

 

 

 

 

![img](https://img.kechuang.org:81/a/6239d658713b0e43e89615d8?c=userAvatar)

[白沫0001](https://www.kechuang.org/u/94933)![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)作者

1年11个月前 IP:辽宁

929740

 

[4楼](https://www.kechuang.org/p/929740) 

> 引用[chenruixi](https://www.kechuang.org/u/96478)发表于[3](https://www.kechuang.org/p/929735?redirect=true)楼的内容
>
> 自己写卡尔曼，精度恐怕问题不小吧线性化处理后的模型会存在较大的截断误差，感觉以328p这种小芯片的算...

其实自己搓卡尔曼的目标更多的事解决Z轴漂移，实测也有一定的优化，不过也会飘，只是飘的不那么离谱了而已，这个代码实测能跑。

我们后面想用jy901b，里面也自带滤波算法。

发动机侧向推力没有测试过，我们没有矢量试车台，下一步我们会转向鸭翼控制，非常感谢老哥的指导

引用

 

评论

 

 

 

 

 

![img](https://img.kechuang.org:81/a/65be1fefba06745174d9e98b?c=userAvatar)

[活着_未来可期](https://www.kechuang.org/u/103157)![浪迹天涯](https://www.kechuang.org/statics/grade_icon/v1l.png)

1年11个月前 IP:浙江

929763

 

[5楼](https://www.kechuang.org/p/929763) 

发动机固定全压螺栓会不会过细。给你看一下我的，不过太粗也不好我这个M8 180mm好像碳纤维管57*55喷口堵头简单3D打印了一个厚度7mm单单这些应该达到了700g。为开源精神致敬！加油![wx_camera_1706414038522.jpg](https://img.kechuang.org:81/r/350495?c=resource)

 **加载全文**

 

引用

 

**评论(2)**

 

 

1

 

 

 

 

![img](https://img.kechuang.org:81/a/6239d658713b0e43e89615d8?c=userAvatar)

[白沫0001](https://www.kechuang.org/u/94933)![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)作者

1年11个月前 IP:辽宁

929787

 

[6楼](https://www.kechuang.org/p/929787) 

> 引用[活着_未来可期](https://www.kechuang.org/u/103157)发表于[5](https://www.kechuang.org/p/929763?redirect=true)楼的内容
>
> 发动机固定全压螺栓会不会过细。给你看一下我的，不过太粗也不好我这个M8 180mm好像碳纤维管57*...



你这个法兰盘和喷口是什么材质，酚醛的嘛，感觉酚醛不太结实呢

我们后面会改良发动机，不过目前的首要目标变成减重了，还是感谢你的支持

引用

 

评论

 

 

 

 

 

![img](https://img.kechuang.org:81/a/65be1fefba06745174d9e98b?c=userAvatar)

[活着_未来可期](https://www.kechuang.org/u/103157)![浪迹天涯](https://www.kechuang.org/statics/grade_icon/v1l.png)

1年11个月前 IP:浙江

929790

 

[7楼](https://www.kechuang.org/p/929790) 

> 引用[白沫0001](https://www.kechuang.org/u/94933)发表于[6](https://www.kechuang.org/p/929787?redirect=true)楼的内容
>
> 你这个法兰盘和喷口是什么材质，酚醛的嘛，感觉酚醛不太结实呢我们后面会改良发动机，不过目前的首要目标变...

不是酚醛树脂，图片上的是PLA(3D打印)无法使用的，之后是上45钢要考虑散热问题。耐高温的好像有钛合金吧但是极贵

引用

 

**评论(1)**

 

 

 

 

 

![img](https://img.kechuang.org:81/a/6239d658713b0e43e89615d8?c=userAvatar)

[白沫0001](https://www.kechuang.org/u/94933)![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)作者

1年11个月前 IP:中国

930015

 

[8楼](https://www.kechuang.org/p/930015) 

> 引用[活着_未来可期](https://www.kechuang.org/u/103157)发表于[7](https://www.kechuang.org/p/929790?redirect=true)楼的内容
>
> 不是酚醛树脂，图片上的是PLA(3D打印)无法使用的，之后是上45钢要考虑散热问题。耐高温的好像有钛...

钛合金确实贵，之前我们也考虑过

引用

 

评论

 

 

1

 

 

 

 

![img](https://img.kechuang.org:81/a/667620e4586c915535653e83?c=userAvatar)

[resfeber](https://www.kechuang.org/u/104252)![浪迹天涯](https://www.kechuang.org/statics/grade_icon/v1l.png)

1年7个月前 IP:四川

932918

 

[9楼](https://www.kechuang.org/p/932918) 

想请教lz个问题，已有尾翼的气动制导为什么还需要矢量喷口呢，是否二者取其一即可？

![sticker](https://img.kechuang.org:81/sticker/314694)



引用

 

**评论(3)**

 

 

 

 

 

![img](https://img.kechuang.org:81/a/6239d658713b0e43e89615d8?c=userAvatar)

[白沫0001](https://www.kechuang.org/u/94933)![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)作者

1年6个月前 IP:中国

934585

 

[10楼](https://www.kechuang.org/p/934585) 

> 引用[resfeber](https://www.kechuang.org/u/104252)发表于[9](https://www.kechuang.org/p/932918?redirect=true)楼的内容
>
> 想请教lz个问题，已有尾翼的气动制导为什么还需要矢量喷口呢，是否二者取其一即可？

进一步提升稳定性，下一步可以做其他的制导

引用

 

评论

 

 

 

 

 

![img](https://img.kechuang.org:81/a/630b0cb73bd4495abc78277c?c=userAvatar)

[氙氟工作室](https://www.kechuang.org/u/97117)![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)

6个月20天前 IP:上海

945585

 

[12楼](https://www.kechuang.org/p/945585) 

同志，能不能发一下项目的GITHUB链接，谢谢同志！



引用

 

评论

 

 

 

 

 

##### 请完成以下任务，获取完整发表权限。



通过入学培训



发表3条电文















































0/100000

专栏

##### 目前还不能开设专栏，通常是因为你参与讨论较少或没有文章被列入精选。

我已阅读并同意遵守与本次发表相关的全部协议。[查看协议](https://www.kechuang.org/protocol)

 

所属专业

[喷气推进](https://www.kechuang.org/f/89)

所属分类

[飞控制导](https://www.kechuang.org/f/89?cat=132)

上级专业

[航空航天](https://www.kechuang.org/f/74)

同级专业

[航空技术](https://www.kechuang.org/f/165)[航天技术](https://www.kechuang.org/f/366)[火箭燃料](https://www.kechuang.org/f/368)

关注

![img](https://img.kechuang.org:81/a/6239d658713b0e43e89615d8?c=userAvatar)

[白沫0001](https://www.kechuang.org/u/94933)

![实习会员](https://www.kechuang.org/statics/grade_icon/v0l.png)进士 机友

文章

 

4

 

回复

 

56

 

学术分

 

-1

2022/03/22注册，2个月2天前活动

无限可能

主体类型：个人

所属领域：无

认证方式：手机号

IP归属地：辽宁

[名片](https://www.kechuang.org/u/94933)私信

作者最新文章

[漫谈卡尔曼滤波算法](https://www.kechuang.org/t/89983)

[软件综合](https://www.kechuang.org/f/134)[白沫0001](https://www.kechuang.org/u/94933) 1年11个月前

[今天，我们实现了一个来自2021年的梦想——星云科技矢量火箭制作流程及开源计划](https://www.kechuang.org/t/89933)

[喷气推进](https://www.kechuang.org/f/89)[白沫0001](https://www.kechuang.org/u/94933) 1年11个月前

[求助：CH340N连接typeC口相关问题](https://www.kechuang.org/t/89809)

[电子技术](https://www.kechuang.org/f/37)[白沫0001](https://www.kechuang.org/u/94933) 2年0个月前

[简单分享一下自己两年来做火箭飞控开发的历程，请大家指教](https://www.kechuang.org/t/89647)

[喷气推进](https://www.kechuang.org/f/89)[白沫0001](https://www.kechuang.org/u/94933) 2年3个月前

相似文章推荐

[【业余火箭制式化系列之三】打造震动式沉降加速器](https://www.kechuang.org/t/33075)

[喷气推进](https://www.kechuang.org/f/89)[ehco](https://www.kechuang.org/u/3525) 15年0个月前

[如何对固体火箭发动机测试数据进行初步处理与计算分析](https://www.kechuang.org/t/90817)

[喷气推进](https://www.kechuang.org/f/89)[LSEQY](https://www.kechuang.org/u/91584) 1年1个月前

[这两个东西是专门为论坛比较牛逼的高人准备的](https://www.kechuang.org/t/34391)

[喷气推进](https://www.kechuang.org/f/89)[qq154884863](https://www.kechuang.org/u/20514) 14年9个月前

[（已更新dark-ll的部分）[CZSA\] （欢迎砖拍）国内业余界第一台35N固体燃料球状引擎试车及固体燃料柱孔球状发动机药柱计算方法](https://www.kechuang.org/t/84942)

[喷气推进](https://www.kechuang.org/f/89)[ERIC20041219](https://www.kechuang.org/u/79161) 6年2个月前

[固体火箭版块资源索引（2005-2008）](https://www.kechuang.org/t/8786)

[喷气推进](https://www.kechuang.org/f/89)[power_rdx](https://www.kechuang.org/u/2998) 17年6个月前

[固体火箭性能计算流程](https://www.kechuang.org/t/960)

[喷气推进](https://www.kechuang.org/f/89)[阿丕](https://www.kechuang.org/u/37) 20年1个月前

[【彩虹出品】APCP第三次试车成功](https://www.kechuang.org/t/58568)

[喷气推进](https://www.kechuang.org/f/89)[彩虹之巅](https://www.kechuang.org/u/32375) 12年8个月前

[液体火箭发动机再生冷却冷却剂物性影响及其关键数据变化规律](https://www.kechuang.org/t/90634)

[喷气推进](https://www.kechuang.org/f/89)[LSEQY](https://www.kechuang.org/u/91584) 1年3个月前

[AHRS设计方案](https://www.kechuang.org/t/35973)

[喷气推进](https://www.kechuang.org/f/89)[xuetianwuran](https://www.kechuang.org/u/22032) 14年7个月前

[【业余火箭制式化系列之一】打造火箭燃料专用真空恒温浇铸仓](https://www.kechuang.org/t/33071)

[喷气推进](https://www.kechuang.org/f/89)[ehco](https://www.kechuang.org/u/3525) 15年0个月前

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

添加笔记
