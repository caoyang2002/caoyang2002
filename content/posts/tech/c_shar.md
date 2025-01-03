> ```c
> 3
> * * *
> *   *
> * * *
>
> 4
> * * * *
> *     *
> *     *
> * * * *
> ```



- 非多组输入

```c
#include <stdio.h>
//行定位
int main() {
    int n = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        if (i == 0 || i == n - 1) {//首尾行输出一行*
            for (int j = 0; j < n; ++j) {
                printf("* ");
            }
        } else {
            for (int j = 0; j < n; ++j) {//其它行首尾输出*
                if(j==0 || j == n-1)
                    printf("* ");
                else
                    printf("  ");
            }
        }
        printf("\n");//换行
    }

    return 0;
}

// 3 ---- n
// * * *  --- 1行每个位置都输出 一共n个
// *   *  --- 其它行1和n位置输出 一共2个
// * * *  --- n行每个位置都输出 一共n个
// 思路：
// 使用for 和 if
// 判断是不吃首尾行 是则输出一行* 不是则输出首尾*


```
----------

- 多组输入

```c
#include <stdio.h>
//行和列定位
int main() {
    int n = 0;
    while(scanf("%d", &n) == 1){//输入的数量为1
        for (int i = 0; i < n; ++i) {//控制行
            for (int j = 0; j < n; ++j) {//控制列
                if(i == 0 || i == n-1 || j == 0 || j == n-1)//第0行，第n-1行，第0列，第n-1列输出 *_,其它位置输出 __
                    printf("* ");
                else
                    printf("  ");
            }
            printf("\n");
        }
    }
    return 0;
}

```
