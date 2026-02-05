+++
title = 'LaTeX 数学公式完整指南'
date = 2026-02-04T22:10:12+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
math = true
+++

> 注意，本站使用 Hugo 构建，在页面上大多数外部工具库都不可用，进而无法渲染出对应的公式。

**参考链接：**

- [LaTeX: Symbols](https://artofproblemsolving.com/wiki/index.php/LaTeX:Symbols)
- [LaTeX: Commands](https://artofproblemsolving.com/wiki/index.php/LaTeX:Commands)

## 基本语法

### 行内公式与行间公式

#### 行内公式

方法1：使用 `$ ... $`

```latex
这是行内公式 $E = mc^2$，在文本中间。
```

这是行内公式 $E = mc^2$，在文本中间。


方法2：使用 `\( ... \)`（推荐）

```latex
爱因斯坦质能方程 \(E = mc^2\) 是著名的物理公式。
```

爱因斯坦质能方程 \(E = mc^2\) 是著名的物理公式。

#### 行间公式（无编号）

方法1：使用 `$$ ... $$`

```latex
$$E = mc^2$$
```

$$E = mc^2$$

方法2：使用 `\[ ... \]`（推荐）

```latex
\[E = mc^2\]
```

\[E = mc^2\]

#### 行间公式（有编号）

```latex
\begin{equation}
E = mc^2
\end{equation}
```

无编号但仍使用 equation 环境

```latex
\begin{equation*}
E = mc^2
\end{equation*}
```

## 数学符号大全

### 基本运算符号

算数运算

| LaTeX 命令 | 渲染结果   | 中文名称 | 英文名称       |
| ---------- | ---------- | -------- | -------------- |
| `+`        | $+$        | 加号     | Plus           |
| `-`        | $-$        | 减号     | Minus          |
| `\pm`      | $\pm$      | 正负号   | Plus-minus     |
| `\mp`      | $\mp$      | 负正号   | Minus-plus     |
| `\times`   | $\times$   | 乘号     | Multiplication |
| `\div`     | $\div$     | 除号     | Division       |
| `\cdot`    | $\cdot$    | 中心点   | Center dot     |
| `\ast`     | $\ast$     | 星号     | Asterisk       |
| `\star`    | $\star$    | 五角星   | Star           |
| `\circ`    | $\circ$    | 圆圈     | Circle         |
| `\bullet`  | $\bullet$  | 实心圆点 | Bullet         |
| `\diamond` | $\diamond$ | 菱形     | Diamond        |

### 关系符号

比较

| LaTeX 命令 | 渲染结果 | 说明     | 英文名称                 |
| ---------- | -------- | -------- | ------------------------ |
| `=`        | $=$      | 等于     | Equals                   |
| `\neq`     | $\neq$   | 不等于   | Not equal                |
| `<`        | $<$      | 小于     | Less than                |
| `>`        | $>$      | 大于     | Greater than             |
| `\leq`     | $\leq$   | 小于等于 | Less than or equal to    |
| `\geq`     | $\geq$   | 大于等于 | Greater than or equal to |
| `\ll`      | $\ll$    | 远小于   | Much less than           |
| `\gg`      | $\gg$    | 远大于   | Much greater than        |
| `\lll`     | $\lll$   | 超小于   | Very much less than      |
| `\ggg`     | $\ggg$   | 超大于   | Very much greater than   |

近似和相似

| LaTeX 命令  | 渲染结果    | 说明     | 英文名称                |
| ----------- | ----------- | -------- | ----------------------- |
| `\approx`   | $\approx$   | 约等于   | Approximately equal to  |
| `\sim`      | $\sim$      | 相似     | Similar to              |
| `\simeq`    | $\simeq$    | 相似等于 | Asymptotically equal to |
| `\cong`     | $\cong$     | 全等     | Congruent to            |
| `\equiv`    | $\equiv$    | 恒等     | Equivalent to           |
| `\propto`   | $\propto$   | 正比     | Proportional to         |
| `\parallel` | $\parallel$ | 平行     | Parallel to             |
| `\perp`     | $\perp$     | 垂直     | Perpendicular to        |


### 集合论符号

包含关系

| LaTeX 命令   | 渲染结果     | 说明             | 英文名称           |
| ------------ | ------------ | ---------------- | ------------------ |
| `\in`        | $\in$        | 属于             | Element of         |
| `\notin`     | $\notin$     | 不属于           | Not an element of  |
| `\ni`        | $\ni$        | 包含（反向属于） | Contains as member |
| `\subset`    | $\subset$    | 子集             | Subset             |
| `\supset`    | $\supset$    | 超集             | Superset           |
| `\subseteq`  | $\subseteq$  | 子集或等于       | Subset or equal    |
| `\supseteq`  | $\supseteq$  | 超集或等于       | Superset or equal  |
| `\subsetneq` | $\subsetneq$ | 真子集           | Proper subset      |
| `\supsetneq` | $\supsetneq$ | 真超集           | Proper superset    |

集合运算

| LaTeX 命令    | 渲染结果      | 说明               | 英文名称            |
| ------------- | ------------- | ------------------ | ------------------- |
| `\cup`        | $\cup$        | 并集               | Union               |
| `\cap`        | $\cap$        | 交集               | Intersection        |
| `\setminus`   | $\setminus$   | 差集               | Set minus           |
| `\emptyset`   | $\emptyset$   | 空集               | Empty set           |
| `\varnothing` | $\varnothing$ | 空集（另一种形式） | Empty set (variant) |

### 逻辑符号

逻辑运算

| LaTeX 命令        | 渲染结果          | 说明              | 英文名称       |
| ----------------- | ----------------- | ----------------- | -------------- |
| `\land`           | $\land$           | 逻辑与            | Logical AND    |
| `\lor`            | $\lor$            | 逻辑或            | Logical OR     |
| `\lnot`           | $\lnot$           | 逻辑非            | Logical NOT    |
| `\neg`            | $\neg$            | 逻辑非（同\lnot） | Logical NOT    |
| `\implies`        | $\implies$        | 蕴含              | Implies        |
| `\impliedby`      | $\impliedby$      | 被蕴含            | Implied by     |
| `\iff`            | $\iff$            | 当且仅当          | If and only if |
| `\Leftrightarrow` | $\Leftrightarrow$ | 等价              | Equivalent to  |
| `\Rightarrow`     | $\Rightarrow$     | 推出              | Right arrow    |
| `\Leftarrow`      | $\Leftarrow$      | 被推出            | Left arrow     |

量词

| LaTeX 命令 | 渲染结果   | 说明     | 英文名称             |
| ---------- | ---------- | -------- | -------------------- |
| `\forall`  | $\forall$  | 全称量词 | For all              |
| `\exists`  | $\exists$  | 存在量词 | There exists         |
| `\nexists` | $\nexists$ | 不存在   | There does not exist |

、

### 箭头符号

基本箭头

| LaTeX 命令        | 渲染结果          | 说明     | 英文名称         |
| ----------------- | ----------------- | -------- | ---------------- |
| `\leftarrow`      | $\leftarrow$      | 左箭头   | Left arrow       |
| `\rightarrow`     | $\rightarrow$     | 右箭头   | Right arrow      |
| `\uparrow`        | $\uparrow$        | 上箭头   | Up arrow         |
| `\downarrow`      | $\downarrow$      | 下箭头   | Down arrow       |
| `\leftrightarrow` | $\leftrightarrow$ | 左右箭头 | Left-right arrow |
| `\updownarrow`    | $\updownarrow$    | 上下箭头 | Up-down arrow    |

长箭头

| LaTeX 命令            | 渲染结果              | 说明       | 英文名称              |
| --------------------- | --------------------- | ---------- | --------------------- |
| `\longleftarrow`      | $\longleftarrow$      | 长左箭头   | Long left arrow       |
| `\longrightarrow`     | $\longrightarrow$     | 长右箭头   | Long right arrow      |
| `\longleftrightarrow` | $\longleftrightarrow$ | 长左右箭头 | Long left-right arrow |

双线箭头

| LaTeX 命令        | 渲染结果          | 说明         | 英文名称                |
| ----------------- | ----------------- | ------------ | ----------------------- |
| `\Leftarrow`      | $\Leftarrow$      | 双线左箭头   | Double left arrow       |
| `\Rightarrow`     | $\Rightarrow$     | 双线右箭头   | Double right arrow      |
| `\Updownarrow`    | $\Updownarrow$    | 双线上下箭头 | Double up-down arrow    |
| `\Leftrightarrow` | $\Leftrightarrow$ | 双线左右箭头 | Double left-right arrow |

映射箭头

| LaTeX 命令        | 渲染结果          | 说明       | 英文名称                   |
| ----------------- | ----------------- | ---------- | -------------------------- |
| `\mapsto`         | $\mapsto$         | 映射到     | Maps to                    |
| `\longmapsto`     | $\longmapsto$     | 长映射到   | Long maps to               |
| `\hookrightarrow` | $\hookrightarrow$ | 带钩右箭头 | Rightwards arrow with hook |
| `\hookleftarrow`  | $\hookleftarrow$  | 带钩左箭头 | Leftwards arrow with hook  |
| `\rightharpoonup` | $\rightharpoonup$ | 右半箭头   | Right harpoon              |
| `\leftharpoonup`  | $\leftharpoonup$  | 左半箭头   | Left harpoon               |

## 希腊字母表

### 小写希腊字母

| LaTeX 命令    | 渲染结果      | 说明               | 英文名称        |
| ------------- | ------------- | ------------------ | --------------- |
| `\alpha`      | $\alpha$      | 阿尔法             | alpha           |
| `\beta`       | $\beta$       | 贝塔               | beta            |
| `\gamma`      | $\gamma$      | 伽马               | gamma           |
| `\delta`      | $\delta$      | 德尔塔             | delta           |
| `\epsilon`    | $\epsilon$    | 艾普西隆           | epsilon         |
| `\varepsilon` | $\varepsilon$ | 艾普西隆（变体）   | epsilon variant |
| `\zeta`       | $\zeta$       | 泽塔               | zeta            |
| `\eta`        | $\eta$        | 伊塔               | eta             |
| `\theta`      | $\theta$      | 西塔               | theta           |
| `\vartheta`   | $\vartheta$   | 西塔（变体）       | theta variant   |
| `\iota`       | $\iota$       | 约塔               | iota            |
| `\kappa`      | $\kappa$      | 卡帕               | kappa           |
| `\lambda`     | $\lambda$     | 拉姆达             | lambda          |
| `\mu`         | $\mu$         | 缪                 | mu              |
| `\nu`         | $\nu$         | 纽                 | nu              |
| `\xi`         | $\xi$         | 克西               | xi              |
| `\pi`         | $\pi$         | 派                 | pi              |
| `\varpi`      | $\varpi$      | 派（变体）         | pi variant      |
| `\rho`        | $\rho$        | 柔                 | rho             |
| `\varrho`     | $\varrho$     | 柔（变体）         | rho variant     |
| `\sigma`      | $\sigma$      | 西格玛             | sigma           |
| `\varsigma`   | $\varsigma$   | 西格玛（词尾形式） | sigma final     |
| `\tau`        | $\tau$        | 陶                 | tau             |
| `\upsilon`    | $\upsilon$    | 宇普西隆           | upsilon         |
| `\phi`        | $\phi$        | 斐                 | phi             |
| `\varphi`     | $\varphi$     | 斐（变体）         | phi variant     |
| `\chi`        | $\chi$        | 希                 | chi             |
| `\psi`        | $\psi$        | 普西               | psi             |
| `\omega`      | $\omega$      | 欧米伽             | omega           |



### 大写希腊字母

| LaTeX 命令 | 渲染结果   | 说明         | 英文名称 |
| ---------- | ---------- | ------------ | -------- |
| `\Gamma`   | $\Gamma$   | 大写伽马     | Gamma    |
| `\Delta`   | $\Delta$   | 大写德尔塔   | Delta    |
| `\Theta`   | $\Theta$   | 大写西塔     | Theta    |
| `\Lambda`  | $\Lambda$  | 大写拉姆达   | Lambda   |
| `\Xi`      | $\Xi$      | 大写克西     | Xi       |
| `\Pi`      | $\Pi$      | 大写派       | Pi       |
| `\Sigma`   | $\Sigma$   | 大写西格玛   | Sigma    |
| `\Upsilon` | $\Upsilon$ | 大写宇普西隆 | Upsilon  |
| `\Phi`     | $\Phi$     | 大写斐       | Phi      |
| `\Psi`     | $\Psi$     | 大写普西     | Psi      |
| `\Omega`   | $\Omega$   | 大写欧米伽   | Omega    |



## 上标与下标

### 基本用法

上标


| LaTeX 命令 | 渲染结果   | 说明           | 示例       |
| ---------- | ---------- | -------------- | ---------- |
| `x^2`      | $x^2$      | 上标           | $x^2$      |
| `x^{10}`   | $x^{10}$   | 多位数字上标   | $x^{10}$   |
| `x^{2n+1}` | $x^{2n+1}$ | 复杂表达式上标 | $x^{2n+1}$ |

下标

| LaTeX 命令 | 渲染结果  | 说明         | 示例      |
| ---------- | --------- | ------------ | --------- |
| `x_1`      | $x_1$     | 下标         | $x_1$     |
| `x_{10}`   | $x_{10}$  | 多位数字下标 | $x_{10}$  |
| `x_{i,j}`  | $x_{i,j}$ | 多字符下标   | $x_{i,j}$ |

上下标同时使用

| LaTeX 命令    | 渲染结果      | 说明                 | 示例          |
| ------------- | ------------- | -------------------- | ------------- |
| `x_1^2`       | $x_1^2$       | 同时上下标（推荐）   | $x_1^2$       |
| `x^2_1`       | $x^2_1$       | 同时上下标（先上标） | $x^2_1$       |
| `x_{i}^{(n)}` | $x_{i}^{(n)}$ | 复杂上下标组合       | $x_{i}^{(n)}$ |

### 复杂上下标

多重上下标

| LaTeX 命令                  | 渲染结果                    | 说明                 | 示例                        |
| --------------------------- | --------------------------- | -------------------- | --------------------------- |
| `x^{x^x}`                   | $x^{x^x}$                   | 多重上标             | $x^{x^x}$                   |
| `x_{y_z}`                   | $x_{y_z}$                   | 多重下标             | $x_{y_z}$                   |



左右上下标
| LaTeX 命令                  | 渲染结果                    | 说明                 | 示例                        |
| --------------------------- | --------------------------- | -------------------- | --------------------------- |
| `\prescript{14}{2}C`        | $\prescript{14}{2}C$        | 前置上下标           | $\prescript{14}{2}C$        |
| `{}^{14}C_2`                | ${}^{14}C_2$                | 前置上标和后置下标   | ${}^{14}C_2$                |

上下标对齐
| LaTeX 命令                  | 渲染结果                    | 说明                 | 示例                        |
| --------------------------- | --------------------------- | -------------------- | --------------------------- |
| `\sideset{_1^2}{_3^4}\prod` | $\sideset{_1^2}{_3^4}\prod$ | 带多组上下标的连乘号 | $\sideset{_1^2}{_3^4}\prod$ |



## 分数与根式

### 分数

基本分数

| LaTeX 命令                | 渲染结果                  | 说明                   | 示例                      |
| ------------------------- | ------------------------- | ---------------------- | ------------------------- |
| `\frac{1}{2}`             | $\frac{1}{2}$             | 基本分数               | $\frac{1}{2}$             |
| `\frac{a+b}{c+d}`         | $\frac{a+b}{c+d}$         | 复杂分子分母           | $\frac{a+b}{c+d}$         |




嵌套分数

| LaTeX 命令                | 渲染结果                  | 说明                   | 示例                      |
| ------------------------- | ------------------------- | ---------------------- | ------------------------- |
| `\frac{1}{1+\frac{1}{2}}` | $\frac{1}{1+\frac{1}{2}}$ | 嵌套分数（连分数）     | $\frac{1}{1+\frac{1}{2}}$ |

行内分数（较小）

| LaTeX 命令                | 渲染结果                  | 说明                   | 示例                      |
| ------------------------- | ------------------------- | ---------------------- | ------------------------- |
| `\tfrac{1}{2}`            | $\tfrac{1}{2}$            | 行内小分数（文本样式） | $\tfrac{1}{2}$            |
| `\dfrac{1}{2}`            | $\dfrac{1}{2}$            | 显示样式大分数         | $\dfrac{1}{2}$            |


斜分数

| LaTeX 命令                | 渲染结果                  | 说明                   | 示例                      |
| ------------------------- | ------------------------- | ---------------------- | ------------------------- |
| `\nicefrac{1}{2}`         | $\nicefrac{1}{2}$         | 斜分数（需nicefrac包） | $\nicefrac{1}{2}$         |

二项式系数

| LaTeX 命令                | 渲染结果                  | 说明                   | 示例                      |
| ------------------------- | ------------------------- | ---------------------- | ------------------------- |
| `\binom{n}{k}`            | $\binom{n}{k}$            | 二项式系数             | $\binom{n}{k}$            |
| `\dbinom{n}{k}`           | $\dbinom{n}{k}$           | 显示样式二项式系数     | $\dbinom{n}{k}$           |
| `\tbinom{n}{k}`           | $\tbinom{n}{k}$           | 文本样式二项式系数     | $\tbinom{n}{k}$           |



### 根式

平方根

| LaTeX 命令          | 渲染结果            | 说明                 | 示例                |
| ------------------- | ------------------- | -------------------- | ------------------- |
| `\sqrt{2}`          | $\sqrt{2}$          | 平方根               | $\sqrt{2}$          |
| `\sqrt{x+y}`        | $\sqrt{x+y}$        | 平方根（复杂表达式） | $\sqrt{x+y}$        |



n次根

| LaTeX 命令          | 渲染结果            | 说明                 | 示例                |
| ------------------- | ------------------- | -------------------- | ------------------- |
| `\sqrt[3]{8}`       | $\sqrt[3]{8}$       | 三次根号             | $\sqrt[3]{8}$       |
| `\sqrt[n]{x}`       | $\sqrt[n]{x}$       | n次根号              | $\sqrt[n]{x}$       |

嵌套根式

| LaTeX 命令          | 渲染结果            | 说明                 | 示例                |
| ------------------- | ------------------- | -------------------- | ------------------- |
| `\sqrt{1+\sqrt{2}}` | $\sqrt{1+\sqrt{2}}$ | 嵌套根式             | $\sqrt{1+\sqrt{2}}$ |



## 求和、积分和极限

### 求和符号

基本求和

| LaTeX 命令              | 渲染结果                | 说明               | 示例                    |
| ----------------------- | ----------------------- | ------------------ | ----------------------- |
| `\sum`                  | $\sum$                  | 求和符号           | $\sum$                  |
| `\sum_{i=1}^{n}`        | $\sum_{i=1}^{n}$        | 带上下限的求和     | $\sum_{i=1}^{n}$        |
| `\sum_{i=1}^{n} i`      | $\sum_{i=1}^{n} i$      | 求和的表达式       | $\sum_{i=1}^{n} i$      |
| `\sum\limits_{i=1}^{n}` | $\sum\limits_{i=1}^{n}$ | 强制上下限在上下方 | $\sum\limits_{i=1}^{n}$ |


其他求和类符号

| LaTeX 命令              | 渲染结果                | 说明               | 示例                    |
| ----------------------- | ----------------------- | ------------------ | ----------------------- |
| `\prod`                 | $\prod$                 | 乘积符号           | $\prod$                 |
| `\coprod`               | $\coprod$               | 副积符号           | $\coprod$               |
| `\bigcup`               | $\bigcup$               | 并集符号           | $\bigcup$               |
| `\bigcap`               | $\bigcap$               | 交集符号           | $\bigcap$               |
| `\bigoplus`             | $\bigoplus$             | 直和符号           | $\bigoplus$             |
| `\bigotimes`            | $\bigotimes$            | 直积符号           | $\bigotimes$            |
| `\bigwedge`             | $\bigwedge$             | 合取符号           | $\bigwedge$             |
| `\bigvee`               | $\bigvee$               | 析取符号           | $\bigvee$               |



### 积分符号

#### 基本积分
| LaTeX 命令 | 渲染结果 | 说明 | 英文名称 |
|------------|----------|------|----------|
| `\int` | $\int$ | 积分符号 | Integral |
| `\int_0^1` | $\int_0^1$ | 定积分（0到1） | Definite integral from 0 to 1 |
| `\int_{-\infty}^{\infty}` | $\int_{-\infty}^{\infty}$ | 无穷积分 | Integral from negative to positive infinity |
| `\int\limits_0^1` | $\int\limits_0^1$ | 强制上下限在上下方 | Integral with limits below and above |

#### 多重积分
| LaTeX 命令 | 渲染结果 | 说明 | 英文名称 |
|------------|----------|------|----------|
| `\iint` | $\iint$ | 二重积分 | Double integral |
| `\iiint` | $\iiint$ | 三重积分 | Triple integral |
| `\iiiint` | $\iiiint$ | 四重积分 | Quadruple integral |
| `\idotsint` | $\idotsint$ | 多重积分（n重） | Multiple integral |

#### 围道积分
| LaTeX 命令 | 渲染结果 | 说明 | 英文名称 |
|------------|----------|------|----------|
| `\oint` | $\oint$ | 围道积分 | Contour integral |
| `\oiint` | $\oiint$ | 面积分 | Surface integral |
| `\oiiint` | $\oiiint$ | 体积分 | Volume integral |

#### 积分变量间距
| LaTeX 命令 | 渲染结果 | 说明 | 英文名称 |
|------------|----------|------|----------|
| `\int x \, dx` | $\int x \, dx$ | 正常间距 | Integral with normal spacing |
| `\int x \: dx` | $\int x \: dx$ | 中等间距 | Integral with medium spacing |
| `\int x \; dx` | $\int x \; dx$ | 较大间距 | Integral with large spacing |
| `\int x \! dx` | $\int x \! dx$ | 紧密间距 | Integral with tight spacing |


### 极限

#### 基本极限
| LaTeX 命令             | 渲染结果               | 说明                | 英文名称                                |
| ---------------------- | ---------------------- | ------------------- | --------------------------------------- |
| `\lim`                 | $\lim$                 | 极限符号            | Limit                                   |
| `\lim_{x \to 0}`       | $\lim_{x \to 0}$       | x趋近于0的极限      | Limit as x approaches 0                 |
| `\lim_{x \to +\infty}` | $\lim_{x \to +\infty}$ | x趋近于正无穷的极限 | Limit as x approaches positive infinity |
| `\lim_{n \to \infty}`  | $\lim_{n \to \infty}$  | n趋近于无穷的极限   | Limit as n approaches infinity          |

#### 上下极限
| LaTeX 命令   | 渲染结果     | 说明       | 英文名称               |
| ------------ | ------------ | ---------- | ---------------------- |
| `\limsup`    | $\limsup$    | 上极限     | Limit superior         |
| `\liminf`    | $\liminf$    | 下极限     | Limit inferior         |
| `\varlimsup` | $\varlimsup$ | 变体上极限 | Variant limit superior |
| `\varliminf` | $\varliminf$ | 变体下极限 | Variant limit inferior |

#### 强制位置
| LaTeX 命令                | 渲染结果                  | 说明           | 英文名称                          |
| ------------------------- | ------------------------- | -------------- | --------------------------------- |
| `\lim\limits_{x \to 0}`   | $\lim\limits_{x \to 0}$   | 强制下标在下方 | Limit with subscript below        |
| `\lim\nolimits_{x \to 0}` | $\lim\nolimits_{x \to 0}$ | 强制下标在右侧 | Limit with subscript to the right |

## 函数和运算符

### 标准函数

#### 三角函数
| LaTeX 命令 | 渲染结果 | 说明 | 英文名称  |
| ---------- | -------- | ---- | --------- |
| `\sin`     | $\sin$   | 正弦 | Sine      |
| `\cos`     | $\cos$   | 余弦 | Cosine    |
| `\tan`     | $\tan$   | 正切 | Tangent   |
| `\cot`     | $\cot$   | 余切 | Cotangent |
| `\sec`     | $\sec$   | 正割 | Secant    |
| `\csc`     | $\csc$   | 余割 | Cosecant  |

#### 反三角函数
| LaTeX 命令 | 渲染结果  | 说明   | 英文名称     |
| ---------- | --------- | ------ | ------------ |
| `\arcsin`  | $\arcsin$ | 反正弦 | Arcsine      |
| `\arccos`  | $\arccos$ | 反余弦 | Arccosine    |
| `\arctan`  | $\arctan$ | 反正切 | Arctangent   |
| `\arccot`  | $\arccot$ | 反余切 | Arccotangent |
| `\arcsec`  | $\arcsec$ | 反正割 | Arcsecant    |
| `\arccsc`  | $\arccsc$ | 反余割 | Arccosecant  |

#### 双曲函数
| LaTeX 命令 | 渲染结果 | 说明     | 英文名称             |
| ---------- | -------- | -------- | -------------------- |
| `\sinh`    | $\sinh$  | 双曲正弦 | Hyperbolic sine      |
| `\cosh`    | $\cosh$  | 双曲余弦 | Hyperbolic cosine    |
| `\tanh`    | $\tanh$  | 双曲正切 | Hyperbolic tangent   |
| `\coth`    | $\coth$  | 双曲余切 | Hyperbolic cotangent |

#### 对数函数
| LaTeX 命令 | 渲染结果 | 说明                       | 英文名称          |
| ---------- | -------- | -------------------------- | ----------------- |
| `\log`     | $\log$   | 对数（以10为底或自然对数） | Logarithm         |
| `\ln`      | $\ln$    | 自然对数                   | Natural logarithm |
| `\lg`      | $\lg$    | 以2为底的对数              | Binary logarithm  |
| `\log_2`   | $\log_2$ | 以2为底的对数（带下标）    | Logarithm base 2  |

#### 其他函数
| LaTeX 命令 | 渲染结果 | 说明       | 英文名称                |
| ---------- | -------- | ---------- | ----------------------- |
| `\exp`     | $\exp$   | 指数函数   | Exponential             |
| `\max`     | $\max$   | 最大值     | Maximum                 |
| `\min`     | $\min$   | 最小值     | Minimum                 |
| `\sup`     | $\sup$   | 上确界     | Supremum                |
| `\inf`     | $\inf$   | 下确界     | Infimum                 |
| `\arg`     | $\arg$   | 辐角       | Argument                |
| `\ker`     | $\ker$   | 核         | Kernel                  |
| `\dim`     | $\dim$   | 维数       | Dimension               |
| `\hom`     | $\hom$   | 同态       | Homomorphism            |
| `\det`     | $\det$   | 行列式     | Determinant             |
| `\gcd`     | $\gcd$   | 最大公约数 | Greatest common divisor |
| `\deg`     | $\deg$   | 次数       | Degree                  |

### 自定义运算符

#### 定义新的运算符
| LaTeX 命令                                 | 渲染结果 | 说明                     | 英文名称                           |
| ------------------------------------------ | -------- | ------------------------ | ---------------------------------- |
| `\DeclareMathOperator{\Tr}{Tr}`            | -        | 定义迹运算符             | Define trace operator              |
| `\DeclareMathOperator*{\argmax}{arg\,max}` | -        | 定义带极限的argmax运算符 | Define argmax operator with limits |
| `\DeclareMathOperator{\rank}{rank}`        | -        | 定义秩运算符             | Define rank operator               |

#### 使用运算符
| LaTeX 命令         | 渲染结果           | 说明          | 英文名称                     |
| ------------------ | ------------------ | ------------- | ---------------------------- |
| `\Tr(A)`           | $\Tr(A)$           | 矩阵A的迹     | Trace of matrix A            |
| `\argmax_{x} f(x)` | $\argmax_{x} f(x)$ | 使f(x)最大的x | Argument that maximizes f(x) |
| `\rank(M)`         | $\rank(M)$         | 矩阵M的秩     | Rank of matrix M             |

#### 临时运算符
| LaTeX 命令            | 渲染结果              | 说明     | 英文名称      |
| --------------------- | --------------------- | -------- | ------------- |
| `\operatorname{sinc}` | $\operatorname{sinc}$ | sinc函数 | Sinc function |

## 矩阵和行列式

### 基本矩阵环境

| LaTeX 命令                                     | 渲染结果                                       | 说明                 | 英文名称                          |
| ---------------------------------------------- | ---------------------------------------------- | -------------------- | --------------------------------- |
| `\begin{matrix} a & b \\ c & d \end{matrix}`   | $\begin{matrix} a & b \\ c & d \end{matrix}$   | 无括号矩阵           | Plain matrix                      |
| `\begin{pmatrix} a & b \\ c & d \end{pmatrix}` | $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ | 圆括号矩阵           | Matrix in parentheses             |
| `\begin{bmatrix} a & b \\ c & d \end{bmatrix}` | $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ | 方括号矩阵           | Matrix in brackets                |
| `\begin{Bmatrix} a & b \\ c & d \end{Bmatrix}` | $\begin{Bmatrix} a & b \\ c & d \end{Bmatrix}$ | 花括号矩阵           | Matrix in braces                  |
| `\begin{vmatrix} a & b \\ c & d \end{vmatrix}` | $\begin{vmatrix} a & b \\ c & d \end{vmatrix}$ | 行列式格式（单竖线） | Determinant format (single lines) |
| `\begin{Vmatrix} a & b \\ c & d \end{Vmatrix}` | $\begin{Vmatrix} a & b \\ c & d \end{Vmatrix}$ | 范数格式（双竖线）   | Norm format (double lines)        |

### 复杂矩阵结构

| LaTeX 命令                                                   | 渲染结果                                                     | 说明                 | 英文名称                               |
| ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------- | -------------------------------------- |
| `\begin{pmatrix} A & B \\ C & D \end{pmatrix}`               | $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$               | 分块矩阵             | Block matrix                           |
| `\begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}` | $\begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}$ | 带省略号的大型矩阵   | Large matrix with ellipsis             |
| `\left(\begin{array}{cc|c} a & b & x \\ c & d & y \end{array}\right)` | $\left(\begin{array}{cc|c} a & b & x \\ c & d & y \end{array}\right)$ | 增广矩阵（带分隔线） | Augmented matrix (with separator line) |
| `\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}`       | $\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}$       | 小型矩阵（行内使用） | Small matrix (for inline use)          |

### 向量表示

| LaTeX 命令                                                  | 渲染结果                                                    | 说明                     | 英文名称                              |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ------------------------ | ------------------------------------- |
| `\begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}` | $\begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}$ | 列向量                   | Column vector                         |
| `\begin{pmatrix} x_1 & x_2 & \cdots & x_n \end{pmatrix}`    | $\begin{pmatrix} x_1 & x_2 & \cdots & x_n \end{pmatrix}$    | 行向量                   | Row vector                            |
| `\vec{v}`                                                   | $\vec{v}$                                                   | 带箭头的向量             | Vector with arrow                     |
| `\mathbf{v}`                                                | $\mathbf{v}$                                                | 粗体向量                 | Bold vector                           |
| `\boldsymbol{v}`                                            | $\boldsymbol{v}$                                            | 粗体符号（包含希腊字母） | Bold symbol (including Greek letters) |
| `\overrightarrow{AB}`                                       | $\overrightarrow{AB}$                                       | 从A到B的向量             | Vector from A to B                    |

## 多行公式

### align 环境

| LaTeX 命令                                                   | 渲染结果                                                     | 说明             | 英文名称                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------- | ----------------------------------- |
| `\begin{align} x &= a + b \\ &= c + d \\ &= e + f \end{align}` | $\begin{align} x &= a + b \\ &= c + d \\ &= e + f \end{align}$ | 带编号的对齐公式 | Aligned equations with numbering    |
| `\begin{align} x &= a + b & y &= p + q \\ &= c + d & &= r + s \end{align}` | $\begin{align} x &= a + b & y &= p + q \\ &= c + d & &= r + s \end{align}$ | 多列对齐公式     | Multi-column aligned equations      |
| `\begin{align*} x &= a + b \\ &= c + d \end{align*}`         | $\begin{align*} x &= a + b \\ &= c + d \end{align*}$         | 无编号的对齐公式 | Aligned equations without numbering |

### 其他多行环境

| LaTeX 命令                                                   | 渲染结果                                                     | 说明                                 | 英文名称                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------ | -------------------------------------------------------- |
| `\begin{gather} x = a + b \\ y = c + d \end{gather}`         | $\begin{gather} x = a + b \\ y = c + d \end{gather}$         | 居中对齐（无对齐点）                 | Gather environment (centered, no alignment)              |
| `\begin{multline} x = a + b + c + d + e \\ + f + g + h + i + j \\ + k + l + m \end{multline}` | $\begin{multline} x = a + b + c + d + e \\ + f + g + h + i + j \\ + k + l + m \end{multline}$ | 多行长公式（首行左对齐，末行右对齐） | Multiline environment (first line left, last line right) |
| `\begin{equation} \begin{split} x &= a + b \\ &\quad + c + d \end{split} \end{equation}` | $\begin{equation} \begin{split} x &= a + b \\ &\quad + c + d \end{split} \end{equation}$ | 拆分环境（在其他环境内使用）         | Split environment (inside other environments)            |
| `\begin{alignat}{2} x &= a & \quad y &= p \\ &= b & z &= q \end{alignat}` | $\begin{alignat}{2} x &= a & \quad y &= p \\ &= b & z &= q \end{alignat}$ | 精确对齐（指定列数）                 | Alignat environment (specified column alignment)         |

### 分类和条件表达式

| LaTeX 命令                                                   | 渲染结果                                                     | 说明                         | 英文名称                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------- | ---------------------------------------- |
| `f(x) = \begin{cases} x^2 & \text{if } x \geq 0 \\ -x^2 & \text{if } x < 0 \end{cases}` | $f(x) = \begin{cases} x^2 & \text{if } x \geq 0 \\ -x^2 & \text{if } x < 0 \end{cases}$ | 分段函数                     | Piecewise function                       |
| `\begin{cases} x + y = 2 \\ x - y = 0 \\ z = 1 \end{cases}`  | $\begin{cases} x + y = 2 \\ x - y = 0 \\ z = 1 \end{cases}$  | 方程组（带大括号）           | System of equations with brace           |
| `\left\{ \begin{aligned} x + y &= 2 \\ x - y &= 0 \end{aligned} \right.` | $\left\{ \begin{aligned} x + y &= 2 \\ x - y &= 0 \end{aligned} \right.$ | 对齐的分组公式（手动大括号） | Aligned grouped equations (manual brace) |

## 空格和对齐

### 数学模式中的空格

| LaTeX 命令     | 渲染结果       | 说明               | 英文名称                           |
| -------------- | -------------- | ------------------ | ---------------------------------- |
| `a\!b`         | $a\!b$         | 负间距（紧密）     | Negative space (tight)             |
| `ab`           | $ab$           | 无间距             | No space                           |
| `a\,b`         | $a\,b$         | 小间距（3/18 em）  | Thin space                         |
| `a\:b`         | $a\:b$         | 中间距（4/18 em）  | Medium space                       |
| `a\;b`         | $a\;b$         | 大间距（5/18 em）  | Thick space                        |
| `a\ b`         | $a\ b$         | 单词间距           | Word space                         |
| `a\quad b`     | $a\quad b$     | 1 em 间距          | 1 em space                         |
| `a\qquad b`    | $a\qquad b$    | 2 em 间距          | 2 em space                         |
| `\int x \, dx` | $\int x \, dx$ | 积分变量前的小间距 | Integral with thin space before dx |
| `\sin x`       | $\sin x$       | 函数名后的自然间距 | Sine function with natural spacing |

### 文本对齐和间距

| LaTeX 命令                                | 渲染结果                                  | 说明                        | 英文名称                                |
| ----------------------------------------- | ----------------------------------------- | --------------------------- | --------------------------------------- |
| `\text{这是文本}`                         | $\text{这是文本}$                         | 数学环境中的文本            | Text in math mode                       |
| `\mbox{文本框}`                           | $\mbox{文本框}$                           | 文本框                      | Text box                                |
| `x = 2 \quad \text{当且仅当} \quad y = 4` | $x = 2 \quad \text{当且仅当} \quad y = 4$ | 带间距的文本分隔            | Text with spacing separators            |
| `\phantom{x}`                             | $\phantom{x}$                             | 幻影（占据x的空间但不显示） | Phantom (takes x's space but invisible) |
| `\hphantom{x}`                            | $\hphantom{x}$                            | 水平幻影                    | Horizontal phantom                      |
| `\vphantom{x}`                            | $\vphantom{x}$                            | 垂直幻影                    | Vertical phantom                        |

## 特殊符号和重音

### 数学重音符号

| LaTeX 命令                       | 渲染结果                         | 说明         | 英文名称                    |
| -------------------------------- | -------------------------------- | ------------ | --------------------------- |
| `\hat{a}`                        | $\hat{a}$                        | 帽子重音     | Hat accent                  |
| `\check{a}`                      | $\check{a}$                      | 检查符号重音 | Check accent                |
| `\breve{a}`                      | $\breve{a}$                      | 短音符重音   | Breve accent                |
| `\acute{a}`                      | $\acute{a}$                      | 锐音符重音   | Acute accent                |
| `\grave{a}`                      | $\grave{a}$                      | 重音符重音   | Grave accent                |
| `\tilde{a}`                      | $\tilde{a}$                      | 波浪线重音   | Tilde accent                |
| `\bar{a}`                        | $\bar{a}$                        | 长音符重音   | Bar accent                  |
| `\vec{a}`                        | $\vec{a}$                        | 向量箭头     | Vector arrow                |
| `\dot{a}`                        | $\dot{a}$                        | 单点重音     | Single dot accent           |
| `\ddot{a}`                       | $\ddot{a}$                       | 双点重音     | Double dot accent           |
| `\widehat{abc}`                  | $\widehat{abc}$                  | 宽帽子重音   | Wide hat accent             |
| `\widetilde{abc}`                | $\widetilde{abc}$                | 宽波浪线重音 | Wide tilde accent           |
| `\overline{abc}`                 | $\overline{abc}$                 | 上划线       | Overline                    |
| `\underline{abc}`                | $\underline{abc}$                | 下划线       | Underline                   |
| `\overbrace{abc}^{\text{说明}}`  | $\overbrace{abc}^{\text{说明}}$  | 上括号带说明 | Overbrace with description  |
| `\underbrace{abc}_{\text{说明}}` | $\underbrace{abc}_{\text{说明}}$ | 下括号带说明 | Underbrace with description |

### 特殊数学符号

| LaTeX 命令        | 渲染结果          | 说明                     | 英文名称                  |
| ----------------- | ----------------- | ------------------------ | ------------------------- |
| `\infty`          | $\infty$          | 无穷大                   | Infinity                  |
| `\partial`        | $\partial$        | 偏导数符号               | Partial derivative        |
| `\nabla`          | $\nabla$          | 梯度算子                 | Nabla (gradient operator) |
| `\angle`          | $\angle$          | 角度符号                 | Angle                     |
| `\measuredangle`  | $\measuredangle$  | 测量角度                 | Measured angle            |
| `\sphericalangle` | $\sphericalangle$ | 球面角度                 | Spherical angle           |
| `30^\circ`        | $30^\circ$        | 30度                     | 30 degrees                |
| `\degree`         | $\degree$         | 度符号（需特定包）       | Degree symbol             |
| `\mathbb{N}`      | $\mathbb{N}$      | 自然数集                 | Natural numbers set       |
| `\mathbb{Z}`      | $\mathbb{Z}$      | 整数集                   | Integers set              |
| `\mathbb{Q}`      | $\mathbb{Q}$      | 有理数集                 | Rational numbers set      |
| `\mathbb{R}`      | $\mathbb{R}$      | 实数集                   | Real numbers set          |
| `\mathbb{C}`      | $\mathbb{C}$      | 复数集                   | Complex numbers set       |
| `\mathcal{A}`     | $\mathcal{A}$     | 手写体A                  | Script A                  |
| `\mathscr{B}`     | $\mathscr{B}$     | 花体B（需mathrsfs包）    | Cursive B                 |
| `\mathfrak{C}`    | $\mathfrak{C}$    | 德文花体C（需amssymb包） | Fraktur C                 |

## 大型运算符的定制

### 自定义大型运算符

| LaTeX 命令                              | 渲染结果                                | 说明                   | 英文名称                                    |
| --------------------------------------- | --------------------------------------- | ---------------------- | ------------------------------------------- |
| `\mathop{\text{lcm}}_{i=1}^n a_i`       | $\mathop{\text{lcm}}_{i=1}^n a_i$       | 自定义最小公倍数运算符 | Custom lcm operator                         |
| `\operatorname*{argmax}_{x \in S} f(x)` | $\operatorname*{argmax}_{x \in S} f(x)$ | argmax运算符（带极限） | Argmax operator with limits                 |
| `\upint_0^1 f(x) dx`                    | $\upint_0^1 f(x) dx$                    | 上积分（需自定义定义） | Upper integral (requires custom definition) |
| `\lowint_0^1 f(x) dx`                   | $\lowint_0^1 f(x) dx$                   | 下积分（需自定义定义） | Lower integral (requires custom definition) |

## 数组和表格

### 基本数组

| LaTeX 命令                                                   | 渲染结果                                                     | 说明                           | 英文名称                                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------ | ------------------------------------------------------- |
| `\begin{array}{ccc} a & b & c \\ d & e & f \end{array}`      | $\begin{array}{ccc} a & b & c \\ d & e & f \end{array}$      | 简单三列数组                   | Simple 3-column array                                   |
| `\begin{array}{|c|c|c|} \hline a & b & c \\ \hline d & e & f \\ \hline \end{array}` | $\begin{array}{|c|c|c|} \hline a & b & c \\ \hline d & e & f \\ \hline \end{array}$ | 带分隔线的数组                 | Array with divider lines                                |
| `\begin{array}{lcr} 左对齐 & 居中 & 右对齐 \\ A & B & C \end{array}` | $\begin{array}{lcr} 左对齐 & 居中 & 右对齐 \\ A & B & C \end{array}$ | 不同对齐方式的列（左、中、右） | Columns with different alignments (left, center, right) |

### 数学表格的高级用法

| LaTeX 命令                                                   | 渲染结果                                                     | 说明                       | 英文名称                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------- | -------------------------------------------------------- |
| `\begin{array}{|c||c|c|c|c|} \hline \theta & 0 & \frac{\pi}{6} & \frac{\pi}{4} & \frac{\pi}{3} \\ \hline\hline \sin\theta & 0 & \frac{1}{2} & \frac{\sqrt{2}}{2} & \frac{\sqrt{3}}{2} \\ \hline \cos\theta & 1 & \frac{\sqrt{3}}{2} & \frac{\sqrt{2}}{2} & \frac{1}{2} \\ \hline \end{array}` | $\begin{array}{|c||c|c|c|c|} \hline \theta & 0 & \frac{\pi}{6} & \frac{\pi}{4} & \frac{\pi}{3} \\ \hline\hline \sin\theta & 0 & \frac{1}{2} & \frac{\sqrt{2}}{2} & \frac{\sqrt{3}}{2} \\ \hline \cos\theta & 1 & \frac{\sqrt{3}}{2} & \frac{\sqrt{2}}{2} & \frac{1}{2} \\ \hline \end{array}$ | 三角函数值表（带双分隔线） | Trigonometric values table (with double separator lines) |

## 定理环境（数学写作）

### 基本定理环境

| LaTeX 命令                                                   | 渲染结果                                                | 说明                           | 英文名称                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------- | ------------------------------ | -------------------------------------------------------- |
| `\usepackage{amsthm}`                                        | -                                                       | 引入amsthm包                   | Include amsthm package                                   |
| `\newtheorem{theorem}{定理}[section]`                        | -                                                       | 定义定理环境（按章节编号）     | Define theorem environment (numbered by section)         |
| `\newtheorem{lemma}[theorem]{引理}`                          | -                                                       | 定义引理环境（与定理共享编号） | Define lemma environment (shares numbering with theorem) |
| `\newtheorem{proposition}[theorem]{命题}`                    | -                                                       | 定义命题环境                   | Define proposition environment                           |
| `\newtheorem{corollary}[theorem]{推论}`                      | -                                                       | 定义推论环境                   | Define corollary environment                             |
| `\theoremstyle{definition}`                                  | -                                                       | 切换到定义样式                 | Switch to definition style                               |
| `\newtheorem{definition}[theorem]{定义}`                     | -                                                       | 定义定义环境                   | Define definition environment                            |
| `\newtheorem{example}[theorem]{例子}`                        | -                                                       | 定义例子环境                   | Define example environment                               |
| `\theoremstyle{remark}`                                      | -                                                       | 切换到注记样式                 | Switch to remark style                                   |
| `\newtheorem{remark}[theorem]{注}`                           | -                                                       | 定义注记环境                   | Define remark environment                                |
| `\newtheorem*{note}{注意}`                                   | -                                                       | 定义无编号的注意环境           | Define unnumbered note environment                       |
| `\begin{theorem}[勾股定理] \label{thm:pythagoras} 在直角三角形中，$a^2 + b^2 = c^2$。 \end{theorem}` | **定理** (勾股定理) 在直角三角形中，$a^2 + b^2 = c^2$。 | 定理环境使用                   | Theorem environment usage                                |
| `\begin{proof} 证明内容... \end{proof}`                      | **证明** 证明内容... □                                  | 证明环境                       | Proof environment                                        |

## 编号和引用

### 公式编号控制

| LaTeX 命令                                                   | 渲染结果                                                     | 说明             | 英文名称                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------- | ------------------------------------------- |
| `\begin{equation} E = mc^2 \end{equation}`                   | $\begin{equation} E = mc^2 \end{equation}$                   | 自动编号公式     | Auto-numbered equation                      |
| `\begin{equation} E = mc^2 \tag{Einstein} \end{equation}`    | $\begin{equation} E = mc^2 \tag{Einstein} \end{equation}$    | 手动设置公式标签 | Equation with custom tag                    |
| `\begin{subequations} \begin{align} a &= b + c \\ d &= e + f \end{align} \end{subequations}` | $\begin{subequations} \begin{align} a &= b + c \\ d &= e + f \end{align} \end{subequations}$ | 子编号公式组     | Subequations group                          |
| `\begin{align} x &= a + b \\ y &= c + d \nonumber \\ z &= e + f \end{align}` | $\begin{align} x &= a + b \\ y &= c + d \nonumber \\ z &= e + f \end{align}$ | 部分公式不编号   | Partial equation numbering (with \nonumber) |

### 交叉引用

| LaTeX 命令                                                   | 渲染结果                                                     | 说明                   | 英文名称                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------- | --------------------------------------- |
| `\begin{equation} E = mc^2 \label{eq:einstein} \end{equation}` | $\begin{equation} E = mc^2 \label{eq:einstein} \end{equation}$ | 标记公式（添加标签）   | Label equation                          |
| `如方程~\eqref{eq:einstein}~所示...`                         | 如方程 (1) 所示...                                           | 引用公式（带括号）     | Reference equation (with parentheses)   |
| `根据公式~(\ref{eq:einstein})...`                            | 根据公式 (1)...                                              | 引用公式（手动加括号） | Reference equation (manual parentheses) |
| `方程~\eqref{eq:first,eq:second,eq:third}~表明...`           | 方程 (1,2,3) 表明...                                         | 多个公式引用           | Multiple equation references            |

## 物理和化学符号

### 物理单位（需要 siunitx 包）

KaTex 需要使用 `\pu{}` 包裹，例如`$\pu{3e8 m s^{-1}}$`，$\pu{3e8 m s^{-1}}$

| LaTeX 命令                    | 渲染结果                      | 说明                 | 英文名称                       |
| ----------------------------- | ----------------------------- | -------------------- | ------------------------------ |
| `\usepackage{siunitx}`        | -                             | 引入siunitx包        | Include siunitx package        |
| `\SI{3e8}{\meter\per\second}` | $\SI{3e8}{\meter\per\second}$ | 科学计数法与单位组合 | Scientific notation with units |
| `\SI{1.602e-19}{\coulomb}`    | $\SI{1.602e-19}{\coulomb}$    | 电荷量单位           | Electric charge unit           |
| `\SI{273.15}{\kelvin}`        | $\SI{273.15}{\kelvin}$        | 温度单位             | Temperature unit               |
| `\num{6.022e23}`              | $\num{6.022e23}$              | 科学计数法数字       | Scientific notation number     |
| `\ang{30}`                    | $\ang{30}$                    | 角度（度）           | Angle (degrees)                |
| `\ang{30;20;15}`              | $\ang{30;20;15}$              | 度分秒角度           | Degrees, minutes, seconds      |

### 化学公式（需要 mhchem 包）

| LaTeX 命令                       | 渲染结果                         | 说明                           | 英文名称                                             |
| -------------------------------- | -------------------------------- | ------------------------------ | ---------------------------------------------------- |
| `\usepackage[version=4]{mhchem}` | -                                | 引入mhchem包（化学方程式支持） | Include mhchem package (chemical equations support)  |
| `\ce{H2SO4}`                     | $\ce{H2SO4}$                     | 化学式（自动上下标）           | Chemical formula (auto subscript/superscript)        |
| `\ce{Ca^2+ + CO3^2- -> CaCO3 v}` | $\ce{Ca^2+ + CO3^2- -> CaCO3 v}$ | 化学反应方程式（带沉淀符号）   | Chemical reaction equation (with precipitate symbol) |
| `\ce{A <=> B}`                   | $\ce{A <=> B}$                   | 可逆反应                       | Reversible reaction                                  |
| `\ce{CO2 + C <=> 2 CO}`          | $\ce{CO2 + C <=> 2 CO}$          | 化学反应（可逆）               | Chemical reaction (reversible)                       |

## 颜色和字体（数学模式）

### 数学中的颜色

| LaTeX 命令                         | 渲染结果                           | 说明                     | 英文名称                                    |
| ---------------------------------- | ---------------------------------- | ------------------------ | ------------------------------------------- |
| `\usepackage{xcolor}`              | -                                  | 引入xcolor包（颜色支持） | Include xcolor package (color support)      |
| `\textcolor{red}{x^2}`             | $\textcolor{red}{x^2}$             | 红色文本                 | Red colored text                            |
| `\color{blue} f(x) = x^2`          | $\color{blue} f(x) = x^2$          | 蓝色公式                 | Blue colored formula                        |
| `{\color{green} \int_0^1 x dx}`    | ${\color{green} \int_0^1 x dx}$    | 绿色积分（局部颜色）     | Green integral (local color)                |
| `\colorbox{yellow}{$E = mc^2$}`    | $\colorbox{yellow}{$E = mc^2$}$    | 黄色背景高亮             | Yellow background highlight                 |
| `\fcolorbox{red}{yellow}{$a + b$}` | $\fcolorbox{red}{yellow}{$a + b$}$ | 红框黄底高亮             | Red border with yellow background highlight |

### 数学字体

| LaTeX 命令            | 渲染结果              | 说明                    | 英文名称                           |
| --------------------- | --------------------- | ----------------------- | ---------------------------------- |
| `\mathrm{ABC}`        | $\mathrm{ABC}$        | 直立（罗马）字体        | Roman (upright) font               |
| `\mathit{ABC}`        | $\mathit{ABC}$        | 斜体                    | Italic font                        |
| `\mathbf{ABC}`        | $\mathbf{ABC}$        | 粗体                    | Bold font                          |
| `\mathsf{ABC}`        | $\mathsf{ABC}$        | 无衬线字体              | Sans-serif font                    |
| `\mathtt{ABC}`        | $\mathtt{ABC}$        | 等宽字体                | Typewriter (monospaced) font       |
| `\mathcal{ABC}`       | $\mathcal{ABC}$       | 花体                    | Script font                        |
| `\mathscr{ABC}`       | $\mathscr{ABC}$       | 手写体（需mathrsfs包）  | Cursive font                       |
| `\mathfrak{ABC}`      | $\mathfrak{ABC}$      | 哥特体（需amssymb包）   | Fraktur (Gothic) font              |
| `\mathbb{ABC}`        | $\mathbb{ABC}$        | 黑板粗体（需amssymb包） | Blackboard bold font               |
| `\boldsymbol{\alpha}` | $\boldsymbol{\alpha}$ | 粗体希腊字母            | Bold Greek letters                 |
| `\bm{\nabla}`         | $\bm{\nabla}$         | 粗体符号（需bm包）      | Bold symbols (requires bm package) |



## 实用示例

### 11.1 二次公式

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

```latex
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
```

### 11.2 泰勒级数

$$f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n + R_n(x)$$

```latex
f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n + R_n(x)
```

### 11.3 欧拉公式

$$e^{i\theta} = \cos\theta + i\sin\theta$$

```latex
e^{i\theta} = \cos\theta + i\sin\theta
```

### 11.4 傅里叶变换

$$F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt$$

```latex
F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt
```

### 11.5 麦克斯韦方程组

$$\begin{align}
\nabla \cdot \mathbf{E} &= \frac{\rho}{\epsilon_0} \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu_0\mathbf{J} + \mu_0\epsilon_0\frac{\partial \mathbf{E}}{\partial t}
\end{align}$$

```latex
\begin{align}
\nabla \cdot \mathbf{E} &= \frac{\rho}{\epsilon_0} \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu_0\mathbf{J} + \mu_0\epsilon_0\frac{\partial \mathbf{E}}{\partial t}
\end{align}
```


```yaml
original: "https://blog.csdn.net/LCCFlccf/article/details/89643585"
author: "LCCFlccf"
title: "LaTeX符号、命令速查表"
```

# LaTeX 符号、命令速查表

## 1. 操作符

| LaTeX 命令 | 渲染结果 | 说明 | 英文名称 |
|------------|----------|------|----------|
| `\pm` | $\pm$ | 正负号 | Plus-minus |
| `\mp` | $\mp$ | 负正号 | Minus-plus |
| `\times` | $\times$ | 乘号 | Multiplication |
| `\div` | $\div$ | 除号 | Division |
| `\cdot` | $\cdot$ | 点乘 | Dot |
| `\ast` | $\ast$ | 星号 | Asterisk |
| `\star` | $\star$ | 五角星 | Star |
| `\dagger` | $\dagger$ | 短剑符号 | Dagger |
| `\ddagger` | $\ddagger$ | 双短剑符号 | Double dagger |
| `\amalg` | $\amalg$ | 合并符号 | Amalgamation |
| `\cap` | $\cap$ | 交集 | Intersection |
| `\cup` | $\cup$ | 并集 | Union |
| `\uplus` | $\uplus$ | 多重并集 | Multiset union |
| `\sqcap` | $\sqcap$ | 方交集 | Square intersection |
| `\sqcup` | $\sqcup$ | 方并集 | Square union |
| `\vee` | $\vee$ | 逻辑或 | Logical or |
| `\wedge` | $\wedge$ | 逻辑与 | Logical and |
| `\oplus` | $\oplus$ | 直和 | Direct sum |
| `\ominus` | $\ominus$ | 直减 | Direct subtraction |
| `\otimes` | $\otimes$ | 张量积 | Tensor product |
| `\circ` | $\circ$ | 复合 | Composition |
| `\bullet` | $\bullet$ | 点 | Bullet |
| `\diamond` | $\diamond$ | 菱形 | Diamond |
| `\lhd` | $\lhd$ | 左正规子群 | Left normal subgroup |
| `\rhd` | $\rhd$ | 右正规子群 | Right normal subgroup |
| `\unlhd` | $\unlhd$ | 左包含子群 | Subgroup with inclusion left |
| `\unrhd` | $\unrhd$ | 右包含子群 | Subgroup with inclusion right |
| `\oslash` | $\oslash$ | 斜线圆 | Slashed circle |
| `\odot` | $\odot$ | 点圆 | Circled dot |
| `\bigcirc` | $\bigcirc$ | 大圆 | Big circle |
| `\triangleleft` | $\triangleleft$ | 左三角 | Left triangle |
| `\Diamond` | $\Diamond$ | 大菱形 | Big diamond |
| `\bigtriangleup` | $\bigtriangleup$ | 大三角形 | Big triangle |
| `\bigtriangledown` | $\bigtriangledown$ | 大倒三角 | Big inverted triangle |
| `\Box` | $\Box$ | 方框 | Box |
| `\triangleright` | $\triangleright$ | 右三角 | Right triangle |
| `\setminus` | $\setminus$ | 差集 | Set minus |
| `\wr` | $\wr$ | 扭曲积 | Wreath product |
| `\sqrt{x}` | $\sqrt{x}$ | 平方根 | Square root |
| `x^{\circ}` | $x^{\circ}$ | 度 | Degree |
| `\triangledown` | $\triangledown$ | 倒三角 | Inverted triangle |
| `\sqrt[n]{x}` | $\sqrt[n]{x}$ | n次方根 | nth root |
| `a^x` | $a^x$ | 幂 | Power |
| `a^{xyz}` | $a^{xyz}$ | 多重幂 | Multiple power |

## 2. 关系符

| LaTeX 命令 | 渲染结果 | 说明 | 英文名称 |
|------------|----------|------|----------|
| `\le` 或 `\leq` | $\le$ | 小于等于 | Less than or equal |
| `\ge` 或 `\geq` | $\ge$ | 大于等于 | Greater than or equal |
| `\neq` | $\neq$ | 不等于 | Not equal |
| `\sim` | $\sim$ | 相似 | Similar |
| `\ll` | $\ll$ | 远小于 | Much less than |
| `\gg` | $\gg$ | 远大于 | Much greater than |
| `\doteq` | $\doteq$ | 近似等于 | Approximately equal |
| `\simeq` | $\simeq$ | 渐近相等 | Asymptotically equal |
| `\subset` | $\subset$ | 子集 | Subset |
| `\supset` | $\supset$ | 超集 | Superset |
| `\approx` | $\approx$ | 约等于 | Approximately equal |
| `\asymp` | $\asymp$ | 渐近 | Asymptotic |
| `\subseteq` | $\subseteq$ | 子集或等于 | Subset or equal |
| `\supseteq` | $\supseteq$ | 超集或等于 | Superset or equal |
| `\cong` | $\cong$ | 全等 | Congruent |
| `\smile` | $\smile$ | 微笑关系 | Smile relation |
| `\sqsubset` | $\sqsubset$ | 方子集 | Square subset |
| `\sqsupset` | $\sqsupset$ | 方超集 | Square superset |
| `\equiv` | $\equiv$ | 恒等 | Equivalent |
| `\frown` | $\frown$ | 皱眉关系 | Frown relation |
| `\sqsubseteq` | $\sqsubseteq$ | 方子集或等于 | Square subset or equal |
| `\sqsupseteq` | $\sqsupseteq$ | 方超集或等于 | Square superset or equal |
| `\propto` | $\propto$ | 正比 | Proportional to |
| `\bowtie` | $\bowtie$ | 领结连接 | Bowtie join |
| `\in` | $\in$ | 属于 | Element of |
| `\ni` | $\ni$ | 包含 | Contains |
| `\prec` | $\prec$ | 前驱 | Precedes |
| `\succ` | $\succ$ | 后继 | Succeeds |
| `\vdash` | $\vdash$ | 证明 | Proves |
| `\dashv` | $\dashv$ | 反证 | Reverse proves |
| `\preceq` | $\preceq$ | 前驱或等于 | Precedes or equal |
| `\succeq` | $\succeq$ | 后继或等于 | Succeeds or equal |
| `\models` | $\models$ | 模型 | Models |
| `\perp` | $\perp$ | 垂直 | Perpendicular |
| `\parallel` | $\parallel$ | 平行 | Parallel |
| `\mid` | $\mid$ | 分隔符 | Divides |
| `\bumpeq` | $\bumpeq$ | 凹凸等于 | Bumpy equals |

## 3. 否定关系符

| LaTeX 命令 | 渲染结果 | 说明 |
|------------|----------|------|
| `\nmid` | $\nmid$ | 不整除 |
| `\nleq` | $\nleq$ | 不小于等于 |
| `\ngeq` | $\ngeq$ | 不大于等于 |
| `\nsim` | $\nsim$ | 不相似 |
| `\ncong` | $\ncong$ | 不全等 |
| `\nparallel` | $\nparallel$ | 不平行 |
| `\not<` | $\not<$ | 不小于 |
| `\not>` | $\not>$ | 不大于 |
| `\not=` 或 `\neq` | $\not=$ | 不等于 |
| `\not\le` | $\not\le$ | 不小于等于 |
| `\not\ge` | $\not\ge$ | 不大于等于 |
| `\not\sim` | $\not\sim$ | 不相似 |
| `\not\approx` | $\not\approx$ | 不约等于 |
| `\not\cong` | $\not\cong$ | 不全等 |
| `\not\equiv` | $\not\equiv$ | 不恒等 |
| `\not\parallel` | $\not\parallel$ | 不平行 |
| `\nless` | $\nless$ | 不小于 |
| `\ngtr` | $\ngtr$ | 不大于 |
| `\lneq` | $\lneq$ | 严格小于不等于 |
| `\gneq` | $\gneq$ | 严格大于不等于 |
| `\lnsim` | $\lnsim$ | 不相似且小于 |
| `\lneqq` | $\lneqq$ | 严格小于不等于 |
| `\gneqq` | $\gneqq$ | 严格大于不等于 |

## 4. 箭头符号

| LaTeX 命令 | 渲染结果 | 说明 |
|------------|----------|------|
| `\gets` | $\gets$ | 左箭头 |
| `\to` | $\to$ | 右箭头 |
| `\leftarrow` | $\leftarrow$ | 左箭头 |
| `\Leftarrow` | $\Leftarrow$ | 双线左箭头 |
| `\rightarrow` | $\rightarrow$ | 右箭头 |
| `\Rightarrow` | $\Rightarrow$ | 双线右箭头 |
| `\leftrightarrow` | $\leftrightarrow$ | 左右箭头 |
| `\Leftrightarrow` | $\Leftrightarrow$ | 双线左右箭头 |
| `\mapsto` | $\mapsto$ | 映射到 |
| `\hookleftarrow` | $\hookleftarrow$ | 带钩左箭头 |
| `\leftharpoonup` | $\leftharpoonup$ | 左半箭头上 |
| `\leftharpoondown` | $\leftharpoondown$ | 左半箭头下 |
| `\rightleftharpoons` | $\rightleftharpoons$ | 左右半箭头平衡 |
| `\longleftarrow` | $\longleftarrow$ | 长左箭头 |
| `\Longleftarrow` | $\Longleftarrow$ | 长双线左箭头 |
| `\longrightarrow` | $\longrightarrow$ | 长右箭头 |
| `\Longrightarrow` | $\Longrightarrow$ | 长双线右箭头 |
| `\longleftrightarrow` | $\longleftrightarrow$ | 长左右箭头 |
| `\Longleftrightarrow` | $\Longleftrightarrow$ | 长双线左右箭头 |
| `\longmapsto` | $\longmapsto$ | 长映射到 |
| `\hookrightarrow` | $\hookrightarrow$ | 带钩右箭头 |
| `\rightharpoonup` | $\rightharpoonup$ | 右半箭头上 |
| `\rightharpoondown` | $\rightharpoondown$ | 右半箭头下 |
| `\leadsto` | $\leadsto$ | 引导箭头 |
| `\uparrow` | $\uparrow$ | 上箭头 |
| `\Uparrow` | $\Uparrow$ | 双线上箭头 |
| `\downarrow` | $\downarrow$ | 下箭头 |
| `\Downarrow` | $\Downarrow$ | 双线下箭头 |
| `\updownarrow` | $\updownarrow$ | 上下箭头 |
| `\Updownarrow` | $\Updownarrow$ | 双线上下箭头 |
| `\nearrow` | $\nearrow$ | 东北箭头 |
| `\searrow` | $\searrow$ | 东南箭头 |
| `\swarrow` | $\swarrow$ | 西南箭头 |
| `\nwarrow` | $\nwarrow$ | 西北箭头 |

**快捷方式：**
- `\iff` 可替代 `\Longleftrightarrow`
- `\implies` 可替代 `\Longrightarrow`

## 5. 点符号

| LaTeX 命令 | 渲染结果 | 说明 |
|------------|----------|------|
| `\cdot` | $\cdot$ | 点 |
| `\vdots` | $\vdots$ | 垂直点 |
| `\dots` | $\dots$ | 点序列 |
| `\ddots` | $\ddots$ | 对角点 |
| `\cdots` | $\cdots$ | 中心点 |
| `\iddots` | $\iddots$ | 反向对角点 |

## 6. 上标符号

| LaTeX 命令 | 渲染结果 | 说明 |
|------------|----------|------|
| `\hat{x}` | $\hat{x}$ | 帽子 |
| `\check{x}` | $\check{x}$ | 检查符号 |
| `\dot{x}` | $\dot{x}$ | 点 |
| `\breve{x}` | $\breve{x}$ | 短音符 |
| `\acute{x}` | $\acute{x}$ | 锐音符 |
| `\ddot{x}` | $\ddot{x}$ | 双点 |
| `\grave{x}` | $\grave{x}$ | 重音符 |
| `\tilde{x}` | $\tilde{x}$ | 波浪线 |
| `\mathring{x}` | $\mathring{x}$ | 环 |
| `\bar{x}` | $\bar{x}$ | 横线 |
| `\vec{x}` | $\vec{x}$ | 向量 |

**特殊用法：** 使用 `\imath` 和 `\jmath` 防止点干扰上标：
- `\vec{\jmath}`: $\vec{\jmath}$
- `\tilde{\imath}`: $\tilde{\imath}$

**宽版本上标：**
- `\widehat{7+x}`: $\widehat{7+x}$
- `\widetilde{abc}`: $\widetilde{abc}$

## 7. 其他符号

| LaTeX 命令 | 渲染结果 | 说明 |
|------------|----------|------|
| `\infty` | $\infty$ | 无穷大 |
| `\triangle` | $\triangle$ | 三角形 |
| `\angle` | $\angle$ | 角 |
| `\aleph` | $\aleph$ | 阿列夫 |
| `\hbar` | $\hbar$ | 约化普朗克常数 |
| `\imath` | $\imath$ | 无点i |
| `\jmath` | $\jmath$ | 无点j |
| `\ell` | $\ell$ | 手写体l |
| `\wp` | $\wp$ | Weierstrass p函数 |
| `\Re` | $\Re$ | 实部 |
| `\Im` | $\Im$ | 虚部 |
| `\mho` | $\mho$ | 电导单位 |
| `\prime` | $\prime$ | 撇号 |
| `\emptyset` | $\emptyset$ | 空集 |
| `\nabla` | $\nabla$ | 梯度算子 |
| `\surd` | $\surd$ | 根号 |
| `\partial` | $\partial$ | 偏导数 |
| `\top` | $\top$ | 顶元素 |
| `\bot` | $\bot$ | 底元素 |
| `\vdash` | $\vdash$ | 证明 |
| `\dashv` | $\dashv$ | 反证 |
| `\forall` | $\forall$ | 全称量词 |
| `\exists` | $\exists$ | 存在量词 |
| `\neg` | $\neg$ | 非 |
| `\flat` | $\flat$ | 降号 |
| `\natural` | $\natural$ | 还原号 |
| `\sharp` | $\sharp$ | 升号 |
| `\backslash` | $\backslash$ | 反斜杠 |
| `\Box` | $\Box$ | 方框 |
| `\Diamond` | $\Diamond$ | 菱形 |
| `\clubsuit` | $\clubsuit$ | 梅花 |
| `\diamondsuit` | $\diamondsuit$ | 方块 |
| `\heartsuit` | $\heartsuit$ | 红心 |
| `\spadesuit` | $\spadesuit$ | 黑桃 |
| `\Join` | $\Join$ | 连接 |
| `\blacksquare` | $\blacksquare$ | 黑方块 |
| `\checkmark` | $\checkmark$ | 勾号 |
| `\mathbb{R}` | $\mathbb{R}$ | 黑板粗体R |
| `\copyright` | $\copyright$ | 版权符号 |
| `\pounds` | $\pounds$ | 英镑符号 |
| `\square` | $\square$ | 方框 |
| `\cup` | $\cup$ | 并集 |
| `\bigstar` | $\bigstar$ | 大星 |
| `\in` | $\in$ | 属于 |

## 8. 命令字符

这些字符在LaTeX中有特殊含义，需要转义：

| 字符 | LaTeX 命令 | 说明 |
|------|------------|------|
| `\` | `\backslash` | 反斜杠 |
| `&` | `\&` | 和号 |
| `%` | `\%` | 百分号 |
| `#` | `\#` | 井号 |
| `_` | `\_` | 下划线 |
| `{` | `\{` | 左花括号 |
| `}` | `\}` | 右花括号 |

## 9. 括号调整和大型符号

**括号大小调整：**
- 使用 `\left(` 和 `\right)` 自动调整括号大小
- 示例：`\left(\frac{a}{x} \right)^2` 得到 $\left(\frac{a}{x} \right)^2$

**跨行符号：**
- `\left\{ x+y=3 \\ 2x+y=5 \right.`: $\left\{ \begin{aligned} x+y&=3 \\ 2x+y&=5 \end{aligned} \right.$
- `\left\lceil\frac{x}{y}\right\rceil`: $\left\lceil\frac{x}{y}\right\rceil$
- `\left\lfloor\frac{x}{y}\right\rfloor`: $\left\lfloor\frac{x}{y}\right\rfloor$

**上下括号：**
- `\underbrace{a_0+a_1+\cdots+a_n}_{x}`: $\underbrace{a_0+a_1+\cdots+a_n}_{x}$
- `\overbrace{a_0+a_1+\cdots+a_n}^{x}`: $\overbrace{a_0+a_1+\cdots+a_n}^{x}$

**带极限的表达式：**
- `\arg \underset{1\leq k \leq n}{\max} \frac{\lambda_k}{\lambda_{k+1}}`: $\arg \underset{1\leq k \leq n}{\max} \frac{\lambda_k}{\lambda_{k+1}}$

**可调整大小的符号：**
| LaTeX 命令 | 渲染结果 |
|------------|----------|
| `\left\uparrow ... \right\uparrow` | 可调整的上箭头 |
| `\left\downarrow ... \right\downarrow` | 可调整的下箭头 |
| `\left\updownarrow ... \right\updownarrow` | 可调整的上下箭头 |

**大型运算符：**
| LaTeX 命令 | 渲染结果 |
|------------|----------|
| `\sum` | $\sum$ |
| `\int` | $\int$ |
| `\oint` | $\oint$ |
| `\prod` | $\prod$ |
| `\coprod` | $\coprod$ |
| `\bigcap` | $\bigcap$ |
| `\bigcup` | $\bigcup$ |
| `\bigsqcup` | $\bigsqcup$ |
| `\bigvee` | $\bigvee$ |
| `\bigwedge` | $\bigwedge$ |
| `\bigodot` | $\bigodot$ |
| `\bigotimes` | $\bigotimes$ |
| `\bigoplus` | $\bigoplus$ |
| `\biguplus` | $\biguplus$ |

## 10. 间距控制

| LaTeX 命令 | 示例 | 说明 |
|------------|------|------|
| `\\` | `a=1\\b=2` | 换行 |
| `\qquad` | `a \qquad b` | 双倍间距 |
| `\quad` | `a \quad b` | 单倍间距 |
| `\ ` | `a\ b` | 空格 |
| `\;` | `a \; b` | 中等间距 |
| `\:` | `a \: b` | 小间距 |
| `\,` | `a \, b` | 微小间距 |
| 无空格 | `ab` | 无间距 |
| `\!` | `a \! b` | 负间距 |
