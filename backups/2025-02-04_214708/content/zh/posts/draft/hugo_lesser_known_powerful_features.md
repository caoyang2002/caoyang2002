+++
title = 'Hugo 不为人知的强大特性'
date = 2025-01-26T01:44:00+08:00
draft = true
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
+++
# Hugo 不为人知的强大特性

Hugo 被称为世界上最快的静态网站生成器，但大多数人只用它来写写博客。这太浪费了，其实它还有很多好玩的地方，我目前的博客主题就是靠的 Hugo，可以说是非常强大了。今天我们来挖掘一下它的进阶特性。

## 1. 模板继承的黑魔法

```go
{{/* 基础模板: baseof.html */}}
<!DOCTYPE html>
<html>
  <head>
    {{ block "head" . }}{{ end }}
  </head>
  <body>
    {{ block "main" . }}{{ end }}
  </body>
</html>

{{/* 子模板 */}}
{{ define "main" }}
  <div>这里是实际内容</div>
{{ end }}
```

看到这个`.`了吗？这是Hugo的上下文传递，相当于其他语言的`this`。很多人不知道，它可以这样玩：

```go
{{ with .Site.Params }}
  {{ .author }} // 直接用点号访问，清爽多了
{{ end }}
```

## 2. 页面捆绑的秘密

```
content/
  └── posts/
      └── tech/
          ├── index.md      # 主文章
          ├── image1.jpg    # 相关资源
          └── data.json     # 数据文件
```

很多人还在用静态目录放图片，太傻了。用页面捆绑，迁移文章时图片跟着走，多爽！

## 3. 自定义短代码进阶

```go
{{/* shortcodes/notice.html */}}
{{ $type := .Get 0 }}
{{ $message := .Get 1 }}
<div class="notice {{ $type }}">
    {{ $message | markdownify }}
</div>
```

用法：
```markdown
{{ % notice "warning" "这是一个**警告**" % }}
```

看到`markdownify`了吗？它能把Markdown转HTML。结合短代码，威力无穷。

## 4. 数据模板黑科技

```yaml
# data/prices.yaml
basic:
  monthly: 9.99
  yearly: 99.99
```

```go
{{ $yearly := index .Site.Data.prices.basic "yearly" }}
{{ $monthly := index .Site.Data.prices.basic "monthly" }}
{{ $savings := sub (mul $monthly 12) $yearly }}

节省: {{ $savings }}
```

Hugo的数学计算被严重低估了。价格计算、数据统计，它都能搞。

## 5. 输出格式耍花活

```go
{{ $data := getJSON "api.json" }}
{{ $data | jsonify (dict "indent" "  ") }}
```

格式化JSON、压缩HTML、自动生成RSS...Hugo都能处理。你的CI/CD流程可以更清爽了。

## 踩坑提醒

1. `.Params`和`.Site.Params`是不同的：
   - `.Params`：页面级参数
   - `.Site.Params`：全站参数
   别混用，否则Debug能让你怀疑人生。

2. 记住：Hugo的模板是强类型的。你可能会看到这样的错误：
```
error: wrong type for value; expected string; got int
```
用`printf "%v"`调试类型，能省很多事。

3. 性能陷阱：
```go
{{ range .Pages }}
  {{ .Content }} // 全文遍历，性能杀手
{{ end }}
```
用`.Summary`或`.Plain`代替，除非真需要全文。

## 实战经验

1. 开发环境配置：
```bash
hugo server --disableFastRender --navigateToChanged
```
修改即时生效，爽到飞起。

2. 用`resource.ExecuteAsTemplate`处理JS/CSS：
```go
{{ $js := resources.Get "js/main.js" | resources.ExecuteAsTemplate "js/main.js" . }}
```
配置信息直接注入前端，优雅！

代码写得再花哨，不解决实际问题都是扯淡。我的建议是：先搞清楚你要解决什么问题，再来看这些技巧。
