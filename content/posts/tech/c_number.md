+++
date = '2024-12-29T09:31:37+08:00'
draft = true
title = 'Go'
toc = true
+++

- 暴力算法
> 时间复杂度过大

```c
#include <stdio.h>
#include <malloc/_malloc.h>
#include <string.h>
#include <errno.h>
// 最大公约数
// 最小公倍数
//计算最小公倍数和最大公约数的和
int main(){
    int n = 0;
    int m = 0;
    while(scanf("%d %d",&n,&m) == 2){//读取两个数
        int min = n < m ? n : m;
        int max = n > m ? n : m;
        int i = min;//最大公约数
        int j = max;//最小公倍数
        while(1){
            if(n%i == 0 && m%i == 0){
                break;
            }
            i--;
        }
        // i就是最大公约数
        while(1){
            if(j%n == 0 && j%m == 0){
                break;
            }
            j++;
        }
        // j就是最大公倍数

        printf("最大公倍数 %d + 最小公约数 %d = %d\n",j,i,j+i);
    }
    return 0;
}
```
----------

- 辗转相除法

> 两个数的***最大公约数***等于其中较小的数字和二者之间余数的最大公约数

``c
24 18 ---- 计算最大公约数
24%18 = 6 ---- 获取余数
18%6 = 0 ---- 较小数字于余数的模为0，这个余数就是最大公约数
```

> 最大公倍数就是两个数字的积除以最大公约数

```c
24 * 18 / 6
```

  最终：

```c
 #include <stdio.h>
// 最大公约数
// 最小公倍数
//计算最小公倍数和最大公约数的和
int main(){
    long n = 0;
    long m = 0;
    while(scanf("%ld %ld",&n,&m) == 2){//读取两个数
        long i = n;
        long j = m;
        long r = 0;
        while(r=i%j){
            i = j;
            j = r;
        }
        //j就是最大公约数
        //m * n / j  //最小公倍数
        printf("%ld\n",m*n/j+j);
    }
    return 0;
}
```
