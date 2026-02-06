+++
title = '最小二乘法'
date = 2026-02-05T23:09:33+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
+++

 我来帮你详细解读这份关于**最小二乘法（Least Squares）**的教材内容。这是机器学习/统计学习中最基础、最重要的方法之一。

---

## 一、本章核心内容概述

本章讲的是**回归分析**中最基础的方法——**最小二乘法（Least Squares, LS）**。

### 1.1 问题设定

- **输入**：d维实数向量 $x$（自变量/特征）
- **输出**：实数值 $y$（因变量/目标值）
- **目标**：学习一个函数 $f_\theta(x)$ 来逼近真实的未知函数 $f$
- **数据**：训练样本 $\{(x_i, y_i)\}_{i=1}^n$，但 $y_i$ 包含噪声（观测误差）

---

## 二、最小二乘学习法（3.1节）

### 2.1 核心思想

**最小化平方误差**：找到参数 $\theta$，使得模型预测值与真实值之间的**平方误差之和最小**。

### 2.2 数学公式

**目标函数（损失函数）**：
$$J_{LS}(\theta) = \frac{1}{2}\sum_{i=1}^{n}\left(f_\theta(x_i) - y_i\right)^2$$

> 注：加上系数 $1/2$ 是为了求导时消去2，简化计算。

**最优解**：
$$\hat{\theta}_{LS} = \arg\min_\theta J_{LS}(\theta)$$

### 2.3 线性模型的情况

当使用**线性模型**时：
$$f_\theta(x) = \sum_{j=1}^{b}\theta_j\phi_j(x) = \theta^T\phi(x)$$

其中 $\phi_j(x)$ 是**基函数**（basis functions），比如多项式、三角函数等。

**矩阵形式**：
$$J_{LS}(\theta) = \frac{1}{2}\|\Phi\theta - y\|^2$$

其中：
- $y = (y_1, \ldots, y_n)^T$ 是 $n$ 维输出向量
- $\Phi$ 是 **$n \times b$ 设计矩阵（Design Matrix）**：

$$\Phi = \begin{pmatrix} 
\phi_1(x_1) & \cdots & \phi_b(x_1) \\
\vdots & \ddots & \vdots \\
\phi_1(x_n) & \cdots & \phi_b(x_n)
\end{pmatrix}$$

### 2.4 解析解的推导

**求梯度并令其为0**：
$$\nabla_\theta J_{LS} = \Phi^T(\Phi\theta - y) = 0$$

**得到正规方程**：
$$\Phi^T\Phi\theta = \Phi^Ty$$

**最小二乘解**：
$$\hat{\theta}_{LS} = \Phi^\dagger y$$

其中 $\Phi^\dagger$ 是 $\Phi$ 的**广义逆矩阵（Moore-Penrose伪逆）**。

当 $\Phi^T\Phi$ 可逆时：
$$\Phi^\dagger = (\Phi^T\Phi)^{-1}\Phi^T$$

---

## 三、实际例子（图3.1和图3.2）

### 3.1 例子说明

使用**三角多项式基函数**拟合复杂非线性函数：
$$\phi(x) = (1, \sin\frac{x}{2}, \cos\frac{x}{2}, \sin x, \cos x, \ldots, \sin\frac{15x}{2}, \cos\frac{15x}{2})$$

**数据生成**：
$$y = \frac{\sin(\pi x)}{\pi x} + 0.1x + 0.05 \times \text{噪声}$$

### 3.2 MATLAB代码解读（图3.2）

```matlab
n=50; N=1000; 
x=linspace(-3,3,n)';      % 50个训练点
X=linspace(-3,3,N)';      % 1000个测试点

% 生成训练数据（含噪声）
pix=pi*x; 
y=sin(pix)./(pix)+0.1*x+0.05*randn(n,1);

% 构建设计矩阵（训练集）
p(:,1)=ones(n,1);         % 常数项
for j=1:15
    p(:,2*j)=sin(j/2*x);   % sin项
    p(:,2*j+1)=cos(j/2*x); % cos项
end

% 构建设计矩阵（测试集）
P(:,1)=ones(N,1);
for j=1:15
    P(:,2*j)=sin(j/2*X);
    P(:,2*j+1)=cos(j/2*X);
end

% 最小二乘求解：t = (P'P)^{-1}P'y
t=p\y;                    % MATLAB中反斜杠直接求解

% 预测
F=P*t;

% 绘图
figure(1); clf; hold on; 
axis([-2.8 2.8 -0.5 1.2]);
plot(X,F,'g-');           % 绿色：拟合曲线
plot(x,y,'bo');           % 蓝色圆圈：训练数据
```

> **关键**：`t=p\y` 是MATLAB的高效解法，直接求解 $\Phi^T\Phi\theta = \Phi^Ty$，避免显式计算逆矩阵。

---

## 四、加权最小二乘法

对不同的训练样本赋予不同的权重 $w_i$：

$$\min_\theta \frac{1}{2}\sum_{i=1}^{n}w_i\left(f_\theta(x_i) - y_i\right)^2$$

**矩阵形式**：
$$\hat{\theta} = (\Phi^TW\Phi)^{-1}\Phi^TWy$$

其中 $W = \text{diag}(w_1, \ldots, w_n)$ 是对角权重矩阵。

**应用场景**：
- 某些样本更可靠（权重更大）
- 处理异方差性（不同样本噪声水平不同）

---

## 五、核模型（3.2节）

### 5.1 核模型形式

$$f_\theta(x) = \sum_{i=1}^{n}\theta_i K(x, x_i)$$

其中 $K(x, x')$ 是**核函数**（如高斯核）。

### 5.2 与线性模型的关系

核模型也是线性模型的一种，只需将设计矩阵 $\Phi$ 替换为**核矩阵 $K$**：

$$K = \begin{pmatrix} 
K(x_1,x_1) & \cdots & K(x_1,x_n) \\
\vdots & \ddots & \vdots \\
K(x_n,x_1) & \cdots & K(x_n,x_n)
\end{pmatrix}$$

然后同样用最小二乘法求解。

---

## 六、最小二乘解的性质（3.2节）

### 6.1 奇异值分解（SVD）

对设计矩阵进行SVD分解：
$$\Phi = \sum_{k=1}^{\min(n,b)}\kappa_k \psi_k \varphi_k^T$$

其中：
- $\kappa_k$：奇异值（非负）
- $\psi_k$：左奇异向量
- $\varphi_k$：右奇异向量

满足正交性：$\psi_i^T\psi_j = \varphi_i^T\varphi_j = \delta_{ij}$

### 6.2 广义逆的SVD表示

$$\Phi^\dagger = \sum_{k=1}^{\min(n,b)}\kappa_k^\dagger \varphi_k \psi_k^T$$

其中：
$$\kappa_k^\dagger = \begin{cases} 1/\kappa_k & (\kappa_k > 0) \\ 0 & (\kappa_k = 0) \end{cases}$$

### 6.3 最小二乘解的SVD形式

$$\hat{\theta}_{LS} = \sum_{k=1}^{\min(n,b)}\kappa_k^\dagger (\psi_k^T y)\varphi_k$$

### 6.4 几何解释（重要！）

**训练输出的预测值**：
$$\hat{y} = \Phi\hat{\theta}_{LS} = \Phi\Phi^\dagger y = \Pi_\Phi y$$

其中 $\Pi_\Phi = \Phi\Phi^\dagger$ 是到 $\Phi$ 的**列空间（值域 $R(\Phi)$）的正交投影矩阵**。

**关键理解**（图3.3）：
- 真实函数输出 $\Phi\theta^*$ 一定在 $R(\Phi)$ 中
- 观测值 $y$ 由于噪声偏离了 $R(\Phi)$
- 最小二乘法将 $y$ **正交投影**到 $R(\Phi)$，从而**去除噪声成分**

### 6.5 统计性质

1. **无偏性**：若噪声期望为0，则 $E[\hat{\theta}_{LS}] = \theta^*$
2. **渐近无偏性**：即使模型不包含真实函数，增加样本数也会收敛到最优近似

---

## 七、大规模数据的学习算法（3.3节）

当 $n$ 或 $b$ 很大时，矩阵求逆内存不足，使用**随机梯度下降法（SGD）**。

### 7.1 梯度下降原理

**参数更新规则**：
$$\theta \leftarrow \theta - \varepsilon \nabla J_i(\theta)$$

其中：
- $\varepsilon$：学习率（步长）
- $\nabla J_i(\theta) = \phi(x_i)(f_\theta(x_i) - y_i)$：第 $i$ 个样本的梯度

### 7.2 算法流程（图3.6）

```
1. 初始化参数 θ
2. 随机选择一个训练样本 (x_i, y_i)
3. 计算梯度并更新：θ ← θ - ε·∇J_i(θ)
4. 重复2-3直到收敛
```

### 7.3 为什么有效？

- **凸函数**：$J_{LS}(\theta)$ 是凸函数（只有一个全局最小值）
- **随机性**：每次用一个样本近似整体梯度，计算快，能逃离局部最优

### 7.4 高斯核模型的SGD实例（图3.7-3.8）

**高斯核**：
$$K(x,c) = \exp\left(-\frac{\|x-c\|^2}{2h^2}\right)$$

**MATLAB代码关键部分**（图3.8）：

```matlab
hh=2*0.3^2;           % 带宽 h=0.3
t0=randn(n,1);        % 随机初始化
e=0.1;                % 学习率

for o=1:n*10          % 最多迭代10轮
    i=ceil(rand*n);   % 随机选样本
    % 计算核向量
    ki=exp(-(x-x(i)).^2/hh);  
    % SGD更新
    t=t0-e*ki*(ki'*t0-y(i));
    
    % 收敛判断
    if norm(t-t0)<0.000001, break, end
    t0=t;
end
```

**观察结果**：
- 50次迭代：初步形状
- 200次迭代：基本近似
- 11556次迭代：完全收敛

**调参技巧**：
- 学习率 $\varepsilon$：先大后小（学习率衰减）
- 收敛阈值：影响精度和计算时间

---

## 八、本章知识图谱

```
最小二乘法
├── 基本形式：min ||Φθ - y||²
├── 解析解：θ = Φ†y = (ΦᵀΦ)⁻¹Φᵀy
├── 加权形式：min ||W^(1/2)(Φθ - y)||²
├── 核方法：将Φ替换为核矩阵K
├── 理论性质
│   ├── SVD分解理解
│   ├── 几何解释（正交投影去噪）
│   └── 统计性质（无偏性）
└── 大规模算法
    └── 随机梯度下降（SGD）
```

---

## 九、关键公式总结

| 概念 | 公式 |
|-----|------|
| 目标函数 | $J_{LS} = \frac{1}{2}\sum_{i=1}^n(f_\theta(x_i)-y_i)^2$ |
| 正规方程 | $\Phi^T\Phi\theta = \Phi^Ty$ |
| 最小二乘解 | $\hat{\theta}_{LS} = (\Phi^T\Phi)^{-1}\Phi^Ty$ |
| SGD更新 | $\theta \leftarrow \theta - \varepsilon \phi(x_i)(f_\theta(x_i)-y_i)$ |
| 预测投影 | $\hat{y} = \Pi_\Phi y$ |

---

## 十、学习建议

1. **动手实现**：用Python（numpy/sklearn）复现图3.2和图3.8的例子
2. **可视化**：观察不同基函数数量、不同学习率对拟合效果的影响
3. **对比实验**：比较解析解和SGD解的差异
4. **深入理解**：SVD分解是理解正则化、降维的基础，务必掌握

最小二乘法是机器学习最基础的"工具"，几乎所有高级方法（岭回归、LASSO、核方法、神经网络）都是在此基础上发展而来的！
