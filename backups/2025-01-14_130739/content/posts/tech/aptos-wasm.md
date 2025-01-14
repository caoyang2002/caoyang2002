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

在使用了其他的 move 库的情况下，会编译失败，找不到 native，目前我不清楚原因，只好另寻出路。

在 `aptos-core/cargo.toml` 中有这样一行代码：

```toml
default-members = [
    ...
    "crates/aptos",
    ...
]
```

有限的 rust 编程经验告诉我，`crates` 是 rust 的程序，为了确认它是不是一个二进制程序，需要看有没有 `cates/aptos/main.rs`。（其实可以看 README）

toml 中也有特征：

1. 从 package 描述可以看出:
```toml
name = "aptos"
description = "Aptos tool for management of nodes and interacting with the blockchain"
```
这明确说明了这是一个工具(tool),也就是二进制程序。

2. 依赖关系显示这是一个完整的命令行工具:
- 使用了 clap (命令行参数解析库)
- 包含了 clap_complete (命令行补全功能)
- 依赖了大量的功能模块,如节点管理、区块链交互等

3. 需要特定的内存分配器,这通常用于可执行程序而不是库。
```toml
[target.'cfg(unix)'.dependencies]
jemallocator = { workspace = true }
```


4. shadow-rs 通常用于在编译时注入版本信息等。
```toml
[build-dependencies]
shadow-rs = { workspace = true }
```

我尝试从 `crates/aptos` 进行编译，运行 `cargo build`。编译时间很长，但是终究是编译出了二进制文件 `aptos`

在 `target/debug` 下，运行编译的二进制文件 `./aptos move init --name test` 初始化 move 项目，然后创建 move 项目，并运行 `./aptos move test` 可以将 move 代码编译成功。

检查源码 `src/lib.rs`，这里只追踪了 `move test` 命令

```rust
pub mod move_tool; // MoveTool 的定义应该在 move_tool.rs 文件或者 move_tool/mod.rs 文件中。

pub enum Tool {
    ...
    #[clap(subcommand)]
    Move(move_tool::MoveTool), // 这是 move 命令的直接依赖
    ...
}
```

继续找

```rust
...
#[derive(Subcommand)]
pub enum MoveTool {
    ...
    Test(TestPackage), // test 命令
    ...
}
impl MoveTool {
    pub async fn execute(self) -> CliResult { // 返回 CliResult 类型
        match self {
            ...
            MoveTool::Test(tool) => tool.execute_serialized().await, // test 命令的实现
            ...
        }
    }
}
...
```

查找 `execute_serialized` 的定义，在 `lib.rs` 中有：

```rust
use crate::common::{
    types::{CliCommand, CliResult, CliTypedResult}, // 推断是在 common 中
    ...
};
```

所幸在 `common/types.rs` 中，找到了定义：

```rust
...
/// A common trait for all CLI commands to have consistent outputs
#[async_trait]
pub trait CliCommand<T: Serialize + Send>: Sized + Send {
    ...
   /// Executes the command, and serializes it to the common JSON output type
    async fn execute_serialized(self) -> CliResult {
        self.execute_serialized_with_logging_level(Level::Warn)
            .await
    }
    /// Execute the command with customized logging level
    ...
}
...
```

继续找命令执行的细节

```rust
use crate::{
    common::{
        init::Network,
        local_simulation,
        utils::{
            ...
            to_common_result, // 在 common/utils 中可以找到细节
            ...
            }
            ...
    }
    ...
}
...

#[async_trait]
pub trait CliCommand<T: Serialize + Send>: Sized + Send {
    ...
    /// Executes the command, returning a command specific type
    async fn execute(self) -> CliTypedResult<T>; // 执行命令的调用
    ...
    /// Execute the command with customized logging level
    async fn execute_serialized_with_logging_level(self, level: Level) -> CliResult {
        let command_name = self.command_name();
        start_logger(level);
        let start_time = Instant::now();
        let jsonify_error_output = self.jsonify_error_output();
        to_common_result( // 执行命令并处理结果
            command_name,
            start_time,
            self.execute().await, // 命令执行逻辑
            jsonify_error_output,
        )
        .await
    }
```

在 `common/utils` 中：

```rust
...
/// For pretty printing outputs in JSON. You can opt out of printing the error as
/// JSON by setting `jsonify_error` to false.
pub async fn to_common_result<T: Serialize>(
    command: &str,
    start_time: Instant,
    result: CliTypedResult<T>,
    jsonify_error: bool,
) -> CliResult {
    let latency = start_time.elapsed();

    if !telemetry_is_disabled() {
        let error = if let Err(ref error) = result {
            // Only print the error type
            Some(error.to_str())
        } else {
            None
        };

        if let Err(err) = timeout(
            Duration::from_millis(2000),
            send_telemetry_event(command, latency, error),
        )
        .await
        {
            debug!("send_telemetry_event timeout from CLI: {}", err.to_string())
        }
    }

    // Return early with a non JSON error if requested.
    if let Err(err) = &result {
        if !jsonify_error {
            return Err(format!("{:#}", err));
        }
    }

    let is_err = result.is_err();
    let result = ResultWrapper::<T>::from(result);
    let string = serde_json::to_string_pretty(&result).unwrap();
    if is_err {
        Err(string)
    } else {
        Ok(string)
    }
}
...
```
