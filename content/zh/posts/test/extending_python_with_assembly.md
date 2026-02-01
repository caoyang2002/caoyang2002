+++
title = '用汇编中编写Python扩展'
date = 2025-12-01T12:12:13+08:00
draft = false
author = "simons"
categories = ["编程"]
tags = ["汇编","python"]
description = "这篇文章介绍了如何使用会变语言写 python 拓展，可以作为学习汇编语言的资料"
cover = "https://tonybaloney.github.io/img/posts/remote-control-car.jpg"
+++

[查看原文](https://tonybaloney.github.io/posts/extending-python-with-assembly.html)
> 原作者：Anthony Shaw，2020年8月15日

# 在汇编中编写Python扩展

有时，你需要把一些东西拆开再重新组装起来才能充分理解它。我相信阅读这篇文章的许多人都是那些孩子之一。孩子们拿着螺丝刀去某事，只是为了看看里面有什么。这是一种刺激，但把它重新组合起来是一种完全不同的技能。

![遥控车](https://tonybaloney.github.io/img/posts/remote-control-car.jpg)

外部的工作机器掩盖了其内部的模式、补丁和变通办法网络。程序员习惯于在系统的内脏上工作，并操纵丑陋的内部工作，使其遵循一些简单的指令。

这个实验也没什么不同。我想看看我是否可以在100%的汇编中编写CPython扩展。

**为什么**？

嗯，因为在读完[CPython Internals书](https://realpython.com/products/cpython-internals-book/)后，汇编代码仍然是一个谜。我开始从[Jo Van Hooey的书中](https://www.apress.com/gp/book/9781484250754)学习x86-64汇编，并理解了一些基本概念，但很难将它们与我熟悉的高级语言联系起来。

有一些问题我想要答案，比如：

- 为什么 CPython 中的扩展需要用 Python 或 C 编写？
- 如果 Python C 扩展编译到共享库，它们内部的魔力是什么，使它们可以通过 Python 加载？
- CPython 在 C 之间有什么 ABI，可以使其更容易被其他语言扩展

## [汇编简要总结](https://tonybaloney.github.io/posts/extending-python-with-assembly.html#assembly-quick-summary)

汇编代码是使用指令集的一系列指令。不同的 CPU 架构有不同的指令集。

最常见的是 x86、ARM 和 x86-64，这些CPU架构上也有扩展说明。在CPU架构的发布中，制造商为该集添加了新的指令。通常是为了提高性能。

CPU有许多寄存器，它从寄存器中加载数据来执行指令。您也可以从内存（RAM）复制数据，但您不能从 RAM 复制到 RAM，它必须通过寄存器进行。这意味着，在编写汇编指令时，您需要运行许多步骤才能完成一些在更高级别的语言中用一行完成的事情。

例如，在Python中将变量`a`分配给变量`b`的引用：

```python
a = b
```

而在汇编中，您首先复制到寄存器（我们将使用 RAX），然后复制到目的地：

```asm
mov RAX, a
mov b, RAX
```

指令`mov RAX, a`将把变量`a`**的地址**复制到寄存器中。寄存器RAX是一个**64位寄存器**，因此它可以包含任何适合64位（8字节）的值。在64位操作系统上，内存地址是64位地址，因此地址值将是64位。

您还可以使用将变量的**值复**制到寄存器中`[]`名字周围：

```x86asm
mov a, 1
mov RAX, [a]
```

现在，`RAX`寄存器的值将是十进制值1（以十六进制表示的`0000 0000 0000 0001`）。

我选择RAX是因为它是第一个寄存器，但如果你正在编写一个独立的应用程序，你可以任意选择任何寄存器。

64位寄存器以`r`开头，前8个寄存器也可以通过引用寄存器的下位来使用32、16或8位值。寄存器的32位地址更快，因此如果值在32位以内，大多数编译器将使用较小的寄存器地址：

| 64位寄存器 | 降低32位 | 降低16位 | 降低8位 |
| :--------- | :------- | :------- | :------ |
| 拉克斯     | 斧头     | 斧       | 阿尔    |
| rbx        | ebx      | bx       | bl      |
| rcx        | ECX      | cx       | 克      |
| rdx        | 教育     | dx       | dl      |
| RSI        | esi      | si       | 西尔    |
| Rdi        | 编辑     | 迪       | 迪尔    |
| rbp        | ebp      | 血压     | bpl     |
| Rsp        | 尤其是   | 斯佩     | 斯普    |
| R8         | R8d      | R8w      | r8b     |
| R9         | R9d      | R9w      | r9b     |
| R10        | R10d     | R10w     | r10b    |
| R11        | R11d     | R11w     | R11b    |
| R12        | R12d     | R12w     | r12b    |
| R13        | R13d     | R13w     | r13b    |
| R14        | R14d     | r14w     | r14b    |
| R15        | R15d     | R15w     | R15b    |

由于组装是一系列指令，分支可能很棘手。实现分支的方法是使用条件和无条件跳转语句将指令指针（`rip`）移动到指令地址。指令地址可以在程序集源代码中标记，程序集将用实际内存地址替换这些名称。此地址是相对的或绝对的（稍后会解释）。

```x86asm
jmp leapfrog ; jump to leapfrog label
mov rax, rcx ; this never gets executed
leapfrog:
mov rcx, rax
```

这个简单的Python代码，在将`a`与十进制值5进行比较时包含一个分支：

```python
a = 2
a += 3
if a == 5:
  print("YES")
else:
  print("NO")
```

您可以在汇编中完成此工作，只需将分配（`a`和增加3）简化为一个简单的比较。大多数编译器会自动进行这种优化，因为他们会确定您正在比较常量值。

以下是一些伪组装来演示：

```x86asm
 mov rcx, 2  ; Move the decimal value 2 to the RCX CPU register
 add rcx, 3  ; Add 3 to the value in the RCX CPU register, RCX is now equal to 5
 cmp rcx, 5  ; Compare RCX to the value 5, 
 je YES      ; If the comparison was equal, jump to the instruction offset YES
 jmp NO      ; Jump to the instruction offset NO
 YES:  ; RCX == 5
   ... 
   jmp END
 NO:   ; RCX != 5
   ...
   jmp END
```

### 调用外部功能[¶](https://tonybaloney.github.io/posts/extending-python-with-assembly.html#calling-external-functions)

除非您想完全重新发明轮子，否则您的应用程序或库可能会使用其他编译库中的函数。

在程序集中，您可以使用具有符號名稱的`extern`指令引用外部函式的地址。如果可执行文件是静态链接的，链接器将用库的实际值替换它，或者如果可执行文件是动态链接的，则取决于运行时值。我不想在这篇文章中进行链接，否则它会一直进入一本迷你书（而且我对链接器不太了解）。

如果您正在用C编写应用程序，并且需要调用另一个库中的函数，您将使用Header（H）文件。

标题文件将告诉编译器：

- 函数的名称（符号）
- 它的返回值和响应的大小
- 论点及其类型

例如，如果您用C定义了一个函数：

```c
char* pad_right(char * message, int width, char padding);
```

这个标题告诉我们的内容：-该函数需要3个参数-第一个参数是`char`指针，因此64位地址指向8位值（`char`）-第二个参数是int，（取决于操作系统和其他一些因素）可能是32位值-第三个参数是`char`，即8位-响应是`char`指针，因此我们需要一个64位地址来存储结果

汇编函数调用没有参数的概念，而是操作系统定义了一个规范（称为调用约定），其中寄存器应该用于哪个参数。

幸运的是，macOS和Linux有相同的[调用约定](https://software.intel.com/sites/default/files/article/402129/mpx-linux64-abi.pdf)，称为System-V的参数，该约定规定，在调用函数时，以下寄存器应填充参数的值：

| 争论  | 64位寄存器 |
| :---- | :--------- |
| 论点1 | Rdi        |
| 论点2 | RSI        |
| 论点3 | rdx        |
| 论点4 | rcx        |
| 论点5 | R8         |
| 论点6 | R9         |

注意：Windows有一个[调用约定](https://cda.ms/1VT)，它使用不同的寄存器来访问System-V。

额外的参数从值堆栈中加载，由于它是值堆栈，您按相反的顺序推送它们。例如，如果函数有10个参数，您将首先推送第10个：

```x86asm
 push arg10
 push arg9
 push arg8
 push arg7
```

This calling convention means that if you’re calling a function written in C, C++, or even Rust, the function will read whatever is in the `rdi`CPU register and use that as the first argument.

如果您想调用`pad_right()`函数，您将编写等效的汇编代码：

```x86asm
extern pad_right
section .data
    message db "Hello", 0 ; null-terminated string
section .bss
    result  resb 11
section .text
    mov rdi, db  ; argument 1 
    mov rsi, 10  ; argument 2
    mov rdx, '-' ; argument 3
    call pad_right
    mov [result], rax ; result
```

调用约定规定，寄存器`rax`将填充结果。由于该函数返回一个`char *`，我们期望结果是一个指针（64位内存地址值）。我们在`bss`部分保留了11个字节（10个字母+空终止符），然后将结果`rax`写到该地址。

另一个需要记住的重要事情是，装配体没有范围。因此，如果您将寄存器用于某物，例如存储值，然后称为外部函数，则该寄存器可能会更改值。注册实际上是全球性的。

在调用函数之前保留寄存器状态的正确方法是将它们推送到值堆栈上，然后在函数调用完成后将其弹出：

```x86asm
... do stuff with r9
push r9
call externalFunction
pop r9
```

当您构建自己的函数时，您需要在指令期间保留调用框架。调用框架使用堆栈指针（`rsp`）和`rbp`寄存器。要做到這一點，彙編功能應該在開頭和結尾包括一些額外的指令（稱為前編和尾聲）：

```x86asm
push rbp
mov rbp, rsp

... your code

mov rsp, rbp
pop rbp
```

Windows定义了[另一种呼叫约定](https://cda.ms/1VV)，使用不同的寄存器作为参数。它还需要不同的前例和尾部曲，用于计算地址限制。这比最初的英特尔规格要复杂一些。

### 将程序集变成可执行文件[¶](https://tonybaloney.github.io/posts/extending-python-with-assembly.html#turning-assembly-into-an-executable)

您不能直接执行程序集源文件。看起来您可能正在编码机器代码，但围绕一个程序集指令有一个包装器，需要让操作系统运行指令（可执行文件格式）。

汇编程序将获取汇编源文件，并将其汇编成机器代码格式。格式是特定于操作系统的。可执行代码的一些常见格式有：

- 适用于macOS的[Mach-O](https://en.wikipedia.org/wiki/Mach-O)
- 适用于Linux的[ELF](https://refspecs.linuxfoundation.org/elf/elf.pdf)
- 适用于Windows的[PE](https://cda.ms/1VW)

可执行文件格式包括几个组件，而不仅仅是说明：

- 机器代码指令（在稱為`text`的部分）
- 外部符号列表（外部参考）
- 内存要求列表（由序列开始的字节，`bss`部分）
- 常量值，如字符串（在称为`data`的部分）

EFF标头还包含操作系统所需的一些其他有用信息。

Mach-O格式在任何数据或指令之前都包含一个详细的标题。我喜欢一个名为[SynalizeIT!](https://www.synalysis.net/)的程序，这是一个十六进制编辑器，可以应用二进制语法来可视化和解码二进制文件格式。Mach-O格式是受支持的语法，如果您打开CPython可执行文件（`/usr/bin/python3`或您安装的任何位置），您可以看到并探索这些标题。

![synalize-screenshot-1](https://tonybaloney.github.io/img/posts/synalize-screenshot-1.png)

在右侧，您可以看到一些属性，例如：

- 组装此二进制文件的CPU架构。将来，当苹果发布ARM MacBook时，此可执行文件将不起作用，因为它将检查此标题，并看到CPU架构中的不匹配（在尝试加载指令之前）
- 数据、文本和bss部分的长度、位置和偏移量
- 任何运行时标志，如位置独立可执行（PIE）（稍后涵盖）

ELF、mach-O和PE格式的另一个特点是能够构建共享库（Linux中的.so文件，macOS中的.dylib或.so文件，以及Windows中的.dll文件）。

共享库可以动态导入（如插件）或在构建阶段作为应用程序的依赖项进行链接。构建CPython C扩展时，您需要将扩展与Python共享库链接。您的C扩展本身也是一个共享库，并由CPython动态加载（当您`import mylibrary`）。

### 汇编中的复杂数据结构[¶](https://tonybaloney.github.io/posts/extending-python-with-assembly.html#complex-data-structures-in-assembly)

如果您调用的函数的参数具有更复杂的数据类型（如指向`struct`的指针），您需要了解C数据类型的存储大小：

| 标量类型       | C数据类型                       | 存储大小（以字节为单位） | 推荐的对齐 |
| :------------- | :------------------------------ | :----------------------- | :--------- |
| INT8           | `char`                          | 1                        | 字节       |
| UINT8          | `unsigned char`                 | 1                        | 字节       |
| INT16          | `short`                         | 2                        | 单词       |
| UINT16         | `unsigned short`                | 2                        | 单词       |
| INT32          | `int`，`long`                   | 4                        | 双字       |
| UINT32         | `unsigned int`，`unsigned long` | 4                        | 双字       |
| INT64          | `__int64`                       | 8                        | 四语       |
| UINT64         | `unsigned __int64`              | 8                        | 四语       |
| FP32（单精度） | `float`                         | 4                        | 双字       |
| FP64（双精度） | `double`                        | 8                        | 四语       |
| 指点器         | `*`                             | 8                        | 四语       |

以C中包含3个整数字段（`x`和`z`的结构为例：

```c
typedef struct { 
    int x; 
    int y;
    int z;
} position
```

这3个字段中的每一个将使用4个字节（32位），因此如果您用C来定义：

```c
position myself = { 3, 9, 0} ;
```

这将使`myself`将变量等同于十六进制值：

```yaml
0000 0003 0000 0009 0000 0000
```

您可以使用`struc`和`istruc`宏在NASM程序集中重新创建此结构：

```x86asm
section .data:
    struc position
        x: resd 1
        y: resd 1
        z: resd 1
    endstruc

    myself:
        istruc position
            at x, dd 3
            at y, dd 9
            at z, dd 0
        iend
```

`struc`宏等同于C中的`struct`构造，用于定义内存结构。`istruc`用定义的值分配一个常量值。指令`resd`表示保留一个双字（4字节），`dd`表示在值上定义一个双字。

这将创建相同的内存序列：

```yaml
0000 0003 0000 0009 0000 0000
```

因为这不适合64位，所以您将向分配的内存地址发送指针。

如果，在C中，你有一个使用typedef的函数：

```c
void calculatePosition(position* p);
```

您可以通过将`rdi`寄存器设置为分配内存的地址，从程序集调用该函数：

```x86asm
mov rdi, myself
call calculatePosition
```

函数`calculatePosition()`不知道它是否是由用C、Assembly、C++等编写的代码调用的。

接下来，我将探索这个原则，看看我们是否可以在Assembly中编写一个动态加载的CPython扩展。

## 注册Python扩展模块[¶](https://tonybaloney.github.io/posts/extending-python-with-assembly.html#registering-the-python-extension-module)

当您在Python中加载模块时，导入库将在`PYTHONPATH`中查找与您提供的名称匹配的模块。

模块可以是C（作为编译扩展）或Python。许多CPython标准库模块都是用C语言编写的，因为它们要么需要与低级操作系统API（磁盘IO、网络等）的接口。标准库模块的其余部分是用Python编写的。有些是两者的组合，Python模块与C扩展函数。这通常被实现为用C编写的隐藏模块，用Python编写的公共模块。Python模块将导入隐藏的C模块并包装其功能。

要编写C扩展模块，您需要：

- 一个C编译器
- 链接器
- Python库
- 设置工具

我们试图重建的C代码是一个名为`PyInit_pymult()`的函数，它返回`PyObject*`，它是由callingPyModule_Create2`PyModule_Create2()`创建的。

```c
PyObject* PyInit_pymult() {
    return PyModule_Create2(&_moduledef, 1033); 
}
```

注册您的模块有很多选择，但我只想采用这种方法，称为单阶段注册。

当您在Python中输入`import XYZ`，它会寻找，

1. Python路径中的一个名为`XYZ-cpython-{version}-{os.name}.so`的文件
2. Python路径中一个名为`XYZ.so`的文件

第一个选项是该版本的Python的编译库。您可以在软件包的二进制分发（轮子）中拥有多个编译库。例如，

- `XYZ-cpython-39-darwin.so`Python 3.9
- `XYZ-cpython-38-darwin.so`蟒蛇3.8
- `XYZ-cpython-37-darwin.so`蟒蛇3.7

如果你想知道什么是“达尔文”，它是macOS内核的旧名称。今天在CPython中仍然被提及。

`PyModule_Create2()`是一个函数，它需要`PyModule_Def *`和CPython版本的`int`，该模块所用。

在CPython `Include/moduleobject.h`中定义的类型结构：

```c
typedef struct PyModuleDef_Base {
  PyObject_HEAD // PyObject header 
  PyObject* (*m_init)(void); // Pointer to the init function
  Py_ssize_t m_index; // index
  PyObject* m_copy; // Optional pointer to a copy() function
} PyModuleDef_Base;
... 
typedef struct PyModuleDef{
  PyModuleDef_Base m_base; // The base data 
  const char* m_name;      // The module name
  const char* m_doc;       // The module docstring
  Py_ssize_t m_size;       // The module size
  PyMethodDef *m_methods;  // A list of methods, terminated by NULL, NULL, NULL, NULL
  struct PyModuleDef_Slot* m_slots; // Defined slots for Python protocols (e.g., __eq__, __contains__)
  traverseproc m_traverse; // Optional custom traverse method
  inquiry m_clear;         // Optional custom clear method
  freefunc m_free;         // Optional custom free method (called when module is destroyed by GC)
} PyModuleDef;
...
```

有了基本C类型的存储要求，我们可以在组装中重现这些结构：

```asm
default rel
bits 64

section .data
    modulename db "pymult", 0
    docstring db "Simple Multiplication function", 0

    struc   moduledef
        ;pyobject header
        m_object_head_size: resq 1
        m_object_head_type: resq 1
        ;pymoduledef_base
        m_init: resq 1
        m_index: resq 1
        m_copy: resq 1
        ;moduledef
        m_name: resq    1
        m_doc:  resq    1
        m_size: resq    1
        m_methods:  resq    1
        m_slots: resq   1
        m_traverse: resq    1
        m_clear: resq   1
        m_free: resq    1
    endstruc
section .bss
section .text
```

然后，我们可以定义一个全局函数，在编译此共享库时导出为符号：

```x86asm
global PyInit_pymult
```

`__init__`函式可以将正确的值加载到moduledef结构中：

```x86asm
PyInit_pymult:
    extern PyModule_Create2
    section .data

        _moduledef:
            istruc moduledef
                at m_object_head_size, dq  1
                at m_object_head_type, dq 0x0  ; null
                at m_init, dq 0x0       ; null
                at m_index, dq 0        ; zero
                at m_copy, dq 0x0       ; null
                at m_name, dq modulename
                at m_doc, dq   docstring
                at m_size, dq 2
                at m_methods, dq 0 ; null - no functions
                at m_slots, dq 0    ; null- no slots
                at m_traverse, dq 0 ; null
                at m_clear, dq 0    ; null - no custom clear
                at m_free, dq 0     ; null - no custom free()
            iend
```

`__init__`函数的指令将遵循System-V调用惯例，并调用`PyModule_Create2(&_moduledef, 1033)`

```x86asm
    section .text
        push rbp                    ; preserve stack pointer
        mov rbp, rsp

        lea rdi, [_moduledef]  ; load module def
        mov esi, 0x3f5              ; 1033 - module_api_version
        call PYMODULE_CREATE2       ; create module, leave return value in register as return result

        mov rsp, rbp ; reinit stack pointer
        pop rbp
        ret
```

常量`0x3f5`是`1033`，是我们正在使用的CPython API的整数值。

接下来，要编译源代码，我们必须组装`pymult.asm`文件，然后将其链接到`libpythonXX`。这需要两个步骤完成。第一步是使用`nasm`创建对象文件。第二步是将对象文件与Python 3链接。X（我的案例是3.9）库：

对于macOS，我们使用`macho64`对象格式，用`-g`包含调试符号，并告诉NASM编译器所有符号都将具有前缀`_`。当外部模块链接时，`PyModule_Create2`将在macOS中称为`_PyModule_Create2`。但稍后，我们将尝试Linux，它不会有那个前缀。

```shell
nasm -g -f macho64 -DMACOS --prefix=_ pymult.asm -o pymult.obj
cc -shared -g pymult.obj -L/Library/Frameworks/Python.framework/Versions/3.9/lib -lpython3.9 -o pymult.cpython-39-darwin.so
```

这将产生可以加载到CPython的工件`pymult.cpython-39-darwin.so`。由于我们使用调试符号（`-g`标志）构建，lldb或gdb调试器可用于在汇编代码中设置断点。

```shell
 $ lldb python3.9
(lldb) target create "python3.9"
Current executable set to 'python3.9' (x86_64).
(lldb) b pymult.asm:128
Breakpoint 2: where = pymult.cpython-39-darwin.so`PyInit_pymult + 16, address = 0x00000001059c7f6c
```

当模块加载时，lldb将击中断点。您可以使用参数`-c 'import pymult'`启动该过程，只需导入新模块并退出：

```shell
(lldb) process launch -- -c "import pymult"
Process 30590 launched: '/Library/Frameworks/Python.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python' (x86_64)
1 location added to breakpoint 1
Process 30590 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 1.1
    frame #0: 0x00000001007f6f6c pymult.cpython-39-darwin.so`PyInit_pymult at pymult.asm:128
   125
   126          lea rdi, [_moduledef]  ; load module def
   127          mov esi, 0x3f5              ; 1033 - module_api_version
-> 128          call PyModule_Create2       ; create module, leave return value in register as return result
   129
   130          mov rsp, rbp ; reinit stack pointer
   131          pop rbp
Target 0: (Python) stopped.
```

万岁！模块正在初始化。此時，您可以操作任何寄存器或可视化数据。

```x86asm
(lldb) reg read
General Purpose Registers:
       rax = 0x00000001007d3d20
       rbx = 0x0000000000000000
       rcx = 0x000000000000000f
       rdx = 0x0000000101874930
       rdi = 0x00000001007f709a  pymult.cpython-39-darwin.so`..@31.strucstart
       rsi = 0x00000000000003f5
       rbp = 0x00007ffeefbfdbf0
       rsp = 0x00007ffeefbfdbf0
        r8 = 0x0000000000000000
        r9 = 0x0000000000000000
       r10 = 0x0000000000000000
       r11 = 0x0000000000000000
       r12 = 0x00000001007d3cf0
       r13 = 0x000000010187c670
       r14 = 0x00000001007f6f5c  pymult.cpython-39-darwin.so`PyInit_pymult
       r15 = 0x00000001003a1520  Python`_Py_PackageContext
       rip = 0x00000001007f6f6c  pymult.cpython-39-darwin.so`PyInit_pymult + 16
    rflags = 0x0000000000000202
        cs = 0x000000000000002b
        fs = 0x0000000000000000
        gs = 0x0000000000000000
```

您还可以检查框架并查看框架堆栈：

```bash
(lldb) fr info
frame #0: 0x0000000101adbf6c pymult.cpython-39-darwin.so`PyInit_pymult at pymult.asm:128
(lldb) bt
* thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 1.1
  * frame #0: 0x0000000101adbf6c pymult.cpython-39-darwin.so`PyInit_pymult at pymult.asm:128
    frame #1: 0x000000010023326a Python`_PyImport_LoadDynamicModuleWithSpec + 714
    frame #2: 0x0000000100232a2a Python`_imp_create_dynamic + 298
    frame #3: 0x0000000100166699 Python`cfunction_vectorcall_FASTCALL + 217
    frame #4: 0x000000010020131c Python`_PyEval_EvalFrameDefault + 28636
    frame #5: 0x0000000100204373 Python`_PyEval_EvalCode + 2611
    frame #6: 0x00000001001295b1 Python`_PyFunction_Vectorcall + 289
    frame #7: 0x0000000100203567 Python`call_function + 471
    frame #8: 0x0000000100200c1e Python`_PyEval_EvalFrameDefault + 26846
    frame #9: 0x0000000100129625 Python`function_code_fastcall + 101
    ...
```

为了为Linux编译，我们需要添加位置独立可执行（PIE或PIC）支持。这通常由GCC编译器完成，但由于我们正在编写直接汇编，我们必须自己完成。独立于位置的代码可以在任何内存地址执行，无需修改，我们唯一需要关心位置的组件是Python C API的外部引用。

而不是像我们为 macOS 那样将外部符号定义为静态位置：

```x86asm
call PyModule_Create2
```

我们需要调用符号相对于[全局偏移表](https://eli.thegreenplace.net/2011/11/03/position-independent-code-pic-in-shared-libraries/)的位置。NASM有一个简写，将其定义为PLT/GOT的偏移量：

```x86asm
call PyModule_Create2 wrt ..plt
```

如果定义了`NOPIE`我们可以使用NASM宏来替换指令，而不是为PIE和非PIE维护两个源文件。

```x86asm
%ifdef PIE
    %define PYARG_PARSETUPLE PyArg_ParseTuple wrt ..plt
    %define PYLONG_FROMLONG PyLong_FromLong wrt ..plt
    %define PYMODULE_CREATE2 PyModule_Create2 wrt ..plt
%else
    %define PYARG_PARSETUPLE PyArg_ParseTuple
    %define PYLONG_FROMLONG PyLong_FromLong
    %define PYMODULE_CREATE2 PyModule_Create2
%endif
```

然后将`call PyModule_Create2`替换为宏值`call PYMODULE_CREATE2`。组装后，NASM将用正确的说明替换它。

Linux使用ELF格式而不是大男子主义，因此在NASM中指定输出格式：

```shell
nasm -g -f elf64 -DPIE pymult.asm -o pymult.obj
cc -shared -g pymult.obj -L/usr/shared/lib -lpython3.9 -o pymult.cpython-39-linux.so
```

## 向模块添加函数[¶](https://tonybaloney.github.io/posts/extending-python-with-assembly.html#adding-a-function-to-the-module)

当我们初始化模块时，我们提供了值`0`）作为函数列表。使用与以前相同的模式，`PyMethodDef`结构是：

```c
struct PyMethodDef {
    const char  *ml_name;   /* The name of the built-in function/method */
    PyCFunction ml_meth;    /* The C function that implements it */
    int         ml_flags;   /* Combination of METH_xxx flags, which mostly
                               describe the args expected by the C func */
    const char  *ml_doc;    /* The __doc__ attribute, or NULL */
};
```

在汇编中，您可以将这些字段表示为：

```x86asm
    struc methoddef
        ml_name:  resq 1
        ml_meth: resq 1
        ml_flags: resd 1
        ml_doc: resq 1

        ml_term: resq 1  // NULL terminator
        ml_term2: resq 1 // NULL terminator
    endstruc

    method1name db "multiply", 0
    method1doc db "Multiply two values", 0

    _method1def:
        istruc methoddef
            at ml_name, dq method1name
            at ml_meth, dq PyMult_multiply
            at ml_flags, dd 0x0001 ; METH_VARARGS
            at ml_doc, dq 0x0
            at ml_term, dq 0x0 ; Method defs are terminated by two NULL values,
            at ml_term2, dq 0x0 ; equivalent to qword[0x0], qword[0x0]
        iend
```

然后定义函数，相当于C代码：

```c
static PyObject* PyMult_multiply(PyObject *self, PyObject *args) {
    long x, y, result;
    if (!PyArg_ParseTuple(args, "LL", &x, &y))
        return NULL;
    result = x * y;
    return PyLong_FromLong(result);
}
```

用C（或汇编）编写扩展模块需要了解CPython C API。例如，如果您正在使用Python整数，它们不会映射到像C long这样的简单低级内存结构。要将C长转换为Python长，您必须调用`PyLong_FromLong`。要将Python长转换为C长，请调用`PyLong_AsLong`。由于Python长可能比C长的最大值长，因此有可能溢出，因此您可以使用`PyLong_AsLongAndOverFlow()`或者，如果值适合`long long`，您可以使用``PyLong_AsLongLong()`

通过调用`PyArg_ParseTuple()`函数将方法参数的元组转换为原生C类型，这些决策将参数抽象为方法。您为此方法提供了一个特殊格式的字符串和指向目的地地址的指针列表。

我们使用的示例是将参数转换为两个C长（“LL”）值和输出地址：

```c
PyArg_ParseTuple(args, "LL", &x, &y)
```

在汇编中完成此工作，您将args（rsi）、字符串作为常量和两个保留的四字内存空间的地址发送给PyArg_ParseTuple。

在组装中，这是使用有效负载地址指令：

```x86asm
lea rdx, [x]
```

使用System-V调用约定，我们可以将C函数转换为汇编函数：

```x86asm
global PyMult_multiply

PyMult_multiply:
    ;
    ; pymult.multiply (a, b)
    ; Multiplies a and b
    ; Returns value as PyLong(PyObject*)
    extern PyLong_FromLong
    extern PyArg_ParseTuple
    section .data
        parseStr db "LL", 0 ; convert arguments to Long, Long
    section .bss
        result resq 1 ; long result
        x resq 1      ; long input
        y resq 1      ; long input
    section .text
        push rbp ; preserve stack pointer
        mov rbp, rsp
        push rbx
        sub rsp, 0x18

        mov rdi, rsi                ; args
        lea rsi, [parseStr]    ; Parse args to LL
        xor ebx, ebx                ; clear the ebx
        lea rdx, [x]           ; set the address of x as the 3rd arg
        lea rcx, [y]           ; set the address of y as the 4th arg

        xor eax, eax                ; clear eax
        call PYARG_PARSETUPLE       ; Parse Args via C-API

        test eax, eax               ; if PyArg_ParseTuple is NULL, exit with error
        je badinput

        mov rax, [x]                ; multiply x and y
        imul qword[y]
        mov [result], rax

        mov edi, [result]           ; convert result to PyLong
        call PYLONG_FROMLONG

        mov rsp, rbp ; reinit stack pointer
        pop rbp
        ret

        badinput:
            mov rax, rbx
            add rsp, 0x18
            pop rbx
            pop rbp
            ret
```

接下来，更改模块定义，以包括`at m_methods, dq _methoddef`的新方法定义。

如果您是mac用户，我推荐[Hopper Disassembler](https://www.hopperapp.com/)，因为它具有漂亮的“伪代码”视图。如果您在Hopper中打开新编译的`.so`文件，并查看您刚刚编写的函数，您可以验证它看起来松散地像您在C中预期的那样：

![料斗截图](https://tonybaloney.github.io/img/posts-original/hopper-screenshot.png)

重新编译并重新导入模块后，您将在`dir(pymult)`上看到函数，它将接受两个参数。

在77行上设置断点

```shell
(lldb) b pymult.asm:77
Breakpoint 4: where = pymult.cpython-39-darwin.so`PyMult_multiply + 67, address = 0x00000001019dbf42
```

现在启动一个进程并在导入后运行函数，lldb应该在断点停止：

```shell
(lldb) process launch -- -c "import pymult; pymult.multiply(2, 3)"
Process 39626 launched: '/Library/Frameworks/Python.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python' (x86_64)
Process 39626 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 4.1
    frame #0: 0x00000001007f6f42 pymult.cpython-39-darwin.so`PyMult_multiply at pymult.asm:77
   74           imul qword[y]
   75           mov [result], rax
   76
-> 77           mov edi, [result]           ; convert result to PyLong
   78           call PyLong_FromLong
   79
   80           mov rsp, rbp ; reinit stack pointer
Target 0: (Python) stopped.
(lldb)
```

您可以通过以下方框检查`rax`寄存器中的十进制值：

```shell
(lldb) p/d $rax
(unsigned long) $6 = 6
```

万岁！起作用了！

*为了记录在案......花*了大约25-30次重新编译和更改才成功完成这项工作。事后看来，这并不**太**复杂，但让它工作起来非常令人沮喪。

組裝的問題之一是，它似乎要麼有效，要麼就慘遭失敗！没有例外，如果你犯了错误，它只会使进程崩溃或损坏主机进程。这非常无情。

## 扩展setuptools/distutils[¶](https://tonybaloney.github.io/posts/extending-python-with-assembly.html#extending-setuptoolsdistutils)

接下来，将一堆汇编源文件推送到PyPi并没有什么好处，因为如果你`pip install`它开箱即用就不起作用。最终用户必须知道如何编译库。

`setuptools`软件包将`build_ext`命令添加到`setup.py`，因此如果您在`setup.py`中有这个命令：

```python
...
setup(
    name='pymult',
    version='0.0.1',
    ...
    ext_modules=[
        Extension(
            splitext(relpath(path, 'src').replace(os.sep, '.'))[0],
            sources=[path],
        )
        for root, _, _ in os.walk('src')
        for path in glob(join(root, '*.c'))
    ],
)
```

然后跑：

```shell
$ python setup.py build_ext --force -v
```

它针对源代码运行GCC编译器，将其链接到您正在运行`setup.py`的Python可执行文件的Python库，并将编译的模块放在`build`目录中。

我们想使用GCC来链接对象，但NASM来编译汇编源。

我们还需要一些特定于NASM的东西：

- 当平台不需要PIE时，请使用`-DNOPIE`
- 在macOS上使用`-f macho64`，或者在linux上使用`-f elf64`
- 如果`setup.py`使用调试标志运行，请使用`-g`添加调试符号
- 在macOS上添加`_`前缀

我已将所有这些添加到一个名为`NasmBuildCommand`的自定义`setuptools`构建命令中。您可以更新`setup()`方法以包含此类，然后指定`.asm`文件：

```shell
    cmdclass={'build_ext': NasmBuildCommand},
    ext_modules=[
        Extension(
            splitext(relpath(path, 'src').replace(os.sep, '.'))[0],
            sources=[path],
            extra_compile_args=[],
            extra_link_args=[],
            include_dirs=[dirname(path)]
        )
        for root, _, _ in os.walk('src')
        for path in glob(join(root, '*.asm'))
    ],
)
```

现在，如果您使用冗长（-v）和调试（`--debug`）运行`setup.py build`，它将为您编译库：

```shell
$ python setup.py build --force -v --debug
running build
running build_ext
building 'pymult' extension
nasm -g -Isrc -I/Users/anthonyshaw/CLionProjects/mucking-around/venv/include -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -f macho64 -DNOPIE --prefix=_ src/pymult.asm -o build/temp.macosx-10.9-x86_64-3.8/src/pymult.obj
cc -shared -g build/temp.macosx-10.9-x86_64-3.8/src/pymult.obj -L/Library/Frameworks/Python.framework/Versions/3.8/lib -lpython3.8 -o build/lib.macosx-10.9-x86_64-3.8/pymult.cpython-38-darwin.so
```

一旦完成这一切，就可以与源代码分发一起创建带有编译二进制文件的轮子：

```shell
$ python setup.py bdist_wheel sdist
```

然后轮子可以上传到PyPi：

```shell
$ twine upload dist/*
```

如果有人在轮子包含的平台上下载此内容（本例中仅为macOS），它将安装编译的库。如果有人在另一个平台上，`pip install`命令将尝试使用自定义`build`命令从源代码编译。

您可以通过运行`pip install --no-binary :all: <package> -v --force`来强制执行此行为，以详细模式查看整个下载和编译过程：

![源代码定制](https://tonybaloney.github.io/img/posts/custom-build-from-source.png)

## GitHub CI/CD工作流程[¶](https://tonybaloney.github.io/posts/extending-python-with-assembly.html#github-cicd-workflows)

最后，我想在GitHub存储库中添加一些单元测试和持续测试，这意味着在GitHub操作上进行编译。

现在，`setuptools`已被扩展到在单个命令中构建，这并不太难。

只有1个单元测试，谨慎地避免负数（！）：

```python
from pymult import multiply


def test_basic_multiplication():
    assert multiply(2, 4) == 8
```

为了在Linux上进行测试，我刚刚从apt安装了NASM，然后在源目录上运行`python setup.py install`（隐式运行`python setup.py build_ext`）：

```yaml
jobs:
  build-linux:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8]
    steps:
    - name: Install NASM
      run: |
        sudo apt-get install -y nasm
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip pytest
        python setup.py install
    - name: Test with pytest
      run: |
        python -X dev -m pytest test.py
```

当CPython崩溃时（而不是if），额外的`-X dev`标志提供了更详细的输出。

对于macOS，构建步骤相同，除了NASM来自brew：

```yaml
    - name: Install NASM
      run: |
        brew install nasm
```

然后，为了危险地生活，在Windows上使用Chocolatey NASM软件包：

```yaml
  build-windows:
    runs-on: windows-latest
    strategy:
      matrix:
        python-version: [3.8]
    steps:
      - name: Install NASM
        run: |
          choco install nasm
      - name: Add NASM to path
        run: echo '::add-path::c:\\Program Files\\NASM'
      - name: Add VC to path
        run: echo '::add-path::C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\bin'
      - uses: actions/checkout@v2
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip pytest
          python setup.py install
      - name: Test with pytest
        run: |
          python -X dev -m pytest test.py
```

## Windows支持[¶](https://tonybaloney.github.io/posts/extending-python-with-assembly.html#windows-support)

我最终确实扩展了`setuptools`以支持NASM + Microsoft Linker作为客户编译器实施，[WinAsmCompiler](https://github.com/tonybaloney/python-assembly-poc/blob/master/winnasmcompiler.py)。

最大的变化是：

- 使用`-f win64`位PE）作为对象格式
- 使用`-DNOPIE`

然而，现有的代码不起作用，因为它假设了System-V调用约定。

您可以编写第二个汇编函数，或抽象调用约定，以允许两个标准，并通过宏交换它们。在这一点上，我决定结束这一天！（虽然它确实编译了，但在导入时崩溃）。

## 结论[¶](https://tonybaloney.github.io/posts/extending-python-with-assembly.html#conclusion)

该项目的完整源代码在[Github上](https://github.com/tonybaloney/python-assembly-poc)。

我学到的一些东西：

- 如何在lldb中探索寄存器，（这真的很有用）
- 如何正确使用料斗
- 如何在组装的庫中设置斷點，以瞭解它們可能因分割故障而崩潰的原因
- setuptools/distutils如何编译C扩展，以及它*真正*需要如何用当前的编译器工具链进行更新
- 如何在GitHub Actions中从汇编编译
- 对象格式的工作原理以及mach-o和ELF之间的区别

我想应用这些知识的地方首先是安全领域。读完《黑帽Python》（顺便说一句，这很棒）后，我还在读《Shellcoders手册》。

我能想到的一些方法来应用这些知识：

- 逆向工程编译库来寻找安全漏洞
- 在[Hack The Box上](https://tonybaloney.github.io/posts/hackthebox.eu)完成更多挑战
- 调整安全漏洞以模仿复杂的C数据结构
- 创建shellcode漏洞，以演示堆栈溢出错误和其他不应该发生的事情

特别是，我认为我可以在编译的Python C扩展中找到安全漏洞。不在标准库中，因为希望它们已经过测试，而是在第三方库中。

脚注：赞扬p403n1x87（Gabriele N.Tornetta）在2018年[破解这个坚果](https://p403n1x87.github.io/python/assembly/2018/03/23/asm_python.html)

## 相关帖子

![将Python嵌入你的。带有CSnakes的NET项目](https://tonybaloney.github.io/img/posts/snake-robot.jpeg)

将Python嵌入你的。带有CSnakes的NET项目

深入研究之间的新整合。NET和Python

*2024年10月4日发布*

![在运行Python。净5](https://tonybaloney.github.io/img/posts/turtle-pileup.jpg)

在运行Python。净5

更新Pyjion项目，使用将JIT插入CPython。NET 5 CLR JIT编译器

*2020年11月11日发布*

![使用子解释器运行Python并行应用程序](https://tonybaloney.github.io/img/posts/four-snakes-square.jpeg)

使用子解释器运行Python并行应用程序

探索使用子解释器运行并行应用程序的可能性
