+++
date = '2023-07-15T09:31:37+08:00'
draft = false
title = '函数栈帧的创建和销毁'
toc = true
+++

`C/C++`

函数栈帧的创建和销毁

在学习最基础的C语言程序的语法与使用时，但你是否有疑问？

比如：

- 函数的作用域是怎么形成的呢？

- 局部变量是如何创建的？

- 为什么未初始化的局部变量的值是随机值或是乱码呢？

- 函数是如何传参的？

  传参的顺序又是怎么样的呢？

- 形参和实参的关系是什么？

- 函数的调用是怎么实现的呢？

- 函数调用结束后是怎么返回的呢？

- 为什么会存在函数递归的最大深度呢？

  到达最大深度所提出的堆栈溢出错误是什么意思呢？

当你了解了函数的栈帧创建与销毁的时候，这些疑惑将会一一解开！带着这些问题，我们来进入函数栈帧！



由于篇幅较长，本系列文章共分为**上、下**两篇。本篇为上篇，将主要介绍：

**有疑问欢迎在公众号后台回复。**

1. **什么是寄存器？**
2. **什么是栈？**
3. **函数栈帧的形成过程**
4. **函数变量的形成过程**

了解函数栈帧需要涉及到反汇编操作，笔者会根据相关的汇编指令来介绍。



圆规正转，进入正题！









# 什么是寄存器？







首先需要了解的：**什么是寄存器？**

计算机硬件中，具有存储功能的硬件有什么？

它们分别是 硬盘 --> 内存 --> 高速缓存(cache) --> 寄存器，它们4个中访问速度和存储速度由上至下不断递增；

同时，它们的大小是从下至上依次递减的。

到最顶上的寄存器，它的存储空间可能只有4byte位的存储单元大小，但它的**访问速度是最快**的，因为寄存器一般是集成在CPU上，与内存是不同的独立的存储空间。

常言道，网速飞快是坐在服务器上打游戏，而读取速度越快就是坐在CPU上读取，寄存器读取快就是这个道理。

![存储硬件](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/storage_hardware.png)



### 寄存器分类

计算机的寄存器还分多种，在程序中我们常用到：

- 一般寄存器:EAX、EBX、ECX、EDX

- ax:累积暂存器，bx:基底暂存器，cx:计数暂存器，ed:资料暂存器

- 索引暂存器:ESI、EDI

- si:来源索引暂存器，di:目的索引暂存器

- 堆叠、基底暂存器:ESP、EBP

- sp:堆叠指标暂存器，bp:基底指标暂存器；

  这两个寄存器，也是函数栈帧中最重要的两个寄存器

其中：

- EAX、ECX、EDX、EBX：

  为ax,bx,cx,dx的延伸，各为32位

- ESI、EDI、ESP、EBP：

  为si,di,sp,bp的延伸，各32位

- EAX, EBX, ECX, EDX, ESI, EDI, EBP, ESP等都是X86 汇编语言中CPU上的通用寄存器的名称，是32位的寄存器。



### 寄存器用途

那么，它们在程序中的用途是怎么样的呢？

这些32位的寄存器但每一个都有“专长”，有各自的特别之处。

- EAX 是"累加器"(accumulator), 它是很多加法乘法指令的缺省寄存器。

- EBX 是"基地址"(base)寄存器, 在内存寻址时存放基地址。

- ECX 是计数器(counter), 是重复(REP)前缀指令和LOOP指令的内定计数器。

- EDX 则总是被用来放整数除法产生的余数。

- ESI/EDI分别叫做"源/目标索引寄存器，因为在很多字符串操作指令中，其中DS:ESI指向源串，而ES:EDI指向的是目标串。

- EBP是"基址指针"， 它最经常被用作高级语言函数调用的"框架指针"。

  在破解软件时,经常可以看见一个标准的函数起始汇编代码:

- push ebp ;保存当前ebpmov ebp,esp ;EBP设为当前堆栈指针sub esp, xxx ;预留xxx字节给函数临时变量....这样一来,EBP 构成了该函数的一个框架, 在EBP上方分别是原来的EBP, 返回地址和参数. EBP下方则是临时变量. 函数返回时作 mov esp,ebp/pop ebp/ret 即可.

- ESP 专门用作堆栈指针，被形象地称为栈顶指针。

  堆栈的顶部是地址小的区域，压入堆栈的数据越多，ESP也就越来越小。

  在32位操作平台上，ESP每次会减少4个字节。

关于寄存器的概念就说到这。实际运用起来是将内容存到寄存器内而使用其地址。**真正与形成函数栈帧有密切关系的是：EBP和ESP这两个寄存器地址。**







# 什么是"栈"？

在开始讲解前，需要再注意一个关键词：**什么是“栈”？**

栈是一类数据存储结构，本篇不会对其实现方法做太多解释，只需要了解它的一个特性：**数据依次放入栈内后，取出元素时顺序是最先进入的元素最后出**；

例如在一个木桶内放入一堆书籍，在你需要取出底部的书时，你需要先把上部分内容取出才能取出最底部的内容。而本篇说的栈区，与我们常说的数据结构是两个概念，函数的栈区是在操作系统级别上的，管理内存区，**是主要运行在系统内存之上的**。

## 函数栈帧的概念

在寄存器内，EBP、ESP这2个寄存器中存放的是地址，**这两个寄存器的指针是用来维护函数栈帧的**。而**这两个指针维护的内存空间就是一个函数的栈帧**。

**每一次函数调用时，都需要在栈区内创建一个空间，而创建的过程就是由这两个指针去实现的**；调用了哪个函数，EBP、ESP两个指针地址就会去维护这个函数的内存空间，这就是函数的栈帧；例如main函数在运行过程的当中，**esp和ebp两个指针地址会位于函数的它的栈顶和栈底。**

这么说，你可能会不理解。那就画图吧！

![函数栈帧](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/function_stack_frame.png)



可以看到的是，esp和ebp两个指针地址会位于函数的它的栈顶和栈底，维护属于main函数的内存空间，而esp和ebp形成的这一块空间就是函数的栈帧。

那么，再回到前面的话题，变量、作用域、函数调用和返回等操作又是如何实现的呢？我们需要来进一步了解函数压栈的过程、





## 函数压栈的过程

本篇将以本段代码进行举例，以此来介绍函数的栈帧、局部变量和函数调用的生成与销毁的过程。

![函数压栈](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/function_stacking.png)





在开始讲解前，我们需要了解的一点是，因为不同的编译器对于程序汇编封装的方法可能是不同的，而更高阶的编译器对于程序的封装会更加细致，不利于观察，所以本处我会**使用VS2013版本演示**函数压栈的过程，并且会带着你一块一步步的读程序运行中的汇编指令并讲解每一个步骤会做出什么样的操作，最后会对整个指令进行一个总结。



本篇中，我将结合C语言X86(32位)代码生成细节的汇编指令文档来讲解本篇的汇编指令，以下是将会常用到的汇编语句。

![常用汇编语句](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/common_assembly_statements.png)

同时，因为汇编指令的地址会随着每次程序编译而变化（因为内容都是随机分配的），**如果你在本地也在进行调试时，请保持在同一个编译情景下以免出现前后差异**。但原理上都是相通的。

（观察方式：运行程序->调试->反汇编，观察变化需要开启内存空间监视器。）



需要说明的是，C语言标准中不允许main函数被调用，但是在VS2013之前的版本中，运行程序调试时查看调用堆栈时会发现main函数也是被其他函数调用的。

分别是__tmainCRTStartup和mainCRTStartup函数，其中，mainCRTStartup压在最底部。

调用逻辑是mainCRTStartup -- > __tmainCRTStartup --> main 函数

**当我们开始运行程序时，main函数被调用，栈帧区的建立过程应该是这样的。**



## 栈帧区的建立过程

mainCRTStartup函数运行__tmainCRTStartup函数

![creation_of_stack_frame_area](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/creation_of_stack_frame_area.png)

![img](https://mmbiz.qpic.cn/mmbiz_png/CbEvhd1Z6nSIufK4pd8YVX9fe8rLYlicKUtibVJe6twHRCxAXZxStpCuSNHQ1ic5Anjribbf0PiciazyjM9MrzNibdeAw/640?wx_fmt=png)



__tmainCRTStartup函数调用main函数

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111508258.png)



根据我们刚刚说的，先运行的会被先压入函数栈的最底部，以此摞下去

由此，我们可以理解此时的内存栈表示为

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111508691.png)



我们刚刚说的，当函数在运行过程当中，会用esp栈顶指针和ebp栈底指针形成一块内存空间而形成函数的栈帧。那么，程序具体是怎么做的呢？



下面，我们通**过查看程序的反汇编**的指令来研究它的压栈过程。以下是主函数的部分反汇编代码，现在我们来看看它的具体原理是如何走的。

**主函数汇编指令** (部分)

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111509538.png)





我们刚刚提到主函数也是被其他函数调用的，当程序进入主函数时，那这个调用主函数的函数是不是已经创建起它的函数栈帧了呢？答案是肯定的。此时原函数__tmainCRTStartup 是被esp和ebp两个栈顶/底指针维护的。

最初开始时的栈区应该如图所示

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111510050.png)









# 一、构建函数栈帧准备 (一)



接下来我们来看main函数进来的第一句汇编指令

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111510438.png)



进来的第一句话就是push ebp，汇编指令中，它的意思是**把ebp的值放到栈顶**

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111510779.png)



那么我们可不可以假设：因为esp维护的是程序的栈顶，此时的esp已经跑到了栈的最顶部，esp的地址会指向ebp的值？如图所示

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111511113.png)



该如何论证这个假设呢？

当你去开启监视器去监控esp就可以发现它的值会变动。

当前是esp栈顶指针的初始值

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111511508.png)





push ebp完成后，esp地址是不是由高到低，所以地址应该是减小吧？

监视器进入逐过程时就可以证明这个道理：a8 到 a4 减少了4个字节

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111512157.png)



那么esp的值会不会是ebp的值呢？打开内存块，搜索新的esp的地址会是ebp的值，答案一目了然！~

刚刚ebp的值时多少？008ffbf4, 现在搜索esp的地址的值就是008ffbf4，假设成立。

esp维护的是程序的栈顶，此时的esp已经跑到了栈的最顶部，新的esp的地址会指向ebp的值

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111512538.png)



而压入的这个ebp是调用函数的ebp，它的作用是什么？我们到下一章会进行讲解。







# 二、构建函数栈帧准备 (二)

现在我们再来看第二句汇编指令：mov 把esp的值给到ebp。

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111512915.png)



事实果真如此吗？我们运行调试下一步，监控器反馈如下

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111513358.png)



此时它的栈区示意图应该是

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111513775.png)







# 三、构建函数栈帧的范围





再来看第三句会汇编指令：sub esp的地址，减去0E4h。（sub是英文中减少的意思，add同理为加上）

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111514204.png)



通常来说，**ebp减去的值都是0E4h**，而这里的0E4h实际上是一个八进制的数字。当你想查看0E4h是一个什么数字时，你可以将它放入监控区后可以显示其十六进制的值，再查看十进制数字

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111514578.png)



![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111514965.png)



走到这里，不就是相当于esp减去了0E4h的值吧？那此时的esp会不会已经发生变化了呢？监视器逐过程查看结果

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111515389.png)



此时的esp的值已经变成了0x008ffac0，相当于**esp的地址值变小上移不再指向原来的地方**，而是指向原地址上方某一块区域内。

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111515741.png)



这个时候你有没有发现，新的esp栈顶和ebp栈顶指针在进入main函数后已经形成的一块新的维度空间，并且esp和ebp不再是维护原来的函数空间了呢？没错，这一块新的区域就是为main函数预开辟的函数栈帧区。而sub就是提出为main函数开辟的多少字节空间。

栈区示意图可以理解成下面这张图

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111516284.png)











四、放入三个非易失寄存器







这里的ebx、esi、edi是我们前面所说的寄存器中**基底、来源索引、目标索引暂存器**，它们三个在这里统称为**非易失寄存器**。这是一个C语言中的**调用约定**，这里将三个寄存器压栈的原因就是实现跨平台使用。在X86平台下的调用约定下这3个寄存器用途在于，调用函数时要求压入这3个寄存器以此用来保存调用前的数据，应在调用期间长期存储。

它们此处是在入栈操作，别忘了入栈的同时，esp栈顶指针也在不断的变化。

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111517432.png)



入栈的过程详情可以如下：

观察监视器内esp和ebx的值

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111518057.png)



ebx开始压入栈时，esp会如何变化呢？答案是肯定的，esp的值会递减向上挪动

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111518455.png)



打开内存器时，会发现对应esp的地址是ebx的值0x007e5000

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111519130.png)



同理继续往里压入esi时，esp的变化如下

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111519746.png)



![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111520589.png)



压入edi时，esp的变化如下

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111521442.png)



![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111522372.png)



综上，原来的esp栈顶指针的值已经由最初的008ffac0变成现在的008ffab4，地址在不断的减小，**栈顶在不断的上移。**

    现在的栈区的示意图可以理解为

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111522891.png)









# 五、加载栈帧有效空间





    到了这里为了方便直观感受与理解，我们会显示汇编符号名。

    到了第七句这里的lea语句，它的全名应该是load effective address(**加载有效地址**)；顾名思义，从此处开始，程序会正式加载当前函数的有效栈帧区域。我们来看看它该如何走吧。

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111523897.png)



    lea edi, [ebp-0E4h]，这里的0E4h是不是很眼熟？没错，就是刚刚在预申请main函数的函数栈帧中所预申请的大小。

    在这里的意思就是将ebp - 0E4h大小的空间存到edi当中去，而ebp-0E4h这块空间就是刚刚esp做减法转移动作使的空间位置，同时这个edi不就是栈顶指针指的寄存器吗？

    由栈区图，我们可以观察到如下情景。

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111524239.png)



    如何论证呢？翻到刚刚前面的三个非易失寄存器未压入栈时esp的地址

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111515389.png)



    现在，我们打开监视器查看ebp-0E4h和edi的地址，答案显而易见！~ebp-0E4h的地址就是当前esp所指的第3个栈——edi的位置，也是三个非易失寄存器未压入栈时esp的地址。

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111524920.png)



    再接着，mov ecx,39h和mov eax,0CCCCCCCCh意思分别是，把39h次和0CCCCCCCCh分别放在ecx, eax寄存器内。

    **这里可能会有点绕，但真正起作用的应该是下一句！**

下一句：rep stos dword ptr es:[edi] ，这里就非常有意思，此处会最终形成函数的栈帧有效空间。来看看指令语句的表述：



    从**edi**内所标记的ebp-0E4h处(**低地址**)开始向高地址重复**拷贝ecx次eax的内容**，直到**栈底指针ebp处**(高地址)。需要注意的是，**dword表达的是double word双字节的意思**，假设一个word是2个字节，**double word就是双字节等同于4字节**。



    它们的具体流程是什么样的呢？**从edi所标记的ebp-0E4h处开始，向高地址的部分进行字节拷贝，每一次拷贝4个字节。拷贝的内容就是eax的内容（0CCCCCCCCh），拷贝次数为39h次，到栈底指针ebp处停止**。

    根据上面的描述，程序会从ebp-0E4h（内存地址：008ffac0）处开始往高地址进行字节拷贝

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111524920.png)

    直到ebp栈底指针处；当你打开内存图查看此时的内存情况时，就可以论证这一个观点~

从008ffac0出开始向高地址拷贝

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111525924.png)



    到008ffba4栈底指针处结束

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111526708.png)



    可能你会有疑问，这个cccccccc是什么意思呢？它们在各个编译器可能都有些许不同，而当我们平时在编写程序时，**变量未定义初始值时，打印输出来的是“烫烫烫”乱码字符，实际上这就是内存中放的0CCCCCCCCh字符**。

综上，栈区的示意图可以如下

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111527264.png)



    程序运行到这里，程序历经五步，为main函数开辟的函数栈帧正式完成，这一块由esp和ebp共同维护形成的区域就是一个函数的栈帧，形成完成后会往一块空间内填入39h次的0CCCCCCCCh字符，而这里面的内容能做什么？函数如何调用和返回，会在下一章进行讲解







生成函数的局部变量







由上面的诸多操作下来，一个函数的有效栈帧区已经形成，此时程序才会真正执行它的有效代码。根据之前写的代码要求，程序一进来会创建局部变量，在栈帧区内，局部变量又是如何被创建的呢？

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111528064.png)



首先我们来看汇编指令：这个语法是不是很熟悉呢？语句的的意思是：依次的将0Ah、14h、0放入到

ebp - 8、ebp - 14h、ebp - 20h 位置处。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/CbEvhd1Z6nSIufK4pd8YVX9fe8rLYlicKGAALWh6pJfB5NzJevADrNKRU2ib7suZ80siaMISnbibhqTof3fMePRrBw/640?wx_fmt=jpeg)



ebp - 8、ebp - 14h、ebp - 20h是以栈底指针为基准向低地址减小的一串地址，在这里就是开辟一块空间分配给0Ah、14h、0 ，而这个0Ah、14h、0 就是计算机的十六进制的10、20、0的表达形式。所

现在我们来论证刚刚所说的。首先来继续观察ebp栈底指针的值，看它是不是往低地址存放变量；

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111528801.jpeg)



  逐过程进入语句，答案很明显，从栈底指针008ffba4处往低地址 - 8处，存放的值就是0ah。此时局部变量a = 10已创建

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111529179.jpeg)



   我们继续看下一步，创建局部变量 b = 20，后面的c同理。

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111529554.jpeg)



   根据观察在栈帧中局部变量的创建过程，我们可以发现局部变量是在形成一片有效的栈帧空间后，由高地址向低地址存放。如果变量未设置初始值时，程序会划定好一块区域规定为该变量的地址。

此时的栈区示意图可以如下

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111529973.jpeg)





# 本节小节

    本篇我们基于main主函数简单介绍了一个函数的栈帧建立的基本过程；我们了解到，一个函数的栈帧实际上是由esp和ebp两个栈顶和栈底指针共同维护的一片内存空间；当一个函数在开始生成栈帧以后，会首先压入上一个函数的栈底指针ebp地址。在生成栈帧过程中，不断扩大的栈帧、压入新的内容或寄存器都会使得esp栈顶指针向上偏移；在进行确定方位相关操作时，都是以栈底指针ebp的位置作为偏移量向低地址开始偏移的。在压入3个非易失寄存器后，程序会基于ebp栈顶指针向低地址的填充一块区域，而这块区域就是一个函数的作用域。在这块作用域中，程序会根据ebp指针向上（低地址）作为方位，生成对应的变量。



下一篇，我们将会介绍函数的调用与返回过程，以及对我们开篇提出的问题做出一个总结。



# C/C++：函数栈帧的创建与销毁(下)











  上一篇中，我们介绍了什么是寄存器、已经一个函数栈帧创建的基本过程和函数变量和作用域是如何生成的。那么本篇我们将继续上一篇内容，继续介绍函数的调用过程以及函数返回值，以及函数栈帧销毁的过程。最后，我们会对整个过程以及相关知识点进行一个总结。







# 生成函数的局部变量







由上面的诸多操作下来，一个函数的有效栈帧区已经形成，此时程序才会真正执行它的有效代码。根据之前写的代码要求，程序一进来会创建局部变量，在栈帧区内，局部变量又是如何被创建的呢？

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111528064.png)



首先我们来看汇编指令：这个语法是不是很熟悉呢？语句的的意思是：依次的将0Ah、14h、0放入到

ebp - 8、ebp - 14h、ebp - 20h 位置处。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/CbEvhd1Z6nSIufK4pd8YVX9fe8rLYlicKGAALWh6pJfB5NzJevADrNKRU2ib7suZ80siaMISnbibhqTof3fMePRrBw/640?wx_fmt=jpeg)



ebp - 8、ebp - 14h、ebp - 20h是以栈底指针为基准向低地址减小的一串地址，在这里就是开辟一块空间分配给0Ah、14h、0 ，而这个0Ah、14h、0 就是计算机的十六进制的10、20、0的表达形式。所

现在我们来论证刚刚所说的。首先来继续观察ebp栈底指针的值，看它是不是往低地址存放变量；

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111528801.jpeg)



  逐过程进入语句，答案很明显，从栈底指针008ffba4处往低地址 - 8处，存放的值就是0ah。此时局部变量a = 10已创建

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111529179.jpeg)



   我们继续看下一步，创建局部变量 b = 20，后面的c同理。

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111529554.jpeg)



   根据观察在栈帧中局部变量的创建过程，我们可以发现局部变量是在形成一片有效的栈帧空间后，由高地址向低地址存放。如果变量未设置初始值时，程序会划定好一块区域规定为该变量的地址。

此时的栈区示意图可以如下

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111529973.jpeg)







###  函数调用与传参过程





   上面已经完成了局部变量的创建，那程序的调用函数操作时如何进行的呢？接下来我们来看一看！废话不多说，先看汇编指令：

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111530413.jpeg)



    前面讲解了这么多汇编指令，到这里看到的指令是不是开始按捺不住跳动的DNA了呢（bu）？能不能直接说出它们都做了什么呢？

- 第一、第三句的mov，含义是将ebp-14h和ebp-8分别放到eax和ecx当中去，我们翻到上一步，看看 ebp-14h和ebp-8是什么呢？根据栈底指针向低地址偏移观察可以看到，没错，就是我们a和b的值。这里是将a和b分别放入寄存器eax和ecx中去。
- 第二、第四局中的push，是压入栈的指令。分别将eax和ecx压入栈(别忘了每一次压入栈时，程序的栈顶指针也在变化哦)，而eax和ecx现在里面是什么呢？不就是a和b的值吗？

此时顶部栈区的示意图应该如下

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111530791.png)



   通过示例函数中我们可以看到。这4个动作是不是很像在进行传参前的准备呢？答案是确定的。那这样的放入和压入操作真的可以把参数传入函数嘛？调用函数又是如何使用我们的参数的呢？让我们继续往下看！

    第五句，call实际上是一个转移指令，转移到另外一个区域内，同时为了执行转移后完成原区域的下一条指令，call指令会总是会将下一条指令压入栈区中，以此实现转移区内指令完成后返回至原地（简单来 说，原地插个眼后传送去支援，最后还能传送回到线上。做到有去有回）。到这里，我们知道call指令会将原区域内的下一个指令的地址压入栈，所以栈顶应该就是下一条指令（00C21450） 的地址，打开内存和监视器确认果真如此

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111531137.jpeg)

    继续看，call指令的右边的一串标识，实际是call的“传送”位置，这个时候我们按下调试的F11进入到声明处，会看到声明处的指令。这里的jmp，就是跳入add函数当中去（本处只需了解jmp也是个转移操作，会在后续深挖细节）

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111531506.jpeg)



   接下来，我们继续往下走，欢迎来到Add函数的内部！！

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111531886.jpeg)



    到这里函数的调用和传参操作已经完成了，我们可以总结出来的是：

- 传参时：程序在传参前会把要传入的参数先放入到寄存器当中，并将寄存器地址压入栈中。再观察他们的顺序 a->b，是由左往右依次压入栈的（示意图显示b在上，根据栈的先进后出原则证明b是后进的），同时栈顶指针在时刻变化。
- 调用函数时：在调用函数时，程序会使用call指令进入函数，call指令首先会将调用函数完成后的下一步指令压入栈区中，以此实现调用后返回至原函数继续执行内容的操作，接着就会根据标识进行转移，最后进入到新的函数中。



此时栈区顶部示意图应该如下：



![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111532309.png)









# 新函数的栈帧的生成

    进入到Add函数内，观察到参数z形成前的所有代码，是不是有一种恍然之间中遇见梦中的那个TA的一般的感觉呢？

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111533022.jpeg)

    没错，这里是在将Add函数基础元素压入栈区并形成其作用域，最后生成这个函数内的局部变量；

这里唯一需要提醒的一点是，我们前面所提到的esp和ebp是用来维护当前运行函数的指针，而push ebp处，实际上是压入main函数的ebp栈底指针地址，以此实现ebp的转移以及函数运行完成后ebp返回原处。

下面一部分就是形成有效的Add函数栈帧区了，由此可以得到栈顶区域的示意图（画完才发现有点粉......

粉色即正义！）





![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111533743.png)



   接下来，我们来观察新函数内是如何使用传入进来的参数的。







# 函数形参的使用





    在开始学习C语言程序时，我们之前一直知道一个函数传参的理论：形参是实参的一份临时拷贝。现在我们来看看它是怎么执行的！

话不多说，上汇编指令！

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111534117.jpeg)



   观察这段汇编指令，ebp+8, ebp+0Ch，顺应十六进制转化就是ebp+8和ebp+12，结合当前ebp所指向的位置翻看栈帧区，这两个位置指向的是哪里呢？

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111534558.png)



   没错，就是进入函数前就已经早早压入栈的函数形参。形参和实参在栈上是两个独立的个体存在，形参的改变不会影响到原来实参的改变，所以有形参是实参的一份临时拷贝。

   汇编指令处，mov 会把ebp+8(a)的值放入寄存器eax中，add会把ebp+12(b)的值加进寄存器eax当中去，这也是程序实现加法的原理。

再看下一条，mov 将寄存器eax内的值放入到ebp-8的位置，ebp-8是什么？ebp-8就是z的值！此时它已经从0变成了30。

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111534971.jpeg)



   到这里我们可以看到，在一个函数内，形参是实参的一份临时拷贝，因为程序是不会主动创建的形参 的，在我们调用这个函数之前程序就已经早早把将会用到的形参压入到栈上的，程序只要往前面去拿就可以拿到想要的形参值。这就是函数的形参使用原理。







# 函数返回值与函数返回的实现

  ## 栈帧销毁的过程）

   我们前面看到，程序会把a+b的值结果赋值给z，再将z返回。按照我们之前所学的，程序会在出作用域内会将局部变量销毁，而z又是在新函数内临时生成的局部变量，那程序又是如何拿到z的返回值的呢？而程序在运行结束后，又是怎么将esp和ebp两个栈顶和栈顶指针回到原位，程序又是如何回到原函数内的下一条指令的呢？

   接下来，我们继续通过汇编指令回答这一个问题。

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111535452.jpeg)



    前面带着你看了那么多汇编指令，现在5秒钟时间可以回到我第一句汇编指令是什么意思吗？5...4...3...2...1，答案没错，就是把ebp-8的值放入到eax当中去。而ebp-8的值就是刚刚z的位置，那么我们可以得到，函数的返回值，通常会放入到临时存放到寄存器eax当中去（为什么叫通常，因为超出寄存器大小时会借用其他的寄存器，比如esi）

    再继续往下看，pop指令是什么意思呢（英文含义是什么）？pop指令出栈的意思，将元素弹出栈区以此释放掉。这里连续的3个pop，想想这是啥？是一个函数顶上的3个非易失寄存器。当函数要返回结束时，这3个寄存器会被弹出去。需要注意一点，弹出栈时esp的位置也在调整（向高地址挪动相加）

弹出栈前esp和ebp的值

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111535806.jpeg)

   弹出3个寄存器地址完成后。

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111536137.jpeg)



   程序要结束弹出栈区了，那我的esp和ebp指针是不是也要回到原地了呢？来下一句的mov esp,ebp，就是在调整esp和ebp的位置，将ebp的值给到esp。

    此时，程序pop掉add函数内的ebp，这里的ebp是在进入Add函数时压入的栈的main函数ebp，那它是如何返回的呢？这需要提到pop指令的一个用法，pop指令可以实现用一个寄存器接收出栈的数据，此处的pop实际上就是将Add函数的ebp弹出后，又获取到原来压到栈上的main函数的ebp，做到ebp的跳转，这就是此处的pop ebp的作用。

   到下面的ret，就比较有意思了。ret是什么意思呢？ret是将栈顶字单元出栈，其值赋给IP寄存器，实现了一个程序的转移。在汇编语言中，IP寄存器是表示即将执行的下一条指令的段内偏移地址。那现在栈顶元素是什么呢？

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111536714.png)

    还记得现在栈顶的这个（00C21450）元素是什么嘛？如果不太了解，答案在这！这是在调用函数前，程序预留的call指令的下一条指令的地址。通过ret指令，程序已经回到main函数内部了。

到此，程序栈区示意图可以如下图

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111537331.png)

综上所述我们可以了解到：

1. 函数返回值的操作是，会暂时将返回值放入到寄存器eax当中去；



2. 当函数运行即将返回时，程序首先会销毁当前函数的局部变量，随后悔将放置在函数栈帧上的3个非易失寄存器以此由上至下弹出栈区；



3. 紧接着程序会把当前栈底指针的ebp的值，赋值给栈顶指针esp，栈帧区的收缩调整，以此实现销毁一个函数的栈帧；与此同时，程序会读取曾经存储在栈区上原函数的ebp的地址（当前位于栈顶），并将ebp转移至之前记录的地址上，之后再弹出压在栈上原函数ebp的地址元素，实现ebp返回至原函数内。



4. 最后，程序会进行ret 操作，目的是读取调用函数前压在栈上的下一条指令的地址，以此实现调用函数后返回至原函数还能继续执行指令的操作。

 根据以上步骤，可得当前栈区示意图



![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111538090.png)





# 返回后形参的销毁与原函数获取返回值

    前面我们提到，形参并非是在新函数栈帧区内创建的，而是临时拷贝一份实参后压在栈上的元素。当函数运行完成后，它的形参又该如何销毁的呢？通过前面的许多步骤和观察上方的函数当前栈帧示意图，现在开动你聪明的大脑思考形参会如何处理时一定会有所思路吧！或许你的思路和答案完全一致，就是弹出栈区。

    本处只会讲到两句指令。话不多说，上才（hui）艺（bian）！



![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111538962.jpeg)



    现在大声告诉我！add esp,8是什么意思？

答案就是，esp向高地址出挪上8个字节，而我们前面说一个32位机器上一个栈帧元素是4个字节，那现在向高地址挪动8个字节，不就是把原来存放在栈帧上的2个形参的空间给销毁了么？一个函数的形参销毁的答案就是如此，不接受任何反驳QWQ！~

    到现在，我们程序也返回了，形参也销毁了，返回值说：“我呢？我呢？”别急，再看下一句，说说看这句话是什么意思呢？



答案：把eax里面的值放到ebp-20h处。



而eax刚刚不就是放的是Add函数的返回值么？到ebp-20h处，我们刚刚提到，ebp已经返回到原函数了，而ebp-20h所指向的区域就是我们之前所声明的变量c的内存空间。这样，一个函数的返回值从返回处获取到原函数的方式就是先把返回值放到eax寄存器内，返回至原函数后再从eax里拿到这个返回值。

根据示例代码剩余的内容无非剩下主函数退出和printf输出。不再做过多赘述。



# 函数栈帧创建与销毁过程总结

    到这里，一个程序的函数栈帧的形成和销毁的全过程就讲解结束啦~你可能会感觉到云里雾里和蒙圈。那现在来带你一点点的回顾整个过程并做出相应的总结吧。

    函数栈帧可以追溯到最顶层的三个非易失寄存器顶上，也可以**将edi所标记的ebp-0E4h处开始向高地址填充内容的区域叫做函数栈帧的有效区域**。当真正有效意义上的栈帧应该是除去三个非易失寄存器的。



## 函数栈帧`创建`可以分为3步：

- 第一步：一个函数在准备调用前会做的第一件事是什么呢？先插眼！程序会首先把当前运行的函数的ebp地址压到内存栈上，以此实现函数运行完成后ebp能返回到调用前的ebp原处。如果是调用普通函数（非main函数），还会压入下一条指令的地址做到调用完后继续执行。同时，因为压入了新的数据，所以esp栈顶指针也会随之上浮挪动，随后ebp栈底指针也会移动到esp栈顶指针处，此时esp和ebp两个指针同处在栈顶区域。

- 第二步：程序会发出sub 地址减法指令，指示esp向低地址偏移一片区域。esp偏移到新的区域后与当前ebp栈顶指针形成的一片新的内存空间就是这个函数的栈帧区，这也是函数的作用域。随后程序会压入3个非易失寄存器eax,esi,edi，这3个寄存器是一个调用约定（为了能够在不同平台运行）。

- 第三步：程序由ebp栈底指针位置为基准发出lea指令，目的是加载一个函数栈帧的有效空间，通常会向低地址偏移0E4H个空间单位直至前面压入的ebx寄存器之下，并在这个空间内填满字符 0CCCCCCCCh，最终这个加载出来的有效空间就是一个函数真正意义上的栈帧有效空间，而这一片由0CCCCCCCCh字符填满的空间就是这个函数的作用域。现在，一个函数的栈帧才真正意义上是完整的。而这时候程序才开始执行它的有效代码。



## 函数栈帧的`销毁和返回`同样可以分为3步：



- 第一步：程序会首先会将函数内的局部变量给弹出栈，如果程序有返回值，会把返回值暂时放入寄存器eax当中。随后会将栈顶上的非易失寄存器ebx、esi、edi弹出。

- 第二步：程序将当前栈底指针的ebp的值，赋值给栈顶指针esp，将esp下移后的释放的那一片空间就是函数的栈帧区。

- 第三步：如果还有下一条指令，程序会读取曾经存储在栈区上原函数的ebp的地址，并将ebp转移至之前记录的地址上，实现ebp返回至原函数内，之后再弹出压在栈上原函数ebp的地址元素。最后，程序读取压在栈上的下一条指令的地址，读取完成后弹出栈区，执行下一条指令。



无论程序做出什么指令，最需要记住的原则就是：**无论取多少偏移量，都是以栈底的ebp指针位置为基准；无论压入什么内容，栈顶的esp指针都要跟着向上偏移。**











我们回到前篇我们提出的几个问题，学习完函数栈帧就已经把这些问题都能一一回答了吧！现在来大声告诉我答案吧！！

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/640-20230825111539407.png)



**问**: **函数的作用域是怎么形成的呢？**

**答**: 一个函数的栈帧就是一个函数的作用域。



**问**: **局部变量是如何创建的？**

**答**: 程序在发出lea（load effective address)指令后开始绘制这个函数的定义域后，开始以底部的 ebp栈底指针为标准不断向低地址划定区域，并将这块区域赋予十六进制的值，这个过程就是局部变量创建的过程。



**问**: **为什么未初始化的局部变量的值是随机值或是乱码呢？**

**答**: 程序在发出lea（load effective address)指令后开始绘制这个函数的定义域并分配好局部变量，因为该区域的初始字符均为0CCCCCCCCh，所以此时打印出来的值多数情况下都是 0CCCCCCCCh的表达形式。



**问**: **函数是如何传参的？传参的顺序又是怎么样的呢？**

**答**: 程序在传参前会把要传入的参数先放入到寄存器当中，并将寄存器地址压入栈中。再观察他们的顺序 a->b，所以有函数传参是由左往右依次压入栈的（示意图显示b在上，根据栈的先进后出原则证明b是后进的）.



**问**: **形参和实参的关系是什么？**

**答**: 在调用函数内，任何新产生的局部变量会在调用函数的栈帧区内创建，而使用形参的方法实际上是回到当前函数栈帧创建前压入栈上的形参数据。正因为形参和实参在栈上是两个独立个体的存在，形参的改变不会影响到原来实参，所以才有形参是实参的一份临时拷贝。



**问**: **函数的调用是怎么实现的呢？**

**答**: 在开始调用函数前，程序会把需要用到的函数形参提前压到栈。在调用一个函数时，程序会首先压入下一条指令和当前函数的ebp的地址进入栈区内，以此实现调用完成后程序继续执行与ebp返回原处。随后就开始以栈顶位置为起始并同时压入3个非易失寄存器形成一个完整的函数栈帧区。一个函数调用过程正是如此。



**问**: **函数调用结束后是怎么返回的呢？**

**答**: 当被调用函数的栈帧被销毁后，程序会读取曾经存储在栈区上原函数的ebp的地址，并将ebp转移至之前记录的地址上，实现ebp返回至原函数内，之后再弹出压在栈上原函数ebp的地址元 素。最后，程序读取压在栈上的下一条指令的地址，读取完成后弹出栈区，执行下一条指令。



**问**: **为什么会存在函数递归的最大深度呢？到达最大深度所提出的堆栈溢出错误是什么意思呢？**

**答**: 函数的递归之所以有最大深度，是因为每个函数都存在函数栈帧，在每次调用时都会生成对应的栈空间，并有esp与ebp两个栈顶和栈底指针维护。受到了栈空间的限制，如果递归深度超出栈所能承受的空间，此时就会出现最大深度的堆栈溢出的警告。而不同的函数深度可能会有所不同，毕竟每个函数所需要的栈空间是不一样的。


<h1 id='函数栈帧的创建与销毁深入了解c的汇编代码）'>函数栈帧的创建与销毁（深入了解c的汇编代码）</h1>
<p></p>
<h1 id='基础知识介绍'>基础知识介绍</h1>
<p>
从逻辑上讲，栈帧就是一个函数执行的环境：函数参数、函数的局部变量、函数执行完后返回到哪里等等。首先应该明白，
<strong>栈是从高地址向低地址延伸</strong>
的。每个函数的每次调用，都有它自己独立的一个栈帧，这个栈帧中维持着所需要的各种信息。寄存器ebp指向当前的栈帧的底部（高地址），寄存器esp指向当前的栈帧的顶部（低地址)。
</p>
<blockquote>
<p>从逻辑上讲，栈帧就是一个函数执行的环境：函数参数、函数的局部变量、函数执行完后返回到哪里等等。首先应该明白，栈是从高地址向低地址延伸的。每个函数的每次调用，都有它自己独立的一个栈帧，这个栈帧中维持着所需要的各种信息。寄存器ebp指向当前的栈帧的底部（高地址），寄存器esp指向当前的栈帧的顶部（低地址)。</p>
</blockquote>
<h2 id='1寄存器的种类与功能'>1.寄存器的种类与功能</h2>
<figure class='table-figure'>
<table>
<thead>
<tr>
<th style='text-align:center;'>寄存器名称</th>
<th style='text-align:left;'>功能</th>
</tr>
</thead>
<tbody>
<tr>
<td style='text-align:center;'>eax</td>
<td style='text-align:left;'>累加寄存器，相对于其他寄存器，在运算方面比较常用。</td>
</tr>
<tr>
<td style='text-align:center;'>ebx</td>
<td style='text-align:left;'>基地址寄存器，在内存寻址时存放基地址。</td>
</tr>
<tr>
<td style='text-align:center;'>ecx</td>
<td style='text-align:left;'>计数寄存器，用于循环操作，比如重复的字符存储操作，或者数字统计。</td>
</tr>
<tr>
<td style='text-align:center;'>edx</td>
<td style='text-align:left;'>作为EAX的溢出寄存器，总是被用来放整数除法产生的余数。</td>
</tr>
<tr>
<td style='text-align:center;'>esp</td>
<td style='text-align:left;'>栈顶指针，堆栈的顶部是地址小的区域，压入堆栈的数据越多，esp也就越来越小。在32位平台上，esp每次减少4字节。栈指针寄存器(extended stack pointer)，其内存放着一个指针，该指针永远指向系统栈最上面一个栈帧的栈顶。是CPU机制决定的，push、pop指令会自动调整esp的值。</td>
</tr>
<tr>
<td style='text-align:center;'>ebp</td>
<td style='text-align:left;'>指栈的栈底指针。基址指针寄存器(extended base pointer)，一般与esp配合使用，可以存取某时刻的esp，这个时刻就是进入一个函数内后，CPU会将esp的值赋给ebp，此时就可以通过ebp对栈进行操作，比如获取函数参数，局部变量等。其内存放着一个指针，该指针永远指向系统栈最上面一个栈帧的底部。</td>
</tr>
</tbody>
</table>
</figure>
<h2 id='2-常用汇编指令'>2. 常用汇编指令</h2>
<p>push指令：他首先减少esp的值，再将源操作数复制到栈地址，在位平台上，esp每次减少4个字节</p>
<p>&nbsp;</p>
<p>解释：首先esp的值减少4个字节，再将ebp的值压入栈中；</p>
<p>
pop指令：它首先把
<code>esp</code>
指向的栈元素内容复制到一个操作数中，再增加
<code>esp</code>
的值。在32位平台上，
<code>esp</code>
每次增加4字节。
</p>
<p>
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/POP_directive.png" referrerpolicy="no-referrer" alt="POP_directive">
</p>
<p>
解释：首先将
<code>esp</code>
所指地址处的值赋给
<code>edi</code>
，再将
<code>esp</code>
的值减少4字节。
</p>
<p>
mov指令：用于将一个数据从源地址传送到目标地址，源操作地址的内容不变。
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/MOV_directive.png" referrerpolicy="no-referrer" alt="POP指令">
</p>
<p>解释：将esp 值赋给ebp，这里并不是将esp所指向的内存空间的值赋给 ebp</p>
<p>sub指令：减操作指令，从寄存器中减去&lt;shifter_operand&gt;表示的数值，并将结果保存到目标寄存器中。</p>
<p>
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/SUB_instruction.png" referrerpolicy="no-referrer" alt="image-20230725064400880">
</p>
<p>解释：esp-0E4h字节的结果保存在esp中。</p>
<p>下面这张图片的指令一般是一起集中出现，所以我集中解释一下：</p>
<p>
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/instruction_set.png" referrerpolicy="no-referrer" alt="image-20230725064602012">
</p>
<p>解释：rep指令：重复其上面的指令，ecx的值是重复的次数，每执行一次，ecx 减 1，直到 ecx 减至0。stos指令：将 eax中的值拷贝到es:[edi]指向的地址。dword：双字 就是四个字节。ptr：pointer缩写 即指针[ ]里的数据是一个地址值，这个地址指向一个双字型数据一次拷贝双字（4个字节)的数据到目的地址。es:[edi]：指向目的串解释：合起来的意思就是，将栈上从 ebp-0E4h开始的位置，向高地址方向的内存赋值 0CCCCCCCCh，重复 39h 次，每次赋值双字（四字节的空间）。</p>
<p>
<strong>call指令</strong>
：将程序下一条指令的位置的IP压入堆栈中，并转移到调用的子程序。
</p>
<p>
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/call_directive.png" referrerpolicy="no-referrer" alt="image-20230725064741484">
</p>
<p>解释：将下一条指令的IP（00BF1A30)压入栈中，并移动到调用的子程序。</p>
<p>
<strong>add指令</strong>
：用于将两个运算子相加，并将结果写入第一个运算子。
</p>
<p>
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/add_directive.png" referrerpolicy="no-referrer" alt="image-20230725064827669">
</p>
<p>
解释：给
<code>esp</code>
加8，也就是
<code>esp</code>
向高地址方向移动 8字节 ，相当于
<code>pop</code>
操作后的指针变化。
</p>
<p>
<strong>ret指令</strong>
：用于终止当前函数的执行，将运行权交还给上层函数。也就是，当前函数的帧将被回收。
</p>
<p>
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/ret_directive.png" referrerpolicy="no-referrer" alt="image-20230725064904454">
</p>
<p>
解释：执行这条命令之后，就自动返回刚才call指令的下一行。
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/end_of_instruction_set.png" referrerpolicy="no-referrer" alt="image-20230725064939577">
</p>
<h2 id='3-内存模型'>3. 内存模型</h2>
<p>
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/memory_model.png" referrerpolicy="no-referrer" alt="image-20230725065436655">
图片来源：CNDN作来源csdn：三•九《函数栈帧的创建和销毁（图解)》
</p>
<p>对于初学者，只需要简单理解为：</p>
<p>
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/memory_model2.png" referrerpolicy="no-referrer" alt="image-20230725065547349">
</p>
<h1 id='演示函数栈帧的创建销毁过程'>演示函数栈帧的创建销毁过程</h1>
<p>首先来看下这次演示使用的代码：</p>
<p>&nbsp;</p>
<pre>
<code>#include &lt;stdio.h&gt;

int Add(int x, int y)
{
int z = 0;
z = x + y;
return z;
}
int main()
{
int a = 10;
int b = 20;
int c = 0;

c = Add(a, b);

printf(&quot;%d\n&quot;, c);
return 0;
}
</code>
</pre>
<p>
按下F10，在视图中打开调用堆栈窗口，我们发现
<code>main()</code>
函数被调用了。
</p>
<p>
但是
<code>main()</code>
函数被谁调用了呢？
</p>
<p>
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/function_code_demonstration.png" referrerpolicy="no-referrer" alt="image-20230725065645687">
</p>
<p>
当我们接着调试到
<code>return 0;</code>
之后，再按F10，我们发现程序跳转到了调用
<code>main()</code>
函数的函数内
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/function_code_demonstration2.png" referrerpolicy="no-referrer" alt="image-20230725065739174">
</p>
<p>
<strong>
原来
<code>main()</code>
函数是被
<code>__tmainCRTStartup</code>
函数调用的，而
<code>__tmainCRTStartup</code>
又是被
<code>mainCRTStartup</code>
调用的。
</strong>
</p>
<h1 id='分步骤演示函数栈帧的创建和销毁的过程'>分步骤演示函数栈帧的创建和销毁的过程。</h1>
<ol start=''>
<li>为main()函数开辟栈帧</li>

</ol>
<p>
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/Opens_up_stack_frames_for_the_main()_function.png" referrerpolicy="no-referrer" alt="image-20230725065823045">
</p>
<p>&nbsp;</p>
<ol start='2'>
<li>在main()函数中创建变量</li>

</ol>
<p>
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/create_a_variable_in_the_main()_function.png" referrerpolicy="no-referrer" alt="image-20230725065938115">
</p>
<p>
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/create_a_variable_in_the_main()_function.gif" referrerpolicy="no-referrer" alt="create_a_variable_in_the_main()_function">
</p>
<p>图片来源：CNDN作者：三•九《函数栈帧的创建和销毁（图解）》</p>
<ol start='3'>
<li>调用Add()函数前的准备</li>

</ol>
<p>
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/preparation_before_calling_the_Add()_function.png" referrerpolicy="no-referrer" alt="image-20230725070259689">
</p>
<p>
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/preparation_before_calling_the_Add()_function.gif" referrerpolicy="no-referrer" alt="preparation_before_calling_the_Add()_function">
</p>
<p>图片来源：CNDN作者：三•九《函数栈帧的创建和销毁（图解）》</p>
<p>&nbsp;</p>
<ol start='4'>
<li>为Add()函数开辟栈帧</li>

</ol>
<p>
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/open_up_stack_frames_for_the_Add()_function.png" referrerpolicy="no-referrer" alt="image-20230725070457380">
图片来源：CNDN作者：三•九《函数栈帧的创建和销毁（图解)》
</p>
<p>&nbsp;</p>
<ol start='5'>
<li>
在Add()函数中创建变量并运算
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/create_variables_in_the_Add()_function_and_operate_on_them.png" referrerpolicy="no-referrer" alt="image-20230725070630148">
</li>

</ol>
<p>
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/create_variables_in_the_Add()_function_and_operate_on_them.gif" referrerpolicy="no-referrer" alt="create_variables_in_the_Add()_function_and_operate_on_them">
图片来源：CNDN作者：三•九《函数栈帧的创建和销毁（图解)》
</p>
<p>6.Add()栈帧的销毁</p>
<p>
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/Add()_destruction_of_stack_frames.png" referrerpolicy="no-referrer" alt="image-20230725070852983">
</p>
<p>
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/Add()_destruction_of_stack_frames.gif" referrerpolicy="no-referrer" alt="Add()_destruction_of_stack_frames">
图片来源：CNDN作者：三•九《函数栈帧的创建和销毁（图解)》
</p>
<p>
返回main()函数栈帧
<img src="https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/returns_the_main()_function_stack_frame.png" referrerpolicy="no-referrer" alt="image-20230725071113069">
</p>
<p>
可以看到这里返回到了第3步(3. 调用Add()函数前的准备)，最后指令
<code>call</code>
的下一条指令。
</p>
<p>接下来的一系列mian函数的销毁与ADD函数销毁相似，不做过多赘述。</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h1 id='思考问题'>思考问题：</h1>
<ol start=''>
<li>局部变量是怎么创建的？</li>
<li>为什么局部变量的值是随机值？</li>
<li>函数是怎么传参的？传参的顺序是怎样的？</li>
<li>形参和实参是什么关系？</li>
<li>函数调用是怎么做的？</li>
<li>函数调用是结束后怎么返回的？</li>

</ol>
