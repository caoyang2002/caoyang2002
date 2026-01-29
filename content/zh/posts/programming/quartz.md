+++
date = '2024-02-29T09:31:37+08:00'
draft = false
title = 'Quartz 教程'
categories = ["技术教程", "网站搭建"]
tags = ["Quartz", "静态网站生成器", "Obsidian", "教程", "配置", "插件开发", "GitHub Pages", "SPA路由"]
description = "一份详细的Quartz静态网站生成器使用教程，涵盖从环境配置、布局定制、组件开发到插件制作的全流程，帮助用户基于Obsidian笔记快速构建个性化网站并部署到GitHub Pages。"
toc = true
+++

> [原作者](https://quartz.jzhao.xyz)
> [个人配置](https://www.chyraw.com)


# 下载
```bash
git clone https://github.com/caoyang2002/quartz-obsidian-webside.git
cd quartz-obsidian-webside
npm i
npx quartz build --serve
```

# 配置

## 布局

某些 emitters 可能还会输出HTML文件。为了方便定制，这些 emitters 允许您完全重新排列页面的布局。
默认页面布局可以在 `quartz.layout.ts` 中找到。

每个页面由多个不同的部分组成，这些部分包含 `QuartzComponents`。以下代码片段列出了您可以向其中添加组件的所有有效部分：

`quartz/cfg.ts`

```typescript
export interface FullPageLayout {
  head: QuartzComponent // 单个组件
  header: QuartzComponent[] // 水平布局
  beforeBody: QuartzComponent[] // 垂直布局
  pageBody: QuartzComponent // 单个组件
  left: QuartzComponent[] // 桌面上垂直布局，在移动设备上水平布局
  right: QuartzComponent[] // 桌面上垂直布局，在移动设备上水平布局
  footer: QuartzComponent // 单个组件
}
```

这些对应于页面的以下部分：

![](https://www.caoyang2002.top/usr/uploads/2024/04/2344105805.png)

注意
还有两个未在上图中显示的附加布局字段。

`head` 是一个单独的组件，用于在HTML中呈现`<head>`标签。这在页面上不会可见，只负责文档的元数据，如标签标题、脚本和样式。
`header` 是一组以水平方式布局的组件，出现在beforeBody部分之前。这使您可以复制旧的Quartz 3标题栏，其中包含标题、搜索栏和暗模式切换。默认情况下，Quartz 4不在标题中放置任何组件。

`Quartz` 组件，就像插件一样，可以接受额外的属性作为配置选项。如果您熟悉React术语，可以将它们视为Higher-order Components。

查看所有可用组件以及其配置选项的列表。如果您有兴趣进一步定制Quartz的行为，请查看创建组件的指南。


## 样式

大多数有意义的样式更改，如颜色方案和字体，都可以通过常规配置选项简单完成。但是，如果您想进行更复杂的样式更改，可以通过编写自己的样式来实现。与Quartz 3一样，Quartz 4也使用Sass进行样式设计。

您可以在 `quartz/styles/base.scss` 中查看基本样式表，并在 `quartz/styles/custom.scss` 中编写自己的样式。

注意
某些组件可能还提供自己的样式！例如，`quartz/components/Darkmode.tsx从quartz/components/styles/darkmode.scss` 导入样式。如果您想为特定组件定制样式，请仔细检查组件定义，以查看其样式是如何定义的。


# 创建自己的Quartz组件

[原文](https://quartz.jzhao.xyz/advanced/creating-components)


> 警告
> 本指南假设您具有编写JavaScript的经验并熟悉TypeScript。

通常在网络上，我们使用HTML编写布局代码，看起来像下面这样：

```html
<article>
  <h1>文章标题</h1>
  <p>一些内容</p>
</article>
```

这段HTML表示一篇文章，具有领先的标题“文章标题”和一个包含文本“一些内容”的段落。这与CSS结合在一起来为页面添加样式，使用JavaScript添加交互。

但是，HTML不允许您创建可重用的模板。如果您想创建一个新页面，您需要复制并粘贴上述代码片段，并自行编辑标题和内容。如果我们的网站上有很多内容共享相似的布局，那么这并不理想。创建React的聪明人也有类似的抱怨，并发明了组件的概念——返回JSX的JavaScript函数——来解决代码重复的问题。

实际上，组件允许您编写一个JavaScript函数，该函数接受一些数据并生成HTML作为输出。虽然Quartz不使用React，但它使用相同的组件概念，以便您可以轻松地在Quartz网站中表达布局模板。

## 示例组件

### 构造函数

组件文件是以 .tsx 文件编写的，位于 `quartz/components` 文件夹中。这些文件被重新导出到 `quartz/components/index.ts` 中，以便您可以更轻松地在布局和其他组件中使用它们。

每个组件文件应该有一个默认导出，满足 `QuartzComponentConstructor` 函数签名。它是一个接受一个可选参数 `opts` 并返回一个 Quartz 组件的函数。参数 opts 的类型由您作为组件创建者决定的 `Options` 接口定义。

在您的组件中，您可以使用配置选项中的值来更改组件内的渲染行为。例如，下面代码片段中的组件如果 `favouriteNumber` 选项小于 0，则不会呈现。

```typescript
interface Options {
  favouriteNumber: number
}

const defaultOptions: Options = {
  favouriteNumber: 42,
}

export default ((userOpts?: Options) => {
  const opts = { ...userOpts, ...defaultOpts }
  function YourComponent(props: QuartzComponentProps) {
    if (opts.favouriteNumber < 0) {
      return null
    }

    return <p>我的最喜欢的数字是 {opts.favouriteNumber}</p>
  }

  return YourComponent
}) 满足 QuartzComponentConstructor
```

## 属性

Quartz 组件本身（上面高亮的第 11-17 行）看起来像一个React组件。它接受属性（有时称为 props）并返回JSX。

所有Quartz组件接受相同的一组属性：

```typescript
// 简化以便演示
export type QuartzComponentProps = {
  fileData: QuartzPluginData
  cfg: GlobalConfiguration
  tree: Node<QuartzPluginData>
  allFiles: QuartzPluginData[]
  displayClass?: "mobile-only" | "desktop-only"
}
```

- `fileData` : 可能已添加到当前页面的任何元数据插件。
- `fileData.slug` : 当前页面的 slug。
- `fileData.frontmatter` : 解析的任何 frontmatter。
- `cfg` : quartz.config.ts 中的配置字段。
- `tree` : 处理和转换文件后的结果HTML AST。如果您想使用 `hast-util-to-jsx-runtime` 渲染内容，这将非常有用（您可以在 `quartz/components/pages/Content.tsx` 中找到此示例）。
- `allFiles` : 已解析的所有文件的元数据。用于执行页面列表或确定整体站点结构非常有用。
- `displayClass` : 指示用户如何在移动设备或桌面环境中渲染它的首选项的实用类。如果要在移动设备或桌面环境中有条件地隐藏组件，则很有帮助。

## 样式

Quartz 组件还可以在实际函数组件上定义 `.css` 属性，Quartz 将对其进行捕获。这预期是一个 CSS 字符串，可以是内联的也可以是从 `.scss` 文件导入的。

请注意，内联样式必须是纯粹的普通 CSS：

```typescript
export default (() => {
  function YourComponent() {
    return <p class="red-text">示例组件</p>
  }

  YourComponent.css = `
  p.red-text {
    color: red;
  }
  `

  return YourComponent
}) 满足 QuartzComponentConstructor
```

但是，导入的样式可以来自 SCSS 文件：

```typescript
// 假设您的样式表位于 quartz/components/styles/YourComponent.scss
import styles from "./styles

/YourComponent.scss"

export default (() => {
  function YourComponent() {
    return <p>示例组件</p>
  }

  YourComponent.css = styles
  return YourComponent
}) 满足 QuartzComponentConstructor
```

警告
Quartz 不使用 CSS 模块，因此在此处声明的任何样式都是全局的。如果您只希望它应用于您的组件，请确保使用特定的类名和选择器。

脚本和交互性

那么交互性呢？假设您想添加一个点击处理程序，例如。与组件上的 `.css` 属性一样，您还可以声明 `.beforeDOMLoaded` 和 `.afterDOMLoaded` 属性，这些属性是包含脚本的字符串。

```typescript
export default (() => {
  function YourComponent() {
    return <button id="btn">点击我</button>
  }

  YourComponent.beforeDOM = `
  console.log("hello from before the page loads!")
  `

  YourComponent.afterDOM = `
  document.getElementById('btn').onclick = () => {
    alert('button clicked!')
  }
  `
  return YourComponent
}) 满足 QuartzComponentConstructor
```

提示
对于那些来自React的人来说，Quartz 组件与React组件不同，因为它只使用JSX进行模板化和布局。像 `useEffect`、`useState` 等钩子不会被渲染，其他接受函数的属性如 `onClick` 处理程序也不起作用。相反，使用一个普通的 JS 脚本，直接修改 DOM 元素。

正如名称所暗示的那样，`.beforeDOMLoaded` 脚本在页面加载完成之前执行，因此它不能访问页面上的任何元素。这主要用于预取任何关键数据。

`.afterDOMLoaded` 脚本在页面完全加载后执行。这是设置任何在站点访问期间应该持续存在的东西的好地方（例如，从本地存储中获取的内容）。

如果需要创建一个依赖于页面特定元素的 afterDOMLoaded 脚本，在导航到新页面时可能会更改，您可以监听 “nav” 事件。每当页面加载时都会触发该事件（如果启用了 SPA 路由，则可能会在导航时发生）。

```typescript
document.addEventListener("nav", () => {
  // 在这里执行页面特定的逻辑
  // 例如，附加事件监听器
  const toggleSwitch = document.querySelector("#switch") as HTMLInputElement
  toggleSwitch.addEventListener("change", switchTheme)
  window.addCleanup(() => toggleSwitch.removeEventListener("change", switchTheme))
})
```

最佳实践是通过 `window.addCleanup` 跟踪任何事件处理程序，以防止内存泄漏。这将在页面导航时调用。

## 导入代码

当然，将代码作为字符串文字写入组件通常既不实际（也不受欢迎！）。

Quartz 支持通过 `.inline.ts` 文件导入组件代码。

```typescript
// @ts-ignore: typescript doesn't know about our inline bundling system
// 所以我们需要消除错误
import script from "./scripts/graph.inline"

export default (() => {
  function YourComponent() {
    return <button id="btn">点击我</button>
  }

  YourComponent.afterDOM = script
  return YourComponent
}) 满足 QuartzComponentConstructor
```

```typescript
// 在这里导入的任何内容都将被浏览器捆绑
import * as d3 from "d3"

document.getElementById("btn").onclick = () => {
  alert("按钮被点击了！")
}
```

此外，就像上面示例中所显示的一样，您可以在 `.inline.ts` 文件中导入包。这将由 Quartz 捆绑并包含在实际脚本中。

使用组件

创建自定义组件后，重新导出它在 `quartz/components/index.ts` ：

```typescript
import ArticleTitle from "./ArticleTitle"
import Content from "./pages/Content"
import Darkmode from "./Darkmode"
import YourComponent from "./YourComponent"

export { ArticleTitle, Content, Darkmode, YourComponent }
```

然后，您可以像在 `quartz.layout.ts` 中使用任何其他组件一样使用它。有关详细信息，请参见布局部分。

由于Quartz组件只是返回 `React` 组件的函数，因此您可以在其他 Quartz 组件中进行组合使用。

```typescript
import YourComponent from "./YourComponent"

export default (() => {
  function AnotherComponent(props: QuartzComponentProps) {
    return (
      <div>
        <p>它是嵌套的！</p>
        <YourComponent {...props} />
      </div>
    )
  }

  return AnotherComponent
}) 满足 QuartzComponentConstructor
```

提示
在 `quartz/components` 中查找更多Quartz组件示例，作为您自己组件的参考！


# 制作自己的插件

[原文](https://quartz.jzhao.xyz/advanced/making-plugins)


> 警告
> 本文档的这一部分将假定您具有 TypeScript 的工作知识，并包含描述 Quartz 插件应该具有的接口的代码片段。

Quartz 的插件是一系列针对内容的转换。下面是处理流水线的图示：

![](https://www.caoyang2002.top/usr/uploads/2024/04/3880798031.png)


所有插件都被定义为一个函数，该函数接受一个参数用于选项类型 `OptionType = object | undefined`，并返回一个与其所属类型相对应的对象。

```typescript
type OptionType = object | undefined
type QuartzPlugin<Options extends OptionType = undefined> = (opts?: Options) => QuartzPluginInstance
type QuartzPluginInstance =
  | QuartzTransformerPluginInstance
  | QuartzFilterPluginInstance
  | QuartzEmitterPluginInstance
```

接下来的几节将详细介绍每种插件类型可以实现的方法。在我们进行之前，让我们澄清一些更模糊的类型：

`BuildCtx` 在 `quartz/ctx.ts` 中定义。它由以下组成：

`argv` : 传递给 Quartz 构建命令的命令行参数
`cfg` : 完整的 Quartz 配置
`allSlugs` : 所有有效内容 `slug` 的列表（有关 `ServerSlug` 的更多信息，请参阅路径部分）
`StaticResources` 在 `quartz/resources.tsx` 中定义。它由以下组成：

`css`: 应加载的样式表的 URL 列表
`js`: 应加载的脚本列表。脚本用 JSResource 类型描述，该类型也在 `quartz/resources.tsx` 中定义。它允许您定义加载时间（在 DOM 加载前或后），是否应为模块以及脚本的源 URL 或内联内容。

## 转换器
转换器对内容进行映射，接受一个 Markdown 文件，并输出修改后的内容或向文件本身添加元数据。

```typescript
export type QuartzTransformerPluginInstance = {
  name: string
  textTransform?: (ctx: BuildCtx, src: string | Buffer) => string | Buffer
  markdownPlugins?: (ctx: BuildCtx) => PluggableList
  htmlPlugins?: (ctx: BuildCtx) => PluggableList
  externalResources?: (ctx: BuildCtx) => Partial<StaticResources>
}
```

所有转换器插件必须至少定义一个 name 字段以注册插件，并且一些可选函数，使您能够连接到转换单个 Markdown 文件的各个部分。

`textTransform` 在将文件解析为 `Markdown AST` 之前执行文本到文本的转换。
`markdownPlugins` 定义一个 `remark` 插件列表。remark 是一个工具，以结构化方式将 `Markdown` 转换为 `Markdown`的工具。
`htmlPlugins` 定义一个 `rehype` 插件列表。与 `remark` 类似，`rehype` 是一个工具，以结构化方式将 HTML 转换为 HTML。
externalResources 定义插件可能需要在客户端加载的任何外部资源。
通常对于 remark 和 rehype，您可以找到现有的插件可供使用。如果您想创建自己的 remark 或 rehype 插件，请查看使用 unified（底层 AST 解析器和转换器库）的插件的指南。

从 `remark` 和 `rehype` 生态系统借鉴的转换器插件的一个很好的例子是 `Latex` 插件：

```typescript
quartz/plugins/transformers/latex.ts
import remarkMath from "remark-math"
import rehypeKatex from "rehype-katex"
import rehypeMathjax from "rehype-mathjax/svg"
import { QuartzTransformerPlugin } from "../types"

interface Options {
  renderEngine: "katex" | "mathjax"
}

export const Latex: QuartzTransformerPlugin<Options> = (opts?: Options) => {
  const engine = opts?.renderEngine ?? "katex"
  return {
    name: "Latex",
    markdownPlugins() {
      return [remarkMath]
    },
    htmlPlugins() {
      if (engine === "katex") {
        // 如果您需要将选项传递给插件，您可以使用 [插件，选项] 的元组
        return [[rehypeKatex, { output: "html" }]]
      } else {
        return [rehypeMathjax]
      }
    },
    externalResources() {
      if (engine === "katex") {
        return {
          css: [
            // 基础 CSS
            "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css",
          ],
          js: [
            {
              // 修复复制行为：https://github.com/KaTeX/KaTeX/blob/main/contrib/copy-tex/README.md
              src: "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/contrib/copy-tex.min.js",
              loadTime: "afterDOMReady",
              contentType: "external",
            },
          ],
        }
      } else {
        return {}
      }
    },
  }
}
```

## 转换器

插件还经常做的一件事是解析文件并为该文件添加额外数据：

```typescript
export const AddWordCount: QuartzTransformerPlugin = () => {
  return {
    name: "AddWordCount",
    markdownPlugins() {
      return [
        () => {
          return (tree, file) => {
            // tree 是一个 `mdast` 根元素
            // file 是一个 `vfile`
            const text = file.value
            const words = text.split(" ").length
            file.data.wordcount = words
          }
        },
      ]
    },
  }
}

// 告诉 TypeScript 关于我们正在添加的自定义数据字段
// 其他插件也将意识到这个数据字段
declare module "vfile" {
  interface DataMap {
    wordcount: number
  }
}
```

最后，您还可以使用 `unist-util-visit` 包中的 `visit` 函数或 `mdast-util-find-and-replace` 包中的 `findAndReplace` 函数对 `Markdown` 或 `HTML AST` 进行转换。

```typescript
export const TextTransforms: QuartzTransformerPlugin = () => {
  return {
    name: "TextTransforms",
    markdownPlugins() {
      return [() => {
        return (tree, file) => {
          // 使用斜体版本替换 _text_
          findAndReplace(tree, /_(.+)_/, (_value: string, ...capture: string[]) => {
            // inner 是正则表达式括号内的文本
            const [inner] = capture
            // 返回一个 mdast 节点
            // https://github.com/syntax-tree/mdast
            return {
              type: "emphasis",
              children: [{ type: 'text', value: inner }]
            }
          })

         // 删除所有链接（替换为仅链接内容）
         // 通过 mdast 节点上的 'type' 字段进行匹配
         // 例如在这个例子中的 https://github.com/syntax-tree/mdast#link
          visit(tree, "link", (link: Link) => {
            return {
              type: "paragraph"
              children: [{ type: 'text', value: link.title }]
            }
          })
        }
      }]
    }
  }
}
```

所有转换器插件都可以在 `quartz/plugins/transformers` 下找到。如果您决定编写自己的转换器插件，请不要忘记在 `quartz/plugins/transformers/index.ts` 下重新导出它。

最后一句话：转换器插件相当复杂，所以如果您一开始不理解也不必担心。查看内置的转换器，了解它们如何在内容上操作，以更好地了解如何实现您想要做的事情。

## 过滤器

过滤器用于过滤内容，接受所有转换器处理的输出，并确定实际要保留的文件以及要丢弃的文件。

```typescript
export type QuartzFilterPlugin<Options extends OptionType = undefined> = (
  opts?: Options,
) => QuartzFilterPluginInstance

export type QuartzFilterPluginInstance = {
  name: string
  shouldPublish(ctx: BuildCtx, content: ProcessedContent): boolean
}
```

过滤器插件必须定义一个 `name` 字段和一个 `shouldPublish` 函数，该函数接受所有转换器处理的内容，并根据是否应将其传递给发射器插件返回 `true` 或 `false`。

例如，这是用于移除草稿的内置插件：

```typescript
quartz/plugins/filters/draft.ts
import { QuartzFilterPlugin } from "../types"

export const RemoveDrafts: QuartzFilterPlugin<{}> = () => ({
  name: "RemoveDrafts",
  shouldPublish(_ctx, [_tree, vfile]) {
    // 使用从转换器解析的 frontmatter
    const draftFlag: boolean = vfile.data?.frontmatter?.draft ?? false
    return !draftFlag
  },
})
```

## 发射器

发射器用于在内容的所有转换和过滤输出上进行缩减，并创建输出文件。

```typescript
export type QuartzEmitterPlugin<Options extends OptionType = undefined> = (
  opts?: Options,
) => QuartzEmitterPluginInstance

export type QuartzEmitterPluginInstance = {
  name: string
  emit(ctx: BuildCtx, content: ProcessedContent[], resources: StaticResources): Promise<FilePath[]>
  getQuartzComponents(ctx: BuildCtx): QuartzComponent[]
}
```

发射器插件必须定义一个 `name` 字段、一个 `emit` 函数和一个 `getQuartzComponents` 函数。`emit` 负责查看所有解析和过滤的内容，然后适当创建文件并返回插件创建的文件路径列表。

创建新文件可以通过常规的 `Node fs` 模块（例如 `fs.cp` 或 `fs.writeFile`）或者通过 `quartz/plugins/emitters/helpers.ts` 中的 `write` 函数进行，如果您正在创建包含文本的文件。`write` 具有以下签名：

```typescript
export type WriteOptions = (data: {
  // 构建上下文
  ctx: BuildCtx
  // 要发出的文件的名称（不包括文件扩展名）
  slug: ServerSlug
  // 文件扩展名
  ext: `.${string}` | ""
  // 要添加的文件内容
  content: string
}) => Promise<FilePath>
```

这是对向适当的输出文件夹写入并确保中间目录存在的简单包装。如果选择使用本机 Node fs API，请确保发出到 `argv.output` 文件夹。

如果您正在创建需要渲染组件的发射器插件，还有三件事需要注意：

您的组件应该使用 `getQuartzComponents` 声明一个 `QuartzComponents` 列表，用于构造页面。有关更多信息，请参阅创建组件页面。
您可以使用 `quartz/components/renderPage.tsx` 中定义的 `renderPage` 函数将 `Quartz` 组件呈现为 `HTML`。
如果需要将 HTML AST 渲染为 JSX，可以使用 `quartz/util/jsx.ts` 中的 `htmlToJsx` 函数。您可以在 `quartz/components/pages/Content.tsx` 中找到一个示例。

例如，以下是一个简化版本的内容页面插件，它呈现每个页面：

```typescript
quartz/plugins/emitters/contentPage.tsx
export const ContentPage: QuartzEmitterPlugin = () => {
  // 构造布局
  const layout: FullPageLayout = {
    ...sharedPageComponents,
    ...defaultContentPageLayout,
    pageBody: Content(),
  }


 const { head, header, beforeBody, pageBody, left, right, footer } = layout
  return {
    name: "ContentPage",
    getQuartzComponents() {
      return [head, ...header, ...beforeBody, pageBody, ...left, ...right, footer]
    },
    async emit(ctx, content, resources, emit): Promise<FilePath[]> {
      const cfg = ctx.cfg.configuration
      const fps: FilePath[] = []
      const allFiles = content.map((c) => c[1].data)
      for (const [tree, file] of content) {
        const slug = canonicalizeServer(file.data.slug!)
        const externalResources = pageResources(slug, resources)
        const componentData: QuartzComponentProps = {
          fileData: file.data,
          externalResources,
          cfg,
          children: [],
          tree,
          allFiles,
        }

        const content = renderPage(cfg, slug, componentData, opts, externalResources)
        const fp = await emit({
          content,
          slug: file.data.slug!,
          ext: ".html",
        })

        fps.push(fp)
      }
      return fps
    },
  }
}
```

请注意，它以 `FullPageLayout` 作为选项。它由共享布局和页面布局组合而成，这两个布局都是通过 `quartz.layout.ts` 文件提供的。

提示
在 Quartz 中查看 `quartz/plugins` 下更多插件的示例，作为您自己插件的参考！

# 国际化
[原文](https://quartz.jzhao.xyz/features/i18n)

国际化允许用户将Quartz界面中的文本翻译成各种支持的语言，而无需进行大量的代码更改。这可以通过 `quartz.config.ts` 中的 locale 配置字段进行更改。

`locale` 字段通常遵循一定的格式：`{language}-{REGION}`

`{language}` 通常是一个由两个小写字母组成的语言代码。
`{REGION}` 通常是一个由两个大写字母组成的地区代码。
有兴趣贡献吗？
我们欢迎翻译的 Pull Request！要贡献翻译，请执行以下操作：

在 `quartz/i18n/locales` 文件夹中，复制 `en-US.ts` 文件。
将其重命名为 `{language}-{REGION}.ts`，使其与上述格式的语言环境匹配。
填写翻译！
在 `quartz/i18n/index.ts` 中的 `TRANSLATIONS` 下添加条目。



# 设置你的 GitHub 仓库

[原文](https://quartz.jzhao.xyz/setting-up-your-GitHub-repository)

首先，确保你已经在本地克隆并设置了 Quartz。

然后，在 GitHub.com 上创建一个新的仓库。不要初始化新仓库，也不要添加 README、许可证或 gitignore 文件。

在 `GitHub.com` 仓库的“快速设置”页面顶部，单击剪贴板图标以复制远程仓库的 URL。

在你选择的终端中，导航到你的 Quartz 文件夹的根目录。然后，运行以下命令，将 `REMOTE-URL` 替换为你刚刚从上一步复制的 URL。

列出所有被跟踪的仓库

```bash
git remote -v
```

如果 origin 不匹配你自己的仓库，将你的仓库设置为 origin

```bash
git remote set-url origin REMOTE-URL
```

如果你没有将上游设置为远程仓库，添加它以便更新工作

```bash
git remote add upstream https://github.com/jackyzha0/quartz.git
```

然后，你可以同步内容以将其上传到你的仓库。这是一个辅助命令，将会将你的内容初始推送到你的仓库。

```bash
npx quartz sync --no-pull
```
致命错误：`--[no-]autostash` 选项只能在 `--rebase` 时有效。

你可能使用的是过时版本的 git。更新 git 应该会解决这个问题。

在以后的更新中，每当你想要 `将更新推送到你的仓库` 时，你只需要运行 `npx quartz sync`。

## 标志和选项

要获取完整的帮助选项，你可以运行 `npx quartz sync --help`。

大多数情况下，它们都有合理的默认值，但如果你有自定义设置，你可以覆盖它们：

`-d` 或 `--directory` ：内容文件夹。通常只是 content。
`-v` 或 `--verbose` ：打印额外的日志信息
`--commit` 或 `--no-commit` ：是否为你的更改进行 git 提交
`--push` 或 `--no-push`：是否将更新推送到你的 Quartz GitHub fork
`--pull` 或 `--no-pull` ：是否在推送之前尝试拉取来自你的 GitHub fork 的任何更新（即来自其他设备的更新）



# 编写内容

[原文](https://quartz.jzhao.xyz/authoring-content)

你的 Quartz 中的所有内容都应该放在 `/content` 文件夹中。Quartz 的主页内容位于 `content/index.md`。如果你已经设置了 Quartz，那么这个文件夹应该已经被初始化了。这个文件夹中的任何 Markdown 文件都将由 Quartz 处理。

推荐你使用 Obsidian 来编辑和维护你的 Quartz。它带有一个漂亮的编辑器和图形界面，可以预览、编辑和链接你的本地文件和附件。

一切都设置好了吗？让我们本地构建和预览你的 Quartz！

## 语法

由于 Quartz 使用 Markdown 文件作为编写内容的主要方式，因此它完全支持 Markdown 语法。默认情况下，Quartz 还附带了一些语法扩展，如 `Github Flavored Markdown`（脚注、删除线、表格、任务列表）和 Obsidian Flavored Markdown（标注、Wiki 链接）。

以下是 GitHub Flavored Markdown 的全部功能和语法：

1. **任务列表（Task Lists）**：使用 `- [ ]` 和 `- [x]` 语法创建待办事项列表，可以勾选或取消勾选每个项目。

2. **表格（Tables）**：使用管道符 `|` 和连字符 `-` 创建简单的表格，包括行和列。

3. **删除线（Strikethrough）**：使用双波浪线 `~~` 表示删除的文本。

4. **自动链接（Autolinks）**：GitHub Flavored Markdown 会自动将 URL 和电子邮件地址转换为链接。

5. **标记语法（Disallowed Raw HTML）**：GitHub Flavored Markdown 不允许使用原始 HTML 标记，以确保安全性。

6. **脚注（Footnotes）**：使用 `[^]` 语法创建文本注释，通常在页面底部显示。


Obsidian Flavored Markdown（OFM）提供了以下功能和语法：

1. **呼唤（Callouts）**：允许在文本中添加特殊样式的注释，以突出显示关键信息或提醒。

2. **内部链接（Wikilinks）**：可以使用双括号 `[[` 和 `]]` 来创建内部链接，链接到其他笔记或文件。

3. **时间戳链接（Timestamp Links）**：可以使用 `[[YYYY-MM-DD]]` 的格式创建时间戳链接，链接到特定日期的笔记。

4. **标签链接（Tag Links）**：可以使用 `#[tag]` 的格式创建标签链接，链接到具有相同标签的笔记。

这些特性使得 Obsidian 用户可以更方便地创建交互式笔记，并在笔记之间建立丰富的关联。


此外，Quartz 还允许你在笔记中指定额外的元数据，称为 frontmatter。

`content/note.md`

```bash
---
title: 示例标题
draft: false
tags:
  - 示例标签
---
```

你的其余内容在这里。你可以在这里使用 **Markdown** :)
一些常见的 frontmatter 字段，Quartz 本身支持：

title: 页面标题。如果没有提供，Quartz 将使用文件名作为标题。
description: 页面描述，用于链接预览。
aliases: 此笔记的其他名称。这是一个字符串列表。
tags: 此笔记的标签。
draft: 是否发布页面。这是在 Quartz 中创建私密页面的一种方式。
date: 表示笔记发布日期的字符串。通常使用 YYYY-MM-DD 格式。
同步你的内容

当你对 Quartz 满意时，你可以将更改保存到 GitHub。首先确保你已经设置了 GitHub 仓库，然后运行 `npx quartz sync`。

自定义

标题、标签、别名和 `cssclasses` 的 `frontmatter` 解析是 `Frontmatter` 插件的功能，日期由 `CreatedModifiedDate` 插件处理，描述由 `Description` 插件处理。查看插件页面以获取自定义选项。



# 配置

[原文](https://quartz.jzhao.xyz/configuration)

Quartz旨在非常可配置，即使您不懂编程也可以进行大多数配置。您应该需要的大多数配置只需编辑quartz.config.ts或更改quartz.layout.ts即可。

> 提示
> 如果您使用像VSCode这样具有TypeScript语言支持的文本编辑器来编辑Quartz配置，当您在配置中出现错误时，它会提醒您，帮助您避免配置错误！

Quartz的配置可以分为两个主要部分：

`quartz.config.ts`
```bash
const config: QuartzConfig = {
  configuration: { ... },
  plugins: { ... },
}
```

## 通用配置

这部分配置涉及可能影响整个站点的任何内容。以下是您可以配置的所有内容的列表：

`pageTitle`：站点标题。这也用于生成站点的RSS Feed时。
`enableSPA`：是否在站点上启用SPA路由。
`enablePopovers`：是否在站点上启用浮窗预览。
`analytics`：站点分析使用什么。值可以是
`null`：不使用分析；
`{ provider: 'google', tagId: '<your-google-tag>' }` ：使用Google Analytics；
`{ provider: 'plausible' }`（托管）或`{ provider: 'plausible', host: '<your-plausible-host>' }`（自托管）：使用Plausible；
`{ provider: 'umami', host: '<your-umami-host>', websiteId: '<your-umami-website-id>' }` ：使用Umami；
`{ provider: 'goatcounter', websiteId: 'my-goatcounter-id' }`（托管）或`{ provider: 'goatcounter', websiteId: 'my-goatcounter-id', host: 'my-goatcounter-domain.com', scriptSrc: 'https://my-url.to/counter.js' }`（自托管）：使用GoatCounter。
`locale` ：用于国际化和日期格式化。
`baseUrl` ：这用于需要绝对URL的站点地图和 RSS feeds，以了解站点的规范‘home’位于何处。这通常是站点的部署URL（例如，对于此站点，quartz.jzhao.xyz）。不包括协议（即`https://`）或任何前导或尾随斜杠。
如果您在 GitHub 页面上没有自定义域名的情况下托管，则此还应包括子路径。例如，如果我的存储库是 jackyzha0/quartz，则GitHub页面将部署到 `https://jackyzha0.github.io/quartz`，并且 `baseUrl` 将是 `jackyzha0.github.io/quartz`。
请注意，Quartz 4将尽可能避免使用此功能，并且在任何情况下都可以使用相对URL以确保您的站点正常工作。
`ignorePatterns` ：Quartz应忽略并在查找内容文件夹中查找文件时不应搜索的一组glob模式。有关更多详细信息，请参见私有页面。
`defaultDateType `：默认要在页面和页面列表上显示的日期是使用created、modified 还是 published。
`theme` ：配置站点外观。
`cdnCaching` ：如果为true（默认值），则使用Google CDN缓存字体。这通常会更快。如果要使Quartz下载字体以便自包含，请禁用（false）它。
`typography` ：要使用的字体。Google字体中的任何字体都可以在这里使用。
`header` ：标题使用的字体
`code` ：内联和块引用的字体。
`body` ：所有内容的字体
`colors` ：控制站点的主题。
`light` ：页面背景
`lightgray` ：边框
`gray` ：图链接，更重的边框
`darkgray` ：正文文本
`dark` ：标题文本和图标
`secondary` ：链接颜色，当前图节点
`tertiary` ：悬停状态和已访问的图节点
`highlight` ：内部链接背景，突出显示的文本，代码行
插件

您可以将Quartz插件视为内容上的一系列转换。



`quartz.config.ts`

```bash
plugins: {
  transformers: [...],
  filters: [...],
  emitters: [...],
}
```
变换器（transformers）对内容进行映射（例如，解析frontmatter、生成描述）
过滤器（filters）过滤内容（例如，过滤掉草稿）
发射器（emitters）在内容上减少（例如，创建RSS Feed或列出所有具有特定标签的文件的页面）
您可以通过在transformers、filters和emitters字段中添加、删除和重新排序插件来自定义Quartz的行为。

注意
每个节点都按顺序由每个变换器修改。某些转换器是位置敏感的，因此您可能需要特别注意它们是在哪些其他插件之前还是之后。

您应该小心将插件添加到与其插件类型相对应的正确条目中。例如，要添加ExplicitPublish插件（一个过滤器），您将添加以下行：

`quartz.config.ts`

```bash
filters: [
  ...
  Plugin.ExplicitPublish(),
  ...
],
```

要删除插件，应从 `quartz.config.ts` 中删除它的所有出现。

要进一步自定义插件，一些插件还可能具有自己的配置设置，您可以传递给它们。如果您没有传递配置，则插件将使用其默认设置。

例如，`Latex` 插件允许您传递一个字段，指定 `renderEngine` 以在 `Katex` 和 `MathJax` 之间进行选择。

`quartz.config.ts`

```bash
transformers: [
  Plugin.FrontMatter(), // 使用默认选项
  Plugin.Latex({ renderEngine: "katex" }), // 设置一些自定义选项
]
```

某些插件默认包含在 `quartz.config.ts` 中，但还有更多可用。

您可以在此处查看所有插件及其配置选项的列表。

如果您想制作自己的插件，请参阅制作自定义插件指南。


# 语法高亮

[原文](https://quartz.jzhao.xyz/plugins/SyntaxHighlighting)

## 插件/变换器

此插件用于在Quartz中的代码块中添加语法高亮。有关更多信息，请参见语法高亮。

注意
有关如何添加、删除或配置插件的信息，请参阅配置页面。

此插件接受以下配置选项：

`theme`：Shikiji 捆绑的主题之一的单独 ID。一个用于浅色模式，一个用于深色模式。默认为 `theme: { light: "github-light", dark: "github-dark" }`。
`keepBackground`：如果设置为 `true`，则将使用 Shikiji 主题的背景。如果为 `false`（默认值），则将改用 Quartz 主题颜色作为背景。
此外，您还可以在 `quartz/styles/syntax.scss` 文件中进一步覆盖颜色。

API

类别：变换器
函数名称：Plugin.SyntaxHighlighting()。
来源：quartz/plugins/transformers/syntax.ts

# SPA 路由

[原文](https://quartz.jzhao.xyz/features/SPA-Routing)

单页面应用程序风格的渲染。这可以防止出现未经样式化的内容闪烁，并提高了 Quartz 的流畅度。

在底层，这是通过劫持页面导航来完成的，而不是直接通过 GET 请求获取 HTML ，然后使用 micromorph 进行差异化和选择性地替换页面的部分。这使我们能够在不完全刷新页面的情况下更改页面的内容，减少浏览器需要加载的内容量。

## 配置

禁用SPA路由：将 `quartz.config.ts` 中配置的 `enableSPA` 字段设置为 `false`。
