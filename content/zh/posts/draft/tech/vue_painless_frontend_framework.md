+++
date = '2025-01-24T13:53:44+08:00'
draft = true
title = 'Vue: 一个让前端开发不再痛苦的框架'
toc = true
categories= ["设计"]
tags = ["排版"]
description = "这是一段描述内容"
+++

# Vue: 一个让前端开发不再痛苦的框架

## 老板又改需求了?

```javascript
// 改个文本要改三个地方
document.getElementById("title").innerText = "新标题";
document.querySelector(".header h1").innerText = "新标题";
document.getElementsByClassName("footer")[0].innerText = "新标题";
```

这就是没用Vue的下场。数据和视图分离,改一个要改几个地方,还容易改出bug。

## Vue是啥?

简单说: Vue = 数据驱动视图 + 组件化开发

```vue
<template>
  <div>
    <!-- 数据自动同步到视图 -->
    <h1>{{title}}</h1>
    <button @click="changeTitle">改标题</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: "原标题"
    }
  },
  methods: {
    changeTitle() {
      // 改数据,视图自动更新
      this.title = "新标题"
    }
  }
}
</script>
```

## 为什么选Vue?

1. **上手容易**
   - 模板语法接近原生HTML
   - 不用学JSX那套
   - 中文文档无障碍

2. **性能够用**
   - 虚拟DOM精确更新
   - 自动依赖收集
   - 按需渲染

3. **生态完整**
   - Vuex状态管理
   - Vue Router路由
   - Vite/Vue CLI脚手架

## 跟其他框架比?

- **React**: JSX太魔性,状态管理复杂
- **Angular**: 太重,学习曲线陡峭
- **jQuery**: 还在用?准备养老了?

## 实战例子

需求:写个Todo List

```vue
<template>
  <div>
    <input v-model="newTodo" @keyup.enter="addTodo">
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <span :class="{done: todo.done}">{{todo.text}}</span>
        <button @click="toggleTodo(todo)">完成</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newTodo: '',
      todos: []
    }
  },
  methods: {
    addTodo() {
      this.todos.push({
        id: Date.now(),
        text: this.newTodo,
        done: false
      })
      this.newTodo = ''
    },
    toggleTodo(todo) {
      todo.done = !todo.done
    }
  }
}
</script>
```

## 坑和经验

1. **响应式陷阱**
   - 数组索引修改不会触发更新
   - 对象新增属性要用Vue.set()
   - computed vs watch分清楚

2. **生命周期要弄懂**
   - created不要操作DOM
   - mounted才是干活的时候
   - destroyed记得清理副作用

3. **组件通信**
   - props向下传
   - emit向上传
   - vuex管全局

记住: Vue不是完美的,但它让前端开发不再是噩梦。

## 思考题

1. Vue3为什么要用Proxy代替Object.defineProperty?
2. Vue的响应式系统是如何工作的?
3. 如何处理Vue项目的性能优化?

共勉。

P.S. 想吐槽Vue的,建议先看看jQuery时代的代码。
