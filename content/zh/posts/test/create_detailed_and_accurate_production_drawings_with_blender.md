+++
title = '使用 Blender 创建详细且准确的生产图纸'
date = 2026-02-05T14:34:53+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
cover = "https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/production-drawing.avif)](https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/production-drawing.avif"
+++

[查看原文](https://cn.windows.day/?p=115726)

生产图纸是许多产品制造过程中不可或缺的一部分。这些文件为机械师和熟练工匠提供了制造精密零件所需的尺寸、材料规格和其他重要细节。当然，它们看起来也非常酷。

使用像 Blender 这样的工具制作自己详细且准确的生产图纸很容易，但你该如何操作呢？加入我们，一起探索将任何 3D 模型转化为美观生产图纸的步骤，这些图纸无论挂在墙上还是作为现实产品，都同样出色。

## 在 Blender 中制作生产图纸需要什么？

在开始制作你的生产图纸之前，你需要收集一些资源。这个项目需要两个 Blender 插件，不过它们都是免费的，可以在网上找到。

- Blender 2.8 及以上
- TechDraw Blender 插件
- MeasureIt Blender 插件
- 3D 模型/混合文件

| 插件名称      | 核心作用               | 关键功能                                                     |
| :------------ | :--------------------- | :------------------------- |
| TechDraw  | 创建2D工程图布局   | 1. 添加标准尺寸图纸背景（如A4）。<br>2. 自动生成模型的多个标准视图（如主视图、俯视图、侧视图）。<br>3. 布局图纸，准备渲染。 |
| MeasureIt | 进行精确测量和标注 | 1. 测量长度：点对点、物体间距、到原点的距离等。<br>2. 标注尺寸：将测量值以尺寸线形式显示在3D视图或渲染图上。<br>3. 添加标签和注释。<br>4. 其高级分支 **MeasureIt_ARCH** 则能创建更专业的建筑或机械图纸，并支持导出为SVG或DXF格式。 |

## 步骤 1：安装 Blender 插件
![安装插件](https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/blender-add-measureit.avif)

Blender 有一个方便的内置插件库，使第一步非常简单。

### MeasureIt

前往 **编辑** > **首选项** > **插件**，然后搜索 **MeasureIt**。你应该会看到同名的插件出现，然后可以点击左上角的复选框来激活它。

![安装 MeasureIt 插件](https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/blender-install-techdraw.avif)

### TechDraw

在安装之前，您需要从 GitHub 下载 [**TechDraw**](https://github.com/Laurent26/techdraw) 插件。

完成后，返回 Blender 的 **插件** 菜单，并在窗口顶部选择 **安装**。然后，选择随插件提供的 zip 文件并打开它以进行安装。安装完成后，您会在菜单中看到该插件，但需要在左上角勾选复选框以启用它。

## 步骤 2：导入/打开您的 3D 文件

![导入](https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/importing-an-stl-in-blender.avif)

安装完插件后，是时候在 Blender 中打开您的 3D 模型文件了。打开文件的方式取决于您可以访问的文件类型。BLEND 文件可以通过进入 **文件** > **打开** 然后选择您想要操作的文件来打开。其他文件类型可以通过进入 **文件** > **导入** > **以…导入**（选择您的文件类型），然后从打开的窗口中选择文件来导入。

![导入模型](https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/blender-change-dimensions.avif)

在继续之前，您需要检查您的尺寸。您可以通过转到屏幕右侧的**场景属性**菜单来查找并更改您正在使用的单位；我们为项目选择了毫米。通过转到屏幕右侧的**项目**选项卡并在列表底部更改尺寸来修改模型的尺寸。

## 步骤 3：添加背景/摄像头

安装 TechDraw 后，它会在屏幕右侧添加一个选项卡。

![选项卡](https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/blender-add-sheet.avif)

要添加背景，请选择 **TechDraw** 选项卡，并展开 **布局设置** 部分，以查看可用的 **图纸** 选项。我们选择了横向的 A4 格式，但你应该选择与正在处理的对象尺寸相匹配的纸张大小。在点击 **添加图纸** 后，可能需要编辑图纸的尺寸。

![添加图纸](https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/blender-camera-added.avif)

在场景中你还需要一台相机来生成高质量的技术图纸渲染，而这是 TechDraw 可以为你完成的。在 **布局设置** 菜单的相机部分，为你的相机添加一个所属集合，然后点击 **添加相机**。

在场景中放置好相机和背景板后，你可以移至 **布局设置** 面板中的 **渲染设置**。选择用于 **背景板** 的主背景对象，以及你刚添加的相机作为 **相机**，然后点击 **更新设置** 来自动调整相机大小。如果此时渲染图像，你会注意到可见内容非常有限。

![img](https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/blender-world-properties.avif)

转到屏幕右侧的 **场景属性** 部分，将 **表面颜色** 更改为白色，然后进入 **渲染属性** 部分，打开 **Freestyle** 选项。这将使你的对象在渲染图像时显示为线条轮廓。

![img](https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/blender-render-settings-1.avif)

## 步骤4：使用您的3D模型创建布局

![img](https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/technical-drawing-render-without-models.avif)

正如你从上面的渲染图中看到的，这张制作图非常单调。在我们添加尺寸之前，需要更多的对象，但这是 TechDraw 插件可以帮助我们的地方。前往 **零件设置** 选项卡，并将你正在处理的对象选择为 **目标**。

![img](https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/techdraw-parts-settings.avif)

在下方，您将看到一个复选框网格，它可以以不同的方向创建您的对象副本。我们的砖块对象只需要从三个方向查看即可获得其所有尺寸：顶部、侧面和底部。勾选您想要创建的副本的每个复选框，然后点击**添加部件视图**来创建它们。如果您的部件彼此之间太远或太近，可以更改**绘制距离**修饰符。

## 第5步：为您的生产图添加尺寸

![img](https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/vertices-selected-for-measuring.avif)

终于到了为你的生产图添加尺寸的时候了。首先选择你要添加尺寸的对象，并进入**编辑模式**，同时启用**顶点选择**。选择两个之间有线段的顶点，然后在视口右侧进入**视图**选项卡。你应该会在这里看到一个标为**MeasureIt**的选项卡。

![img](https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/measurement-on-block.avif)

在 **添加测量** 部分点击 **段**，以在您选择的顶点之间创建测量。您可以在 MeasureIt 工具的 **项目** 部分找到您添加的每个测量，从而可以更改测量注释的颜色和位置。

除了线段测量外，您还可以在设计中添加角度、弧线、标签和其他注释。我们的模块非常简单，但您可能希望在制作图示时更加富有创意。

## 步骤 6：添加材料和其他规格（可选）

![img](https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/blender-changing-text.avif)

你在第3步中添加到项目的工作表有一个用于详细说明你设计的部分。你可以通过选择相关文本并进入**编辑模式**来编辑它，这将允许你直接更改文本。你也可以选择完全删除文本或在Blender中添加新文本以改进你的绘图。

## 第7步：制作施工图

![img](https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/rendering-images.avif)

这个过程的最后一步到了，现在是时候创建你从一开始就想要的图像了。首先，进入 MeasureIt 工具的 **渲染** 选项卡，然后点击 **渲染**。完成渲染需要几秒钟，但你可以通过进入主 **渲染菜单** > **渲染图像** 来继续操作。图像渲染完成后，关闭出现的窗口。

![渲染](https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/composition-nodes.avif)

你需要将你创建的两张图片叠加在一起（Blender 会为你保存它们），这是在 **合成工作区** 完成的。在执行以下操作以获得上图中的效果之前，勾选标有 **使用节点** 的选项。使用 Blender 节点可能是一个具有挑战性的学习过程，但你可以在网上找到相关的指南来帮助你。

- 添加一个 **Alpha 叠加颜色** 节点，并将其连接到 **渲染层** 节点。
- 添加一个**图像输入**节点，并将其连接到**Alpha Over**节点，然后再将其链接到名为**measureit_output**的图像。
- 添加一个 **查看器输出** 节点，并将其连接到 **Alpha Over** 节点。

![img](https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/save-production-drawing.avif)

在单独的面板中打开 **图像编辑器**，并使用编辑器顶部的下拉菜单将其链接到名为 **查看器节点** 的图像。这将显示包括背景、对象和尺寸的图像。在工具栏上，点击 **图像** > **另存为** 来创建生产图纸的最终版本。

## 为您的施工图添加特色

![为您的施工图添加特色](https://cn.windows.day/common-images/using-blender-create-detailed-accurate-production-drawings/production-drawing-with-color.avif)

我们创建的生产图纸非常适合制造，但它看起来并不漂亮。你可以做很多事情来增强生产图纸的视觉吸引力。改变模型的颜色是一个不错的开始，但你也可以更改所使用的字体，甚至为你的图纸找到新的背景。

## 使用您的生产图纸

像这样的生产图纸在制造业中至关重要，但如果你投入足够的时间，它们也可以成为出色的艺术品。像 Fractory 和 Xiometry 这样的网站需要这样的文档，以便使用 CNC 机床和其他工业设备创建产品。当然，这些图纸也可以对你自己的工作非常有用。
