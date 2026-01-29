+++
date = '2025-01-18T11:35:14+08:00'
draft = false
title = 'mac 汇编笔记'
categories = ["编程", "汇编语言"]
tags = ["macOS", "ARM64", "汇编基础", "LLVM", "系统调用", "HelloWorld", "学习笔记"]
description = "本文记录了在 Apple Silicon Mac 上学习 ARM64 汇编语言的入门笔记。从最简单的空程序开始，到编写并运行 Hello World，详细介绍了汇编、链接和调试的基本步骤与工具链使用，并提供了相关权威参考资料。"
toc = true
+++

https://evian-zhang.github.io/learn-assembly-on-Apple-Silicon-Mac/index.html

# 梦开始的地方

# 简单的 asm

`null.s`
```asm
.section    __TEXT,__text
.globl  _main
.p2align    2
_main:
mov    w0, #0
ret
```

```c
int main() {
    return 0;
}
```

```bash
as null.s -o null.o # 汇编
ld null.o -lSystem -L $(xcrun --show-sdk-path -sdk macosx)/usr/lib -o null # 链接（由于在 macOS 上不能创建静态链接的可执行文件，因此在链接时必须使用 -lSystem 动态链接上系统库。）
./null # 运行

# or
clang null.s -o null

# or
gcc null.s -o null
```

> `as` 是 LLVM 的汇编器, `lldb` 是 LLVM 的调试器。
> `GCC` 套件是 GNU 操作系统的一个部分，GNU 是开源的、社区驱动的。而 LLVM 项目也是开源的，现在主要是 Apple 在投资运行。因此，既然在 macOS 上，我就主要用的是 LLVM 系的工具。

## hello world

`hello.s`

```asm
.section    __TEXT,__text    ; 代码段声明
.globl      _main           ; 声明 main 函数对外可见
.p2align    2              ; 4字节对齐

_main:                     ; main 函数入口
    ; 准备系统调用参数
    mov     x0, #1        ; stdout 文件描述符
    adrp    x1, message@PAGE     ; 获取消息的页地址
    add     x1, x1, message@PAGEOFF ; 加上页内偏移
    mov     x2, #13       ; 消息长度
    mov     x16, #4       ; write 系统调用号
    svc     #0x80         ; 触发系统调用

    ; 返回值设为 0
    mov     x0, #0        ; 返回值放入 x0
    ret                   ; 返回

.section    __DATA,__data    ; 数据段声明
message:
    .ascii  "Hello World!\n"
```

```c
int main() {
    printf("Hello World!\n");
    return 0;
}
```

编译

```bash
as hello.s -o hello.o
ld hello.o -lSystem -L $(xcrun --show-sdk-path -sdk macosx)/usr/lib -o hello
./hello
```



# 参考

- [Using `as`](https://sourceware.org/binutils/docs/as/index.html)
- [OS X Assembler Reference](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/Assembler)
- [Armv8-A Instruction Set Architecture](https://developer.arm.com/-/media/Arm Developer Community/PDF/Learn the Architecture/Armv8-A Instruction Set Architecture.pdf)
- [Arm Architecture Reference Manual for A-profile architecture](https://developer.arm.com/documentation/ddi0487/latest)
- [ARM Assembly Language](https://www.oreilly.com/library/view/arm-assembly-language/9781482229851/)
- [Writing ARM64 Code for Apple Platforms](https://developer.apple.com/documentation/xcode/writing-arm64-code-for-apple-platforms)
