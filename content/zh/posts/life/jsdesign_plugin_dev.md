+++
date = '2025-01-24T12:56:26+08:00'
draft = false
title = '即时设计插件开发'
author = "simons"
toc = true
categories= ["开发"]
tags = ["插件"]
description = "关于即使设计开发中的项目结构和代码组织介绍"
+++

# 简述

这是一款即时设计的插件，使用 ts/react 开发，代码是官方的，这里只是解析，[GitHub 地址](https://github.com/jsdesigndev/plugin-samples/tree/main/react%20插件示例)

# 一、前置条件

1. 即时设计客户端

https://js.design/download

2. vscode

https://code.visualstudio.com/Download

> **code 快捷命令（可选）**
>
> macOS 系统快捷键：<kbd>⌘</kbd> + <kbd>⇧</kbd> + <kbd>P</kbd> （command + shift + p）
>
> Windows/Linux 快捷键: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
>
>搜索安装 `shell command`

3. nodejs/npm

https://nodejs.org/en/download/

4. react

```bash
npm install @types/react @types/react-dom
```

> **启用类型提示**
> 在 vscode 按 <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>b</kbd> 开发即时设计类型提示



## 效率工具

### webpack

> 关于 webpack 的简介，可以查看[这篇文章]()

https://webpack.docschina.org/guides/getting-started/

```bash
# 安装 webpack
npm install webpack webpack-cli --save-dev
# 安装 TypeScript 编译器和 loader
npm install --save-dev typescript ts-loader
```



### 开发依赖

**开发依赖 (`devDependencies`)**

1. `@jsdesigndeveloper/plugin-typings`

   - **作用**: 提供 jsd 插件开发的 TypeScript 类型定义。

   - **安装命令**:

     ```bash
     npm install --save-dev @jsdesigndeveloper/plugin-typings
     ```



2. `@types/node`

   - **作用**: 提供 Node.js 的类型定义，用于 TypeScript 开发。

   - **安装命令**:

     ```bash
     npm install --save-dev @types/node
     ```

3. `css-loader`

   - **作用**: 让 Webpack 能够处理 CSS 文件，并将其转换为 JavaScript 模块。

   - **安装命令**:

     ```bash
     npm install --save-dev css-loader
     ```

4. `html-webpack-inline-source-plugin`

   - **作用**: 将 JavaScript 和 CSS 文件内联到 HTML 文件中。

   - **安装命令**:

     ```bash
     npm install --save-dev html-webpack-inline-source-plugin
     ```

5. `html-webpack-plugin`

   - **作用**: 自动生成 HTML 文件，并将打包后的 JavaScript 和 CSS 文件注入到 HTML 中。

   - **安装命令**:

     ```bash
     npm install --save-dev html-webpack-plugin
     ```

6. `ts-loader`

   - **作用**: 让 Webpack 能够处理 TypeScript 文件，并将其转换为 JavaScript。

   - **安装命令**:

     ```bash
     npm install --save-dev ts-loader
     ```

7. `typescript`

   - **作用**: TypeScript 编译器，用于将 TypeScript 代码编译为 JavaScript。

   - **安装命令**:

     ```bash
     npm install --save-dev typescript
     ```

8. `url-loader`**

   - **作用**: 将文件（如图片、字体）转换为 Base64 编码的 URL，并内联到 JavaScript 或 CSS 中。

   - **安装命令**:

     ```bash
     npm install --save-dev url-loader
     ```

9. `webpack`

   - **作用**: 前端项目的模块打包工具，用于将 JavaScript、CSS、图片等资源打包成一个或多个文件。

   - **安装命令**:

     ```
     npm install --save-dev webpack
     ```

10. `webpack-cli`

    - **作用**: Webpack 的命令行工具，用于运行 Webpack 命令。

    - **安装命令**:

      ```bash
      npm install --save-dev webpack-cli
      ```

**生产依赖 (`dependencies`)**

1. `@types/react`**

   - **作用**: 提供 React 的类型定义，用于 TypeScript 开发。

   - **安装命令**:

     ```bash
     npm install @types/react
     ```

2. `@types/react-dom`

   - **作用**: 提供 React DOM 的类型定义，用于 TypeScript 开发。

   - **安装命令**:

     ```bash
     npm install @types/react-dom
     ```

3. `react`

   - **作用**: React 核心库，用于构建用户界面。

   - **安装命令**:

     ```bash
     npm install react
     ```

4. `react-dev-utils`

   - **作用**: 提供一些 React 开发工具，例如 Webpack 插件和实用函数。

   - **安装命令**:

     ```bash
     npm install react-dev-utils
     ```

5. `react-dom`

   - **作用**: 将 React 组件渲染到 DOM 中。

   - **安装命令**:

     ```bash
     npm install react-dom
     ```



# 二、开发示例

这是一个自动生成矩形的插件

## 创建项目

在 `即时设计` 软件中，在菜单中，选择<kbd>插件</kbd> ><kbd>插件开发</kbd> > <kbd>创建新插件</kbd>，输入插件名称，选择有交互插件。随即打开即时设计创建的这个插件文件。

创建的文件结构如下：

```bash
plugin
├── code.js
├── manifest.json
├── package.json
└── ui.html
```

在 `vscode` 中打开创建的这个插件

> `code 插件名称`，输入你自己创建的插件名称



在项目根目录下生成 `ts` 配置文件

```bash
npx tsc --init
```

在项目根目录下创建 `webpack` 配置文件

```bash
touch webpack.config.js
```

> 现在文件中是空的，一会儿再加代码



现在目录结构如下

```bash
plugin
├── /src
    └── code.js
├── manifest.json
├── package.json
├── package-lock.json
├── webpack.config.js
├── tsconfig.json
└── ui.html
```



## 处理插件逻辑

### 项目依赖文件：

```json
{
	"version": "1.0.0",
	"description": "",
	"main": "code.js",
	"scripts": {
	  "test": "echo \"Error: no test specified\" && exit 1",
	  "build": "webpack"
	},
	"devDependencies": {
		"@jsdesigndeveloper/plugin-typings": "^1.0.12",
		"@types/node": "^16.7.1",
		"css-loader": "^6.2.0",
		"html-webpack-inline-source-plugin": "0.0.10",
		"html-webpack-plugin": "^5.3.2",
		"style-loader": "^3.2.1",
		"ts-loader": "^9.2.5",
		"typescript": "^4.3.5",
		"url-loader": "^4.1.1",
		"webpack": "^5.51.1",
		"webpack-cli": "^4.10.0"
	},
	"dependencies": {
		"@types/react": "^19.0.8",
		"@types/react-dom": "^19.0.3",
		"react": "^19.0.0",
		"react-dev-utils": "^12.0.1",
		"react-dom": "^19.0.0"
	}
}
```



### TS 配置文件

在 `tsconfig.json` 输入

```json
{
  "compilerOptions": {
    "target": "es6", // 编译后的代码将符合 ES6 (ES2015) 标准。
    "jsx": "react", // 将 JSX 转换为 React.createElement 调用。
    "noEmit": false, //编译器会生成编译后的 JavaScript 文件。如果设置为 true，则只进行类型检查，不生成输出文件。
    "typeRoots": [ // 类型定义文件（.d.ts 文件）的查找路径
      "./node_modules/@types",
      "./node_modules/@jsdesigndeveloper"
    ]
  },
  "include": ["src/**/*.ts", "src/**/*.tsx"] // 需要编译的文件或目录。
}
```

### webpack 配置文件

在 `webpack.config.js` 输入

```js
const InlineChunkHtmlPlugin = require('react-dev-utils/InlineChunkHtmlPlugin'); // 用于将 JavaScript 代码内联到 HTML 文件中。
const HtmlWebpackPlugin = require('html-webpack-plugin') //用于生成 HTML 文件，并自动注入打包后的 JavaScript 文件。
const path = require('path') // Node.js 的内置模块，用于处理文件路径。
const webpack = require('webpack') // Webpack 的核心模块。

module.exports = (env, argv) => ({ // 导出配置 (环境，命令行参数)
  mode: argv.mode === 'production' ? 'production' : 'development', // 设置 Webpack 的构建模式：

  // This is necessary because jsDesign's 'eval' works differently than normal eval
  devtool: argv.mode === 'production' ? false : 'inline-source-map', // 控制是否生成 source map，用于调试代码：

  entry: { // 定义项目的入口文件：
    ui: './src/ui.tsx', // UI 的入口
    code: './src/code.ts', // 插件逻辑的入口
  },

  module: {
    rules: [ // 定义模块的加载规则：
      // Converts TypeScript code to JavaScript
      {
        test: /\.tsx?$/,
        use: 'ts-loader', // 将 TypeScript 文件转换为 JavaScript。
        exclude: /node_modules/
      },

      // Enables including CSS by doing "import './file.css'" in your TypeScript code
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"], // 允许在 TypeScript 中导入 CSS 文件。
      },
      // Allows you to use "<%= require('./file.svg') %>" in your HTML code to get a data URI
      // { test: /\.(png|jpg|gif|webp|svg|zip)$/, loader: [{ loader: 'url-loader' }] }
      {
        test: /\.svg/,
        type: 'asset/inline' // 将 SVG 文件作为内联资源（Base64 编码）嵌入到代码中。
      }
    ]
  },

  // Webpack tries these extensions for you if you omit the extension like "import './file'"
  resolve: { extensions: ['.tsx', '.ts', '.jsx', '.js'] }, // 设置模块解析的扩展名。

  output: { // 定义输出文件的配置：
    filename: '[name].js', // 输出文件的名称，[name] 会被替换为入口名称（如 ui.js 和 code.js）。
    path: path.resolve(__dirname, 'dist'), // 输出文件的目录，这里是项目根目录下的 dist 文件夹。
    // Compile into a folder called "dist"
  },

  // Tells Webpack to generate "ui.html" and to inline "ui.ts" into it
  plugins: [ // 配置 Webpack 插件：
    new webpack.DefinePlugin({ // 定义全局变量，这里用于修复 global 变量的缺失问题。
      'global': {} // 修复在开发者 VM 中运行时的全局变量错误
    }),
    new HtmlWebpackPlugin({ // 根据模板 ./src/ui.html 生成 ui.html 文件，并自动注入 ui.js。
      inject: "body",
      template: './src/ui.html',
      filename: 'ui.html',
      chunks: ['ui']
    }),
    new InlineChunkHtmlPlugin(HtmlWebpackPlugin, [/ui/]), // 将 ui.js 内联到 ui.html 中。
  ],
})

```

### 插件逻辑文件

创建 `src/code.ts` 文件

```ts
jsDesign.showUI(__html__); // 显示插件的用户界面（UI）。__html__  是一个特殊的变量，通常用于嵌入 HTML 内容。在这里，它表示插件的 UI 界面（通过 HtmlWebpackPlugin 生成的 ui.html 文件）。

jsDesign.ui.onmessage = (msg) => { // 从 UI 发送过来的消息对象。
  if (msg.type === "create-rectangles") { // 消息的类型，用于区分不同的操作。
    const nodes = [];

    // 创建矩形的逻辑
    for (let i = 0; i < msg.count; i++) { // 从 UI 传递过来的参数，表示需要创建的矩形数量。
      const rect = jsDesign.createRectangle(); //创建一个矩形节点。
      rect.x = i * 150; // 设置矩形的水平位置（每次递增 150，避免矩形重叠）。
      rect.fills = [{ type: "SOLID", color: { r: 0.8, g: 0.8, b: 0.8 } }]; // 置矩形的填充颜色（这里是浅灰色）。
      jsDesign.currentPage.appendChild(rect); // 将矩形添加到当前页面。
      nodes.push(rect); // 将创建的矩形节点保存到数组中。
    }

    jsDesign.currentPage.selection = nodes; // 将创建的矩形设置为当前选中的对象。
    jsDesign.viewport.scrollAndZoomIntoView(nodes); // 将视图滚动并缩放到适合查看所有矩形的位置。
  }

  jsDesign.closePlugin(); //  在处理完消息后关闭插件。
};
```

### ui 逻辑文件

`src/ui.tsx`


```tsx
// 通过 React 实现了一个简单的表单，允许用户输入矩形的数量并触发创建矩形的操作。
import * as React from 'react' // React 核心库，用于构建组件。
import * as ReactDOM from 'react-dom' // 用于将 React 组件渲染到 DOM 中。
import './ui.css' //  引入样式文件，用于美化 UI。

declare function require(path: string): any // 这是一个 TypeScript 声明，用于告诉编译器 require 函数的存在。通常用于加载静态资源（如图片、字体等），但在这里并未实际使用。

class App extends React.Component {
  textbox: HTMLInputElement // 一个类属性，用于保存输入框的 DOM 元素引用。

  countRef = (element: HTMLInputElement) => { // 一个回调函数，用于绑定输入框的 DOM 元素。当输入框渲染完成后，会将其默认值设置为 5，并保存到 textbox 属性中。
    if (element) element.value = '5'
    this.textbox = element
  }

  onCreate = () => { // 点击“创建”按钮时触发的函数。
    const count = parseInt(this.textbox.value, 10) // 从输入框中获取用户输入的值（矩形数量）。
    parent.postMessage({ pluginMessage: { type: 'create-rectangles', count } }, '*') // 向 JSD 插件主逻辑发送消息，消息类型为 create-rectangles，并传递 count 参数。
  }

  onCancel = () => { // 点击“取消”按钮时触发的函数。
    parent.postMessage({ pluginMessage: { type: 'cancel' } }, '*') // 向 JSD 插件主逻辑发送消息，消息类型为 cancel。
  }

  render() { // 渲染组件的 UI。
    return <div>
      <h2>创建矩形</h2>
      <p>数量： <input ref={this.countRef} /></p>
      <button id="create" onClick={this.onCreate}>创建</button>
      <button onClick={this.onCancel}>取消</button>
    </div>
  }
}

//---
ReactDOM.render(<App />, document.getElementById('react-page')) // 将 App 组件渲染到 DOM 中，挂载到 id 为 react-page 的元素上。
//---
// 对于 React 18+，你需要使用 createRoot() 替换 ReactDOM.render()：
// 替换如下
// import { createRoot as createReactRoot } from 'react-dom/client';

// function createRoot(element: HTMLElement) {
//   return createReactRoot(element);
// }
// root.render(<App />)
```

### 插件模板

> webpack 会自动注入 js

`src/ui.html`

```html
<div id="react-page"></div>
```



### `mainfest.json`  jsd 插件识别文件

`manifest.json` 是 ssd 读取插件的配置文件，只改 `main` 和 `ui`

```json
{
  "name": "your_plugin_name",
  "id": "your_plugin_id",
  "api": "1.0.0",
  "main": "dist/code.js", // code.js 的位置
  "ui": "dist/ui.html" // ui.js 的位置
}
```



## 三、构建插件

```bash
pnpm run build
```



## 四、在 jsd 中运行插件

在菜单中，选择<kbd>插件</kbd> ><kbd>插件开发</kbd> 顶部会出现你创建的插件，如果没有，就在  <kbd>通过 manifest 导入插件</kbd>（通过即时设计创建的插件，会自动生成这个文件）

现在插件的开发就结束了
