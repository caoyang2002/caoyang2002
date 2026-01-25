+++
date = '2025-01-15T11:48:53+08:00'
draft = false
title = 'Rust 函数式编程'
tags = ["编程", "rust"]
toc = true
+++

让我用这种方式来讲解 Rust 的函数式编程概念：

# 引入问题

想象这样一个场景：你需要处理一个电商系统的订单数据。要求：
1. 过滤出金额大于 100 的订单
2. 计算这些订单的总金额
3. 给每个订单加上 10% 的折扣

传统的命令式编程可能是这样：
```rust
let mut total = 0;
for order in orders {
    if order.amount > 100 {
        total += order.amount * 0.9;
    }
}
```

这段代码有什么问题？
- 可读性不高：逻辑分散在循环中
- 难以修改：如果要改变处理逻辑，需要修改循环内部
- 难以复用：这段逻辑很难在其他地方重用
- 易出错：可变状态(total)增加了出错风险

# 问题模型

我们需要一种方式能够：
1. 将数据转换表达为清晰的步骤
2. 避免可变状态
3. 提高代码复用性
4. 增强代码可读性

这就引出了函数式编程的核心概念：**将计算表达为数据转换的管道**。

# 不同的解决方案

## 方案1：传统命令式
```rust
// 命令式方式
let mut filtered_orders = Vec::new();
for order in orders {
    if order.amount > 100 {
        filtered_orders.push(order);
    }
}

let mut discounted_orders = Vec::new();
for order in filtered_orders {
    discounted_orders.push(order.amount * 0.9);
}

let mut total = 0;
for amount in discounted_orders {
    total += amount;
}
```
优点：
- 直观，容易理解
- 控制流清晰

缺点：
- 代码冗长
- 大量可变状态
- 难以复用

## 方案2：函数式方案
```rust
let total = orders
    .iter()
    .filter(|order| order.amount > 100)
    .map(|order| order.amount * 0.9)
    .sum();
```
优点：
- 代码简洁
- 无可变状态
- 易于理解和修改
- 每个步骤都可复用

缺点：
- 需要学习新的概念
- 对性能有轻微影响

# 核心概念解析

1. Iterator（迭代器）：
```rust
// 创建迭代器
let numbers = vec![1, 2, 3];
let iter = numbers.iter();

// 迭代器转换
let doubled: Vec<i32> = iter.map(|x| x * 2).collect();
```

2. 高阶函数：
```rust
// map: 转换每个元素
let squares: Vec<i32> = vec![1, 2, 3].iter()
    .map(|x| x * x)
    .collect();

// filter: 过滤元素
let evens: Vec<i32> = vec![1, 2, 3, 4].iter()
    .filter(|x| *x % 2 == 0)
    .collect();

// fold: 累积操作
let sum = vec![1, 2, 3].iter()
    .fold(0, |acc, x| acc + x);
```

3. 闭包：
```rust
let multiplier = 2;
let double = |x| x * multiplier;  // 捕获外部变量
```

# 最佳实践

1. 使用链式调用提高可读性：
```rust
// 好的实践
let result = data
    .iter()
    .filter(|x| x.is_valid())
    .map(|x| x.process())
    .collect();

// 避免
let filtered = data.iter().filter(|x| x.is_valid());
let processed = filtered.map(|x| x.process());
let result = processed.collect();
```

2. 适当使用类型标注：
```rust
let numbers: Vec<i32> = vec![1, 2, 3]
    .iter()
    .map(|x| x * 2)
    .collect();
```

3. 使用合适的组合子：
```rust
// 使用 find 代替 filter().next()
let first_even = numbers.iter().find(|x| *x % 2 == 0);

// 使用 any 代替 filter().count() > 0
let has_even = numbers.iter().any(|x| *x % 2 == 0);
```

4. 注意性能：
```rust
// 好的实践：及早过滤
let result = data
    .iter()
    .filter(|x| x.is_valid())  // 先过滤
    .map(expensive_operation)   // 再处理
    .collect();

// 避免：不必要的中间集合
let temp: Vec<_> = data.iter().map(expensive_operation).collect();
let result: Vec<_> = temp.iter().filter(|x| x.is_valid()).collect();
```

# 方法论总结

1. 思考管道：
   - 将复杂操作分解为简单的转换步骤
   - 每个步骤都应该是单一职责

2. 保持不可变性：
   - 优先使用不可变数据结构
   - 通过转换而不是修改来改变数据

3. 组合优于继承：
   - 使用小的、可组合的函数
   - 通过组合创建复杂行为

4. 类型驱动开发：
   - 让编译器帮助你保证代码正确性
   - 使用强类型系统来表达意图

通过这种函数式的思维方式，我们能够写出更加清晰、可维护、可靠的代码。这不仅仅是一种编程范式，更是一种解决问题的思维方式。
