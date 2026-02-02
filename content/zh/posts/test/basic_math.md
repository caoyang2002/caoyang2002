+++
title = 'MATLAB 简明教程'
date = 2026-02-02T16:39:29+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
cover = "https://www.wikihow.com/images/3/3f/Make-3D-Plots-Using-MATLAB-Step-10.jpg"
+++

**官方资源**：
- [MATLAB官方文档](https://ww2.mathworks.cn/help/matlab/index.html)
- [MATLAB示例库](https://ww2.mathworks.cn/help/matlab/examples.html)
- [MATLAB论坛](https://ww2.mathworks.cn/matlabcentral/)

# MATLAB 简明教程

## 目录
1. [MATLAB 简介](#简介)
2. [基础语法与操作](#基础语法)
3. [矩阵与数组操作](#矩阵操作)
4. [控制流与函数](#控制流)
5. [数据可视化](#数据可视化)
6. [文件操作](#文件操作)
7. [实用技巧](#实用技巧)

## 1. MATLAB 简介 <a name="简介"></a>

MATLAB（Matrix Laboratory）是一种用于数值计算、可视化和编程的高级语言和交互式环境。

### 1.1 MATLAB 环境
```matlab
% 查看当前工作目录
pwd

% 列出当前目录下的文件
dir  % 或 ls

% 改变工作目录
cd 'C:\Users\YourName\Documents'

% 清理命令窗口
clc

% 清理工作空间变量
clear

% 关闭所有图形窗口
close all
```

### 1.2 获取帮助
```matlab
% 查看函数帮助
help function_name

% 详细文档
doc function_name

% 查找相关函数
lookfor keyword
```

## 2. 基础语法与操作 <a name="基础语法"></a>

### 2.1 变量与数据类型
```matlab
% 基本变量赋值
a = 10;                % 标量
b = 3.14159;           % 浮点数
c = 'Hello MATLAB';    % 字符串
d = true;              % 逻辑值

% 查看变量信息
whos                    % 显示所有变量信息
class(a)                % 查看变量类型

% 特殊变量
pi                      % 圆周率 π
eps                     % 机器精度
inf                     % 无穷大
NaN                     % 非数字
i 或 j                  % 虚数单位

% 清除特定变量
clear a b
```

### 2.2 基本运算
```matlab
% 算术运算
x = 10 + 5;      % 加法
y = 10 - 5;      % 减法
z = 10 * 5;      % 乘法
w = 10 / 5;      % 除法
v = 10 ^ 2;      % 幂运算
u = mod(10, 3);  % 取模运算

% 关系运算
a == b           % 等于
a ~= b           % 不等于
a > b            % 大于
a < b            % 小于
a >= b           % 大于等于
a <= b           % 小于等于

% 逻辑运算
~a               % 非
a & b            % 与
a | b            % 或
xor(a, b)        % 异或
```

## 3. 矩阵与数组操作 <a name="矩阵操作"></a>

### 3.1 创建矩阵
```matlab
% 直接创建
A = [1 2 3; 4 5 6; 7 8 9]      % 3×3矩阵

% 特殊矩阵
zeros(3, 4)                     % 3×4零矩阵
ones(2, 3)                      % 2×3全1矩阵
eye(4)                          % 4×4单位矩阵
rand(3, 3)                      % 3×3随机矩阵（0-1）
randn(2, 2)                     % 2×2正态分布随机矩阵
magic(3)                        % 3阶魔方阵

% 序列生成
1:5                             % [1 2 3 4 5]
1:0.5:3                         % [1 1.5 2 2.5 3]
linspace(0, 10, 5)              % [0 2.5 5 7.5 10]
logspace(0, 2, 5)               % 对数间隔序列
```

### 3.2 矩阵操作
```matlab
A = [1 2 3; 4 5 6; 7 8 9];

% 索引与切片
A(2, 3)                         % 第2行第3列元素
A(2, :)                         % 第2行所有元素
A(:, 3)                         % 第3列所有元素
A(1:2, 2:3)                     % 子矩阵
A(end, :)                       % 最后一行
A(:)                            % 展开为列向量

% 矩阵运算
A + B                           % 矩阵加法
A - B                           % 矩阵减法
A * B                           % 矩阵乘法
A .* B                          % 逐元素乘法
A / B                           % 矩阵右除
A \ B                           % 矩阵左除
A'                              % 转置
inv(A)                          % 逆矩阵
det(A)                          % 行列式
eig(A)                          % 特征值
```

### 3.3 数组函数
```matlab
A = [1 4 3; 2 5 6];

% 统计函数
max(A)                          % 每列最大值
min(A)                          % 每列最小值
mean(A)                         % 每列平均值
median(A)                       % 每列中位数
std(A)                          % 标准差
sum(A)                          % 每列求和
prod(A)                         % 每列乘积

% 排序
sort(A)                         % 每列升序排序
sort(A, 'descend')              % 降序排序
sortrows(A, 1)                  % 按第1列排序行

% 形状操作
size(A)                         % 矩阵大小
length(A)                       % 最大维度长度
numel(A)                        % 元素总数
reshape(A, 3, 2)                % 改变形状
repmat(A, 2, 3)                 % 重复矩阵
```

## 4. 控制流与函数 <a name="控制流"></a>

### 4.1 条件语句
```matlab
% if-elseif-else
x = 10;
if x > 0
    disp('正数');
elseif x < 0
    disp('负数');
else
    disp('零');
end

% switch-case
day = 3;
switch day
    case 1
        disp('星期一');
    case 2
        disp('星期二');
    otherwise
        disp('其他日子');
end
```

### 4.2 循环
```matlab
% for 循环
for i = 1:5
    fprintf('i = %d\n', i);
end

% while 循环
n = 1;
while n <= 5
    fprintf('n = %d\n', n);
    n = n + 1;
end

% 提前退出循环
for i = 1:10
    if i == 5
        break;      % 退出循环
    end
    if mod(i, 2) == 0
        continue;   % 跳过本次迭代
    end
    fprintf('%d ', i);
end
```

### 4.3 函数
```matlab
% 创建函数文件 myfunction.m
function [output1, output2] = myfunction(input1, input2)
    % 函数说明
    % 输入: input1, input2
    % 输出: output1, output2
    
    output1 = input1 + input2;
    output2 = input1 * input2;
end

% 匿名函数
f = @(x) x^2 + 2*x + 1;
result = f(3);  % 计算 f(3)

% 函数句柄
g = @sin;
y = g(pi/2);    % 计算 sin(π/2)
```

## 5. 数据可视化 <a name="数据可视化"></a>

### 5.1 基本绘图
```matlab
% 线图
x = 0:0.1:2*pi;
y = sin(x);
plot(x, y);
title('正弦函数');
xlabel('x');
ylabel('sin(x)');
grid on;
legend('sin(x)');

% 多条曲线
y1 = sin(x);
y2 = cos(x);
plot(x, y1, 'r-', x, y2, 'b--');
legend('sin(x)', 'cos(x)');

% 子图
subplot(2, 2, 1); plot(x, sin(x));
subplot(2, 2, 2); plot(x, cos(x));
subplot(2, 2, 3); plot(x, tan(x));
subplot(2, 2, 4); plot(x, exp(-x));
```

### 5.2 其他图形
```matlab
% 散点图
x = randn(100, 1);
y = randn(100, 1);
scatter(x, y);
title('随机散点图');

% 柱状图
data = [10, 20, 15, 25, 30];
bar(data);
title('柱状图示例');

% 直方图
data = randn(1000, 1);
histogram(data, 20);
title('正态分布直方图');

% 3D图形
[X, Y] = meshgrid(-2:0.1:2, -2:0.1:2);
Z = X .* exp(-X.^2 - Y.^2);
surf(X, Y, Z);
title('3D曲面图');
xlabel('X'); ylabel('Y'); zlabel('Z');
```

### 5.3 图形属性设置
```matlab
x = 0:0.1:10;
y = sin(x);

% 线型和颜色
plot(x, y, 'r--', 'LineWidth', 2, 'Marker', 'o');

% 设置坐标轴
xlim([0, 10]);
ylim([-1.5, 1.5]);
axis equal;          % 等比例坐标轴
axis tight;          % 紧致坐标轴

% 添加文本
text(5, 0, '零点', 'FontSize', 12);

% 保存图形
saveas(gcf, 'myplot.png');
print(gcf, '-dpdf', 'myplot.pdf');
```

## 6. 文件操作 <a name="文件操作"></a>

### 6.1 读写文本文件
```matlab
% 写入文本文件
data = [1 2 3; 4 5 6; 7 8 9];
dlmwrite('data.txt', data, 'delimiter', '\t');

% 读取文本文件
loaded_data = dlmread('data.txt');

% 写入CSV
csvwrite('data.csv', data);

% 读取CSV
csv_data = csvread('data.csv');
```

### 6.2 Excel文件操作
```matlab
% 读取Excel文件
[num, txt, raw] = xlsread('data.xlsx');

% 写入Excel文件
data = {'Name', 'Age', 'Score'; 'Alice', 25, 85; 'Bob', 30, 90};
xlswrite('output.xlsx', data);
```

### 6.3 MAT文件操作
```matlab
% 保存变量到MAT文件
save('mydata.mat', 'A', 'B', 'C');
save('alldata.mat');            % 保存所有变量

% 加载MAT文件
load('mydata.mat');

% 保存为ASCII格式
save('data.txt', 'A', '-ascii');
```

### 6.4 文件管理
```matlab
% 检查文件是否存在
exist('filename.txt', 'file')

% 获取文件信息
info = dir('*.m');

% 复制文件
copyfile('source.txt', 'destination.txt');

% 删除文件
delete('filename.txt');

% 创建目录
mkdir('newfolder');
```

## 7. 实用技巧 <a name="实用技巧"></a>

### 7.1 调试技巧
```matlab
% 设置断点
dbstop if error               % 出错时暂停
dbstop in function_name at line_number

% 调试命令
dbstep                        % 单步执行
dbcont                        % 继续执行
dbquit                        % 退出调试模式

% 显示变量值
disp(variable_name)
fprintf('变量值: %f\n', variable)

% 测量执行时间
tic
% 执行代码
toc
```

### 7.2 性能优化
```matlab
% 预分配数组
n = 10000;
A = zeros(n, n);  % 预分配内存

% 向量化操作（避免循环）
% 慢的方式
for i = 1:n
    B(i) = A(i)^2;
end

% 快的方式
B = A.^2;

% 使用逻辑索引
idx = A > 0;
B = A(idx);

% 稀疏矩阵
S = sparse(A);    % 转换为稀疏矩阵
```

### 7.3 常用工具箱函数
```matlab
% 符号计算
syms x y
f = x^2 + y^2;
diff(f, x)        % 对x求导
int(f, x)         % 对x积分

% 图像处理
img = imread('image.jpg');
imshow(img);
gray_img = rgb2gray(img);

% 信号处理
fs = 1000;         % 采样频率
t = 0:1/fs:1;
signal = sin(2*pi*50*t);
spectrum = fft(signal);

% 优化求解
f = @(x) x^2 + 2*x + 1;
x0 = 0;
x_opt = fminsearch(f, x0);
```

### 7.4 实用小技巧
```matlab
% 获取当前时间
datetime('now')
date

% 暂停执行
pause(2)           % 暂停2秒

% 声音提示
beep

% 错误处理
try
    % 可能出错的代码
catch ME
    disp(['错误: ' ME.message]);
end

% 格式化输出
fprintf('π = %.4f\n', pi);
fprintf('结果: %d, 时间: %s\n', result, datestr(now));
```
