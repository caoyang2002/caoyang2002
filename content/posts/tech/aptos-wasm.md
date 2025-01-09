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

我看不懂 `aptos-core/third_party` 从的功能，所以在
