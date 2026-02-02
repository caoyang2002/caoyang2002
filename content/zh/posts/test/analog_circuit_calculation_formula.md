+++
title = '模拟电路公式简述'
date = 2026-02-03T01:33:42+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
+++


### 一、 基础定律（所有计算的基石）
1.  **欧姆定律**
    *   \( V = I \times R \)
    *   描述线性电阻中电压、电流、电阻的关系。

2.  **基尔霍夫定律**
    *   **KCL（电流定律）**：流入任一节点的电流之和等于流出该节点的电流之和。\(\sum I_{in} = \sum I_{out}\)
    *   **KVL（电压定律）**：沿任一闭合回路，所有电压降的代数和为零。\(\sum V = 0\)
    *   这是分析任何复杂电路的根基。

3.  **功率计算**
    *   \( P = V \times I = I^2 \times R = \frac{V^2}{R} \)

---

### 二、 分立器件模型与公式

#### 1. 二极管
*   **肖克利方程（理想）**：
    \( I_D = I_S (e^{\frac{V_D}{n V_T}} - 1) \)
    *   \(I_S\)：反向饱和电流
    *   \(V_T\)：热电压 (\( \frac{kT}{q} \approx 26mV @ 300K\))
    *   \(n\)：发射系数（通常1-2）
*   **简化模型（工程常用）**：
    *   导通时：硅管压降 \(V_D \approx 0.6 - 0.7V\)， 锗管 \(V_D \approx 0.2 - 0.3V\)。
    *   截止时：\(I_D \approx 0\)。

#### 2. 双极型晶体管（BJT）
*   **放大模式（Active）工作前提**：
    *   NPN：\(V_C > V_B > V_E\)， 发射结正偏，集电结反偏。
*   **电流关系（核心）**：
    *   \(I_E = I_C + I_B\)
    *   \(\beta\)（直流电流放大系数）：\( \beta = \frac{I_C}{I_B} \)， \(I_C = \beta I_B\)
    *   \(\alpha\)：\( \alpha = \frac{I_C}{I_E} = \frac{\beta}{\beta + 1}\)
*   **Ebers-Moll模型**：描述BJTV-I特性的基本方程。

#### 3. 场效应晶体管（MOSFET）
*   **工作区域判断**：
    *   **截止区**：\(V_{GS} < V_{th}\) （阈值电压）， \(I_{DS} \approx 0\)
    *   **三极管区/线性区**：\(V_{GS} > V_{th}\) 且 \(V_{DS} < (V_{GS} - V_{th})\)
        \(I_D = \mu_n C_{ox} \frac{W}{L} [ (V_{GS}-V_{th})V_{DS} - \frac{1}{2}V_{DS}^2 ]\)
    *   **饱和区/恒流区（放大区）**：\(V_{GS} > V_{th}\) 且 \(V_{DS} \ge (V_{GS} - V_{th})\)
        \(I_D = \frac{1}{2} \mu_n C_{ox} \frac{W}{L} (V_{GS}-V_{th})^2 (1 + \lambda V_{DS})\)
    *   其中 \(k_n = \mu_n C_{ox} \frac{W}{L}\) 称为**跨导参数**。

---

### 三、 基本放大器参数与公式

#### 1. 通用增益公式
*   **电压增益**：\( A_v = \frac{V_{out}}{V_{in}} \)
*   **电流增益**：\( A_i = \frac{I_{out}}{I_{in}} \)
*   **跨阻增益**：\( A_r = \frac{V_{out}}{I_{in}} \) （单位：Ω）
*   **跨导增益**：\( A_g = \frac{I_{out}}{V_{in}} \) （单位：S）

#### 2. 小信号模型关键参数
*   **BJT的跨导**：\( g_m = \frac{I_C}{V_T} \approx \frac{I_C (mA)}{26mV} \)
*   **BJT的输入电阻（rπ）**：\( r_\pi = \frac{\beta}{g_m} \)
*   **MOSFET的跨导（饱和区）**：\( g_m = \frac{\partial I_D}{\partial V_{GS}} = \sqrt{2 \mu_n C_{ox} \frac{W}{L} I_D} = \frac{2I_D}{V_{GS}-V_{th}} \)
*   **MOSFET的输出电阻（考虑沟道长度调制）**：\( r_o = \frac{1}{\lambda I_D} \approx \frac{V_A}{I_D} \) （\(V_A\)为厄尔利电压）

---

### 四、 基本放大器组态（以BJT为例）

#### 1. 共射放大器（CE）
*   **电压增益（带负载Rc，忽略ro）**：\( A_v = -g_m (R_C // r_o // R_L) \approx -g_m (R_C // R_L) \)
    *   “-”号表示反相。
*   **输入电阻**：\( R_{in} = R_B // r_\pi \)
*   **输出电阻**：\( R_{out} \approx R_C // r_o \)

#### 2. 共集放大器（射随器，CC）
*   **电压增益**：\( A_v \approx 1 \) （略小于1，同相）
*   **输入电阻**：\( R_{in} = R_B // [r_\pi + (\beta+1)(R_E // R_L)] \) （很高）
*   **输出电阻**：\( R_{out} = R_E // \frac{r_\pi + (R_{source}//R_B)}{\beta+1} \) （很低）

#### 3. 共基放大器（CB）
*   **电压增益**：\( A_v = g_m (R_C // R_L) \) （同相，值大）
*   **输入电阻**：\( R_{in} \approx \frac{1}{g_m} \) （很低）
*   **输出电阻**：\( R_{out} \approx R_C \) （高）

---

### 五、 运算放大器（Op-Amp）理想公式
**黄金法则（负反馈工作时）**：
1.  **虚短**：\( V_+ \approx V_- \) （两输入端电压差为零）。
2.  **虚断**：\( I_+ \approx I_- \approx 0 \) （两输入端输入电流为零）。

**由此推导出常见电路公式**：
*   **反相放大器**：
    \( A_v = \frac{V_{out}}{V_{in}} = -\frac{R_f}{R_{in}} \)
    \( R_{in} = R_{in} \) （从信号源看进去的输入电阻）
*   **同相放大器**：
    \( A_v = \frac{V_{out}}{V_{in}} = 1 + \frac{R_f}{R_{in}} \)
    \( R_{in} \to \infty \) （理想）
*   **电压跟随器**：\( A_v = 1 \)
*   **加法器**：\( V_{out} = -R_f (\frac{V_1}{R_1} + \frac{V_2}{R_2} + ...) \)
*   **差分放大器**：\( V_{out} = \frac{R_f}{R_{in}}(V_2 - V_1) \) （当电阻匹配时）

---

### 六、 频率响应与滤波器
*   **RC电路的时间常数**：\( \tau = R \times C \)
*   **截止频率（-3dB点）**：
    *   RC低通/高通：\( f_c = \frac{1}{2\pi RC} \)
    *   更一般地，对于单极点系统：\( f_c = \frac{1}{2\pi \tau} \)， 其中 \(\tau\) 是**从电容看出去的开路电阻（戴维南等效电阻）**与电容C的乘积。
*   **积分器（近似）**：\( V_{out} \approx -\frac{1}{RC} \int V_{in} dt \)
*   **微分器（近似）**：\( V_{out} \approx -RC \frac{dV_{in}}{dt} \)

---

### 七、 反馈系统
*   **基本反馈方程**：
    \( A_f = \frac{A}{1 + A \beta} \)
    *   \(A\)：开环增益
    *   \(\beta\)：反馈系数
    *   \(A_f\)：闭环增益
    *   \(1 + A\beta\)：**环路增益**，决定稳定性、精度改善程度。
