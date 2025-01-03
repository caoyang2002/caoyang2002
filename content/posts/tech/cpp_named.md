[codeif](https://codeif.xinke.org.cn)

# 文件命名

> 所有文件
>
> 头文件和原文件成对出现

**全部小写, 可是使用下划线"_"(默认)或连字符"-", 称完整, 不要有歧义**

- system_file.c  & system_file.h
- item_name.c
- item-name.c

# 类型命名

> 类, 结构体, 类型定义(Typedef), 枚举, 类型模板参数

**每个单词首字母大写, 不使用下划线**

- Number
- Timer
- File
- Name

# 变量命名

> 变量, 函数参数, 数据成员名

**全部小写, 使用下划线连接"_"<br>类的成员变量以下划线结尾**

- var

- itme_var

- struct

- itme_struct

- calss_

- itme_class_

  ```cpp
  普通变量命名:
  string name;
  string other_name;
  int a;
  int a_other;
  char b;

  类数据成员:
  class PeopleInfo{
  public:
      string name;
      string other_name
      int age;
      int itme_num;
      static Pool<Psople>* pool_;
  }

  结构体变量:
  struct person{
      string name;
      int num_age;
      static Pool<person>* pool_;
  }
  ```



# 常量

> 声明为constexpr 或 const的变量,或在程序运行期间其值始终不变的
>
> 静态变量, 全局变量,

**以"k"开头, 所有首字母大小, 大驼峰命名**



# 函数命名

> 函数名

**首字母大写(大驼峰命名), 或使用下划线**

- my_parent()
- MyParent()



# 枚举命名

> 枚举和宏或常量一样

**首字母大写, 大驼峰命名**

- Name

- OtherName

  ```cpp
  enum Name{
      lisa,
      tom = 1,

  }
  ```



# 宏命名

> 不建议使用宏

**单词全部大小,使用下划线连接**

- NAME_ONE

- MY_NAME

  ```cpp
  #define MY_NAME
  #define ORUND(x)...
  #define PI_NUMBER 3.14
  ```
