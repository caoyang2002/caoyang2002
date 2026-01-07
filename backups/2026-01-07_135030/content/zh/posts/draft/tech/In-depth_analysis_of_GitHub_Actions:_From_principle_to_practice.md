+++
title = 'GitHub Actions 深入剖析：从原理到实践'
date = 2025-01-26T10:47:26+08:00
draft = true
author = "simons"
categories = ["编程"]
tags = ["github"]
description = "Github 的 Action 概述"
+++

# GitHub Actions 深入剖析：从原理到实践

最近收到一个问题："为什么我的 CI/CD 流水线总是莫名其妙失败？"这让我想起了 GitHub Actions 的一些有趣特性。今天就来扒一扒它的底层原理。

## GitHub Actions 的本质

本质上，GitHub Actions 就是一个事件驱动的工作流自动化引擎。它监听 GitHub 事件，然后执行预定义的动作。

```yaml
# 这是最基础的工作流
name: CI
on: [push]  # 事件触发器
jobs:
  build:    # 工作单元
    runs-on: ubuntu-latest  # 运行环境
    steps:   # 执行步骤
    - uses: actions/checkout@v2
    - run: npm test
```

但这只是表象，让我们深入看看它的架构：

## 核心概念解析

1. Runner（执行器）
```bash
# Runner 其实就是一个 Docker 容器
docker run --rm -v $PWD:/workspace \
  -e GITHUB_TOKEN=$token \
  myrunner:latest
```

2. Workflow（工作流）
```yaml
# 这才是真正的工作流定义
name: Complex Flow
on:
  push:
    branches: [ main ]
    paths-ignore: [ '**.md' ]
jobs:
  build:
    strategy:
      matrix:
        node: [12, 14, 16]
    steps:
      - uses: actions/setup-node@v2
        with:
          node-version: ${{ matrix.node }}
```

## 深入原理

GitHub Actions 的执行过程：

1. 事件触发
2. 工作流匹配
3. Runner 分配
4. 容器初始化
5. 步骤执行

关键在于它的上下文传递：
```yaml
# 上下文是如何传递的？
steps:
  - id: step1
    run: echo "::set-output name=foo::bar"
  - run: echo ${{ steps.step1.outputs.foo }}
```

这里涉及到环境变量、文件系统和网络隔离。

## 实战技巧

1. 缓存优化
```yaml
- uses: actions/cache@v2
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
```

2. 矩阵构建
```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [12, 14, 16]
    exclude:
      - os: windows-latest
        node: 12
```

3. 条件执行
```yaml
if: github.event_name == 'push' && github.ref == 'refs/heads/main'
```

## 常见坑点

1. 权限问题
```yaml
# 这样写才能访问其他仓库
jobs:
  build:
    permissions:
      contents: read
      packages: write
```

2. 环境变量作用域
```yaml
env:
  GLOBAL_VAR: value  # 全局
jobs:
  build:
    env:
      JOB_VAR: value  # 作业级别
```

3. Runner 选择
```yaml
# 自托管 runner 要考虑并发
runs-on: [self-hosted, linux]
```

## 架构设计思考

1. 为什么用 YAML？
   - 人类可读
   - 版本控制友好
   - 但是逻辑复杂时很痛苦

2. 事件驱动的优缺点
   - 优点：解耦、灵活
   - 缺点：调试困难

3. Runner 的设计
   - 容器隔离
   - 资源限制
   - 安全考虑

记住：
1. Actions 不是万能的，某些场景还是本地构建更合适
2. 理解原理比记忆语法更重要
3. 安全永远是第一位的

最后说一句：工具用对了是银弹，用错了是手雷。关键是理解它的设计思想和实现原理。

真受不了那些表面的介绍，今天我们扒开 GitHub Actions 的底裤，看看它到底是个啥玩意。

## Event（事件） - 一切的起点

事件就是触发器，就这么简单。但关键是要理解事件的类型和它们的上下文数据。

```yaml
# 最常见的事件触发
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '0 0 * * *'  # 每天零点触发
```

妈的，光写这些配置有啥用？重点是要理解每个事件会带来什么上下文：

```yaml
jobs:
  print-context:
    runs-on: ubuntu-latest
    steps:
      - name: 看看push事件带来了啥
        if: github.event_name == 'push'
        run: |
          echo "提交人: ${{ github.actor }}"
          echo "提交SHA: ${{ github.sha }}"
          echo "修改的文件: ${{ join(github.event.commits.*.modified, ', ') }}"
```

## Workflow（工作流）- 编排你的自动化过程

工作流说白了就是一个YAML文件，放在 `.github/workflows` 目录下。但关键是要搞清楚这个文件的结构：

```yaml
name: 构建测试部署一条龙
on: [push]
env:
  GLOBAL_VAR: "全局变量老子想用就用"

jobs:
  job1:
    runs-on: ubuntu-latest
    outputs:
      output1: ${{ steps.step1.outputs.test }}
    steps:
      - id: step1
        run: echo "::set-output name=test::value"

  job2:
    needs: job1  # 依赖关系，老子等job1完事才开始
    runs-on: ubuntu-latest
    steps:
      - run: echo ${{ needs.job1.outputs.output1 }}
```

## Job（作业）- 实际干活的地方

Job 是最小的执行单元，但它里面的水太深了：

```yaml
jobs:
  build:
    runs-on: ubuntu-latest  # 这他妈才是关键，选错环境分分钟给你玩死
    container:
      image: node:14  # 想用容器？来！
    services:
      redis:  # 需要依赖服务？安排！
        image: redis
    strategy:
      matrix:  # 多环境测试
        node: [12, 14, 16]
        os: [ubuntu-latest, windows-latest]
      fail-fast: false  # 一个失败其他继续跑
    steps: ...
```

## Action（动作）- 组件化的精髓

Action 就是一个可重用的组件，但是它也分三种：

1. JavaScript Action
```javascript
const core = require('@actions/core');
const github = require('@actions/github');

try {
  const nameToGreet = core.getInput('who-to-greet');
  console.log(`Hello ${nameToGreet}!`);
} catch (error) {
  core.setFailed(error.message);
}
```

2. Docker Container Action
```dockerfile
FROM alpine:3.10
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

3. Composite Action
```yaml
runs:
  using: "composite"
  steps:
    - run: echo "这他妈就是个组合动作"
      shell: bash
```

## 实战技巧

1. Secrets管理
```yaml
steps:
  - name: 配置密钥
    env:
      SSH_KEY: ${{ secrets.SSH_KEY }}
    run: |
      mkdir -p ~/.ssh
      echo "$SSH_KEY" > ~/.ssh/id_rsa
      chmod 600 ~/.ssh/id_rsa
```

2. 缓存依赖
```yaml
- uses: actions/cache@v3
  with:
    path: |
      ~/.npm
      node_modules
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

3. 条件执行和错误处理
```yaml
steps:
  - name: 部署到生产环境
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    continue-on-error: true  # 出错了也别停
    run: |
      curl ${{ secrets.DEPLOY_HOOK }}
```

## 实战案例：完整CI/CD流程

```yaml
name: 完整流程
on:
  push:
    branches: [ main ]

jobs:
  ci-cd:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: 缓存依赖
        uses: actions/cache@v3
        with:
          path: ~/.npm
          key: npm-deps-${{ hashFiles('**/package-lock.json') }}

      - name: 安装依赖
        run: npm ci

      - name: 代码检查
        run: |
          npm run lint
          npm run type-check

      - name: 运行测试
        run: npm test

      - name: 构建
        run: npm run build

      - name: 部署
        if: success()
        env:
          DEPLOY_KEY: ${{ secrets.DEPLOY_KEY }}
        run: |
          echo "$DEPLOY_KEY" > deploy_key
          chmod 600 deploy_key
          rsync -e "ssh -i deploy_key" ./dist/ user@server:/var/www/
```

最后说点实在的：
1. runner要选对，别tm用windows跑linux命令
2. cache一定要用，不然慢死你
3. secrets别写错，不然调试死你
4. 报错信息好好看，别瞎改配置

要是你能把这些都整明白了，那就算入门了。想要进阶？自己写个Action练练手，看看GitHub官方的Action源码。记住：source code is your best teacher。
