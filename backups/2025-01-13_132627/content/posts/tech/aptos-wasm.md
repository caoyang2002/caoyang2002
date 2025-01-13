+++
date = '2025-01-05T11:08:24+08:00'
draft = true
title = 'Aptos Wasm 开发笔记'
toc = true
+++

# 起因

最近有一个项目需要使用到 Apots 的 Move 开发环境，但是官方并没有提供 Move-2 的Wasm，处于对技术的“狂热”，决定自己学一下这个技术。

对于我来说，可以了解到 Rust 和 Move 的编译原理，这是一个很好的机会，虽然我从来没正式写过 Rust 和 Move。

# 开始

我看不懂 `aptos-core` 从的功能，所以一开始就尝试编译这整个项目，不巧的是，这个项目编译所需磁盘空间高达 20G，我只好更深入地分析这个项目，在 `aptos-core/third_party` 我看到了 `move` 编译器相关的东西，所以我就从这里开始。

把目录结构扔给 `claude` 后，解析出来的正是 `move` 编译器的实现，根据 `move/move-compiler/README.md` 的描述，可以发现有两个二进制文件 `move-check` 和 `move-build` 所以，我通过 `cargo build -p move-compiler` 命令进行编译，在 `aptos-core/target/debug` 中找到了这两个编译的二进制文件。

在 `debug` 目录下，写一个简单的 move 代码测试是否可以直接运行：

`test.move`
```move
module 0x42::test {
    use 0x42::aptos;
}

```

运行 `./move-build --flavor dev --compiler_v2 test.move` （`--flavor` 是一个必要的参数，但是我并不清楚为什么需要这个参数）

到目前为止，我只需要把 这个程序分离出来，能够读取文件就可以了


## 1月 12 号

发现 build 二进制无法解析 `Move.toml` 文件，在源代码中添加了 `println`，尝试通过调试的方式，理解编译过程。在 move-build.rs 中添加输出后，始终无法输出内容，猜测有其他的前置工具。

在 `tools` 中有一份 README，提到 `move-cli` 的命令，所以猜测 `move-cli` 是一个完备的 move 工具，在 `move-cli` 下运行：

```bash
cargo build
```

在 `target/` 中找到 `move` 二进制文件，运行 `./move` 会输出这个二进制的使用方式。

在当前目录创建一个 move 包

```bash
./move new demo
```

成功创建了 demo 目录，并且包含了 `Move.toml` 和 `sources` 目录，写一个 move 测试代码


`sources/main.move`
```move
module 0x42::test{

}
```

在 demo 目录下 运行 `./move build` 成功编译，并生成了 `build` 目录。现在可以确定，只要把 mvoe-cli 打包成 wasm 就可以了。

## wasm 基础

回忆一下 wasm 的开发过程，先是使用 `extern crate wasm_bindgen;` 和 `use wasm_bindgen::prelude::*;` 导入了 `wasm_bindgen` 库，

外部函数声明，即这个函数的实现在其他地方

```bash
extern "C" {
    fn alert(s: &str);
}
```

这段代码实际上是在告诉 Rust 编译器：

"有一个名为 alert 的外部函数，它接受一个字符串引用作为参数。这个函数的实现不在这里，它在别处（在这个场景中，是在 JavaScript 的 window.alert 中）。"

目前已经了解了 wasm 的实现

使用命令 `wasm-pack build --target web` 打包 wasm 并生成 ts 包装。


在 `move-cli/lib.rs` 中有 `run_cli()`，这是命令行的首次调用的方式，注意到下方这段代码，这能直接匹配命令行的参数：

```rust
match cmd {
    Command::Build(c) => c.execute(move_args.package_path, move_args.build_config),
    Command::Coverage(c) => c.execute(move_args.package_path, move_args.build_config),
    Command::Disassemble(c) => c.execute(move_args.package_path, move_args.build_config),
    Command::Docgen(c) => c.execute(move_args.package_path, move_args.build_config),
    Command::Errmap(c) => c.execute(move_args.package_path, move_args.build_config),
    Command::New(c) => c.execute_with_defaults(move_args.package_path),
    Command::Prove(c) => c.execute(move_args.package_path, move_args.build_config),
    Command::Test(c) => c.execute(
        move_args.package_path,
        move_args.build_config,
        natives,
        genesis,
        Some(cost_table.clone()),
    ),
}

```
`Command::Build(c)` 是模式匹配的一部分：

`Command` 是一个枚举（enum）
Build 是枚举的一个变体（variant）
`(c)` 表示从这个变体中解构出一个值，并将它绑定到变量 `c`

`=>` 是匹配臂（match arm）的语法，表示"如果匹配成功，就执行后面的代码"
`c.execute(...)` 是匹配成功后执行的代码：

`c` 是从 Build 变体中解构出来的值
`execute` 是对这个值调用的方法
括号中是传递给 execute 的参数

编译：

```bash
../move test --compiler-version=2 --language-version=1
```
