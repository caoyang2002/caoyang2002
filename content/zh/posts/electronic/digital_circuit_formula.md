+++
title = '数字电路公式介绍'
date = 2026-02-03T01:35:10+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
+++

数字电路的核心计算公式主要集中在**布尔代数**、**逻辑门运算**和**触发器时序**等方面。

## 一、**布尔代数基本公式**

### 1. 基本运算
- **与（AND）**：\( F = A \cdot B \)  
- **或（OR）**：\( F = A + B \)  
- **非（NOT）**：\( F = \bar{A} \)
- **异或（XOR）**：\( F = A \oplus B = A\bar{B} + \bar{A}B \)
- **同或（XNOR）**：\( F = A \odot B = \overline{A \oplus B} = AB + \bar{A}\bar{B} \)

### 2. 基本定律
- **交换律**：  
  \( A + B = B + A \)  
  \( A \cdot B = B \cdot A \)
- **结合律**：  
  \( (A + B) + C = A + (B + C) \)  
  \( (A \cdot B) \cdot C = A \cdot (B \cdot C) \)
- **分配律**：  
  \( A \cdot (B + C) = A \cdot B + A \cdot C \)  
  \( A + (B \cdot C) = (A + B) \cdot (A + C) \)

### 3. 恒等式
- \( A + 0 = A \)， \( A \cdot 1 = A \)
- \( A + 1 = 1 \)， \( A \cdot 0 = 0 \)
- \( A + A = A \)， \( A \cdot A = A \)
- \( A + \bar{A} = 1 \)， \( A \cdot \bar{A} = 0 \)

### 4. 德摩根定理（De Morgan's Theorem）
- **与或转换**：  
  \( \overline{A \cdot B} = \bar{A} + \bar{B} \)  
  \( \overline{A + B} = \bar{A} \cdot \bar{B} \)
- **推广到多变量**：  
  \( \overline{A \cdot B \cdot C} = \bar{A} + \bar{B} + \bar{C} \)  
  \( \overline{A + B + C} = \bar{A} \cdot \bar{B} \cdot \bar{C} \)

### 5. 常用化简公式
- **吸收律**：  
  \( A + A \cdot B = A \)  
  \( A \cdot (A + B) = A \)
- **合并律**：  
  \( A \cdot B + A \cdot \bar{B} = A \)  
  \( (A + B) \cdot (A + \bar{B}) = A \)
- **冗余律**：  
  \( A + \bar{A} \cdot B = A + B \)  
  \( A \cdot (\bar{A} + B) = A \cdot B \)

---

## 二、**组合逻辑电路相关公式**
### 1. 逻辑函数表示
- **标准与或式（SOP）**：最小项之和  
  \( F = \sum m(0, 1, 3) \)
- **标准或与式（POS）**：最大项之积  
  \( F = \prod M(2, 4, 5, 6, 7) \)

### 2. 多路选择器（MUX）
- \( n \) 个选择控制端 → 可选择 \( 2^n \) 路输入  
  输出 \( Y = \sum_{i=0}^{2^n-1} (D_i \cdot M_i) \)，其中 \( M_i \) 为选择信号对应的最小项。

---

## 三、**时序逻辑电路公式**
### 1. 触发器特征方程
- **D触发器**：\( Q_{n+1} = D \)
- **JK触发器**：\( Q_{n+1} = J\bar{Q}_n + \bar{K}Q_n \)
- **T触发器**：\( Q_{n+1} = T \oplus Q_n \)
- **SR触发器**：\( Q_{n+1} = S + \bar{R}Q_n \)（约束条件：\( S \cdot R = 0 \)）

### 2. 时序电路分析
- **状态方程**：\( Q_{n+1} = f(Q_n, \text{输入}) \)
- **输出方程**：\( Z = g(Q_n, \text{输入}) \)

---

## 四、**脉冲与时钟相关**
### 1. 频率与周期
- \( f = \frac{1}{T} \)，\( T = t_{\text{high}} + t_{\text{low}} \)
- **占空比**：\( D = \frac{t_{\text{high}}}{T} \times 100\% \)

### 2. 计数器模值
- **模 \( N \) 计数器**：\( N = 2^n \)（n位二进制计数器）
- 非2的幂次模值：需用反馈或预置数实现（如模10计数器）。

---

## 五、**常用集成电路参数公式**
### 1. 传播延迟
- \( t_{pd} = \max(t_{PHL}, t_{PLH}) \)，其中 \( t_{PHL} \) 为高到低延迟，\( t_{PLH} \) 为低到高延迟。

### 2. 噪声容限
- **低电平噪声容限**：\( NM_L = V_{IL(max)} - V_{OL(max)} \)
- **高电平噪声容限**：\( NM_H = V_{OH(min)} - V_{IH(min)} \)

---

## 六、**存储器容量计算**
- **容量 = 地址单元数 × 数据位宽**
  例如：\( 2^{10} \) 个地址 × 8位 = \( 1024 \times 8 \) bit = 1 KB
