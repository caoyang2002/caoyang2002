+++
title = '免费字体'
date = 2026-02-19T16:33:16+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
+++

https://wordshub.github.io/free-font/font.html?SiYuanSongTi_Regular

字体转换： https://formafont.com/zh

前端 nodejs 使用 https://github.com/wc-ex/cn-fontsource

# 几个技巧把字体文件压缩到十分之一的体积

有时候我们需要让网页加载自定义字体文件，但是通常的字体格式（TTF、OTF）体积太大了，这就需要我们将其转换为更小体积的字体文件格式（[WOFF2](https://zhida.zhihu.com/search?content_id=216441698&content_type=Article&match_order=1&q=WOFF2&zhida_source=entity)）。

之前我尝试使用类似 [CloudConvert](https://zhida.zhihu.com/search?content_id=216441698&content_type=Article&match_order=1&q=CloudConvert&zhida_source=entity) 的在线工具去转换 OTF 字体文件，但是不知道为何转换出来的字体损坏了，无法使用。经过多方面研究，现在我找到了一种本地压缩字体可行的方法，因此分享给大家。

## **字体格式科普**

常见的字体格式有以下几种，这里只作简单介绍。

### **TTF**

> TTF（TrueTypeFont）是Apple 公司和Microsoft公司共同推出的[字体](https://link.zhihu.com/?target=https%3A//baike.baidu.com/item/%E5%AD%97%E4%BD%93/5167264%3FfromModule%3Dlemma_inlink)文件格式，随着 windows 的流行，已经变成最常用的一种字体文件表示方式。（来源：[百度百科](https://link.zhihu.com/?target=https%3A//baike.baidu.com/item/ttf/10525802)）

这种格式的字体文件体积比较大，以[思源宋体](https://link.zhihu.com/?target=https%3A//github.com/adobe-fonts/source-han-serif/tree/release)为例，字体文件可以达到 24MB+，通常只用作安装到计算机中的字体，或者在网页中设备不支持 WOFF2 字体情况的兜底处理。

### **OTF**

> **OpenType**，是一种可缩放字体（scalable font）[电脑字体](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/%E7%94%B5%E8%84%91%E5%AD%97%E4%BD%93)类型，采用[PostScript](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/PostScript)格式，是[美国](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/%E7%BE%8E%E5%9C%8B)[微软公司](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/%E5%BE%AE%E8%BB%9F%E5%85%AC%E5%8F%B8)与[Adobe](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/Adobe)公司联合开发，用来替代[TrueType](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/TrueType)字体的新字体。这类字体的[文件扩展名](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/%E6%96%87%E4%BB%B6%E6%89%A9%E5%B1%95%E5%90%8D)有`.otf`、`.ttf`、`.ttc`，类型代码是`OTTO`，现行标准为OpenType 1.9。（来源：[维基百科](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/OpenType)）

可以理解为和 TTF 字体差不多，这里我们主要讨论体积问题，OTF 字体文件体积也很大，基本和 TTF 差不多。

### **WOFF & WOFF2**

> **Web开放字体格式**（Web Open Font Format，简称**WOFF**）是一种网页所采用的[字体](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/%E5%AD%97%E9%AB%94)格式标准。此字体格式发展于2009年，[[3\]](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/Web%E9%96%8B%E6%94%BE%E5%AD%97%E5%9E%8B%E6%A0%BC%E5%BC%8F%23cite_note-spec-3)由[万维网联盟](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/%E4%B8%87%E7%BB%B4%E7%BD%91%E8%81%94%E7%9B%9F)的Web字体工作小组标准化，现在已经是[推荐标准](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/W3C%E6%8E%A8%E8%8D%90%E6%A0%87%E5%87%86)。[[4\]](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/Web%E9%96%8B%E6%94%BE%E5%AD%97%E5%9E%8B%E6%A0%BC%E5%BC%8F%23cite_note-charter-4)此字体格式不但能够有效利用压缩来减少文件大小，并且不包含加密也不受DRM（[数字著作权管理](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/%E6%95%B8%E4%BD%8D%E8%91%97%E4%BD%9C%E6%AC%8A%E7%AE%A1%E7%90%86)）限制。（来源：[维基百科](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/Web%E9%96%8B%E6%94%BE%E5%AD%97%E5%9E%8B%E6%A0%BC%E5%BC%8F)）

这是专门给网页使用的字体格式，体积非常小，实测压缩[思源宋体](https://link.zhihu.com/?target=https%3A//github.com/adobe-fonts/source-han-serif/tree/release)字体文件，可以把体积压缩到 OTF 字体 70% 的大小。

WOFF 和 WOFF2 的区别在于：

> WOFF本质上是包含了基于[SFNT](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/SFNT)的字体（如[TrueType](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/TrueType)、[OpenType](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/OpenType)或其他开放字体格式），且这些字体均经过WOFF的编码工具压缩，以便嵌入网页中。[[3\]](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/Web%E9%96%8B%E6%94%BE%E5%AD%97%E5%9E%8B%E6%A0%BC%E5%BC%8F%23cite_note-spec-3)WOFF 1.0使用[zlib](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/Zlib)压缩，[[3\]](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/Web%E9%96%8B%E6%94%BE%E5%AD%97%E5%9E%8B%E6%A0%BC%E5%BC%8F%23cite_note-spec-3)文件大小一般比TTF小40%。[[11\]](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/Web%E9%96%8B%E6%94%BE%E5%AD%97%E5%9E%8B%E6%A0%BC%E5%BC%8F%23cite_note-11)而WOFF 2.0使用[Brotli](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/Brotli)压缩，文件大小比上一版小30%。（来源：[维基百科](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/Web%E9%96%8B%E6%94%BE%E5%AD%97%E5%9E%8B%E6%A0%BC%E5%BC%8F)）

因此，一般推荐直接使用 WOFF2。

### **[SVG](https://zhida.zhihu.com/search?content_id=216441698&content_type=Article&match_order=1&q=SVG&zhida_source=entity)**

> **可缩放矢量图形**（英语：Scalable Vector Graphics，缩写：**SVG**）是一种基于[可扩展标记语言](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/XML)（XML），用于描述二维[矢量图形](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/%E7%9F%A2%E9%87%8F%E5%9B%BE%E5%BD%A2)的图形格式。SVG由[W3C](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/W3C)制定，是一个[开放标准](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/%E5%BC%80%E6%94%BE%E6%A0%87%E5%87%86)。（来源：[维基百科](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/%E5%8F%AF%E7%B8%AE%E6%94%BE%E5%90%91%E9%87%8F%E5%9C%96%E5%BD%A2)）

这种字体是非常早期的标准，**已经不推荐使用**。我们可以从 [Can i use](https://link.zhihu.com/?target=https%3A//caniuse.com/%3Fsearch%3Dsvg%20font) 里面查到它的兼容性非常差：

![img](https://pic2.zhimg.com/v2-2c871e94a049fc43c3c3a308c803ee21_1440w.jpg)

全都可以变红

## **两步压缩**

这部分是正式的压缩方法了，主要分为两步，分别是：取子集、压缩。

这里我使用到的是 Python 的一个库：[fonttools](https://link.zhihu.com/?target=https%3A//github.com/fonttools/fonttools)，使用最新版 Python 的 pip 命令安装即可在 Shell 中使用：

```text
 $ pip install fonttools
```

### **取子集**

中文汉字数量很多，以[思源宋体](https://link.zhihu.com/?target=https%3A//github.com/adobe-fonts/source-han-serif/tree/release)为例，思源宋体遵循 GB 18030 和通用规范汉字表，包含 8105 个规范字（来源：[少数派](https://link.zhihu.com/?target=https%3A//sspai.com/post/38705)），可能还有其他语言的字符，实际字符数量肯定是远超这个数字的。

实际上，常用汉字数量也就 3500 个左右，如果你的文本相对固定，可以考虑删减掉其他不常用的汉字。

极端做法是只保留文本中出现的字符，其他的全部删掉，但是我个人更倾向于折中保留 3500 汉字，在未来如果修改了文本，也不至于每次都要重新压缩一遍字体。

这种删减字符的做法叫**“取子集”**。取子集我们需要定义一个纯文本文件，里面包含所有要保留的字符，这里给大家分享一个自己正在使用的文件：[现代汉语常用 3500 字.txt](https://link.zhihu.com/?target=https%3A//gist.github.com/f94d0c594e47113b209156a653aaba93%23file-%E7%8E%B0%E4%BB%A3%E6%B1%89%E8%AF%AD%E5%B8%B8%E7%94%A83500%E5%AD%97-txt)。

使用以下命令即可对字体文件取子集：

```text
 $ fonttools subset "$input_file" --text-file="$text_file" --output-file="$output_file"
```

变量含义：

- $input_file：输入的字体文件。
- $text_file：定义保留字符的纯文本文件路径。
- $output_file：输出的字体文件路径。

我测试对[思源宋体](https://link.zhihu.com/?target=https%3A//github.com/adobe-fonts/source-han-serif/tree/release)取完子集后，文件体积从 25.4MB 减少到了 2.5MB，足足小了 1/10。

### **压缩**

取完子集后，我们将对字体文件进行压缩，主要是压缩成 WOFF2 格式。

压缩命令很简单：

```text
 $ fonttools ttLib.woff2 compress "$input_file" -o "$output_file"
```

变量含义：

- $input_file：输入的字体文件。
- $output_file：输出的字体文件路径。

对上面已取子集的字体经过压缩后，体积差不多减少了 70%，从 2.5MB 减小到了 1.9MB。

## **组合方法**

经过上面两个步骤后，字体体积大约减少了 1/10 还要小，极大提高了加载速度。

但是有时候我们需要用到一些非常用但是又不是很生僻的汉字，这里分两种情况：如果文本是确定的，可以将这些字加入到定义保留字符的文件中即可；如果文本不确定（比如有用户输入），又对字体要求较高，我们也可以仅仅执行压缩步骤，也能将字体体积减小到 70%，总比没有好。

## **脚本**

因为经常有需要压缩字体（批量）的需求，所以我自己写了个小脚本来使用，现在分享给大家：[压缩脚本.sh](https://link.zhihu.com/?target=https%3A//gist.github.com/f94d0c594e47113b209156a653aaba93%23file-%E5%8E%8B%E7%BC%A9%E8%84%9A%E6%9C%AC-sh)。

这个脚本可以选择是否取子集，如果需要取子集，输入的第二个参数需要为 true，否则就不用提供。大家可以根据实际情况去进行修改。

本作品采用[知识共享署名-相同方式共享 4.0 国际许可协议](https://link.zhihu.com/?target=http%3A//creativecommons.org/licenses/by-sa/4.0/)进行许可。
