+++
title = '5f5f68c2'
date = 2026-03-03T21:31:34+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"

+++

### **魔方转动公式符号及示意图** Notation

![Gancube](https://www.gancube.cn/wp-content/themes/chtemp/static/CFOP/images/new_images/img1.png)

小写字母：双层转  

大写字母：顺时针转 90°  

字母 + `‘`：逆时针转 90° 

字母 + 2：转 180°   **Letter + 2:** Turn 180°

蓝色字母：用左食指拨动   **Blue Letter:** By left index finger

红色字母：用右拇指拨动   **Red Letter:** By right thumb

橙色字母：用中指/无名指/尾指拨动
**Orange Letter:** By middle finger/ring finger/little finger

### **CFOP复原步骤** CFOP Steps

![Gancube](https://www.gancube.cn/wp-content/themes/chtemp/static/CFOP/images/new_images/img2.png)

OLL 和 PLL 是俯视图 OLL and PLL are vertical views.

OLL：蓝块和小蓝条表示黄色块
OLL: The blue bars and squares represent the yellow pieces.

PLL：小黑条表示特征 / 相同色块
PLL: The black bars represent the same colored pieces.

***温馨提示 Tips**

CROSS 复原方法较多，本教程主要介绍后面 3 步的复原公式。

There are many ways to solve CROSS, this tutorial introduces the next three steps of CFOP.

### F2L

### 前两层归位 First 2 Layers

![Gancube](https://www.gancube.cn/wp-content/themes/chtemp/static/CFOP/images/new_images/img3.png)

### OLL

### 最后一层翻色 Orientation of Last Layer

![Gancube](https://www.gancube.cn/wp-content/themes/chtemp/static/CFOP/images/new_images/img4.png)

### PLL

### 最后一层翻色 Permutation of Last Layer

![Gancube](https://www.gancube.cn/wp-content/themes/chtemp/static/CFOP/images/new_images/img5.png)

![Gancube](https://www.gancube.cn/wp-content/themes/chtemp/static/CFOP/images/new_images/img6.png)![Gancube](https://www.gancube.cn/wp-content/themes/chtemp/static/CFOP/images/new_images/img7.png)

**魔方日常护理**

1、日常使用时，需要定时给魔方添加养护油，以便长期养护，减少磨损；当魔方手感干涩时，需要给魔方添加润滑油；当魔方过滑时，可给魔方添加稳速油。

2、给魔方上油时，应向接触面或卡脚处滴入1-2滴（油太多会导致魔方变粘），然后转动魔方数次，使油均匀粘附在魔方内部。

3、切勿使用魔方油以外的润滑油，否则可能会导致魔方手感变差。

# 转动逻辑

菱角归位中，一个角，如果需要转向“上+右”，

例如：

标准的颜色位置是，绿色在上面，红色在正面，白色的右面，

但是需要调整的角是，绿色在右面，红色在上面，白色在正面。

那么可以通过 `F'` `U'` 即可归正，但是其他面会乱，

那么如何如何不影响其他面进行归位呢？

我也说不上来如何归位，就是看，我直觉就是把需要调的放在不会动的一面，然后转动需要调整的，直到出现机会。



如果是中间层的两个交换位置，那么直接`F'2` 即可，然后就是归位：

首先可以发现底面在上方了，这时候直接`F2` 是完成归位的方案，但是会丢失中间层已经完成的交换，如何避免中间层的交换呢？

可以通过中间层临时换到一个不会被更改的位置上去。比如`E'`，然后 `F2` 即可

# 中间层归位

类型一：在上方有一个中间的，需要移动到下方中间层，那么就需要先放到中间层，然后再归位。

可以通过`R'` 可以放到中间并完成归位，但是这时候转动中间层灰破坏完整的一面，所以需要更改策略。

1. 目标块所在侧面相内旋转一次`R'`
2. 正面逆时针旋转一次
3. 顶面向右旋转一次
4. 正面



类型二：无法通过右侧一次旋转的，需要额外将两个面颜色自转一次的类型：

1. 顶面向右旋转一次
2. 目标块所在侧面向下旋转一次
3. 两块旋转
4. 归位
5. 回到类型一

类型三：中间的两面块，位置无论如何都不能变。

向上旋转一下，可以改变位置到上一个类型。

## 📋 CFOP 完整公式表

### 第一部分：Cross（底层十字）
**目标**：8步内完成底层十字
**说明**：这一步没有固定公式，需要根据具体情况灵活处理。建议练习盲拧十字，即观察时规划好十字的完整路径。

---

### 第二部分：F2L（前两层，41个标准公式）

F2L 的核心是**将角块和棱块配对后插入**。以下是41个标准形态的公式，按类型分组：

#### 组1：角块在顶层，棱块在顶层（基本型）

|  编号  | 形态描述                     | 公式           |
| :----: | :--------------------------- | :------------- |
| **F1** | 角块白色朝上，棱块在相邻位置 | `U R U' R'`    |
| **F2** | 角块白色朝上，棱块在相对位置 | `y' U' R' U R` |
| **F3** | 角块白色朝侧，棱块在对应位置 | `R U R'`       |
| **F4** | 角块白色朝侧，棱块需调整     | `y' R' U' R`   |

#### 组2：角块在底层，棱块在顶层

|  编号  | 形态描述                       | 公式                   |
| :----: | :----------------------------- | :--------------------- |
| **F5** | 角块已归位，棱块在顶层         | `U R U' R' U' F' U F`  |
| **F6** | 角块在底层但方向错，棱块在顶层 | `R U' R' U R U R'`     |
| **F7** | 角块白色朝右，棱块在顶层右侧   | `U' R U R' U2 R U' R'` |
| **F8** | 角块白色朝前，棱块在顶层前方   | `U F' U' F U' R U R'`  |

#### 组3：角块在顶层，棱块在中层

|  编号   | 形态描述                     | 公式                   |
| :-----: | :--------------------------- | :--------------------- |
| **F9**  | 棱块在中层，角块在顶层       | `R U' R' U R U R'`     |
| **F10** | 棱块在中层错位，角块白色朝上 | `U R U2 R' U R U' R'`  |
| **F11** | 棱块在中层，角块白色朝侧     | `y' R' U R U' R' U' R` |

#### 组4：角块和棱块都在底层（最复杂的情况）

|  编号   | 形态描述                 | 公式                           |
| :-----: | :----------------------- | :----------------------------- |
| **F12** | 角块棱块都在底层但分离   | `R U' R' U' R U R' U2 R U' R'` |
| **F13** | 角块棱块连在一起但方向错 | `R U R' U' R U R'`             |
| **F14** | 角块棱块错位连接         | `y' R' U' R U' R' U R`         |

> **提示**：F2L 的41个公式可以简化为理解4个基本型，其他都是通过调整位置转化为基本型。建议先理解原理再记忆。

---

### 第三部分：OLL（顶层翻色，57个公式）

OLL 分为**十字OLL**（已有十字）和**非十字OLL**。这里列出最常用的20个：

#### 3.1 十字OLL（7个）

|  编号   | 图形  | 公式                            |
| :-----: | :---- | :------------------------------ |
| **O21** | 直线  | `F R U R' U' F'`                |
| **O22** | 拐角  | `f R U R' U' f'`                |
| **O23** | 点    | `F R U R' U' F' f R U R' U' f'` |
| **O24** | 鱼形1 | `R U R' U R U2 R'`              |
| **O25** | 鱼形2 | `R' U' R U' R' U2 R`            |
| **O26** | 坦克1 | `R U2 R' U' R U' R'`            |
| **O27** | 坦克2 | `R' U2 R U R' U R`              |

#### 3.2 常用非十字OLL（10个）

|  编号   | 图形   | 公式                                |
| :-----: | :----- | :---------------------------------- |
| **O1**  | H形    | `R U R' U' R' F R F'`               |
| **O2**  | 反H    | `F R U R' U' F'`                    |
| **O3**  | 闪电1  | `r U R' U R U2 r'`                  |
| **O4**  | 闪电2  | `l' U' L U' L' U2 l`                |
| **O5**  | 十字架 | `R U2 R2 U' R2 U' R2 U2 R`          |
| **O6**  | 小拐角 | `R' F R U R' F' R F U' F'`          |
| **O7**  | 大拐角 | `L F' L' U' L F L' F' U F`          |
| **O8**  | 双鱼   | `R U2 R2 U' R U' R' U2 F R F'`      |
| **O9**  | 眼镜   | `R' U' R U' R' U2 R F R U R' U' F'` |
| **O10** | 风车   | `R U R' U R U2 R' F R U R' U' F'`   |

---

### 第四部分：PLL（顶层归位，21个公式）

PLL 分为**棱换**、**角换**和**对角换**三类：

#### 4.1 棱换（4个）

|  编号  | 名称             | 公式                                   |
| :----: | :--------------- | :------------------------------------- |
| **P1** | 三棱换（顺时针） | `R U' R U R U R U' R' U' R2`           |
| **P2** | 三棱换（逆时针） | `R2 U R U R' U' R' U' R' U R'`         |
| **P3** | 对棱换           | `M2 U M2 U2 M2 U M2`                   |
| **P4** | 邻棱换           | `R U R' U' R' F R2 U' R' U' R U R' F'` |

#### 4.2 角换（4个）

|  编号  | 名称             | 公式                                           |
| :----: | :--------------- | :--------------------------------------------- |
| **P5** | 三角换（顺时针） | `x' R U' R' D R U R' D' R U R' D R U' R' D' x` |
| **P6** | 三角换（逆时针） | `x' R U R' D R U' R' D' R U' R' D R U R' D' x` |
| **P7** | 对角换           | `F R U' R' U' R U R' F' R U R' U' R' F R F'`   |
| **P8** | 邻角换           | `R U R' F' R U R' U' R' F R2 U' R' U'`         |

#### 4.3 对角+对棱（13个最常用）

|  编号   | 名称   | 公式                                                    |
| :-----: | :----- | :------------------------------------------------------ |
| **P9**  | T型    | `R U R' U' R' F R2 U' R' U' R U R' F'`                  |
| **P10** | Y型    | `F R U' R' U' R U R' F' R U R' U' R' F R F'`            |
| **P11** | F型    | `R' U' F' R U R' U' R' F R2 U' R' U' R U R' U R`        |
| **P12** | V型    | `R' U R' U' y R' F' R2 U' R' U R' F R F`                |
| **P13** | N型1   | `R U R' U R U R' F' R U R' U' R' F R2 U' R' U2 R U' R'` |
| **P14** | N型2   | `R' U R U' R' F' U' F R U R' F R' F' R U' R`            |
| **P15** | J型1   | `R U R' F' R U R' U' R' F R2 U' R' U'`                  |
| **P16** | J型2   | `R' U2 R U R' U2 L U' R U L'`                           |
| **P17** | R型1   | `R U2 R' U2 R' F R2 U' R' U' R U R' F'`                 |
| **P18** | R型2   | `R' U2 R U2 R B' R2 U R U R' U' R B`                    |
| **P19** | G型1   | `R U R' U' R' F R2 U' R' U' R U R' F'`                  |
| **P20** | G型2   | `R' U' R U R B' R2 U R U R' U' R B`                     |
| **P21** | 终极型 | `R U2 R' U' R U2 L' U R' U' L`                          |

---

## 📊 学习路线图

| 阶段       | 目标 | 需要掌握的公式                                        |
| :--------- | :--- | :---------------------------------------------------- |
| **入门期** | 60秒 | F2L基本型(10个) + 二步OLL(7个十字) + 二步PLL(6个棱换) |
| **进阶段** | 30秒 | 全F2L(41个) + 二步OLL(10个) + 全PLL(21个)             |
| **高手期** | 15秒 | 全F2L + 全OLL(57个) + 全PLL + 双向公式 + 非标         |

## 💡 记忆技巧

1. **分组记忆**：OLL和PLL按图形分组，一组一组学
2. **理解而非死记**：F2L重在理解角棱运动规律
3. **逐步替代**：先用层先法复原，遇到一个情况学一个公式
4. **反复练习**：每天练习10-15分钟，肌肉记忆自然形成

需要我详细讲解某个具体公式的手法和技巧吗？
