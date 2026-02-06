+++
title = '5 个 MATLAB 开源替代方案'
date = 2026-02-06T11:44:18+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
+++

> [本文](https://open-source.com.cn/alternatives/matlab)最初发表于 2016 年 6 月，现已更新，提供了一些您可能希望考虑的其他选项。

对于许多数学、物理科学、工程、经济学以及其他具有大量数值成分领域的学生来说，MATLAB 是他们第一次接触编程或一般科学计算。

它可能是一个很好的学习工具，尽管（以我的经验）学生和研究人员使用 MATLAB 进行的许多事情都不是特别苛刻的计算；相反，它们可以很容易地使用任何数量的基本脚本工具进行，无论是否带有统计或数学导向的软件包。然而，它在许多学术环境中几乎无处不在，带来了庞大的用户社区，他们熟悉该语言、插件和一般功能。

但是 MATLAB 是一种专有工具。在无法访问其源代码的情况下，您对其工作方式以及如何修改它的理解有限。对于学术环境之外的许多人来说，它也贵得令人望而却步，单个副本的许可费用可能高达数千美元。

幸运的是，有很多很棒的开源替代方案。根据您的确切目标，您可能会发现其中一个或另一个更适合您的特定需求。以下是三个值得考虑的方案

## Julia

[Julia](https://julia-lang.cn/) 是一种动态类型编程语言，具有 [Lisp](https://open-source.com.cn/article/21/5/learn-lisp) 风格的宏、用于并行计算的内置原语以及专为矩阵操作、数据可视化等设计的功能。它旨在感觉像一种脚本语言，而不是 C 风格的编程语言，甚至具有交互模式 (REPL)，并且可以通过其嵌入 API 嵌入到其他语言中。

Julia 的用户有很多理由喜欢它的语法和功能，但一些流行的例子包括它的*广播*功能，它允许您将函数应用于一个或多个数组，而无需编写复杂的循环，其简单的数组函数允许您旋转和重塑数组、矩阵变换、自动微分、原生 Unicode 支持、集成单元测试、轻松并行化以及更简单的全方位语法，且不损失功能（并提高了代码效率）。

Julia 拥有一个活跃的社区围绕其开发和使用，因此它也针对特定领域进行了定制，包括图像处理 [(JuliaImages)](https://juliaimages.github.io/latest/)、生物学 [(BioJulia)](https://github.com/BioJulia)、量子物理学 [(QuantumBFS)](https://github.com/QuantumBFS)、非线性动力学 [(JuliaDynamics)](https://github.com/JuliaDynamics)、经济学 [(QuantEcon)](https://github.com/QuantEcon)、天文学 [(JuliaAstro)](https://juliaastro.github.io/) 等。

Julia 在 [MIT 许可证](https://open-source.com.cn/MIT license) 下获得许可，可以从 [julialang.org](https://julia-lang.cn/) 下载。

## GNU Octave

[GNU Octave](https://gnu.ac.cn/software/octave/) 可能是最知名的 MATLAB 替代方案。Octave 已经活跃开发了近三十年，可在 Linux、Windows 和 Mac 上运行，并且为大多数主要发行版打包。如果您正在寻找一个尽可能接近实际 MATLAB 语言的项目，Octave 可能很适合您；它力求实现完全兼容性，因此您为 MATLAB 开发的许多项目可能无需修改即可在 Octave 中运行。

Octave 为默认附带的版本 4 之外的前端交互提供了许多不同的选择；有些比其他更像 MATLAB 的界面。Octave 的 [维基百科页面](https://en.wikipedia.org/wiki/GNU_Octave) 列出了几个选项。

Octave 在 [GPL](https://gnu.ac.cn/copyleft/gpl.html) 下获得许可，其源代码可以在 GNU [下载站点](ftp://ftp.gnu.org/gnu/octave) 上找到。

## NumPy

[NumPy](https://numpy.com.cn/) 是用于 Python 科学计算的主要软件包（顾名思义）。它可以处理 N 维数组、复杂矩阵变换、线性代数、傅里叶变换，并且可以充当 C 和 C++ 集成的网关。它已用于游戏和电影视觉效果开发领域，并且是 SciPy Stack 的基本数据数组结构，SciPy Stack 是一个基于 Python 的数学、科学和工程软件生态系统。NumPy 在 [BSD 许可证](https://numpy.com.cn/license.html#license) 下获得许可，并且软件包可用于 Linux、Windows 和 Mac OS X。

## Scilab

[Scilab](http://www.scilab.org/) 是另一个用于数值计算的开源选项，可在所有主要平台（包括 Windows、Mac 和 Linux）上运行。Scilab 可能是 Octave 之外最知名的替代方案，并且（像 Octave 一样）它在实现上与 MATLAB 非常相似，尽管完全兼容性不是项目开发人员的目标。

Scilab 作为开源在 GPL 兼容的 [CeCILL](http://www.scilab.org/scilab/license) 许可证下分发，其 [源代码](http://www.scilab.org/development/sources/stable) 在项目网站上提供。

## Sage

[SageMath](http://www.sagemath.org/index.html) 是另一个开源数学软件系统，对于那些寻求 MATLAB 替代方案的人来说可能是一个不错的选择。它建立在各种著名的基于 Python 的科学计算库之上，其自身的语言在语法上与 Python 相似。它具有许多功能，包括命令行界面、基于浏览器的笔记本、用于在其他文档中嵌入公式的工具，当然还有许多数学库。

SageMath 在 [GPL](https://gnu.ac.cn/copyleft/gpl.html) 许可证下可用，其源代码可以在 [项目网站](http://www.sagemath.org/download-source.html) 上找到。

------

此列表仅触及研究人员和学生可能选择用作 MATLAB 开源替代方案的工具的皮毛。R、Julia、Python 和其他标准编程语言可能非常适合您，具体取决于您的确切需求。您可能需要考虑的其他一些开源工具包括：

- [Genius Mathematic Tool](http://www.jirka.org/genius.html)，一个积极开发的计算器程序和研究工具。它使用 Genius Extension Language 为 Linux 和 Unix 计算机编写，并在 [GPL GNU](https://gnu.ac.cn/licenses/gpl.html) 许可证下可用。
- [Maxima](http://maxima.sourceforge.net/)，另一个经常更新的 MATLAB 替代方案。它基于 Macsyma，这是一个“传奇的计算机代数系统”，于 1960 年代在 MIT 开发，可以在 Linux、Mac OS X 和 Windows 上编译，并在 [GPLv2](https://sourceforge.net/directory/license:gpl/) 下可用。
- [SymPy](http://www.sympy.org/en/index.html)，另一个 [BSD](https://github.com/sympy/sympy/blob/master/LICENSE) 许可的 Python 库，用于符号数学。它可以安装在任何运行 Python 的计算机上。它的目标是成为一个完整的计算机代数系统；拥有一个活跃的开发社区，定期发布版本；并在许多其他项目（包括上面的 SageMath）中使用。

您是否使用过这些工具或其他工具作为 MATLAB 的替代方案？您更喜欢哪一个，为什么？请在下面的评论中告诉我们。
