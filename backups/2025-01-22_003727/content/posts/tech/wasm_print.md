+++
date = '2025-01-15T00:31:17+08:00'
draft = false
title = 'Wasm 打印输出和浏览器特性等最佳实践'
toc = true
+++

在 Rust WASM 中，有几种方式可以实现打印输出和调用浏览器特性：

1. 使用 `web_sys` 和 `wasm_bindgen` 进行浏览器 API 调用：

```rust
use wasm_bindgen::prelude::*;
use web_sys::{console, window};

pub fn move_test(name: &str) {
    // 控制台打印
    console::log_1(&JsValue::from_str(&format!("move test: {}", name)));

    // 使用 console.warn
    console::warn_1(&JsValue::from_str("This is a warning"));

    // 使用 console.error
    console::error_1(&JsValue::from_str("This is an error"));

    // 浏览器 alert
    if let Some(window) = window() {
        window
            .alert_with_message(&format!("Hello, {}!", name))
            .expect("alert failed");
    }

    // 确认对话框
    if let Some(window) = window() {
        if window
            .confirm_with_message("Do you want to continue?")
            .expect("confirm failed")
        {
            console::log_1(&JsValue::from_str("User clicked OK"));
        } else {
            console::log_1(&JsValue::from_str("User clicked Cancel"));
        }
    }
}
```

2. 在 Cargo.toml 中需要添加必要的依赖：

```toml
[dependencies]
wasm-bindgen = "0.2"
web-sys = { version = "0.3", features = [
    "console",
    "Window",
    "Document",
    "Element",
    "HtmlElement",
    "Node",
    "Location"
]}
```

3. 如果需要格式化打印，可以使用 `console::log!` 宏：

```rust
use web_sys::console;

// 需要引入宏
#[macro_export]
macro_rules! console_log {
    ($($t:tt)*) => (console::log_1(&JsValue::from_str(&format!($($t)*))))
}

pub fn move_test(name: &str) {
    console_log!("Testing move with name: {}", name);
}
```

4. 操作 DOM 示例：

```rust
use wasm_bindgen::prelude::*;
use web_sys::{Document, Element, HtmlElement, window};

pub fn move_test(name: &str) {
    // 获取 document
    let window = window().expect("no global window exists");
    let document = window.document().expect("no document exists");

    // 创建新元素
    if let Some(div) = document.get_element_by_id("test-input") {
        // 修改输入框的值
        if let Some(input) = div.dyn_ref::<HtmlElement>() {
            input.set_inner_text(&format!("New value: {}", name));
        }
    }

    // 创建新元素
    let new_div = document.create_element("div").unwrap();
    new_div.set_text_content(Some(&format!("Hello {}", name)));

    // 添加到 body
    if let Some(body) = document.body() {
        body.append_child(&new_div).unwrap();
    }
}
```

5. 处理错误和 Result：

```rust
pub fn move_test(name: &str) -> Result<(), JsValue> {
    // 使用 ? 运算符处理错误
    let window = window().ok_or("no global window exists")?;
    let document = window.document().ok_or("no document exists")?;

    // 处理可能的错误
    match document.get_element_by_id("test-input") {
        Some(element) => {
            console::log_1(&JsValue::from_str(&format!("Found element: {}", name)));
            Ok(())
        },
        None => Err(JsValue::from_str("Element not found"))
    }
}
```

6. 使用本地存储：

```rust
use web_sys::Storage;

pub fn move_test(name: &str) -> Result<(), JsValue> {
    let window = window().ok_or("no global window exists")?;

    // 获取 localStorage
    if let Some(storage) = window.local_storage()? {
        // 存储数据
        storage.set_item("user_name", name)?;

        // 读取数据
        if let Ok(Some(saved_name)) = storage.get_item("user_name") {
            console::log_1(&JsValue::from_str(&format!("Saved name: {}", saved_name)));
        }
    }

    Ok(())
}
```

记住在使用任何 web-sys 功能时，需要在 Cargo.toml 中启用相应的 feature。例如，如果要使用 localStorage，需要添加 "Storage" feature：

```toml
web-sys = { version = "0.3", features = [
    "console",
    "Window",
    "Storage",
    // ... 其他需要的 features
]}
```

这些示例展示了在 Rust WASM 中如何与浏览器进行交互的基本方法。你可以根据需要组合使用这些功能。



以下是 Rust WebAssembly 开发的最佳实践建议：

1. 错误处理
```rust
use wasm_bindgen::prelude::*;
use web_sys::console;

// 定义自定义错误类型
#[derive(Debug)]
pub enum WasmError {
    JsError(String),
    CustomError(String)
}

// 实现错误转换
impl From<WasmError> for JsValue {
    fn from(error: WasmError) -> Self {
        JsValue::from_str(&format!("{:?}", error))
    }
}

// 使用 Result 处理错误
pub fn move_test(name: &str) -> Result<(), WasmError> {
    // 优雅处理错误
    if name.is_empty() {
        return Err(WasmError::CustomError("Name cannot be empty".into()));
    }

    // 记录日志
    console::log_1(&format!("Processing: {}", name).into());

    Ok(())
}
```

2. 性能优化
```rust
use wasm_bindgen::prelude::*;
use std::rc::Rc;
use std::cell::RefCell;

// 使用 Rc 和 RefCell 来共享数据
struct State {
    count: i32,
    data: Vec<String>
}

#[wasm_bindgen]
pub struct App {
    state: Rc<RefCell<State>>
}

#[wasm_bindgen]
impl App {
    // 尽量减少 JS/Rust 边界调用
    pub fn batch_operation(&self, items: &[JsValue]) -> Result<(), JsValue> {
        let mut state = self.state.borrow_mut();

        // 批量处理
        for item in items {
            // 处理逻辑
        }

        Ok(())
    }
}
```

3. 模块化设计
```rust
// lib.rs
mod utils;
mod components;
mod types;

use utils::logging;
use components::button;
use types::custom_types;

// 清晰的模块结构
pub fn initialize() {
    logging::setup_logging();
    button::register_components();
}
```

4. 日志和调试
```rust
#[macro_export]
macro_rules! console_log {
    ($($t:tt)*) => {
        web_sys::console::log_1(&format!($($t)*).into())
    }
}

#[macro_export]
macro_rules! console_error {
    ($($t:tt)*) => {
        web_sys::console::error_1(&format!($($t)*).into())
    }
}

// 使用
pub fn debug_operation(data: &str) {
    console_log!("Starting operation with: {}", data);
    // ... 操作代码
    console_log!("Operation completed");
}
```

5. 内存管理
```rust
#[wasm_bindgen]
pub struct LargeData {
    // 使用 Vec<u8> 而不是 String 处理二进制数据
    buffer: Vec<u8>,
}

impl Drop for LargeData {
    fn drop(&mut self) {
        // 清理资源
        self.buffer.clear();
    }
}
```

6. 异步操作处理
```rust
use wasm_bindgen_futures::JsFuture;
use web_sys::{Request, RequestInit, Response};

// 异步函数处理
pub async fn fetch_data(url: &str) -> Result<JsValue, JsValue> {
    let mut opts = RequestInit::new();
    opts.method("GET");

    let request = Request::new_with_str_and_init(url, &opts)?;
    let window = web_sys::window().unwrap();
    let resp_value = JsFuture::from(window.fetch_with_request(&request)).await?;
    let resp: Response = resp_value.dyn_into().unwrap();

    JsFuture::from(resp.json()?).await
}
```

7. 测试策略
```rust
#[cfg(test)]
mod tests {
    use super::*;
    use wasm_bindgen_test::*;

    wasm_bindgen_test_configure!(run_in_browser);

    #[wasm_bindgen_test]
    fn test_basic_functionality() {
        // 浏览器环境测试
        let result = move_test("test");
        assert!(result.is_ok());
    }
}
```

8. 构建优化
```toml
# Cargo.toml
[package]
name = "wasm-project"
version = "0.1.0"

[lib]
crate-type = ["cdylib"]

[profile.release]
lto = true
opt-level = 'z'
codegen-units = 1
```

9. 类型安全

```rust
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
pub struct UserData {
    name: String,
    age: u32,
}

#[wasm_bindgen]
impl UserData {
    // 提供类型安全的接口
    pub fn new(name: &str, age: u32) -> Result<UserData, JsValue> {
        if name.is_empty() {
            return Err("Name cannot be empty".into());
        }
        Ok(UserData {
            name: name.to_string(),
            age,
        })
    }
}
```

10. 文档注释

```rust
/// Performs a move test operation
///
/// # Arguments
///
/// * `name` - The name to test with
///
/// # Returns
///
/// * `Result<(), WasmError>` - Ok if successful, Err with error details if failed
///
/// # Examples
///
/// ```
/// let result = move_test("test");
/// assert!(result.is_ok());
/// ```

#[wasm_bindgen]
pub fn move_test(name: &str) -> Result<(), WasmError> {
    // 实现代码
}
```
