+++
date = '2025-01-15T13:22:26+08:00'
draft = false
title = '简述 Rust 中的闭包'
tags = ["编程", "rust"]
toc = true
+++


# 为什么需要闭包？

```rust
// 问题1：函数复用
// 没有闭包时，需要传入所有参数
fn add(x: i32, base: i32) -> i32 { x + base }

// 有了闭包，可以部分应用
let base = 5;
let add_five = |x| x + base;

// 问题2：函数式编程需求
vec![1, 2, 3].iter().map(|x| x * 2);  // 更简洁
vec![1, 2, 3].iter().map(multiply);    // 需要单独定义函数

// 问题3：上下文捕获
// 没有闭包时很难处理
struct Context { value: i32 }
let ctx = Context { value: 42 };
let use_context = || println!("{}", ctx.value);
```

# 闭包是什么？
- 闭包是可以捕获其环境的匿名函数
- 它"封闭"了其定义时的环境，故称"闭包"
- 闭包 = 函数 + 环境

# 闭包的优势
```rust
// 1. 简洁的语法
let add = |a, b| a + b;  // vs fn add(a: i32, b: i32) -> i32

// 2. 灵活的环境捕获
let multiplier = 2;
let double = |x| x * multiplier;  // 捕获 multiplier

// 3. 支持函数式编程
let numbers: Vec<i32> = vec![1, 2, 3, 4, 5];
let even_numbers: Vec<i32> = numbers
    .into_iter()
    .filter(|x| x % 2 == 0)
    .collect();
```

# 理解闭包

我用 Python 和 TypeScript 的概念来解释 Rust 的闭包：

## Python 风格理解：
```python
# Python 的 lambda
lambda x: x + 1

# Python 的闭包
def outer(a):
    # 捕获外部变量 a
    def inner(x):
        return x + a
    return inner
```

```rust
# 对应的 Rust 代码
|x| x + 1

let a = 1;
let closure = |x| x + a;
```

## TypeScript 风格理解：

```typescript
// TypeScript 的箭头函数
const add = (x: number) => x + 1;

// 带类型标注的闭包
const multiply: (x: number) => number = (x) => x * 2;

// 对应的 Rust 代码
let add = |x: i32| x + 1;
let multiply: fn(i32) -> i32 = |x| x * 2;
```

## Rust 闭包的特殊之处：

```rust
// 1. Rust 闭包有三种类型
// FnOnce - 获取所有权
let owns = |x| takes_ownership(x);

// FnMut - 可变借用
let mut mutates = |x| mutates_value(x);

// Fn - 不可变借用
let reads = |x| reads_value(x);

// 2. 闭包会自动推断捕获方式
let mut val = 5;
let mut closure = || {
    val += 1;    // 自动推断需要可变借用
    println!("{}", val);
};
```

主要区别：
1. Rust 的闭包更关注内存安全和所有权
2. Python/TS 的闭包主要关注词法作用域
3. Rust 的闭包语法更简洁（使用 `||` 而不是 `()=>`）
4. Rust 的闭包有更严格的类型系统和借用规则

人们常说："如果你理解 JavaScript/TypeScript 的箭头函数，就很容易理解 Rust 的闭包语法；如果你理解 Python 的 lambda 和闭包概念，就很容易理解 Rust 闭包的用途。"

# 如何使用闭包

```rust
// 1. 基本语法
let closure = |params| body;

// 2. 带类型标注
let closure = |x: i32| -> i32 { x + 1 };

// 3. 作为函数参数
fn apply<F>(f: F, x: i32) where F: Fn(i32) -> i32 {
    println!("Result: {}", f(x));
}

// 4. 在迭代器中使用
let v = vec![1, 2, 3];
v.iter().map(|x| x * 2).collect::<Vec<_>>();
```

# 最佳实践

```rust
// 1. 选择合适的特征界定
// Fn - 不可变借用
fn call_closure<F>(closure: F) where F: Fn(i32) -> i32 {
    closure(1);
}

// FnMut - 可变借用
fn call_closure_mut<F>(mut closure: F) where F: FnMut(i32) -> i32 {
    closure(1);
}

// FnOnce - 获取所有权
fn call_closure_once<F>(closure: F) where F: FnOnce(i32) -> i32 {
    closure(1);
}

// 2. 避免过度捕获
let x = 1;
let y = 2;
// 好的做法
let closure = move |z| x + y + z;  // 明确使用 move
// 不好的做法
let closure = |z| x + y + z;  // 隐式捕获

// 3. 保持闭包简洁
// 好的做法
let is_even = |x| x % 2 == 0;

// 不好的做法 - 过于复杂
let complex = |x| {
    let mut result = x;
    for i in 0..10 {
        result += i;
    }
    result % 2 == 0
};

// 4. 适当的错误处理
// 好的做法
let safe_divide = |x, y| {
    if y == 0 {
        None
    } else {
        Some(x / y)
    }
};

// 5. 文档和类型标注
/// 计算一个数的平方
let square: fn(i32) -> i32 = |x| x * x;
```

# 常见用例

```rust
// 1. 回调函数
button.on_click(|| println!("Clicked!"));

// 2. 自定义排序
let mut vec = vec![1, 5, 2];
vec.sort_by(|a, b| b.cmp(a));  // 降序排序

// 3. 惰性计算
let expensive_closure = || {
    // 复杂计算
    compute_something_expensive()
};

// 4. 配置和构建模式
let config = Config::new()
    .with_timeout(|c| c.timeout(Duration::from_secs(5)))
    .with_retry(|c| c.max_retries(3));
```

掌握闭包可以让代码更简洁、更灵活，同时提高代码的可维护性和重用性。但要注意在使用时遵循最佳实践，以确保代码的清晰性和性能。
