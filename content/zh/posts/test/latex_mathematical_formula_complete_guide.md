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

| LaTeX 命令 | 渲染结果 | 中文名称 | 英文名称 |
|------------|----------|----------|----------|
| `+` | $+$ | 加号 | Plus |
| `-` | $-$ | 减号 | Minus |
| `\pm` | $\pm$ | 正负号 | Plus-minus |
| `\mp` | $\mp$ | 负正号 | Minus-plus |
| `\times` | $\times$ | 乘号 | Multiplication |
| `\div` | $\div$ | 除号 | Division |
| `\cdot` | $\cdot$ | 中心点 | Center dot |
| `\ast` | $\ast$ | 星号 | Asterisk |
| `\star` | $\star$ | 五角星 | Star |
| `\circ` | $\circ$ | 圆圈 | Circle |
| `\bullet` | $\bullet$ | 实心圆点 | Bullet |
| `\diamond` | $\diamond$ | 菱形 | Diamond |

### 关系符号

比较

| LaTeX 命令 | 渲染结果 | 说明 | 英文名称 |
|------------|----------|------|----------|
| `=` | $=$ | 等于 | Equals |
| `\neq` | $\neq$ | 不等于 | Not equal |
| `<` | $<$ | 小于 | Less than |
| `>` | $>$ | 大于 | Greater than |
| `\leq` | $\leq$ | 小于等于 | Less than or equal to |
| `\geq` | $\geq$ | 大于等于 | Greater than or equal to |
| `\ll` | $\ll$ | 远小于 | Much less than |
| `\gg` | $\gg$ | 远大于 | Much greater than |
| `\lll` | $\lll$ | 超小于 | Very much less than |
| `\ggg` | $\ggg$ | 超大于 | Very much greater than |

近似和相似

| LaTeX 命令 | 渲染结果 | 说明 | 英文名称 |
|------------|----------|------|----------|
| `\approx` | $\approx$ | 约等于 | Approximately equal to |
| `\sim` | $\sim$ | 相似 | Similar to |
| `\simeq` | $\simeq$ | 相似等于 | Asymptotically equal to |
| `\cong` | $\cong$ | 全等 | Congruent to |
| `\equiv` | $\equiv$ | 恒等 | Equivalent to |
| `\propto` | $\propto$ | 正比 | Proportional to |
| `\parallel` | $\parallel$ | 平行 | Parallel to |
| `\perp` | $\perp$ | 垂直 | Perpendicular to |


### 集合论符号

包含关系

| LaTeX 命令 | 渲染结果 | 说明 | 英文名称 |
|------------|----------|------|----------|
| `\in` | $\in$ | 属于 | Element of |
| `\notin` | $\notin$ | 不属于 | Not an element of |
| `\ni` | $\ni$ | 包含（反向属于） | Contains as member |
| `\subset` | $\subset$ | 子集 | Subset |
| `\supset` | $\supset$ | 超集 | Superset |
| `\subseteq` | $\subseteq$ | 子集或等于 | Subset or equal |
| `\supseteq` | $\supseteq$ | 超集或等于 | Superset or equal |
| `\subsetneq` | $\subsetneq$ | 真子集 | Proper subset |
| `\supsetneq` | $\supsetneq$ | 真超集 | Proper superset |

集合运算

| LaTeX 命令 | 渲染结果 | 说明 | 英文名称 |
|------------|----------|------|----------|
| `\cup` | $\cup$ | 并集 | Union |
| `\cap` | $\cap$ | 交集 | Intersection |
| `\setminus` | $\setminus$ | 差集 | Set minus |
| `\emptyset` | $\emptyset$ | 空集 | Empty set |
| `\varnothing` | $\varnothing$ | 空集（另一种形式） | Empty set (variant) |

### 逻辑符号

逻辑运算

| LaTeX 命令 | 渲染结果 | 说明 | 英文名称 |
|------------|----------|------|----------|
| `\land` | $\land$ | 逻辑与 | Logical AND |
| `\lor` | $\lor$ | 逻辑或 | Logical OR |
| `\lnot` | $\lnot$ | 逻辑非 | Logical NOT |
| `\neg` | $\neg$ | 逻辑非（同\lnot） | Logical NOT |
| `\implies` | $\implies$ | 蕴含 | Implies |
| `\impliedby` | $\impliedby$ | 被蕴含 | Implied by |
| `\iff` | $\iff$ | 当且仅当 | If and only if |
| `\Leftrightarrow` | $\Leftrightarrow$ | 等价 | Equivalent to |
| `\Rightarrow` | $\Rightarrow$ | 推出 | Right arrow |
| `\Leftarrow` | $\Leftarrow$ | 被推出 | Left arrow |

量词

| LaTeX 命令 | 渲染结果 | 说明 | 英文名称 |
|------------|----------|------|----------|
| `\forall` | $\forall$ | 全称量词 | For all |
| `\exists` | $\exists$ | 存在量词 | There exists |
| `\nexists` | $\nexists$ | 不存在 | There does not exist |

、

### 箭头符号

基本箭头

| LaTeX 命令 | 渲染结果 | 说明 | 英文名称 |
|------------|----------|------|----------|
| `\leftarrow` | $\leftarrow$ | 左箭头 | Left arrow |
| `\rightarrow` | $\rightarrow$ | 右箭头 | Right arrow |
| `\uparrow` | $\uparrow$ | 上箭头 | Up arrow |
| `\downarrow` | $\downarrow$ | 下箭头 | Down arrow |
| `\leftrightarrow` | $\leftrightarrow$ | 左右箭头 | Left-right arrow |
| `\updownarrow` | $\updownarrow$ | 上下箭头 | Up-down arrow |

长箭头

| LaTeX 命令 | 渲染结果 | 说明 | 英文名称 |
|------------|----------|------|----------|
| `\longleftarrow` | $\longleftarrow$ | 长左箭头 | Long left arrow |
| `\longrightarrow` | $\longrightarrow$ | 长右箭头 | Long right arrow |
| `\longleftrightarrow` | $\longleftrightarrow$ | 长左右箭头 | Long left-right arrow |

双线箭头

| LaTeX 命令 | 渲染结果 | 说明 | 英文名称 |
|------------|----------|------|----------|
| `\Leftarrow` | $\Leftarrow$ | 双线左箭头 | Double left arrow |
| `\Rightarrow` | $\Rightarrow$ | 双线右箭头 | Double right arrow |
| `\Updownarrow` | $\Updownarrow$ | 双线上下箭头 | Double up-down arrow |
| `\Leftrightarrow` | $\Leftrightarrow$ | 双线左右箭头 | Double left-right arrow |

映射箭头

| LaTeX 命令 | 渲染结果 | 说明 | 英文名称 |
|------------|----------|------|----------|
| `\mapsto` | $\mapsto$ | 映射到 | Maps to |
| `\longmapsto` | $\longmapsto$ | 长映射到 | Long maps to |
| `\hookrightarrow` | $\hookrightarrow$ | 带钩右箭头 | Rightwards arrow with hook |
| `\hookleftarrow` | $\hookleftarrow$ | 带钩左箭头 | Leftwards arrow with hook |
| `\rightharpoonup` | $\rightharpoonup$ | 右半箭头 | Right harpoon |
| `\leftharpoonup` | $\leftharpoonup$ | 左半箭头 | Left harpoon |

## 希腊字母表

### 小写希腊字母

| LaTeX 命令 | 渲染结果 | 说明 | 英文名称 |
|------------|----------|------|----------|
| `\alpha` | $\alpha$ | 阿尔法 | alpha |
| `\beta` | $\beta$ | 贝塔 | beta |
| `\gamma` | $\gamma$ | 伽马 | gamma |
| `\delta` | $\delta$ | 德尔塔 | delta |
| `\epsilon` | $\epsilon$ | 艾普西隆 | epsilon |
| `\varepsilon` | $\varepsilon$ | 艾普西隆（变体） | epsilon variant |
| `\zeta` | $\zeta$ | 泽塔 | zeta |
| `\eta` | $\eta$ | 伊塔 | eta |
| `\theta` | $\theta$ | 西塔 | theta |
| `\vartheta` | $\vartheta$ | 西塔（变体） | theta variant |
| `\iota` | $\iota$ | 约塔 | iota |
| `\kappa` | $\kappa$ | 卡帕 | kappa |
| `\lambda` | $\lambda$ | 拉姆达 | lambda |
| `\mu` | $\mu$ | 缪 | mu |
| `\nu` | $\nu$ | 纽 | nu |
| `\xi` | $\xi$ | 克西 | xi |
| `\pi` | $\pi$ | 派 | pi |
| `\varpi` | $\varpi$ | 派（变体） | pi variant |
| `\rho` | $\rho$ | 柔 | rho |
| `\varrho` | $\varrho$ | 柔（变体） | rho variant |
| `\sigma` | $\sigma$ | 西格玛 | sigma |
| `\varsigma` | $\varsigma$ | 西格玛（词尾形式） | sigma final |
| `\tau` | $\tau$ | 陶 | tau |
| `\upsilon` | $\upsilon$ | 宇普西隆 | upsilon |
| `\phi` | $\phi$ | 斐 | phi |
| `\varphi` | $\varphi$ | 斐（变体） | phi variant |
| `\chi` | $\chi$ | 希 | chi |
| `\psi` | $\psi$ | 普西 | psi |
| `\omega` | $\omega$ | 欧米伽 | omega |



### 大写希腊字母

| LaTeX 命令 | 渲染结果 | 说明 | 英文名称 |
|------------|----------|------|----------|
| `\Gamma` | $\Gamma$ | 大写伽马 | Gamma |
| `\Delta` | $\Delta$ | 大写德尔塔 | Delta |
| `\Theta` | $\Theta$ | 大写西塔 | Theta |
| `\Lambda` | $\Lambda$ | 大写拉姆达 | Lambda |
| `\Xi` | $\Xi$ | 大写克西 | Xi |
| `\Pi` | $\Pi$ | 大写派 | Pi |
| `\Sigma` | $\Sigma$ | 大写西格玛 | Sigma |
| `\Upsilon` | $\Upsilon$ | 大写宇普西隆 | Upsilon |
| `\Phi` | $\Phi$ | 大写斐 | Phi |
| `\Psi` | $\Psi$ | 大写普西 | Psi |
| `\Omega` | $\Omega$ | 大写欧米伽 | Omega |



## 上标与下标

### 基本用法

上标


| LaTeX 命令 | 渲染结果 | 说明 | 示例 |
|------------|----------|------|------|
| `x^2` | $x^2$ | 上标 | $x^2$ |
| `x^{10}` | $x^{10}$ | 多位数字上标 | $x^{10}$ |
| `x^{2n+1}` | $x^{2n+1}$ | 复杂表达式上标 | $x^{2n+1}$ |

下标

| LaTeX 命令 | 渲染结果 | 说明 | 示例 |
|------------|----------|------|------|
| `x_1` | $x_1$ | 下标 | $x_1$ |
| `x_{10}` | $x_{10}$ | 多位数字下标 | $x_{10}$ |
| `x_{i,j}` | $x_{i,j}$ | 多字符下标 | $x_{i,j}$ |

上下标同时使用
| LaTeX 命令 | 渲染结果 | 说明 | 示例 |
|------------|----------|------|------|
| `x_1^2` | $x_1^2$ | 同时上下标（推荐） | $x_1^2$ |
| `x^2_1` | $x^2_1$ | 同时上下标（先上标） | $x^2_1$ |
| `x_{i}^{(n)}` | $x_{i}^{(n)}$ | 复杂上下标组合 | $x_{i}^{(n)}$ |


### 复杂上下标

```latex
% 多重上下标
x^{x^x}         % x^(x^x)
x_{y_z}         % x_{y_z}

% 左右上下标
\prescript{14}{2}C      % ¹⁴₂C（前置上下标）
{}^{14}C_2              % 同上，另一种写法

% 上下标对齐
\sideset{_1^2}{_3^4}\prod   % 带上下标的 ∏
```

## 分数与根式

### 分数

```latex
% 基本分数
\frac{1}{2}             % 1/2
\frac{a+b}{c+d}         % (a+b)/(c+d)

% 嵌套分数
\frac{1}{1+\frac{1}{2}} % 连分数

% 行内分数（较小）
\tfrac{1}{2}            % 适合行内使用的小分数
\dfrac{1}{2}            % 强制使用显示样式的大分数

% 斜分数
\nicefrac{1}{2}         % 1/2（需要 nicefrac 包）

% 二项式系数
\binom{n}{k}            % C_n^k 或 (n choose k)
\dbinom{n}{k}           % 显示样式
\tbinom{n}{k}           % 文本样式
```

### 根式

```latex
% 平方根
\sqrt{2}                % √2
\sqrt{x+y}              % √(x+y)

% n次根
\sqrt[3]{8}             % ∛8
\sqrt[n]{x}             % ⁿ√x

% 嵌套根式
\sqrt{1+\sqrt{2}}       % √(1+√2)
```

## 求和、积分和极限

### 求和符号

```latex
% 基本求和
\sum                    % Σ
\sum_{i=1}^{n}          % 带上下限的求和
\sum_{i=1}^{n} i        % Σ(i=1 to n) i
\sum\limits_{i=1}^{n}   % 强制上下限在上下方

% 其他求和类符号
\prod                   % ∏（乘积）
\coprod                 % ∐（副积）
\bigcup                 % ⋃（并集）
\bigcap                 % ⋂（交集）
\bigoplus               % ⊕（直和）
\bigotimes              % ⊗（直积）
\bigwedge               % ⋀（合取）
\bigvee                 % ⋁（析取）
```

### 积分符号

```latex
% 基本积分
\int                    % ∫
\int_0^1                % 定积分
\int_{-\infty}^{\infty} % 无穷积分
\int\limits_0^1         % 强制上下限在上下方

% 多重积分
\iint                   % ∬（二重积分）
\iiint                  % ∭（三重积分）
\iiiint                 % ⨌（四重积分）
\idotsint               % 多重积分（n重）

% 围道积分
\oint                   % ∮（围道积分）
\oiint                  % ∯（面积分）
\oiiint                 % ∰（体积分）

% 积分变量间距
\int x \, dx            % 正常间距
\int x \: dx            % 中等间距
\int x \; dx            % 较大间距
\int x \! dx            % 紧密间距
```

### 极限

```latex
% 基本极限
\lim                    % lim
\lim_{x \to 0}          % lim(x→0)
\lim_{x \to +\infty}    % lim(x→+∞)
\lim_{n \to \infty}     % lim(n→∞)

% 上下极限
\limsup                 % lim sup
\liminf                 % lim inf
\varlimsup              % 变体上极限
\varliminf              % 变体下极限

% 强制位置
\lim\limits_{x \to 0}   % 强制下标在下方
\lim\nolimits_{x \to 0} % 强制下标在右侧
```

## 函数和运算符

### 标准函数

```latex
% 三角函数
\sin        % sin
\cos        % cos
\tan        % tan
\cot        % cot
\sec        % sec
\csc        % csc

% 反三角函数
\arcsin     % arcsin
\arccos     % arccos
\arctan     % arctan
\arccot     % arccot
\arcsec     % arcsec
\arccsc     % arccsc

% 双曲函数
\sinh       % sinh
\cosh       % cosh
\tanh       % tanh
\coth       % coth

% 对数函数
\log        % log
\ln         % ln
\lg         % lg
\log_2      % log₂（需要下标）

% 其他函数
\exp        % exp
\max        % max
\min        % min
\sup        % sup
\inf        % inf
\arg        % arg
\ker        % ker
\dim        % dim
\hom        % hom
\det        % det
\gcd        % gcd
\deg        % deg
```

### 自定义运算符

```latex
% 定义新的运算符
\DeclareMathOperator{\Tr}{Tr}       % 迹
\DeclareMathOperator*{\argmax}{arg\,max}  % argmax（带极限）
\DeclareMathOperator{\rank}{rank}   % 秩

% 使用
\Tr(A)              % Tr(A)
\argmax_{x} f(x)    % argmax_x f(x)
\rank(M)            % rank(M)

% 临时运算符
\operatorname{sinc} % sinc
```

## 矩阵和行列式

### 基本矩阵环境

```latex
% matrix：无括号
\begin{matrix}
a & b \\
c & d
\end{matrix}

% pmatrix：圆括号
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}

% bmatrix：方括号
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}

% Bmatrix：花括号
\begin{Bmatrix}
a & b \\
c & d
\end{Bmatrix}

% vmatrix：行列式（单竖线）
\begin{vmatrix}
a & b \\
c & d
\end{vmatrix}

% Vmatrix：范数（双竖线）
\begin{Vmatrix}
a & b \\
c & d
\end{Vmatrix}
```

### 复杂矩阵结构

```latex
% 分块矩阵
\begin{pmatrix}
A & B \\
C & D
\end{pmatrix}

% 带省略号的矩阵
\begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}

% 增广矩阵
\left(\begin{array}{cc|c}
a & b & x \\
c & d & y
\end{array}\right)

% 小型矩阵（行内使用）
\begin{smallmatrix}
a & b \\
c & d
\end{smallmatrix}
```

### 向量表示

```latex
% 列向量
\begin{pmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{pmatrix}

% 行向量
\begin{pmatrix} x_1 & x_2 & \cdots & x_n \end{pmatrix}

% 向量符号
\vec{v}             % 向量箭头
\mathbf{v}          % 粗体向量
\boldsymbol{v}      % 粗体符号（包括希腊字母）
\overrightarrow{AB} % 从A到B的向量
```

## 多行公式

### align 环境

```latex
% 基本对齐
\begin{align}
x &= a + b \\
  &= c + d \\
  &= e + f
\end{align}

% 多个对齐点
\begin{align}
x &= a + b & y &= p + q \\
  &= c + d &   &= r + s
\end{align}

% 无编号版本
\begin{align*}
x &= a + b \\
  &= c + d
\end{align*}
```

### 其他多行环境

```latex
% gather：居中，无对齐
\begin{gather}
x = a + b \\
y = c + d
\end{gather}

% multline：第一行左对齐，最后一行右对齐，中间居中
\begin{multline}
x = a + b + c + d + e \\
+ f + g + h + i + j \\
+ k + l + m
\end{multline}

% split：必须在其他环境内使用
\begin{equation}
\begin{split}
x &= a + b \\
  &\quad + c + d
\end{split}
\end{equation}

% alignat：指定对齐列数
\begin{alignat}{2}
x &= a & \quad y &= p \\
  &= b &       z &= q
\end{alignat}
```

### 分类和条件表达式

```latex
% cases 环境：分段函数
f(x) = \begin{cases}
x^2 & \text{if } x \geq 0 \\
-x^2 & \text{if } x < 0
\end{cases}

% 复杂条件
\begin{cases}
x + y = 2 \\
x - y = 0 \\
z = 1
\end{cases}

% 大括号分组
\left\{
\begin{aligned}
x + y &= 2 \\
x - y &= 0
\end{aligned}
\right.
```

## 空格和对齐

### 数学模式中的空格

```latex
% 空格大小（从小到大）
a\!b            % 负间距
ab              % 无间距
a\,b            % 小间距（3/18 em）
a\:b            % 中间距（4/18 em）
a\;b            % 大间距（5/18 em）
a\ b            % 单词间距
a\quad b        % 1 em 间距
a\qquad b       % 2 em 间距

% 实际使用示例
\int x \, dx    % 积分变量前的小间距
\sin x          % 函数名后的自然间距
```

### 文本对齐和间距

```latex
% 在数学环境中插入文本
\text{这是文本}
\mbox{文本框}

% 带间距的文本
x = 2 \quad \text{当且仅当} \quad y = 4

% 幻影（占空间但不显示）
\phantom{x}     % 占据 x 的空间但不显示
\hphantom{x}    % 水平幻影
\vphantom{x}    % 垂直幻影
```

## 特殊符号和重音

### 数学重音符号

```latex
% 单字符重音
\hat{a}         % â（帽子）
\check{a}       % ǎ（检查符号）
\breve{a}       % ă（短音符）
\acute{a}       % á（锐音符）
\grave{a}       % à（重音符）
\tilde{a}       % ã（波浪线）
\bar{a}         % ā（长音符）
\vec{a}         % a⃗（向量）
\dot{a}         % ȧ（一点）
\ddot{a}        % ä（两点）

% 宽重音（适用于多字符）
\widehat{abc}   % 宽帽子
\widetilde{abc} % 宽波浪线
\overline{abc}  % 上划线
\underline{abc} % 下划线
\overbrace{abc}^{\text{说明}}      % 上括号
\underbrace{abc}_{\text{说明}}     % 下括号
```

### 特殊数学符号

```latex
% 无穷大
\infty          % ∞

% 偏导数
\partial        % ∂

% 梯度算子
\nabla          % ∇

% 角度
\angle          % ∠
\measuredangle  % ∡
\sphericalangle % ∢

% 度数
30^\circ        % 30°
\degree         % °（需要特定包）

% 整数集合等
\mathbb{N}      % ℕ（自然数）
\mathbb{Z}      % ℤ（整数）
\mathbb{Q}      % ℚ（有理数）
\mathbb{R}      % ℝ（实数）
\mathbb{C}      % ℂ（复数）

% 手写体字母
\mathcal{A}     % 𝒜
\mathscr{B}     % ℬ（需要 mathrsfs 包）
\mathfrak{C}    % 𝔄（需要 amssymb 包）
```

## 大型运算符的定制

### 自定义大型运算符

```latex
% 使用 \mathop
\mathop{\text{lcm}}_{i=1}^n a_i         % 最小公倍数

% 使用 \operatorname*
\operatorname*{argmax}_{x \in S} f(x)   % argmax

% 自定义积分类符号
\def\upint{\mathchoice%
    {\mkern13mu\overline{\vphantom{\intop}\mkern7mu}\mkern-20mu}%
    {\mkern7mu\overline{\vphantom{\intop}\mkern7mu}\mkern-14mu}%
    {\mkern7mu\overline{\vphantom{\intop}\mkern7mu}\mkern-14mu}%
    {\mkern7mu\overline{\vphantom{\intop}\mkern7mu}\mkern-14mu}%
  \int}
\def\lowint{\mkern3mu\underline{\vphantom{\intop}\mkern7mu}\mkern-10mu\int}

% 使用自定义积分
\upint_0^1 f(x) dx      % 上积分
\lowint_0^1 f(x) dx     % 下积分
```

## 数组和表格

### 基本数组

```latex
% 简单数组
\begin{array}{ccc}
a & b & c \\
d & e & f
\end{array}

% 带分隔线的数组
\begin{array}{|c|c|c|}
\hline
a & b & c \\
\hline
d & e & f \\
\hline
\end{array}

% 列对齐：l(左), c(中), r(右)
\begin{array}{lcr}
左对齐 & 居中 & 右对齐 \\
A & B & C
\end{array}
```

### 数学表格的高级用法

```latex
% 三角函数值表
\begin{array}{|c||c|c|c|c|}
\hline
\theta & 0 & \frac{\pi}{6} & \frac{\pi}{4} & \frac{\pi}{3} \\
\hline\hline
\sin\theta & 0 & \frac{1}{2} & \frac{\sqrt{2}}{2} & \frac{\sqrt{3}}{2} \\
\hline
\cos\theta & 1 & \frac{\sqrt{3}}{2} & \frac{\sqrt{2}}{2} & \frac{1}{2} \\
\hline
\end{array}
```

## 定理环境（数学写作）

### 基本定理环境

```latex
% 需要 amsthm 包
\usepackage{amsthm}

% 定义定理环境
\newtheorem{theorem}{定理}[section]
\newtheorem{lemma}[theorem]{引理}
\newtheorem{proposition}[theorem]{命题}
\newtheorem{corollary}[theorem]{推论}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{定义}
\newtheorem{example}[theorem]{例子}

\theoremstyle{remark}
\newtheorem{remark}[theorem]{注}
\newtheorem*{note}{注意}

% 使用定理环境
\begin{theorem}[勾股定理]
\label{thm:pythagoras}
在直角三角形中，$a^2 + b^2 = c^2$。
\end{theorem}

\begin{proof}
证明内容...
\end{proof}
```

## 编号和引用

### 公式编号控制

```latex
% 自动编号
\begin{equation}
E = mc^2
\end{equation}

% 手动设置编号
\begin{equation}
E = mc^2
\tag{Einstein}
\end{equation}

% 子编号
\begin{subequations}
\begin{align}
a &= b + c \\
d &= e + f
\end{align}
\end{subequations}

% 不编号的行
\begin{align}
x &= a + b \\
y &= c + d \nonumber \\
z &= e + f
\end{align}
```

### 交叉引用

```latex
% 标记公式
\begin{equation}
E = mc^2
\label{eq:einstein}
\end{equation}

% 引用公式
如方程~\eqref{eq:einstein}~所示...
根据公式~(\ref{eq:einstein})...

% 多个引用
方程~\eqref{eq:first,eq:second,eq:third}~表明...
```

## 物理和化学符号

### 物理单位（需要 siunitx 包）

```latex
\usepackage{siunitx}

% 数值和单位
\SI{3e8}{\meter\per\second}         % 3×10⁸ m/s
\SI{1.602e-19}{\coulomb}            % 1.602×10⁻¹⁹ C
\SI{273.15}{\kelvin}                % 273.15 K
\num{6.022e23}                      % 6.022×10²³

% 角度
\ang{30}                            % 30°
\ang{30;20;15}                      % 30°20′15″
```

### 化学公式（需要 mhchem 包）

```latex
\usepackage[version=4]{mhchem}

% 化学方程式
\ce{H2SO4}                          % H₂SO₄
\ce{Ca^2+ + CO3^2- -> CaCO3 v}      % Ca²⁺ + CO₃²⁻ → CaCO₃↓
\ce{A <=> B}                        % A ⇌ B
\ce{CO2 + C <=> 2 CO}               % CO₂ + C ⇌ 2CO
```

## 颜色和字体（数学模式）

### 数学中的颜色

```latex
\usepackage{xcolor}

% 彩色数学
\textcolor{red}{x^2}                % 红色的 x²
\color{blue} f(x) = x^2             % 蓝色的函数
{\color{green} \int_0^1 x dx}       % 绿色的积分

% 高亮背景
\colorbox{yellow}{$E = mc^2$}       % 黄色背景
\fcolorbox{red}{yellow}{$a + b$}    % 红框黄底
```

### 数学字体

```latex
% 字体变体
\mathrm{ABC}        % 直立（罗马）字体
\mathit{ABC}        % 斜体
\mathbf{ABC}        % 粗体
\mathsf{ABC}        % 无衬线字体
\mathtt{ABC}        % 等宽字体
\mathcal{ABC}       % 花体
\mathscr{ABC}       % 手写体（需要 mathrsfs 包）
\mathfrak{ABC}      % 哥特体（需要 amssymb 包）
\mathbb{ABC}        % 黑板粗体（需要 amssymb 包）

% 组合使用
\boldsymbol{\alpha}     % 粗体希腊字母
\bm{\nabla}             % 粗体符号（需要 bm 包）
```


# LaTeX数学排版详细指南

## 1. 数学模式基础

### 1.1 行内数学模式

使用 `$...$` 或 `\(...\)` 来插入行内公式：

```latex
这是行内公式：$E = mc^2$
或者：\(F = ma\)
```

### 1.2 独立数学模式

使用 `$$...$$` 或 `\[...\]` 来创建独立的数学公式：

```latex
$$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$$

\[
\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}
\]
```

## 2. 数学符号和运算符

### 2.1 基本运算符

|符号|LaTeX代码|说明|
|---|---|---|
|+|`+`|加号|
|-|`-`|减号|
|×|`\times`|乘号|
|÷|`\div`|除号|
|±|`\pm`|正负号|
|∓|`\mp`|负正号|
|·|`\cdot`|点乘|
|⋅|`\bullet`|实心点|

### 2.2 关系符号

|符号|LaTeX代码|说明|
|---|---|---|
|=|`=`|等于|
|≠|`\neq`|不等于|
|<|`<`|小于|
|>|`>`|大于|
|≤|`\leq` 或 `\le`|小于等于|
|≥|`\geq` 或 `\ge`|大于等于|
|≈|`\approx`|约等于|
|≡|`\equiv`|恒等于|
|∝|`\propto`|正比于|

### 2.3 集合符号

|符号|LaTeX代码|说明|
|---|---|---|
|∈|`\in`|属于|
|∉|`\notin`|不属于|
|⊂|`\subset`|子集|
|⊆|`\subseteq`|子集或等于|
|∪|`\cup`|并集|
|∩|`\cap`|交集|
|∅|`\emptyset`|空集|
|∞|`\infty`|无穷大|

### 2.4 希腊字母

#### 小写希腊字母

```latex
\alpha, \beta, \gamma, \delta, \epsilon, \zeta, \eta, \theta,
\iota, \kappa, \lambda, \mu, \nu, \xi, \pi, \rho,
\sigma, \tau, \upsilon, \phi, \chi, \psi, \omega
```

#### 大写希腊字母

```latex
\Gamma, \Delta, \Theta, \Lambda, \Xi, \Pi, \Sigma,
\Upsilon, \Phi, \Psi, \Omega
```

## 3. 上标和下标

### 3.1 基本用法

```latex
% 上标
x^2, y^{10}, e^{i\pi}

% 下标
x_1, y_{max}, a_{i,j}

% 同时使用
x_1^2, y_{max}^{n+1}
```

### 3.2 复杂的上下标

```latex
% 多层上标
x^{y^z}, e^{e^x}

% 前置上下标
{}^14C, {}^{235}U

% 左右上下标
{}^a_b X^c_d
```

## 4. 分数和根号

### 4.1 分数

```latex
% 基本分数
\frac{1}{2}, \frac{a}{b}

% 复杂分数
\frac{1 + \frac{1}{x}}{2 + \frac{1}{y}}

% 连分数
\cfrac{1}{2 + \cfrac{1}{3 + \cfrac{1}{4}}}
```

### 4.2 根号

```latex
% 平方根
\sqrt{2}, \sqrt{x^2 + y^2}

% n次根
\sqrt[3]{8}, \sqrt[n]{x}

% 嵌套根号
\sqrt{\sqrt{x}}
```

## 5. 求和、积分和极限

### 5.1 求和符号

```latex
% 基本求和
\sum_{i=1}^n x_i

% 复杂求和
\sum_{i=1}^{\infty} \frac{1}{i^2}

% 多重求和
\sum_{i=1}^m \sum_{j=1}^n a_{ij}
```

### 5.2 积分符号

```latex
% 定积分
\int_0^1 x^2 dx

% 不定积分
\int f(x) dx

% 多重积分
\iint_{D} f(x,y) dxdy
\iiint_{V} f(x,y,z) dxdydz

% 围道积分
\oint_C f(z) dz
```

### 5.3 极限

```latex
% 基本极限
\lim_{x \to 0} \frac{\sin x}{x}

% 上下极限
\limsup_{n \to \infty} a_n
\liminf_{n \to \infty} a_n

% 左右极限
\lim_{x \to 0^+} f(x)
\lim_{x \to 0^-} f(x)
```

## 6. 矩阵和行列式

### 6.1 基本矩阵

```latex
% 圆括号矩阵
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}

% 方括号矩阵
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}

% 花括号矩阵
\begin{Bmatrix}
a & b \\
c & d
\end{Bmatrix}
```

### 6.2 行列式

```latex
% 行列式
\begin{vmatrix}
a & b \\
c & d
\end{vmatrix}

% 大行列式
\begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{vmatrix}
```

### 6.3 特殊矩阵

```latex
% 单位矩阵
I = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}

% 零矩阵用省略号
\begin{pmatrix}
0 & \cdots & 0 \\
\vdots & \ddots & \vdots \\
0 & \cdots & 0
\end{pmatrix}
```

## 7. 多行公式和对齐

### 7.1 align环境

```latex
\begin{align}
x &= a + b + c \\
  &= d + e \\
  &= f
\end{align}
```

### 7.2 分情况讨论

```latex
f(x) = \begin{cases}
x^2, & \text{if } x \geq 0 \\
-x^2, & \text{if } x < 0
\end{cases}
```

### 7.3 方程组

```latex
\begin{align}
x + y &= 1 \\
2x - y &= 0
\end{align}

% 或使用cases
\begin{cases}
x + y = 1 \\
2x - y = 0
\end{cases}
```

## 8. 特殊函数和符号

### 8.1 三角函数

```latex
\sin x, \cos x, \tan x, \cot x, \sec x, \csc x
\arcsin x, \arccos x, \arctan x
\sinh x, \cosh x, \tanh x
```

### 8.2 对数函数

```latex
\log x, \ln x, \lg x, \log_2 x, \log_{10} x
```

### 8.3 微分符号

```latex
% 导数
\frac{dy}{dx}, \frac{d^2y}{dx^2}, \frac{\partial f}{\partial x}

% 微分
dx, dy, d\theta

% 全微分
df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy
```

### 8.4 向量符号

```latex
% 向量表示
\vec{a}, \overrightarrow{AB}

% 单位向量
\hat{i}, \hat{j}, \hat{k}

% 向量运算
\vec{a} \cdot \vec{b}, \vec{a} \times \vec{b}
```

## 9. 空间和字体

### 9.1 空间控制

```latex
% 细空格
a\,b

% 中等空格
a\;b

% 大空格
a\ b

% 特大空格
a\quad b
a\qquad b
```

### 9.2 数学字体

```latex
% 粗体
\mathbf{A}, \boldsymbol{\alpha}

% 花体
\mathcal{A}, \mathscr{B}

% 黑板粗体
\mathbb{R}, \mathbb{C}, \mathbb{N}

% 罗马字体
\mathrm{sin}, \mathrm{cos}

% 打字机字体
\mathtt{code}
```

## 10. 常用数学环境

### 10.1 定理环境

```latex
% 需要在导言区定义
\newtheorem{theorem}{定理}
\newtheorem{lemma}{引理}
\newtheorem{proof}{证明}

% 使用
\begin{theorem}
这是一个定理。
\end{theorem}

\begin{proof}
证明过程...
\end{proof}
```

### 10.2 编号控制

```latex
% 不编号的公式
\begin{align*}
x &= y \\
z &= w
\end{align*}

% 手动编号
\begin{align}
x &= y \tag{1} \\
z &= w \nonumber
\end{align}
```

## 11. 实用示例

### 11.1 二次公式

```latex
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
```

### 11.2 泰勒级数

```latex
f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n + R_n(x)
```

### 11.3 欧拉公式

```latex
e^{i\theta} = \cos\theta + i\sin\theta
```

### 11.4 傅里叶变换

```latex
F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt
```

### 11.5 麦克斯韦方程组

```latex
\begin{align}
\nabla \cdot \mathbf{E} &= \frac{\rho}{\epsilon_0} \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu_0\mathbf{J} + \mu_0\epsilon_0\frac{\partial \mathbf{E}}{\partial t}
\end{align}
```

## 12. 调试和优化技巧

### 12.1 常见错误

- 忘记使用数学模式：`$x^2$` 而不是 `x^2`
- 括号不匹配：检查所有 `{` 和 `}` 是否配对
- 上下标超过一个字符时忘记使用花括号：`x^{10}` 而不是 `x^10`

### 12.2 提高可读性

- 使用适当的空格：`\,`, `\;`, `\quad`
- 合理使用换行和对齐
- 选择合适的数学字体

### 12.3 性能优化

- 避免过度嵌套的分数
- 使用适当的矩阵环境
- 合理分割长公式

这份指南涵盖了LaTeX数学排版的主要内容，可以作为参考手册使用。根据需要可以进一步扩展特定领域的数学符号和环境。
