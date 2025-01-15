+++
date = '2025-01-15T11:38:20+08:00'
draft = true
title = 'Rust 所有权'
toc = true
+++

让我用这个思维结构来解释 Rust 的所有权：

1. 产生疑问
```rust
let s1 = String::from("hello");
let s2 = s1;
println!("{}", s1); // 编译错误！为什么我不能用 s1 了？
```
- 为什么把值赋给另一个变量后，原变量就不能用了？
- 为什么基本类型（如 i32）赋值后还能继续使用，但 String 不行？
- 为什么要设计这么奇怪的规则？

2. 理解
```rust
// 深入内存模型
let s1 = String::from("hello");
// s1 在栈上存储：ptr -> 指向堆上的内容
//              len -> 5
//              capacity -> 5
// 堆上存储: h e l l o

let s2 = s1;
// 发生了所有权转移（move）
// s2 获得了对堆内存的所有权
// s1 被废弃，防止双重释放问题
```

3. 思考
- 内存安全问题：
  - 如果两个变量同时拥有堆内存的所有权，谁负责释放？
  - 如果重复释放会怎样？
  - 如果忘记释放会怎样？

- 系统设计权衡：
  ```rust
  // 选择 1: 深拷贝（像 Python）
  let s2 = s1.clone(); // 性能开销大

  // 选择 2: 引用计数（像 Python 的内部实现）
  use std::rc::Rc;
  let s2 = Rc::clone(&s1); // 运行时开销

  // 选择 3: 所有权系统（Rust 的选择）
  let s2 = s1; // 零开销抽象
  ```

4. 试错
```rust
// 尝试 1：直接使用
let s1 = String::from("hello");
let s2 = s1;
println!("{}", s1); // 错误：s1已被移动

// 尝试 2：使用引用
let s1 = String::from("hello");
let s2 = &s1;
println!("{}", s1); // 成功！

// 尝试 3：克隆
let s1 = String::from("hello");
let s2 = s1.clone();
println!("{}", s1); // 成功！

// 尝试 4：理解作用域
{
    let s1 = String::from("hello");
    let s2 = s1;
} // s2 离开作用域，内存被释放
```

5. 结论

主要规则：
```rust
// 1. 每个值只能有一个所有者
let s1 = String::from("hello");
let s2 = s1;  // s1 的所有权移动到 s2

// 2. 引用（借用）不转移所有权
let s1 = String::from("hello");
let s2 = &s1;  // s2 借用 s1

// 3. 作用域结束时自动释放
{
    let s = String::from("hello");
} // s 被释放

// 4. Copy 类型例外（栈上的值）
let x = 5;
let y = x; // x 仍然可用，因为 i32 是 Copy 类型
```

最佳实践：
```rust
// 1. 优先使用引用，除非需要所有权
fn process(s: &String) { /* ... */ }

// 2. 需要修改时使用可变引用
fn modify(s: &mut String) { /* ... */ }

// 3. 只在必要时使用 clone()
let s2 = s1.clone(); // 当真的需要副本时

// 4. 理解并利用 RAII
struct MyResource { /* ... */ }
impl Drop for MyResource {
    fn drop(&mut self) {
        // 清理代码
    }
}
```

这个系统虽然初看很严格，但它实现了：
- 零成本抽象的内存安全
- 无需垃圾回收的自动内存管理
- 并发安全的保证
- 高效的资源管理

这就是为什么 Rust 能在保证内存安全的同时达到接近 C++ 的性能。
