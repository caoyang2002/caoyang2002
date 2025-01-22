+++
date = '2024-04-29T09:31:37+08:00'
draft = false
title = 'SQL 教程'
tags: ["编程", "sql"]
toc = true
+++

<p style=color:red;> 在idea中分号并不是必须加的, 在执行多条语句才必须加, 在控制台使用的时候必须加<p>

# 数据库相关的操作
查询数据库	 `SHOW DATABASES`

创建数据库
`CREATE DATABASE 数据库名`
`CREATE DATABASE mydatabase`

查看数据库信息
`SHOW CREATE DATABASE 数据库名`
`SHOW CREATE DATABASE database`

删除数据库
`DROP DATABASE 数据库名`
`DROP DATABASE mydatabase`

使用数据库
 `USE 数据库名`
 `USE mydatabase`

# DDL语句	 数据定义语言
 创建表
 ```sql
 CREATE TABLE 表名(
    列名1 类型[长度] [DEFAULT 默认值] [约束条件]
    列名2 类型
    ……
);

CREATE TABLE userinfo(
    id INT
    username VARCHAR(32)
    password VARCHAR(32)
    nickname VARCHAR(32)
    age INT(3)
);
 ```

 查看当前数据库创建的所有表
 `SHOW TABLES;`

 查看表的详细信息
 `SHOW CREATE TABLE 表名`
 `SHOW CREATE TABLE table;`

查看表结构
`DESC 表名`
`DESC table;`

删除表
`DROP TABLE 表名`
`DROP TABLE table;`

修改表名
`RENAME TABLE 原表名 TO 新表名`
`RENAME TABLE old_table TO new_table;`

修改表结构
`ALTER TABLE`
- 添加列
	`ALTER TABLE 表名 ADD 列名 类型[长度]`
	`ALTER TABLE hero ADD age INT(3)`

- 在表中插入一个字段
	`ALTER TABLE 表名 ADD 列名 类型[长度] AFTER 字段名`
	`ALTER TABLE table ADD col VARCHAR(32) AFTER name`

- 删除表中现有的列
	`ALTER TABLE 表名 DROP 列名`
	`ALTER TABLE table DROP col`

- 修改表中现有的列
	`ALTER TABLE 表名 CHANGE 原字段名 新字段名 新类型`
	`ALTER TABLE table CHANGE old_name new_old VARCHAR(10)`

# DML语句（数据操作语言，对表中数据进行操作的语言）（增、删、改操作）
PreparedStatement

插入数据
	`INSERT INTO 表名[(字段1,字段2...)] VALUES(字段1的值,字段2的值...)`
	`INSERT INTO person(name,age) VALUES('张三',22)`

查看表中的所有数据
	`SELECT * FROM 表名`
	`SELECT * FROM person`

修改表数据
	`UPDATE 表名 SET 字段名1=心值1[字段2=新值2...][WHERE 过滤条件]`
	`UPDATE person SET age=23 WHERE name='李四'`

删除数据
	`DELETE FROM 表名[WHERE 过滤条件]`
	`DELETE FROM person WHERE name='李老四'`



# DQL语句	数据查询语句	 PreparedStatement
使用数据库
	`USE 数据库名`
	`USE mydb`

 查询数据库
	`SHOW DATABASE`

创建数据库
	`CREATE DATABASE 数据库名`
	`SHOW DATABASE mydb`

 查询表的部分所有字段
	`SELECT 字段名1[字段名2，字段名3，... 或 *] FROM 表名`
	`SELECT * FROM user`

 查看emp表的特定的字段
	`SELECT name,job FROM emp`
- WHERE字句（添加过滤条件，查询满足条件的）
	```sql
	SELECT name,job,sal
	FROM emp
	WHERE sal>1000;
	```
	连接多个条件
	 `AND、OR`


 值在列表中
	`IN(列表)	IN(emp) `

区间
	`BETWWEEN 2000 AND 3000	`

去重
	`SELECT DISTINCT`
	`SELECT DISTINCT job FROM emp`

多列去重
	- 去除指定列中有重复的行
	`SELECT DISTINCT job,dept_id FROM emp`

模糊查询
	- LIKE  （两个通配符：_表示一个字符，和%表示任意个字符）
	`WHERE name LIKE '%name%'`

总结:
- %X%:字符串中包含'X'
- %X:字符串以X结尾
- X%:字符串以X开头
- _X%:字符串第二个字符是X
- %X_:倒数第二个字符是X
- X%Y:字符串以X开头Y结尾
- X_Y:字符串只有三个字，第一个是X，第三个是Y

根据指定的字段排序查询结果集
	（该子句只能放在查询语句的最后一个子句上），默认升序，DESC降序
`ORDER BY 字段	ORDER BY sal DESC`

多字段查询
	`ORDER BY 字段1,字段2,...`
	`ORDER BY sal,dept_id DESC`

分页查询
	`LIMIT 跳过的记录数（（页数-1）* 每页的记录数），，每页显示的记录数	 `
  > 查询的字段可以使用表达式	SELECT
  > `SELECT name,sal,sal*12 FROM emp;`
  > 查询时可使用函数的结果作为字段
  > `SELECT CONCAT(name,'的职位是',job) FROM emp;`



# 数据库相关的操作

查询数据库：
`SHOW DATABASES;`

创建数据库：
`CREATE DATABASE 数据库名;`
`CREATE DATABASE mydb;`

数据库创建时可以指定字符集：
`CREATE DATABASE 数据库名字 CHARSET=UTF8/GBK  (字符集);`
`CREATE DATABASE db1 CHARSET=UTF8;`

创建数据库db1(字符集用gbk) db2(字符集UTF8);
`CREATE DATABASE db1 CHARSET=UTF8;`
`CREATE DATABASE db2 CHARSET=GBK;`

查看数据库信息
`SHOW CREATE DATABASE 数据库名;`
`SHOW CREATE DATABASE db1;`

删除数据库
`DROP DATABASE 数据库名`
`DROP DATABASE db2;`

使用数据库
`USE 数据库名字`
`USE mydb;`





# 表相关的操作

> （列：字段，是一组数据中各属性信息）
> （行：记录，一条记录保存一组数据）

# DDL语句

>（数据定义语言：用来操作数据库对象的）（数据库对象：表、视图、索引都属于数据库对象）

创建表
```sql
CREATE TABLE 表名(
  列名1 类型[(长度)] [DEFAULT 默认值] [约束条件],
	列名2 类型...
)[CHARSET=UTF8/GBK]

CREATE TABLE userinfo(
    id INT,
    username VARCHAR(32),
    password VARCHAR(32),
    nickname VARCHAR(32),
    age INT(3)
);
```
> 数字的长度表示位数，VACHAR的长度表示最多占用的字节数















---

---





















# 插入数据
`INSERT INTO 表名[(字段1,字段2...)] VALUES (字段1的值,字段2的值...)`

`INSERT INTO person(name,age) VALUES ('张三',22);`
`INSERT INTO person(age,name) VALUES (27,'赵六'); # 对应即可`

未指定的列插入都是列的默认值，当创建表时没有为列声明特定的默认值时，列的默认值为null

`INSERT INTO person(name) VALUES ('李四');`

字段名可以忽略不写，此时为全列插入，即：VALUES需要指定每一列的值，且顺序、个数、类型必须与表相同

`INSERT INTO person VALUES ('王五',24);`

查看person表中的所有数据

`SELECT * FROM person;`

修改表数据操作: UPDATE语句

`UPDATE 表名 STE 字段名1=新值1[字段2=新值2...][WHERE 过滤条件]`

`UPDATE person SET age=23 WHERE name='李四';`



WHERE 中常用的条件: =,>,<,>=,<=,<>不等于（!= 不是所有数据库都支持）

`UPDATE person SET age=25 WHERE age>50;`

`UPDATE person SET age=age+1 ;`

`UPDATE person`
`SET name='李老四',age=55`
`WHERE age=24;`

通常修改语句要添加WHERE子句，用于添加过滤条件来定位要修改的记录，不添加WHERE子句则是全表所有记录都修改

`UPDATE person SET age=55;`


# 删除数据
`DELETE FROM 表名 [WHERE 过滤条件]`

注意！！！不添加WHERE条件则是全发表删除！！！

`DELETE FROM person WHERE name='李老四';`

`UPDATE person SET age=20 WHERE name='张三';`
`DELETE FROM person WHERE age>25; #删除年龄大于25岁的人`

```sql
CREATE DATABASE day1db CHARSET=UTF8;
USE day1db;
CREATE TABLE t_hero(
    name VARCHAR(32)
)CHARSET UTF8;
RENAME TABLE t_hero TO hero;
ALTER TABLE hero ADD money INT(10);
ALTER TABLE hero ADD id INT FIRST;
ALTER TABLE hero ADD age INT(3) AFTER name;

INSERT INTO hero(name,age,money) VALUES ('李白',22,6888);
INSERT INTO hero(name,age,money) VALUES ('赵云',30,13888);
INSERT INTO hero(name,age,money) VALUES ('刘备',25,6888);

SELECT name FROM hero WHERE money=6888;
SELECT * FROM hero;

UPDATE hero SET age=52 WHERE name='刘备';
UPDATE hero SET money=5000 WHERE age<50;

DELETE FROM hero WHERE money=5000;
DROP TABLE hero;
DROP DATABASE  day1db;
USE empdb;
SELECT * FROM emp;
USE mydb;
```






# 数据类型
# 数字类型
- 整数: INT(m)和BIGINT(m)  m表示的是长度  例如:m=5,存数字18,实际存储00018
- 浮点数:DOUBLE(m,n) m表示整体数字长度,n表示小数位  例如:DOUBLE(5,3)  99.999  （实际插入数据时，当精度超过可保存范围时，会四舍五入）

# 字符类型
- CHAR(n):定长字符串，每条记录实际占用的字节空间是定长的，不足的部分补充空字符来满足长度要求
          优点:查询速度快  缺点:浪费磁盘空间
- VARCHAR(n):变长字符串，最多存n指定的字节数对应的字符，实际保存时，用多少占多少  （推荐）
          优点:节省磁盘空间  缺点:查询速度慢
- TEXT(n):可变长字符串，最大65535

日期时间类型

- DATE:保存年月日
- TIME:保存十分秒
- DATETIME:保存年月日时分秒
- TIMESTAMP:时间戳，记录UTC时间，从1970-01-01 00:00:00到表示的时间之间经过的毫秒

```sql
DROP TABLE userinfo;
CREATE TABLE userinfo(
    id INT,
    name VARCHAR(30),
    birth DATETIME,
    salary DOUBLE(7,2)
)CHARSET UTF8;
set names UTF8;
INSERT INTO userinfo VALUES (1,'张三','1992-08-02 11:22:05',5000.59);
INSERT INTO userinfo VALUES (2,'李四','1999-05-16',6500.23);
INSERT INTO userinfo VALUES (3,'王五','06:12:45',9700.342);
DELETE FROM userinfo;
SELECT * FROM userinfo;
DELETE FROM userinfo WHERE name='王五';
```



约束:约束是为表中某个字段添加特定的限制条件，只有符合条件的记录才可以保存
主键约束:该字段非空且唯一，用该字段的值唯一表示一条记录
非空约束:该字段的值不允许为空
外键约束:实际开发中几乎不用

```sql
CREATE TABLE student(
    id INT AUTO_INCREMENT PRIMARY KEY ,# AUTO_INCREMENT 自增
    name VARCHAR(30) NOT NULL ,
    age INT(3),
    gender CHAR(1)
);
DESC student;
SELECT * FROM student;

INSERT INTO student VALUES (NULL,NULL,55,'m');
INSERT INTO student VALUES (NULL,'刘桑',55,'m');
INSERT INTO student(name,age,gender) VALUES ('克晶',18,'f');
```

不允许

```sql
INSERT INTO student(age,gender) VALUES (18,'f');

INSERT INTO student(name,age,gender) VALUES ('传奇',22,NULL);
INSERT INTO student(name,age) VALUES ('国斌',33);

DELETE FROM student WHERE id=3;



CREATE TABLE teacher(
    id INT PRIMARY KEY ,
    name VARCHAR(30) NOT NULL,
    age INT(3),
    gender CHAR(1)
);
INSERT INTO teacher VALUES (1,'张三',22,'F');
INSERT INTO teacher VALUES (1,'李四',23,'M');# 不可重复
INSERT INTO teacher VALUES (NULL,'李四',23,'M');
SELECT * FROM teacher;
```




# NULL 要作为条件，要使用IS NULL 或 IS NOT NULL
```sql
SELECT * FROM student WHERE gender IS NULL;
SELECT * FROM student WHERE gender IS NOT NULL;
```



# DQL语句  数据查询语句
## 基本语法:

`SELECT 字段名1[字段名2，字段名2，...或 * ]  FROM 表名`

`USE empdb;`

查看emp表的所有字段

`SELECT * FROM emp;`
查看特定的字段
`SELECT name,job,hiredate FROM emp;`

## WHERE子句，用来添加过滤条件，此时可以仅将满足条件的记录查询出来

比较运算符:=,<,>,>=,<=,<>

查看工资大于1000的员工的名字，职位，工资

```sql
SELECT name,job,sal
FROM emp
WHERE sal>1000;

SELECT  name,job,sal
FROM emp
WHERE job<>'人事';

SELECT name,job,sal,dept_id
FROM emp
WHERE dept_id=2;
```

## 使用AND和OR来连接多个条件

```sql
SELECT name,sal,job,dept_id
FROM emp
WHERE dept_id=2 AND sal>1000;

SELECT name,sal,job,dept_id
FROM emp
WHERE job='人事' OR job='销售';

SELECT name,sal,job
FROM emp
WHERE job='人事' OR sal>1000 AND job='销售';

SELECT name,sal,job
FROM emp
WHERE (job='人事' OR job='销售') AND sal>1000; # and优先级大于or,可以通过（）提高优先级
```



## IN(列表) 值在列表中（等于列表中的其中之一）

```sql
SELECT name,sal,job,dept_id
FROM emp
WHERE job IN ('人事','销售');

SELECT name,sal,job,dept_id
FROM emp
WHERE job NOT IN ('人事','销售');
```

## 区间

```sql
SELECT name,sal,job
FROM emp
WHERE sal BETWEEN 2000 AND 3000;
```

## 去重

```sql
SELECT DISTINCT job FROM emp;
```

多列去重时，就是去除指定这些列的值的组合有重复的行

```sql
SELECT DISTINCT job,dept_id FROM emp;


SELECT *
FROM emp
WHERE dept_id=2 AND sal>1000;

SELECT name,job,sal,dept_id
FROM emp
WHERE dept_id=3 OR sal=5000;

SELECT name,job,sal,dept_id
FROM emp
WHERE sal BETWEEN 1000 AND 2000;

SELECT name,sal,job,dept_id
FROM emp
WHERE sal NOT IN (2000,5000);

SELECT DISTINCT job
FROM emp
WHERE dept_id=1;
```

## 模糊查询: LIKE

### LIKE 中两个通配符:_和%

- %:表示任意的一个字符(0-多个)
- _:表示一个字符

```sql
SELECT name,sal,job
FROM emp
WHERE name LIKE '孙%';

SELECT name,sal,job
FROM emp
WHERE name LIKE '%悟%';

SELECT name,sal,job
FROM emp
WHERE name LIKE '__精';

SELECT name,sal,job
FROM emp
WHERE name LIKE '_骨%';
```

总结:

- %X%:字符串中包含'X'
- %X:字符串以X结尾
- X%:字符串以X开头
- _X%:字符串第二个字符是X
- _%X_:倒数第二个字符是X
- X%Y:字符串以X开头Y结尾
- X_Y:字符串只有三个字，第一个是X，第三个是Y

```sql
SELECT name
FROM emp
WHERE name LIKE '猪%';

SELECT *
FROM emp
WHERE name LIKE '%僧%';

SELECT name
FROM emp
WHERE name LIKE '%精';

SELECT *
FROM emp
WHERE job LIKE '%销售%' AND sal>1500;

SELECT name,job
FROM emp
WHERE job LIKE '_售%';

SELECT *
FROM emp
WHERE dept_id IN (1,2) AND job LIKE '市%';
```

### ORDER BY 子句，根据指定的字段排序查询结果集，该子句只能放在查询语句的最后一个子句上

默认升序    DESC降序

```sql
SELECT name,sal
FROM emp
ORDER BY sal;

SELECT name,hiredate
FROM emp
ORDER BY hiredate;

SELECT name,sal
FROM emp
ORDER BY sal DESC;
```

按照多字段排序，在前的优先，可以单独设置升序和降序

```sql
SELECT name,dept_id,sal
FROM emp
ORDER BY dept_id,sal DESC;


SELECT *
FROM emp
WHERE manager IS NOT NULL
ORDER BY hiredate;

SELECT *
FROM emp
WHERE dept_id=1 AND name LIKE '%八%';

SELECT *
FROM emp
WHERE dept_id IN (2,3) AND sal<5000;

SELECT name,sal,job
FROM emp
WHERE job IN ('人事','程序员') AND sal>2500;

SELECT name,job,sal
FROM emp
WHERE job NOT IN ('CEO') AND sal>2000
ORDER BY sal DESC ;
```



# 分页查询
将满足查询条件的数据分段分批查询出来。这可以减少不必要的系统开销。

LIMITE 跳过的记录数，显示的记录数

LIMITE (页数-1)*美页显示的记录数，每页显示的记录数

```sql
SELECT name,sal
FROM emp
ORDER BY sal LIMIT 3,3;
```

## 查询的字段可以使用表达式

`SELECT name,sal,sal*12 FROM emp;`

## 查询时也可以使用函数的结果作为字段

`SELECT CONCAT(name,'的职位是',job) FROM emp;`

`SELECT CONCAT(name,'的奖金是',comm) FROM emp;`

数字与NULL运算，结果就是NULL

`SELECT sal,comm,sal+comm`
`FROM emp;`

NVL函数 用来替换NULL值

NVL(arg1,arg2)  当arg1不为NULL时，则函数返回arg1的值，如果arg1为NULL在返回arg2的值

`SELECT name,sal,NVL(comm,0) FROM emp;`

## 别名（字段和表）

为字段定义别名:

1.隐藏实际表字段名

2.为计算表达式或函数的结果值作为字段时定义可读性更好的字段名

`SELECT name ename,sal salary FROM emp;`
`SELECT name,sal*12 salary FROM emp;`

## 支持的语法

字段名 别名

`SELECT name,sal*12 salary FROM emp;`

## 字段名 as 别名

`SELECT name,sal*12 as salary FROM emp;`

## 字段名 as '别名'

`SELECT name,sal*12 as 'salary' FROM emp;`

## 字段名 as "别名"

`SELECT name,sal*12 as "salary" FROM emp;`

```sql
SELECT *
FROM emp
WHERE dept_id=3 AND sal>1500;

SELECT *
FROM emp
WHERE dept_id=2 OR manager IS NULL;

SELECT name,sal
FROM emp
WHERE manager IS NOT NULL
ORDER BY sal;

SELECT name,hiredate
FROM emp
WHERE dept_id IN (2,3)
ORDER BY hiredate DESC ;

SELECT name
FROM emp
WHERE name LIKE '%僧%' OR  name LIKE '%精%';

SELECT DISTINCT job
FROM emp
WHERE sal>2000;

SELECT sal
FROM emp
ORDER BY sal LIMIT 6,2;


```

聚合函数（多行函数）: 用来将多条记录统计为一条记录  (忽略NULL值)

MIN():求最小值

MAX():求最大值

COUNT():统计记录数

AVG():求平均值

SUM():求和

```sql
SELECT MIN(sal) 最低工资,MAX(sal) 最高工资,AVG(sal) 平均工资,SUM(sal) 工资总和 FROM emp;


SELECT AVG(sal)
FROM emp
WHERE job='销售';


SELECT MAX(sal)
FROM emp
WHERE job='程序员';

SELECT COUNT(*)
FROM emp
WHERE name LIKE '%精%';

SELECT SUM(sal)
FROM emp
WHERE job LIKE '%销售%';

SELECT MAX(sal) 最高工资, MIN(sal) 最低工资
FROM emp
WHERE dept_id=2;
```



GROUP BY子句，分组
GROUP BY 也是为统计服务的，所以是搭配在聚合函数上使用的

SELECT子句中不在聚合函数中的其他字段必须出现GROUP BY子句中

```sql
SELECT AVG(sal),dept_id FROM emp GROUP BY dept_id;

SELECT MAX(sal),job FROM emp GROUP BY job;

SELECT MAX(sal),dept_id FROM emp GROUP BY dept_id; #查询最高工资

SELECT COUNT(*)
FROM emp
WHERE sal>2000
GROUP BY dept_id;

SELECT MIN(sal),job FROM emp GROUP BY job;

SELECT COUNT(*),dept_id
FROM emp
WHERE dept_id IN (1,2)
GROUP BY dept_id;

SELECT AVG(sal) avg,dept_id
FROM emp
GROUP BY dept_id
ORDER BY avg DESC
LIMIT 0,1;
```



聚合函数不能写在WHERE子句中

```sql
SELECT AVG(sal) avg,dept_id
FROM emp
WHERE AVG(sal)>2000
ORDER BY dept_id;
```



HAVING子句 HAVING子句是跟在GROUP BY子句之后，对分组统计出的结果再进行过滤的

```sql
SELECT AVG(sal),dept_id
FROM emp
GROUP BY dept_id
HAVING AVG(sal)>2000;

SELECT AVG(sal),dept_id
FROM emp
GROUP BY dept_id
HAVING MIN(sal)>1000;


SELECT SUM(sal) sal,dept_id
FROM emp
WHERE manager IS NOT NULL
GROUP BY dept_id
HAVING SUM(sal)>5400;
```



### 嵌套在其他SQl语句中的查询语句被称作“子查询”

```sql
SELECT name,sal
FROM emp
HAVING sal> (SELECT AVG(sal) FROM emp);

SELECT *
FROM emp
HAVING sal> (SELECT AVG(sal) FROM emp WHERE dept_id=2);

SELECT *
FROM emp
HAVING sal<(SELECT sal FROM emp WHERE name='沙僧');

SELECT *
FROM emp
HAVING job=(SELECT job FROM emp WHERE name='孙悟空');

SELECT *
FROM emp
HAVING dept_id=(SELECT dept_id FROM emp WHERE sal=(SELECT MIN(sal) FROM emp));


SELECT *
FROM emp
WHERE sal>ALL(SELECT sal FROM emp WHERE dept_id IN (2,3));

SELECT *
FROM emp
WHERE sal>ANY(SELECT sal FROM emp WHERE dept_id IN (2,3));
```

### 子查询分类（按查询结果集分类）:

单行单列查询（结果集只有一个值）
多行单列子查询（结果集有多个值）
多行多列子查询（结果集是一个表）

单行单列查询通常在过滤条件中使用
单行单列可以配合>,>=,=,<,<=使用
多行单列可以配合ANY,ALL,IN使用
例如:

>ALL(子查询)
><ALL(子查询)
>ANY(子查询)
><ANY(子查询)：
>IN(子查询)：等于子查询结果集中的任意一个值

多行多列子查询（结果通常是一个表），通常就当做一个表，可以跟在FROM子句中，或者跟在DDl语句中，可以基于一个查询结果集创建表。

```sql
CREATE  TABLE emp_dept1
AS
SELECT * FROM emp WHERE dept_id=1;
SELECT * FROM emp_dept1;
如果创建表基于的子查询某个字段是一个表达式或函数时，要给该字段取别名，那么创建出来的表该字段会以别名作为字段名

CREATE TABLE emp_dept_sal
AS
SELECT MAX(sal) max_sal,MIN(sal) min_sal,AVG(sal) avg_sal, SUM(sal) sum_sal,dept_id
FROM emp
GROUP BY dept_id;

SELECT * FROM emp_dept_sal;


DROP TABLE emp_annual_salary;
CREATE TABLE emp_annual_salary
AS
SELECT name aneme,sal salary,sal+12 a_salary,dept_id
FROM emp;

SELECT * FROM emp_annual_salary;

SELECT aneme,a_salary
FROM emp_annual_salary
WHERE aneme LIKE '%精%';


SELECT * FROM dept;
```






### 关联查询
查询结果集中的数据来自多张表，而表中的数据之间的对应关系就是关联关系

两张表就可以产生关联关系了，关联关系分为三类:
1:一对一  A表中的1条记录只唯一对应B表中的1条记录
2:一对多  A表中的1条记录可以对应B表中的多条记录
3:多对多  A表与B表双向都是一对多时，就是多对多关系。


关联查询就是基于多张表联合查询数据而形成一个结果集的过程，在关联查询中一个至关重要的点就是关联条件
原则:N张表关联查询至少要有N-1个连接条件。
缺失连接条件会产生笛卡尔积，该查询结果集的记录数是关联表中所有记录数乘积的结果，它通常是一个无意义的结果集，要
尽量避免产生

关联查询语法:

 SELECT 字段

 FROM 表A，表B[，表C，表D...]

 WHERE 过滤条件

 AND 连接条件

 注意:连接条件必须与过滤条件同时成立!!

```sql
SELECT *
FROM emp,dept;

当表中的字段名相同时，我们可以通过给表取别名用"别名.字段名"
SELECT e.name,e.sal,e.dept_id,d.name,d.loc
FROM emp e,dept d
WHERE e.dept_id=d.id;

SELECT e.name,e.sal,e.job,d.name,d.loc
FROM emp e,dept d
WHERE e.dept_id=d.id
AND d.loc='天庭';

SELECT e.name,d.loc
FROM emp e,dept d
WHERE e.dept_id=d.id
AND e.name LIKE '%飞%';

SELECT e.name,MAX(e.sal) max_sal,d.loc
FROM emp e ,dept d
WHERE e.dept_id=d.id
AND d.loc='天庭'
GROUP BY d.loc;


SELECT AVG(e.sal),d.loc
FROM emp e ,dept d
WHERE e.dept_id=d.id
GROUP BY d.loc;

SELECT sal,name
FROM emp
WHERE sal>3000;
```



内连接JOIN子句

SELECT 字段

FROM A表 a

JOIN B表

ON a.xx=b.xx(连接条件)

JOIN C表 c

ON c.xxx=b.xxx或c.xxx=a.xxx;

JOIN...ON...

```sql
SELECT e.name,e.job,e.manager,e.sal,d.name,d.loc
FROM emp e
JOIN dept d
on e.dept_id=d.id;

在内连接中，过滤条件还是写在WHERE子句中
SELECT e.*,d.loc
FROM emp e
JOIN dept d
ON e.dept_id = d.id
WHERE e.sal>1300;

在关联查询中不满足连接条件的记录会被排除在外
SELECT * FROM emp;
INSERT INTO emp(name,dept_id) VALUES ('灭霸',5);

SELECT e.name,e.job,e.manager,e.sal,d.name,d.loc
FROM emp e
JOIN dept d
ON e.dept_id = d.id
```



如果需要在结果集中列出不满足连接条件的记录时我们需要使用外连接
外连接:
左外连接: 以LEFT JOIN左侧表为主表，其中的记录都要展示，不满足连接条件时来自左侧记录的字段值全部为NULL
右外连接: 以RIGHT JOIN右侧表为主表，其中的记录都要展示，不满足连接条件时来自左侧记录的字段值全部为NULL

```sql
SELECT e.name,e.job,e.manager,e.sal,d.name,d.loc
FROM emp e
LEFT JOIN dept d  #此为主表，展示所有，不满足的为NULL
ON e.dept_id = d.id;

SELECT e.name,e.job,e.manager,e.sal,d.name,d.loc
FROM dept d
RIGHT JOIN emp e
ON d.id = e.dept_id
```



全连接效果，结果集包含满足连接条件的左连接和有连接的所有数据

```sql
SELECT e.name,e.job,e.manager,e.sal,d.name,d.loc
FROM emp e
LEFT JOIN dept d  #此为主表，展示所有，不满足的为NULL
ON e.dept_id = d.id;
UNION
SELECT e.name,e.job,e.manager,e.sal,d.name,d.loc
FROM emp e
RIGHT JOIN dept d
ON d.id = e.dept_id;

SELECT e.*,d.*
FROM emp e
JOIN dept d on d.id = e.dept_id
WHERE sal>(SELECT AVG(sal) FROM emp WHERE e.dept_id);
```



查看比本部门平均工资高的员工工资
1.查看每个部门的平均工资

```sql
avg_sal
SELECT AVG(sal) avg_sal,dept_id FROM emp GROUP BY dept_id;
```



2.将子查询结果当做表进行关联

```sql
SELECT e.name,e.sal,e.dept_id,a.avg_sal
FROM emp e,(SELECT AVG(sal) avg_sal,dept_id FROM emp GROUP BY dept_id) a
WHERE e.dept_id=a.dept_id
AND e.sal>a.avg_sal;
SELECT * FROM dept d,emp e WHERE d.id=e.dept_id;
```



1.查看每个地区的平均工资

```sql
SELECT AVG(e.sal) avg_sal,d.loc
FROM emp e
JOIN dept d
ON d.id = e.dept_id
GROUP BY d.loc;


SELECT e.name,e.sal,e.dept_id,a.avg_sal,d.loc,d.id
FROM emp e,
     (SELECT AVG(e.sal) avg_sal,d.loc
            FROM emp e
            JOIN dept d
            ON d.id = e.dept_id
            GROUP BY d.loc) a,dept d
WHERE a.loc=d.loc AND d.id=e.dept_id
AND e.sal>a.avg_sal;
```






1.查看每个员工的工资及其所在的地区
```sql
SELECT e.sal,d.loc
FROM emp e,dept d
WHERE e.dept_id=d.id;
```
2.每个地区平均工资（按照loc字段分组）
```sql
SELECT AVG(e.sal) avg_sal,d.loc
FROM emp e,dept d
WHERE e.dept_id=d.id
GROUP BY d.loc;
```
3.关联三张表查询:员工表-部门表-（第二步子查询的结果作为表）
```sql

SELECT e.name,e.sal,a.avg_sal,d.loc
FROM emp e,dept d,(SELECT  AVG(e.sal) avg_sal,d.loc
                   FROM emp e,dept d
                   WHERE e.dept_id=d.id
                   GROUP BY d.loc) a
WHERE e.dept_id=d.id
AND d.loc=a.loc
AND e.sal>a.avg_sal;
```
内连接写法
```sql
SELECT e.name,e.sal,a.avg_sal,d.loc
FROM emp e
JOIN dept d
ON e.dept_id=d.id
JOIN (SELECT  AVG(e.sal) avg_sal,d.loc
                   FROM emp e,dept d
                   WHERE e.dept_id=d.id
                   GROUP BY d.loc) a
ON d.loc=a.loc
WHERE e.sal>a.avg_sal;
```


查看每个地区的最高工资是谁

查看最高工资
```sql
SELECT MAX(sal)
FROM emp

SELECT MAX(sal),loc,e.name
FROM emp e
JOIN dept d
ON e.dept_id = d.id  # 将部门关联起来
GROUP BY loc; # 按地区分组
```

内连接
自连接的设计是为了保存同样的一组数字卡的数据，之间又存在上下级关系时（树状结构数据）

查看每个员工和他的领导是谁
```sql
SELECT e.name,m.name
FROM emp e,emp m
WHERE e.manager=m.id

SELECT e.name,m.name
FROM emp e
JOIN emp m
ON e.manager=m.id;
```

查看刘备的手下
```sql
SELECT * FROM emp;
SELECT e.name name,m.name manager
FROM emp e
JOIN emp m
ON e.manager=m.id
WHERE m.name='刘备';
```

查看孙悟空的领导
```sql
SELECT e.name name,m.name manager,m.sal
FROM emp e
JOIN emp m
ON e.manager=m.id
WHERE e.name='孙悟空';

SELECT name,sal
FROM emp
WHERE sal>(SELECT m.sal
           FROM emp e
           JOIN emp m
           ON e.manager=m.id
           WHERE e.name='孙悟空');

CREATE TABLE userinfo(
    id INT primary key auto_increment,
    username VARCHAR(30) NOT NULL ,
    password VARCHAR(30),
    age INT(3),
    salary DOUBLE(7,2)
);
DROP TABLE userinfo;

DESC userinfo;

CREATE TABLE Student(
    id INT primary key auto_increment,
    name VARCHAR(32),
    age INT(3),
    class_id INT(3)
);

CREATE TABLE Class(
    id INT primary key auto_increment,
    name VARCHAR(32)
);
DESC Student;
DESC class;

DROP TABLE student;
DROP TABLE class;
SELECT * FROM class;
```

---

练习
1. 查询工资大于等于3000的员工姓名和工资
SELECT name,sal
FROM emp
WHERE sal>=3000;

2. 查询1号部门的员工姓名和工作
SELECT name,job
FROM emp
WHERE dept_id=1;

3. 查询不是程序员的员工姓名和工作(两种写法)
SELECT name,job
FROM emp
WHERE NOT IN '程序员' ;

SELECT name,job
FROM emp
WHERE job<>'程序员'

4. 查询奖金等于300的员工姓名,工资和工作
SELECT name,sal,job
FROM emp
WHERE comm=300;

5. 查询1号部门工资大于2000的员工信息
SELECT *
FROM emp
WHERE sal>2000 AND dept_id=1

6. 查询3号部门或工资等于5000的员工信息
SELECT *
FROM emp
WHERE dept_id=3 OR sal=5000

7. 查询出CEO和项目经理的名字
SELECT name
FROM emp
WHERE job='CEO' OR job='项目经理'

8. 查询工资为3000,1500和5000的员工信息
SELECT *
FROM emp
WHERE sal IN (3000,1500,5000)

9. 查询工资不等于3000,1500和5000的员工信息
SELECT *
FROM emp
WHERE sal NOT IN (3000,1500,5000)

10. 查询工资在1000到2000之间的员工信息
SELECT *
FROM emp
WHERE sal>1000 AND sal<2000

11. 查询工资在1000到2000以外的员工信息
SELECT *
FROM emp
WHERE sal<1000 OR sal>2000

12. 查询有领导的员工姓名和领导id
SELECT name,manager
FROM emp
WHERE manager IS NOT NULL

13. 查询没有领导的员工姓名和领导id
SELECT name ,manager
FROM emp
WHERE manager IS NULL

14. 查询员工表中出现了哪几种不同的工作
SELECT job
FROM emp
GROUP BY job

15. 查询员工表中出现了那几个部门的id
SELECT dept_id
FROM emp
GROUP BY dept_id

16. 查询姓孙的员工姓名
SELECT name
FROM emp
WHERE name LIKE '孙%'

17. 查询名字最后一个字是精的员工信息
SELECT *
FROM emp
WHERE name LIKE '%精'

18. 查询工作中包含销售的员工信息
SELECT *
FROM emp
WHERE job LIKE '%销售%'

19. 查询工作中第二个字是售的员工信息
SELECT *
FROM emp
WHERE job LIKE '_售%'

20. 查询名字中包含僧的员工并且工资高于2000的员工信息
SELECT *
FROM emp
WHERE name LIKE '%僧%' AND sal>2000

21. 查询1号和2号部门中工作以市开头的员工信息
SELECT *
FROM emp
WHERE name LIKE '市%' AND dept_id IN (1,2)

22. 查询所有员工的姓名和工资 按照工资升序排序
SELECT name,sal
FROM emp
ORDER BY sal;

23. 查询所有员工的姓名和工资 按照工资降序排序
SELECT name,sal
FROM emp
ORDER BY sal DESC;

24. 查询所有员工姓名 工资和部门id 按照部门id降序排序,如果部门id一致则按照工资升序排序
SELECT name,sal,dept_id
FROM emp
ORDER BY dept_id DESC,sal;

25. 查询员工表中3号部门工资高于1500的员工信息
SELECT *
FROM emp
WHERE dept_id=3 AND sal>1500

26. 查询2号部门员工或者没有领导的员工信息
SELECt *
FROM emp
WHERE dept_id=2 OR manager IS NULL;

27. 查询有领导的员工姓名,工资按照工资降序排序
SELECT name,sal
FROM emp
WHERE manager IS NOT NULL
ORDER BY sal DESC

28. 查询2号和3号部门的员工姓名和入职日期hiredate 按照入职日期降序排序
SELECT name,hiredate
FROM emp
WHERE dept_id IN (2,3)
ORDER BY hiredate DESC

29. 查询名字中包含僧和包含精的员工姓名
SELECT name
FROM emp
WHERE name LIKE '%僧%'AND name LIKE'%精%'

30. 查询工资高于2000的工作有哪几种?
SELECT job
FROM emp
WHERE sal>2000
GROUP BY job

31. 查询工资最高的前三个员工
SELECT *,MAX(sal) max_sal
FROM emp
ORDER BY sal LIMIT 0,3

32. 查询员工表按照id排序, 第2页的5条数据
SELECT *
FROM emp
ORDER BY id LIMIT 1,5

33. 查询员工表按照id排序, 第3页的4条数据
SELECt *
FROM emp
OEDER BY id LIMIT 2,4

34. 查询3号部门工资最低的员工姓名和工资
SELECT name,MIN(sal)
FROM emp

35. 查询工作不是人事的员工中工资降序第二页的3条数据
SELECT *
FROM emp
WHERE job<>'人事'
ORDER BY sal LIMIT 1,3

36. 查询没有领导的员工和3号部门的员工,工资降序取前三条
SELECT *
FROM emp
WHERE manager IS NULL AND dept_id=3
ORDER BY sal DESC LIMIT 0,3

37. 查询2号部门的最高工资
SELECT MAX(sla)
FROM emp
WHERE dept_id=2

40. 查询有领导的员工中工资在1000到2000之间的人数

41. 查询3号部门的工资总和
42. 查询程序员和销售的总人数
43. 查询1号部门有领导的员工的平均工资
44. 查询1号部门的最低工资和最高工资
45. 查询和销售相关的工作人数
46. 查询工资不是1500和3000的员工人数
47. 查询1号部门出现了哪几种工作
48. 查询名字包含精的员工数量
49. 查询和销售相关的工作一个月工资总和
50. 查询2号部门的最高工资和最低工资起别名
51. 查询每个部门的平均工资
52. 查询每种工作的平均工资
53. 查询每个部门的最高工资
54. 查询每种工作的最低工资
55. 查询每个部门工资高于2000的人数
56. 查询每个部门有领导的员工人数
57. 查询1号部门每种工作的最低工资
58. 查询平均工资最高的部门id和平均工资
59. 查询每个部门的平均工资,要求平均工资大于2000
60. 查询每种工作的人数,只查询人数大于1的
61. 查询每个部门的工资总和,只查询有领导的员工, 并且要求工资总和大于5400.
62. 查询每个部门的平均工资, 只查询工资在1000到3000之间的,并且过滤掉平均工资低于2000的











/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 5.5.68-MariaDB : Database - newdb3
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`empdb` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `empdb`;

/*Table structure for table `dept` */

DROP TABLE IF EXISTS `dept`;

CREATE TABLE `dept` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `name` varchar(14) NOT NULL,
  `loc` varchar(13) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `DNAME` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Data for the table `dept` */

insert  into `dept`(`id`,`name`,`loc`) values (1,'神仙','天庭'),(2,'妖怪','盘丝洞'),(3,'普通人','北京'),(4,'赛亚人','外星球');

/*Table structure for table `emp` */

DROP TABLE IF EXISTS `emp`;

CREATE TABLE `emp` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `job` varchar(9) DEFAULT NULL,
  `manager` int(4) DEFAULT NULL,
  `hiredate` date DEFAULT NULL,
  `sal` double(7,2) DEFAULT NULL,
  `comm` double(7,2) DEFAULT NULL,
  `dept_id` int(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

/*Data for the table `emp` */

insert  into `emp`(`id`,`name`,`job`,`manager`,`hiredate`,`sal`,`comm`,`dept_id`) values (1,'孙悟空','销售',4,'1980-12-17',800.00,NULL,1),(2,'猪八戒','销售',4,'1981-02-20',1600.00,300.00,1),(3,'沙僧','销售',4,'1981-02-22',1250.00,500.00,1),(4,'唐僧','销售经理',8,'1981-04-02',2975.00,NULL,1),(5,'刘备','项目经理',NULL,'1981-09-28',1250.00,1400.00,3),(6,'关羽','程序员',5,'1981-05-01',2850.00,NULL,3),(7,'张飞','程序员',5,'1981-06-09',2450.00,NULL,3),(8,'观音','CEO',NULL,'1981-11-17',5000.00,NULL,1),(9,'白骨精','人事',8,'1981-09-08',1500.00,0.00,2),(10,'蜘蛛精','人事',8,'1981-12-03',950.00,NULL,2),(11,'黑熊怪','市场',8,'1981-12-03',3000.00,NULL,2);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
set names UTF8;
