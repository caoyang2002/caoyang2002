+++
title = 'TypeScript: 静态类型，所以 NB'
date = '2025-01-24T13:46:32+08:00'
draft = true
toc = true
categories= ["设计"]
tags = ["排版"]
description = "这是一段描述内容"
+++

# TypeScript: 静态类型，所以 NB

## 你遇到过这些问题吗?

```javascript
// 调用一个不存在的方法
obj.nonexistMethod()

// 传错参数类型
calculateArea("5", "10")

// 对象属性拼写错误
user.namee = "Bob"
```

玩过JavaScript的同学一定很熟悉这些坑。这就是为什么我们需要 TypeScript。

## TypeScript是个啥?

简单说:TypeScript = JavaScript + 类型系统

```typescript
// 变量类型
let name: string = "老陈"

// 函数类型
function add(x: number, y: number): number {
    return x + y
}

// 接口
interface User {
    id: number
    name: string
    age?: number  // 可选属性
}
```

## 为什么要用TypeScript?

1. **不用写单元测试了?**
   - 别想多了,该写还得写
   - 但80%的低级错误在编译时就能抓出来

2. **代码更好维护**
   - 重构代码不再靠猜
   - IDE提示准确,不用查文档
   - 新人上手更快,代码即文档

3. **面向对象特性**
   - 类、接口、泛型一应俱全
   - JavaScript原型继承太难懂?用Class

## 跟其他方案比?

- **Flow**: Facebook的玩具,社区都快凉了
- **JSDoc**: 注释太冗长,IDE支持有限
- **纯JS**: 想调试到头秃么?

## 实战例子

需求:写个用户管理系统

```typescript
// 定义接口
interface IUser {
    id: number;
    name: string;
    email: string;
}

// 用户管理类
class UserManager {
    private users: Map<number, IUser> = new Map();

    addUser(user: IUser): void {
        this.users.set(user.id, user);
    }

    getUser(id: number): IUser | undefined {
        return this.users.get(id);
    }
}

// 使用
const manager = new UserManager();
manager.addUser({id: 1, name: "老陈", email: "laoc@cool.com"});
```

## 坑点和经验

1. **any是万恶之源**
   - 能不用就不用
   - 实在要用,先问问自己为什么

2. **泛型不是越多越好**
   - 可读性 > 精确性
   - 过度设计等于自废武功

3. **渐进迁移策略**
   - 先允许JS和TS共存
   - 关键模块先迁移
   - 新代码必须用TS

记住: TypeScript不是银弹,但能让你少掉几根头发。

想学更多?源码在: [typescript-examples](https://github.com/microsoft/TypeScript)

## 思考题

1. 为什么JavaScript要加入类型系统?
2. TypeScript编译器是如何工作的?
3. 如何平衡类型安全和开发效率?

共勉。
