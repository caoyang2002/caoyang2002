# 如何生成 .dll文件
生成dll文件同时会生成lib文件

1. 在VS开始界面，搜索dll，创建dll动态链接库
2. 创建一个类（右键创建类，会自动包含需要的文件） 以查询目录下的文件为例
创建的文件可以不用管
`.cpp`文件 输入自己的代码
```cpp
#include "pch.h"
#include "check_repository.h"
namespace fs = std::filesystem;
    int Check::CheckRepository() {
        std::string folderName = ".Rysigy";
        fs::path currentPath = fs::current_path();
        fs::path folderPath = currentPath / folderName;

        if (fs::exists(folderPath) && fs::is_directory(folderPath)) {
            std::cout << "存储库 '.Rysigy' 文件夹存在\n" << std::endl;
        }
        else {
            std::cout << "[错误]\t存储库 '.Rysigy' 文件夹不存在\n请在右键菜单中点击 '创建存储库'\n" << std::endl;
        }
        std::cout << "点击任意按键退出..." << std::endl;
        _getch();
        return 0;
};


```
`.h`文件
```cpp
#pragma once
#include <iostream>
#include <filesystem>
#include <conio.h>
// 查询当前的目录下是否有.Rysigy
class __declspec(dllexport) Check{
public:
    int CheckRepository();//检查是否有存储库
};
```

为了让生成的文件尽量小，可以使用release模式，以及MT运行库MT生成
