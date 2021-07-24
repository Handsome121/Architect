	Python面试大全

## 1.Python基础

### 1.1 文件操作

1.有一个jsonline格式的文件file.txt大小约为10K

```python
def get_lines():
	with open ("file.txt","rb") as f :
        return f.readlins() # 读取文件的每一行到一个列表中
if __name__ == "__main__":
    for e in get_lines():
        process(e) # 处理每一行数据
```

现在要处理一个大小为10G的文件，但是内存只有4G，如果在只修改get_lines 函数而其他代码保持不
变的情况下，应该如何实现？需要考虑的问题都有那些？

```python
def get_lines():
	with open('file.txt','rb') as f:
		for i in f:
		yield i #打印所有行
for i in get_lines():
    print(i) # 一次返回所有行，读取时间太长
```

以上读取次数太多，设置一下每次读取的行数

```python
def get_lines():
    l = []
	with open('file.txt','rb') as f:
		data = f.readlines(60000)
    l.append(data)
	yield i 
```

**要考虑的问题有：内存只有4G无法一次性读入10G文件，需要分批读入，分批读入数据要记录每次读入数据的位置。分批每次读取数据的大小，太小会在读取操作花费过多时间。**

2、将一个文件复制到另外一个文件中

方法一：

```python
import time
def copy(filename):
    fr=open(filename,"rb")
    file="%s-%s-%s.jpg"%time.localtime()[:3]
    # time.struct_time(tm_year=2020, tm_mon=9, tm_mday=12, tm_hour=22, tm_min=11, tm_sec=47, tm_wday=5, tm_yday=256, tm_isdst=0)
    fw=open(file,"wb")
    while True:
        data=fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()
copy("../timg.jpg")
```

方法二：

```python
import time
def copy(filename):
    with open(filename,"rb") as fr :
        lines = fr.readlines()
        file="%s-%s-%s.jpg"%time.localtime()[:3]
        # time.struct_time(tm_year=2020, tm_mon=9, tm_mday=12, tm_hour=22, tm_min=11, tm_sec=47, tm_wday=5, tm_yday=256, tm_isdst=0)
        with open(file,"wb") as fw:
            fw.writelines(lines)
copy("../timg.jpg")
```

3、补充缺失的代码

```python
def print_directory_contents(s_Path):
"""
这个函数接收文件夹的名称作为输入参数
返回该文件夹中文件的路径
以及其包含文件夹中文件的路径
"""
import os
for s_child in os.listdir(s_path):	# os.listdir(path) 列出指定目录下的文件和子目录
	s_child_path = os.path.join(s_path, s_child)	# os.path.join(path1[, path2[, ...]]) 把目录和文件名合成一个路径
	if os.path.isdir(s_child_path):	# os.path.isdir(s_child_path) 判断路径是否为目录
		print_directory_contents(s_child_path)	# 如果是目录，则继续合并目录和文件
	else:
		print(s_child_path)	# 如果是文件，则输出文件路径
```

4、设计实现遍历目录与子目录，抓取.pyc文件(重点代码)

```python
方法一：
import os
def get_files(dir,suffix):
	res = []
	for root,dirs,files in os.walk(dir):
        if dirs = []:
            for filename in files:
                name,suf = os.path.splitext(filename)
                if suf == suffix:
                    res.append(os.path.join(root,filename))
        else:
            for dir in dirs:
                get_files(dir,suffix)
	print(res)
get_files("../",".pyc"）
```

```python
方法二：
import os 
def pick(obj):
    if obj.endwith(".pyc"):
        print(obj)
def scan(ph):
    file_list=os.listdir(ph)
    for obj in file_list:
        if os.path.isfile(obj):
            pick(obj)
        elif os.path.isdir(obj):
            scan(obj)
if __name__ == "__main__":
    path = input("请输入路径")
    scan(path)
```



### 1.2 模块与包

1、输入日期， 判断这一天是这一年的第几天？

```python
import datetime
def dayofyear():
    year = input("请输入年份: ")
	month = input("请输入月份: ")
	day = input("请输入天: ")
    date1 = datetime.date(year = int(year),month = int(month),day = int(day))
    date2 = datetime.date(year = int(year),month = 1,day = 1)
    return (date1-date2).days+1
```



### 1.3 数据类型

1、打乱一个排好序的list对象alist？

```python
import random 
alist = [1,2,3,4,5,6]
random.shuffle(alist) # 打乱列表对象
print(alist)
```

2、现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?

```python
sorted(d.items())
```

3、字典推导式

```python
d = {key,value for (key,value) in iterable}
```

4、请反转字符串 "aStr"?

```python
print("astr"[::-1])
```

5、将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}

```python
str1 = "k:1 |k1:2|k2:3|k3:4"
def str2dict(str1):
	dict1 = {}
	for iterms in str1.split('|'):
		key,value = iterms.split(':')
		dict1[key] = value
	return dict1
d = {k:int(v) for t in str1.split("|") for k, v in (t.split(":"))}
```

6、请按alist中元素的age由大到小排序

```python
alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
def sort_by_age(list1):
    return sorted(alist,key=lambda x:x["age"],reverse=True)
```

7、下面代码的输出结果将是什么？

```python
list = ['a','b','c','d','e']
print(list[10:])
[]
```

8、写一个列表生成式，产生一个公差为11的等差数列

```python
print([x * 11 for x in range(10)])
```

9、给定两个列表，怎么找出他们相同的元素和不同的元素？

```python
list1 = [1,2,3]
list2 = [3,4,5]
set1 = set(list1)
set2 = set(list2)
print(set1 & set2)
print(set1 ^ set2)
```

10、请写出一段python代码实现删除list里面的重复元素？

```python
l1 = ['b','c','d','c','a','a']
l2 = list(set(l1))
print(l2)
l1 = ['b','c','d','c','a','a']
l2 = []
for i in l1:
	if not i in l2:
	l2.append(i)
	print(l2)
```

11、给定两个list A，B ,请用找出A，B中相同与不同的元素

```python
A,B 中相同元素： print(set(A)&set(B))
A,B 中不同元素: print(set(A)^set(B))
```

12、Python语言有哪些数据类型

```python
答：
可变对象
	例如:列表，集合，字典
        特点：预留空间，自动扩容，动态改变
        自动扩容：
        	1、开辟更大空间
            2、拷贝原始数据
            3、替换引用（地址）
        优点：
        	动态添加数据
        缺点：
        	原始数据成为垃圾
        解决：
        	预留空间
不可变对象
	例如：数值，字符串，元组，bool
    	特点：按需分配（省内存）
存储多个数据：优先选择元组，因为性能更高，如果需要修改，再使用列表
```

13、使用自定义算法升序排序(重点代码)

```python
list01 = [4,3,2,4,5,6,7,90,199]
for r in range(len(list01)-1):
    for c in range(r+1,len(list01)):
        if list01[c] < list01[r]:
            list01[c],list01[r] = list01[r],list01[c]
            print(list01)
```

14、Python-遍历列表时删除元素的正确做法

```python
方法一
a = [1,2,3,4,5,6,7,8,9]
b = filter(lambda x: x > 5,a)
```

```python
a = [1,2,3,4,5,6,7,8,9]
b = [i for i in a if a > 5]
print(b)
```

```python
方法三(倒序删除)
a = [1,2,3,4,5,6,7,8,9]
for i in range(len(a)-1,-1,-1):
    if a[i] > 5:
        del a[i]
print(a)
```

15、可变类型和不可变类型

```python
1,可变类型有list,dict.不可变类型有string，number,tuple.
2,当进行修改操作时，可变类型传递的是内存中的地址，也就是说，直接修改内存中的值，并没有开辟新的内存。
3,不可变类型被改变时，并没有改变原内存地址中的值，而是开辟一块新的内存，将原地址中的值复制
过去，对这块新开辟的内存中的值进行操作。
```

16、is和==有什么区别？

```python
is：比较的是两个对象的id值是否相等，也就是比较俩对象是否为同一个实例对象。是否指向同一个内存地址
== ： 比较的两个对象的内容/值是否相等，默认会调用对象的eq()方法
```

17、用一行python代码写出1+2+3+10248

```python
from functools import reduce
#1使用sum内置求和函数
num = sum([1,2,3,10248])
#2使用reduce聚合函数
num1 = reduce(lambda x,y:x+y,[1,2,3,10248])
print(num1)
```

18、Python中变量的作用域？（变量查找顺序)

```python
函数作用域的LEGB顺序
1.什么是LEGB?
L： local 函数内部作用域
E: enclosing 函数内部与内嵌函数之间
G: global 全局作用域
B： build-in 内置作用域
python在函数里面的查找分为4种，称之为LEGB，也正是按照这是顺序来查找的
```

19、字符串 "123" 转换成 123 ，不使用内置api，例如 int()

```python
方法一： 利用 str 函数
def atoi(s):
	num = 0
	for v in s:
		for j in range(10):
			if v == str(j):
				num = num * 10 + j
	return num
```

```python
方法二： 利用 ord 函数
def atoi(s):
	num = 0
	for v in s:
		num = num * 10 + ord(v) - ord('0')
	return num
```

```python
方法三: 利用 eval 函数
def atoi(s):
	num = 0
	for v in s:
		t = "%s * 1" % v
		n = eval(t)
		num = num * 10 + n
	return num
```

方法四: 结合方法二，使用 reduce ，一行解决

```python
from functools import reduce
def atoi(s):
	return reduce(lambda num, v: num * 10 + ord(v) - ord('0'), s, 0)
```

20、python代码实现删除一个list里面的重复元素

```python
方法一:
def distFunc1(a):
    a = list(set(a))
    print(a)
```

```python
方法二:
def disFunc2(a):
    list = []
    for i in a:
        if i not list:
            list.append(i)
    list.sort()
    print(list)
```

22、python2与python3的区别？

| 类别             | python2                                                      | python3                    |
| :--------------- | ------------------------------------------------------------ | -------------------------- |
| print函数        | 使用print语句                                                | 使用print函数              |
| 编码             | ASCII编码                                                    | UTF-8                      |
| 除法             | / 结果是一个整数商                                           | / 结果是正确的结果         |
| xrange()函数     | 生成器                                                       | 使用range函数              |
| range()函数      | 生成列表                                                     |                            |
| 不等于运算符     | != 和<>                                                      | !=                         |
| 数据类型         | long，int                                                    | int(包含了long)范围增加    |
| input和raw_input | raw_input将输入的数据当作字符串来看待，input输入必须是合法的表达式 | input()函数                |
| 缩进             | 1个tab和8个space是等价的，可以同时存在                       | 不能同时存在，单独可以使用 |
| 打开文件         | file()和open()                                               | open()                     |
|                  |                                                              |                            |

PEP8编码规范

```

```



## 2.Python高级

### 2.1 函数

1、函数参数都有哪些？

```python
实际参数：与形参对应
	位置实参：按顺序
    	函数名称（数据1，数据2，数据3）
    关键字实参：按名称
    	函数名称（形参名1=数据1，形参名2=数据2）
    序列实参：拆
    	函数名称（*序列）
    字典实参：拆
    	函数名称（**字典）
形式参数：规定实参
	默认形参：实参可选
    	def 函数名（形参名1=数据1，形参名2=数据2）
    位置形参：实参必填
    	def 函数名（形参名1，形参名2）
    命名关键字形参：必须是关键字实参
    	def 函数名（*args,形参名1，形参名2）
        def 函数名（*，形参名1，形参名2）
    星号元组形参：位置实参数量无限，合
		def 函数名称（*args）
    双星号字典形参：关键字实参数量无限，合
    	def 函数名称（**kwargs）
```

2、python中的高阶函数

```python
map（函数，可迭代对象）：使用可迭代对象中的每个元素调用函数，将返回值作为新可迭代对象元素；返回值为新可迭代对象。
filter(函数，可迭代对象)：根据条件筛选可迭代对象中的元素，返回值为新可迭代对象。
sorted(可迭代对象，key = 函数,reverse = bool值)：排序，返回值为排序结果。
max(可迭代对象，key = 函数)：根据函数获取可迭代对象的最大值。
min(可迭代对象，key = 函数)：根据函数获取可迭代对象的最小值。
```

3、什么是函数式编程，主要思想是什么？

```python
函数式编程思想：
	分：将变化点单独定义到函数中
	隔：用参数在不变的代码中，调用变化的函数
	做：以参数调用的方式为规定，制作变化函数
实用性：
	好多相似的代码，但核心算法不同
参数：
	传递列表视为数据灵活
	传递函数视为逻辑灵活
```

4、什么是Hash（散列函数）？

```python
散列函数（英语：Hash function）又称散列算法、哈希函数，是一种从任何一种数据中创建小的数字“指纹”的方法。散列函数把消息或数据压缩成摘要，使得数据量变小，将数据的格式固定下来。该函数将数据打乱混合，重新创建一个叫做散列值（hash values，hash codes，hash sums，或hashes）的指纹。散列值通常用一个短的随机字母和数字组成的字符串来代表
```

5、编写函数的4个原则

```python
1.函数设计要尽量短小
2.函数声明要做到合理、简单、易于使用
3.函数参数设计应该考虑向下兼容
4.一个函数只做一件事情，尽量保证函数语句粒度的一致性
```

6、函数调用参数的传递方式是值传递还是引用传递？

```python
Python的参数传递有：位置参数、默认参数、可变参数、关键字参数。
函数的传值到底是值传递还是引用传递、要分情况：
不可变参数用值传递：像整数和字符串这样的不可变对象，是通过拷贝进行传递的，因为你无论如何都不可能在原处改变不可变对象。
可变参数是引用传递：比如像列表，字典这样的对象是通过引用传递、和C语言里面的用指针传递数组很相似，可变对象能在函数内部改变。
```

```
函数的参数传递：当进行函数调用的时候，要填入与函数形式参数个数相同的实际参数，在程序运行的过程中，实参会将参数值传递给形参，这就是函数的参数传递。
函数参数传递有以下三种：

一. 值传递
1. 用值传递方式，实际上是把实参的内容复制到形参中，实参和形参是存放在两个不同的内存空间中。在函数体内对形参的一切修改对实参都没有影响；
2. 如果形参是类的对象，利用值传递的话每次都要调用类的构造函数构造对象，效率比较低。
二. 指针传递（地址传递）
1. 当进行指针传递的时候，形参是指针变量，实参是一个变量的地址或者是指针变量，调用函数的时候，形参指向实参的地址；
2. 指针传递中，函数体内可以通过形参指针改变实参地址空间的内容。
三. 传递引用
1.引用实际上是某一个变量的别名，和这个变量具有相同的内存空间；
2. 实参把变量传递给形参引用，相当于形参是实参变量的别名，对形参的修改都是直接修改实参；
3. 在类的成员函数中经常用到类的引用对象作为形参，大大的提高代码的效率。 
```

7、裝飾器（重点）

```python
import time
def print_execution_time(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        # 执行旧功能
        result = func(*args,**kwargs)
        stop = time.time()
        print(f"執行時間是：{stop-start}")
        return result
    return wrapper
@print_execution_time
def sum_data(n):
    sum_value = 0
    for number in range(n):
        sum_value +=number
    return sum_value
```

8、map函数和reduce函数？

```python
map(lambda x: x * x, [1, 2, 3, 4]) # 使用 lambda
# [1, 4, 9, 16]
reduce(lambda x, y: x * y, [1, 2, 3, 4]) # 相当于 ((1 * 2) * 3) * 4
# 24
```

9、回调函数，如何通信的?

```python
回调函数是把函数的指针(地址)作为参数传递给另一个函数，将整个函数当作一个对象，赋值给调用的函数。
```

10、Python主要的内置数据类型都有哪些？ print dir( ‘a ’) 的输出？

```python
内建类型：布尔类型，数字，字符串，列表，元组，字典，集合
输出字符串'a'的内建方法
```

11、hasattr() getattr() setattr() 函数使用详解？

hasattr(object,name)函数:

判断一个对象里面是否有name属性或者name方法，返回bool值，有name属性（方法）返回True，否
则返回False。

```python
class function_demo(object):
	name = 'demo'
	def run(self):
		return "hello function"
functiondemo = function_demo()
res = hasattr(functiondemo, "name") # 判断对象是否有name属性，True
res = hasattr(functiondemo, "run") # 判断对象是否有run方法，True
res = hasattr(functiondemo, "age") # 判断对象是否有age属性，False
print(res)
```

getattr(object, name[,default])函数：

获取对象object的属性或者方法，如果存在则打印出来，如果不存在，打印默认值，默认值可选。注意：如果返回的是对象的方法，则打印结果是：方法的内存地址，如果需要运行这个方法，可以在后面添加括号().

```python
functiondemo = function_demo()
getattr(functiondemo, "name")# 获取name属性，存在就打印出来 --- demo
getattr(functiondemo, "run") # 获取run 方法，存在打印出方法的内存地址
getattr(functiondemo, "age") # 获取不存在的属性，报错
getattr(functiondemo, "age", 18)# 获取不存在的属性，返回一个默认值
```

setattr(object, name, values)函数：

给对象的属性赋值，若属性不存在，先创建再赋值

```python
class function_demo(object):
	name = "demo"
	def run(self):
		return "hello function"
functiondemo = function_demo()
res = hasattr(functiondemo, "age") # 判断age属性是否存在，False
print(res)
setattr(functiondemo, "age", 18) # 对age属性进行赋值，无返回值
res1 = hasattr(functiondemo, "age") # 再次判断属性是否存在，True
```

综合使用

```python
class function_demo(object):
	name = "demo"
	def run(self):
		return "hello function"
functiondemo = function_demo()
res = hasattr(functiondemo, "addr") # 先判断是否存在
if res:
	addr = getattr(functiondemo, "addr")
	print(addr)
else:
	addr = getattr(functiondemo, "addr", setattr(functiondemo, "addr", "北京首都"))
print(addr)
```

12、一句话解决阶乘函数？

```python
reduce(lambda x,y : x*y,range(1,n+1))
```

13、什么是lambda函数？ 有什么好处？

```python
lambda 函数是一个可以接收任意多个参数(包括可选参数)并且返回单个表达式值的函数
1.lambda函数比较轻便，即用即仍，很适合需要完成一项功能，但是此功能只在此一处使用，连名字都很随意的情况下
2.匿名函数，一般用来给filter，map这样的函数式编程服务
3.作为回调函数，传递给某些应用，比如消息处理
```

14、递归函数停止的条件？

```python
递归的终止条件一般定义在递归函数内部，在递归调用前要做一个条件判断，根据判断的结果选择是继续调用自身，还是return，，返回终止递归。
终止的条件：判断递归的次数是否达到某一限定值
判断运算的结果是否达到某个范围等，根据设计的目的来选择
```

15、解释一下什么是闭包？

```python
内部函数可以引用外部函数的参数和局部变量，当外部函数返回内部函数时，相关参数和变量都保存在返回的函数中，这种特性称之为"闭包"，闭包是两个函数的嵌套，外部函数返回内部函数的引用，外部函数一定要有参数
总结为三句话：有内有外，内访问外，外返回内。
```

16、什么是Python的装饰器？

```python
装饰器本质上是一个函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，提高了代码的复用性，装饰器是一个函数，它可以接收一个函数返回另外一个函数，装饰器主要有以下功能：
	引入日志
    函数执行时间统计
    执行函数前预备处理
    执行函数后的清理功能
    权限校验等场景
    缓存
```



### 2.2  面向对象

1、python新式类和经典类的区别？

```python
a. 在python里凡是继承了object的类，都是新式类
b. Python3里只有新式类
c. Python2里面继承object的是新式类，没有写父类的是经典类
d. 经典类目前在Python里基本没有应用
e. 保持class与type的统一对新式类的实例执行a.class与type(a)的结果是一致的，对于旧式类来说就不
一样了。
f.对于多重继承的属性搜索顺序不一样新式类是采用广度优先搜索，旧式类采用深度优先搜索。
```

2、Python中类方法、类实例方法、静态方法有何区别？

```python
类方法: 是类对象的方法，在定义时需要在上方使用 @classmethod 进行装饰,形参为cls，表示类对象，类对象和实例对象都可调用
类实例方法: 是类实例化对象的方法,只有实例对象可以调用，形参为self,指代对象本身
静态方法: 是一个任意函数，在其上方使用 @staticmethod 进行装饰，可以用对象直接调用，静态方法实际上跟该类没有太大关系
```

3、内存泄露是什么？如何避免？

```python
内存泄漏指由于疏忽或错误造成程序未能释放已经不再使用的内存。内存泄漏并非指内存在物理上的消失，而是应用程序分配某段内存后，由于设计错误，导致在释放该段内存之前就失去了对该段内存的控制，从而造成了内存的浪费。
有__del__() 函数的对象间的循环引用是导致内存泄露的主凶。不使用一个对象时使用: del object 来删除一个对象的引用计数就可以有效防止内存泄露问题。
```

4、面向对象中的属性是怎么实现的？

```python
属性@property:将方法的使用方式像操作变量一样方便，从而保护实例变量

注意:1、属性名与实例变量名相同
    2、属性操作私有变量
class Wife():
    def __init__(self,name="",age=0):
        self.name = name
        self.age = age
    @property #读属性
    def age(self):
        return self.__age
   	@age.setter #写属性
    def age(self,age):
        if 30 <= value <=60:
            self.__age = value
        else:
            raise Exception("我不要")
```

5、读写属性写法：

```python
# 快捷键：props+回车
class Wife():
    def __init__(self,name="",age=0):
        self.name = name
        self.age = age
    @property #读属性
    def age(self):
        return self.__age
   	@age.setter #写属性
    def age(self,age):
        if 30 <= value <=60:
            self.__age = value
        else:
            raise Exception("我不要")
```

6、只读属性：

```python
# 快捷键：prop+回车
# 实用性：类中确定的数据，类外只能读取，不能修改
class Wife():
    def __init__(self,name="",age=0):
        self.name = name
        self.age = age
    @property #读属性
    def age(self):
        return self.__age
```

7、只写属性：

```python
class Wife():
    def __init__(self,name="",age=0):
        self.name = name
        self.age = age

    def age(self,age):
        self.__age = value
    age = property(fset=data)
```

8、属性原理

```python
原理：
	目标：保护实例变量
    理念：拦截对变量的操作，改为对方法的调用
    一个属性对象，包装了两个方法（负责读取，负责写入）
class Wife():
    def __init__(self,name="",age=0):
        self.name = name
        self.age = age
        #self.set_age(age)
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if 30 <= value <=60:
            self.__age = value
        else:
            raise Exception("我不要")
    #@property 原理如下
    #property() 函数的作用是在新式类中返回属性值
    age = property(get_age)
    #age.setter 原理如下
    age = age.setter(set_age)
```

9、谈谈你对面向对象的理解？

```
面向对象是相当于面向过程而言的，面向过程语言是一种基于功能分析的，以算法为中心的程序设计方法，而面向对象是一种基于结构分析的，以数据为中心的程序设计思想。在面向对象语言中有一个很重要的东西，叫做类。面向对象有三大特性：封装、继承、多态。
```

10、三大特征和六大原则

```
三大特征：
	封装（分）：
		数据角度讲：将一些基本数据类型复合成一个自定义类型
		行为角度讲：向类外提供必要的功能，隐藏实现的细节
		设计角度讲：
			分而治之：将一个大的需求分解为许多类，每个类处理一个独立的功能，每个类完成一项独立的发功能
			变则疏之：变化的地方独立封装，避免影响其他类。数据不同用实例封装，行为不同，用类来封装
			高内聚：类中各个方法都在完成一项任务(单一职责的类)，每个类都在独立完成单一的一件事情
			低耦合：类与类的关联性与依赖度要低(每个类独立)，让一个类的改变，尽少影响其他类
	继承（隔离变化）：
		语法角度将：继承方法。继承数据
		设计角度讲：将相关类的共性进行抽象，统一概念，隔离变化
	多态（做）：
		设计角度讲：父类的同一种动作或者行为，在不同的子类上有不同的实现；多态的发生要有两个前提条件，第一，继承-多态一定发生在子类与父类之间；第二，		   重写—子类重写了父类的方法
		语法角度讲：子类实现了父类中相同的方法（方法名、参数）。在调用该方法时，实际执行的是子类的方法。
六大原则：
	开闭原则（总的指导思想）：
		Open Closed Principle
		对扩展开放，对修改关闭。
		增加新功能，不改变原有代码。
	类的单一职责：
		Single Responsibility Principle   
		一个类有且只有一个改变它的原因。
	依赖倒置（依赖抽象）：
		Dependency Inversion Principle
		客户端代码(调用的类)尽量依赖(使用)抽象。
		抽象不应该依赖细节，细节应该依赖抽象。
	组合复用原则（复用的最佳实践）：
		Composite Reuse Principle
		如果仅仅为了代码复用优先选择组合复用，而非继承复用。是作为参数传递，是一种拥有的关系，而非是的关系
	里氏替换（继承后的重写，指导继承的设计）：
		Liskov Substitution Principle
		父类出现的地方可以被子类替换，在替换后依然保持原功能。
		子类要拥有父类的所有功能。
		子类在重写父类方法时，尽量选择扩展重写，防止改变了功能。
	迪米特法则（类与类交互的原则）：
		Law of Demeter
		不要和陌生人说话。
		类与类交互时，在满足功能要求的基础上，传递的数据量越少越好。因为这样可能降低耦合度。
```

oop,ooa,ood?

```
oop:面向对象程序设计(Object Oriented Programming)
ooa:Object-Oriented Analysis（面向对象分析方法）
ood:面向对象设计(OOD)原则
```



### 2.3 设计模式

1、对设计模式的理解？简述你了解的设计模式

```
设计模式是经过总结，优化的，对我们经常会碰到的一些编程问题的可重用解决方案。一个设计模式并
不像一个类或一个库那样能够直接作用于我们的代码，反之，设计模式更为高级，它是一种必须在特定
情形下实现的一种方法模板。
常见的是工厂模式和单例模式
单例模式：
	单例模式（Singleton Pattern）是 Java 中最简单的设计模式之一。这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。这种模式涉及到一个单一的类，该类负责创建自己的对象，同时确保只有单个对象被创建。这个类提供了一种访问其唯一的对象的方式，可以直接访问，不需要实例化该类的对象。
意图：保证一个类仅有一个实例，并提供一个访问它的全局访问点。

主要解决：一个全局使用的类频繁地创建与销毁。
何时使用：当您想控制实例数目，节省系统资源的时候。
如何解决：判断系统是否已经有这个单例，如果有则返回，如果没有则创建。
关键代码：构造函数是私有的。
使用场景：
1、要求生产唯一序列号。
2、WEB 中的计数器，不用每次刷新都在数据库里加一次，用单例先缓存起来。
3、创建的一个对象需要消耗的资源过多，比如 I/O 与数据库的连接等。
工厂模式：
	工厂模式（Factory Pattern）是 Java 中最常用的设计模式之一。这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。在工厂模式中，我们在创建对象时不会对客户端暴露创建逻辑，并且是通过使用一个共同的接口来指向新创建的对象。
	意图：定义一个创建对象的接口，让其子类自己决定实例化哪一个工厂类，工厂模式使其创建过程延迟到子类进行。

主要解决：主要解决接口选择的问题。
何时使用：我们明确地计划不同条件下创建不同实例时。
如何解决：让其子类实现工厂接口，返回的也是一个抽象的产品。
关键代码：创建过程在其子类执行。
```

2、对装饰器的理解，并写出一个计时器记录方法执行性能的装饰器？

```python
装饰器其实是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，提高了代码的复用性、
import time
def print_execution_time(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result=func(*args,**kwargs)
        stop = time.time()
        return result
    return wrapper
@print_execution_time
def sum_data(n):
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value
print(sum_data(10))
```

什么单例模式，其应用场景都有哪些？

```
确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实
例，这个类称为单例类，单例模式是一种对象创建型模式。
Windows 的Task Manager（任务管理器）、Recycle Bin（回收站）、网
站计数器
单例模式应用的场景一般发现在以下条件下：
（1）资源共享的情况下，避免由于资源操作时导致的性能或损耗等。如
上述中的日志文件，应用配置。
（2）控制资源的情况下，方便资源之间的互相通信。如线程池等。
```

3、yiled的用法？

```python
# 定义函数，在列表中找出所有偶数
def find_event(list_target):
    for item in list_target:
        if item % 2 == 0:
            yield item
list01 = [32,45,67,32,12,89]
result = find_event(list01)
for i in result:
    print(i)
执行过程：
	调用生成器函数会自动创建
    调用迭代器对象的__next__()方法才执行生成器函数
    每次执行到yield语句时返回数据，暂时离开
    待下次调用__next__方法时继续从离开处继续执行
原理：生成迭代器对象的大致规则如下：                                                                                          
		将yield关键字以前的代码放在next方法中。
		将yield关键字后面的数据作为next方法的返回值。

```

4、迭代对象，迭代器，生成器？

```python
"""
容器（container）
"""
# 容器是一种把多个元素组织在一起的数据结构，容器中的元素可以逐个地迭代获取，可以用in, not in关键字判断元素是否包含在容器中。
# 通常这类数据结构把所有的元素存储在内存中（并不是所有的元素都放在内存中，比如迭代器和生成器对象）
# 尽管绝大多数容器提供了某种方式来获取其中的每一个元素，但这并不是容器本身，而是可迭代对象赋予了容器这种能力，当然并不是所有的容器都是可迭代的
# 从技术角度讲当它可以用来询问某个元素是否包含在其中时，那么这个对象就可以认为时一个容器
"""
可迭代对象(iterable)
"""
# 刚才说过，很多容器都是可迭代对象，此外还有更多的对象同样也是可迭代对象，但凡可以返回一个迭代器的对象都可称之为可迭代对象
x = [1, 2, 3]
y = x.__iter__()  # y=iter(x)
z = x.__iter__()  # z=iter(x)
print(next(y))
print(next(y))
print(type(x))
print(type(y))
# 这里X时一个可迭代对象，可迭代对象和容器一样时一种通俗的叫法，并不是指某种具体的数据类型，List是可迭代对象，dict是可迭代对象，y和z是两个独立的迭代器
# 迭代器内部持有一个状态，该状态记录当前迭代所在的位置，以方便下次迭代的时候获取正确的元素，迭代器有一种具体的迭代器类型，比如list_iterator,set_iterator
# 可迭代对象实现了__iter__方法，该方法返回一个迭代器对象
"""
迭代器对象（iterator）
"""
# 迭代器，它是一个带状态的对象，他能在你调用next()方法的时候返回容器中的下一个值，任何实现了__iter__和__next__方法的对象都是迭代器对象，__iter__返回迭代器自身
# __next__返回容器中的下一个值，如果容器中没有更多元素了，则抛出StopIteration
# 所以迭代器实现了工厂模式的对象，它在你每次询问要下一个值的时候给你返回
class Fib:
    def __init__(self, n=10):  # 初始化
        self.prev = 0
        self.curr = 1
        self.n = n

    def __iter__(self):  # 调用__iter__方法返回迭代器对象，返回自身，自身就是迭代器对象
        return self

    def __next__(self):  # 调用__next__方法返回下一个值
        self.prev, self.curr = self.curr, self.curr + self.prev
        if self.prev > self.n:
            raise StopIteration
        return self.prev


# f = Fib(20)
# for i in f:
#     print(i)
#Fib既是一个可迭代对象（因为它实现了__iter__方法），又是一个迭代器（因为实现了__next__方法），实例变量prev,curr用户维护迭代器内部的状态
#每次调用next()方法的时候做两件事：
#1、为下一次调用next()方法修改状态  2、为当前这次调用生成返回结果
"""
生成器
"""
# 生成器是一种特殊的迭代器，只需要一个yield关键字,生成器一定是迭代器，反之不成立
def fibs():
    prev,curr=0,1
    while curr<10:
        yield curr
        prev,curr=curr,prev+curr
f=fibs()
for i in f:
    print(i)
"""
总结
"""
#1、容器时一系列元素的集合，容器都可以被迭代，因此它们都被称为可迭代对象
#2、可迭代对象实现了__iter__方法，该方法返回一个迭代器对象
#3、迭代器持有一个内部状态的字段，用于记录下次迭代返回值，它实现了__iter__和__next__方法，迭代器不会一次性把所有元素加载到内存，而是需要的时候才生成返回结果
#4、生成器是一种特殊的迭代器，他的返回值不是通过return而是通过yield
```

5、请手写一个单例

```
class A(object):
	__instance = None
	def __new__(cls,*args,**kwargs):
		if cls.__instance is None:
			cls.__instance = objecet.__new__(cls)
			return cls.__instance
		else:
			return cls.__instance
```

6、单例模式的应用场景有哪些？

```
单例模式应用的场景一般发现在以下条件下：
1、资源共享的情况下，避免由于资源操作时导致的性能或损耗等，如日志文件，应用配置。
2、控制资源的情况下，方便资源之间的互相通信。如线程池等，1,网站的计数器 2,应用配置 3.多线程池 4
数据库配置 数据库连接池 5.应用程序的日志应用...
```

7、递归函数停止的条件？

```
递归的终止条件一般定义在递归函数内部，在递归调用前要做一个条件
判断，根据判断的结果选择是继续调用自身，还是return;返回终止递归。
终止的条件：
1.判断递归的次数是否达到某一限定值
2. 判断运算的结果是否达到某个范围等，根据设计的目的来选择
```

8、python 是强语言还是弱语言？

```
Python 是强类型的动态脚本语言。
强类型：不允许不同类型相加
动态：不使用显示数据类型声明，且确定一个变量的类型是在第一次给它赋值的时候
脚本语言：一般也是解释型语言，运行代码只需要一个解释器，不需要编译
```

9、python 的内存管理机制及调优手段？

```
内存管理机制：引用计数、垃圾回收、内存池
引用计数
引用计数是一种非常高效的内存管理手段, 当一个Python 对象被引用时其引用计数增加1, 当其不再被一个变量引用时则计数减1. 当引用计数等于0 时对象被删除.
垃圾回收
1. 引用计数
引用计数也是一种垃圾收集机制，而且也是一种最直观，最简单的垃圾收集技术。当Python 的某个对象的引用计数降为0 时，说明没有任何引用指向该对象，该对象就成为要被回收的垃圾了。比如某个新建对象，它被分配给某个引用，对象的引用计数变为1。如果引用被删除，对象的引用计数为0，那么该对象就可以被垃圾回收。不过如果出现循环引用的话，引用计数机制就不再起有效的作用了
2. 标记清除
如果两个对象的引用计数都为1，但是仅仅存在他们之间的循环引用，那么这两个对象都是需要被回收的，也就是说，它们的引用计数虽然表现为非0，但实际上有效的引用计数为0。所以先将循环引用摘掉，就会得出这两
个对象的有效计数。
3. 分代回收
从前面“标记-清除”这样的垃圾收集机制来看，这种垃圾收集机制所带来的额外操作实际上与系统中总的内存块的数量是相关的，当需要回收的内存块越多时，垃圾检测带来的额外操作就越多，而垃圾回收带来的额外操作就越少；反之，当需回收的内存块越少时，垃圾检测就将比垃圾回收带来更少的额外操作。

举个例子：
当某些内存块M 经过了3 次垃圾收集的清洗之后还存活时，我们就将内存块M 划到一个集合A 中去，而新分配的内存都划分到集合B 中去。当垃圾收集开始工作时，大多数情况都只对集合B 进行垃圾回收，而对集合A 进行垃圾回收要隔相当长一段时间后才进行，这就使得垃圾收集机制需要处理的内存少了，效率自然就提高了。在这个过程中，集合B 中的某些内存块由于存活时间长而会被转移到集合A 中，当然，集合A 中实际上也存在一些垃圾，这些垃圾的回收会因为这种分代的机制而被延迟。
内存池
1.Python 的内存机制呈现金字塔形状，-1，-2 层主要有操作系统进行操作；
2.第0 层是C 中的malloc，free 等内存分配和释放函数进行操作；
3.第1 层和第2 层是内存池，有Python 的接口函数PyMem_Malloc 函数实现，当对象小于256K 时有该层直接分配内存；
4.第3 层是最上层，也就是我们对Python 对象的直接操作；Python 在运行期间会大量地执行malloc 和free 的操作，频繁地在用户态和核心态之间进行切换，这将严重影响Python 的执行效率。为了加速Python 的执行效率，Python 引入了一个内存池机制，用于管理对小块内存的申请和释放。
Python 内部默认的小块内存与大块内存的分界点定在256 个字节，当申请的内存小于256 字节时，PyObject_Malloc 会在内存池中申请内存；当申请的内存大于256 字节时，PyObject_Malloc 的行为将蜕化为malloc 的行为。当然，通过修改Python 源代码，我们可以改变这个默认值，从而改变Python的默认内存管理行为。

调优手段（了解）
1.手动垃圾回收
2.调高垃圾回收阈值
3.避免循环引用（手动解循环引用和使用弱引用）
```

10、Python 中有日志吗?怎么使用?

```
有日志；
python 自带logging 模块，调用logging.basicConfig()方法，配置需要的日志等级和相应的参数，python 解释器会按照配置的参数生成相应的日志
```

11、回调函数，如何通信的?

```
回调函数是把函数的指针(地址)作为参数传递给另一个函数，将整个函数当作一个对象，赋值给调用的函数
```

12、init 和news 的区别？

```
init 在对象创建后，对对象进行初始化
new 是在对象创建之前创建一个对象，并将该对象返回给init
```

13、解释一下Python 中的and-or 语法？

```
逻辑运算and-or，在计算机运算中的短路规则（以尽量少运算，得出正确结果）可以提高计算效率，
```

14、Python 中类方法、类实例方法、静态方法有何区别？

```
类方法：是类对象的方法，在定义时需要在上方使用“@classmethod”进行装饰，形参为cls，表示类对象，类对象和实例对象都可调用；
类实例方法：是类实例化对象的方法，只有实例对象可以调用，形参为self，指代对象本身；
静态方法：是一个任意函数，在其上方使用“@staticmethod”进行装饰，可以用对象直接调用，静态方法实际上跟该类没有太大关系
```

15、谈谈你对同步、异步、阻塞、非阻塞的理解

```
同步就是指一个进程在执行某个请求的时候，若该请求需要一段时间才能返回信息，那么这个进程就会一直等待下去，直到收到返回信息才继续执行下去

异步是值进程不需要一直等下去，而继续执行下面的操作，不管其他进程的状态。当有消息返回时系统会通知进程进行处理，这样可以提高执的效率。举个例子，打电话时就是同步通信，发短息时就是异步通信。

阻塞调用是指调用结果返回之前，当前线程会被挂起。函数只有在得到结果之后才会返回。有人也许会把阻塞调用和同步调用等同起来，实际上他是不同的。对于同步调用来说，很多时候当前线程还是激活的，只是从逻辑上当前函数没有返回而已。例如，我们在CSocket 中调用Receive 函数，如果缓冲区中没有数据，这个函数就会一直等待，直到有数据才返回。而此时，当前线程还会继续处理各种各样的消息。如果主窗口和调用函数在同一个线程中，除非你在特殊的界面操作函数中调用，其实主界面还是应该可以刷新。socket 接收数据的另外一个函数recv 则是一个阻塞调用的例子。当socket工作在阻塞模式的时候，如果没有数据的情况下调用该函数，则当前线程就会被挂起，直到有数据为止。

非阻塞和阻塞的概念相对应，指在不能立刻得到结果之前，该函数不会
阻塞当前线程，而会立刻返回。
```

16、Python 里面如何拷贝一个对象？

```
python 中的拷贝分为浅拷贝和深拷贝，若不特殊说明拷贝一般是浅拷贝浅拷贝是将对象顶层拷贝，拷贝了引用，并没有拷贝内容，原对象改变，新对象也跟着改变
深拷贝是对一个对象的所有层次的拷贝（递归），但是修改原来的值，新对象不受影响
浅拷贝对于可变类型和不可变类型是不同的，对于可变类型只拷贝顶层，不可变类型依然是原来的对象
```



### 2.4 正则表达式

1、普通字符

```python
print(re.findall("ab", "abacadabab"))  # ['ab', 'ab', 'ab']注意：# 正则表达式在python中也可以匹配中文
```

2、| 

```python
print(re.findall("com|cn", "www.baidu.com/www.tmooc.cn")) # 匹配规则: 匹配 | 两侧任意的正则表达式即可
```

3、.

```python
print(re.findall('张.丰', "张三丰,张四丰,张五丰")) # 匹配规则：匹配除换行外的任意一个字符
```

4、[字符集]

```python
print(re.findall('[aeiou]', "How are you!")) # 匹配规则: 匹配字符集中的任意一个字符
```

5、【^字符集】

```python
print(re.findall('[^0-9]', "Use 007 port")) # 匹配规则：匹配除了字符集以外的任意一个字符
```

6、^

```python
print(re.findall("^Jame", "Jame a Jame")) # 匹配规则：匹配目标字符串的开头位置
```

7、$

```python
print(re.findall("Jame$", "Jame a Jame")) # 匹配规则：匹配目标字符串的开头位置
```

8、？

```python
print(re.findall("-?[0-9]+","Jame,age:18.-26")) # 匹配前面的字符出现0次或1次
```

9、*

```python
print(re.findall("wo*","wooooooo~~w!")) # 匹配前面的字符出现0次或多次
```

10、+

```python
print(re.findall("[A-Z][a-z]+","Hello world")) # 匹配前面的字符出现1次或者多次
```

11、{n}

```python
print(re.findall("1[0-9]{10}","Jame 13891080465")) # 匹配前面的字符出现n次
```

12、{m,n}

```python
print(re.findall("[1-9][0-9]{5,10}","Baron 12564789621")) # 匹配前面的字符出现m-n次
```

13、\d   \D

```python
print(re.findall("\d{1,5}","Mysql: 3306,http:80")) # \d匹配任意数字字符 \D匹配任意非数字字符
```

14、\w   \W

```python
print(re.findall("\w+","server_port=8888")) # \w匹配任何语言的单词字符、数字、下划线_ \W匹配非普通字符
```

15、\s  \S

```python
print(re.findall('\w+\s+\w+',"hello    world")) # \s匹配空字符串  \S匹配非空字符串 空字符指 空格 \r \n \t \v \f 字符
```

16、\b   \B

```python
print(re.findall(r'\bis\b',"This is a test.")) # \b表示单词边界  \B 表示非单词边界
#注意:当元字符符号与Python字符串中转义字符冲突的情况则需要使用r将正则表达式字符串声明为原始字符串，如果不确定那些是Python字符串的转义字符，则可以在所有正则表达式前加r
```

17、模块使用

```python
# re.findall(pattern, string, flags=0)  ->匹配到的内容列表
# 功能: 根据正则表达式匹配目标字符串内容
# 参数: pattern     正则表达式
#       string      目标字符串
#       flags       功能标志位, 扩展正则表达式的匹配
# 返回值: 匹配到的内容列表, 如果正则表达式有子组则只能获取到子组对应的内容
print(re.findall(r"(1[0-9]{10})\s(\d+)","Jame 13891080465 55555"))
#--------------------------------------------------------------------
# re.split(pattern, string, max，flags = 0)  ->切割后的内容列表
# 功能: 使用正则表达式匹配内容, 切割目标字符串
# 参数: pattern   正则表达式
# string   目标字符串
# max   最多切割几部分
# flags   功能标志位, 扩展正则表达式的匹配
# 返回值: 切割后的内容列表
print(re.split(r'is',"This is a test."))
#-------------------------------------------------------------------
# re.sub(pattern, replace, string, count, flags=0)  ->替换后的字符串
# 功能: 使用一个字符串替换正则表达式匹配到的内容
# 参数: pattern   正则表达式
# replace   替换的字符串
# string   目标字符串
# count   最多替换几处, 默认替换全部
# flags   功能标志位, 扩展正则表达式的匹配
# 返回值: 替换后的字符串

# 生成match对象
# re.finditer(pattern,string,flags = 0)  ->匹配结果的迭代器
#  功能: 根据正则表达式匹配目标字符串内容
#  参数: pattern  正则表达式
#       string 目标字符串
#       flags  功能标志位,扩展正则表达式的匹配
#  返回值: 匹配结果的迭代器
iters = re.finditer(r'\d+', '12a32bc43jf3')
for match in iters:
    print(match.group())
#----------------------------------------------------------------------
# re.match(pattern,string,flags=0)  ->匹配内容match object
# 功能：匹配某个目标字符串开始位置
# 参数：pattern 正则
# 	string  目标字符串
# 返回值：匹配内容match object
result = re.match("it","itxiaoze.cn")
print(result.group())
#----------------------------------------------------------------------
# re.search(pattern,string,flags=0)  ->匹配内容match object
# 功能：匹配目标字符串第一个符合内容
# 参数：pattern 正则
# 	string  目标字符串
# 返回值：匹配内容match object
result = re.search("it","xiaozeit.cn")
print(result.group())
#---------------------------------------------------------------------
#match对象有以下几个方法：
#group()方法返回匹配的子字符串
#start()方法返回子字符串的开始索引
#end()方法返回子字符串的结束索引
#span()方法返回子字符串的跨度,它是一个二元素的元组
```

18、flags参数扩展

```python
#flags参数扩展
# *作用函数：re模块调用的匹配函数。如：re.findall, re.search....
# *功能：扩展丰富正则表达式的匹配功能
# *常用flag
# A == ASCII   元字符只能匹配ascii码
# I == IGNORECASE   匹配忽略字母大小写
# S == DOTALL   使.可以匹配换行
# M == MULTILINE   使 ^  $可以匹配每一行的开头结尾位置
# > 注意：同时使用多个flag,可以用竖线连接  flags = re.I | re.A
```

19、特殊字符匹配

```python
#目的 ： 如果匹配的目标字符串中包含正则表达式特殊字符，则在表达式中元字符就想表示其本身含义时就需要进行 \ 处理
#特殊字符: . * + ? ^ $ [] () {} | \
#操作方法：在正则表达式元字符前加 \ 则元字符就是去其特殊含义，就表示字符本身
import re
print(re.findall('-?\d+\.?\d*',"123,-123,1.23,-1.23"))
#贪婪模式和非贪婪模式
# 贪婪模式: 默认情况下，匹配重复的元字符总是尽可能多的向后匹配内容。比如: *  +  ?  {m,n}
# 非贪婪模式(懒惰模式): 让匹配重复的元字符尽可能少的向后匹配内容。
# 贪婪模式转换为非贪婪模式  在对应的匹配重复的元字符后加 '?' 号即可
print(re.findall(r'\(.+?\)',"(abcd)efgh(higk)"))
```

20、练习

```python
import re

# 1、验证手机号码是否符合规则(不考虑边界问题)
# 规则如下：
# 1.都是数字
# 2.长度为11
# 3.第一位是1
# 4.第二位是35678中的一位

# 首先清楚手机号的规则
# 1.都是数字 2.长度为11 3.第一位是1 4.第二位是35678中的一位
pattern = "1[35678]\d{9}"
phoneStr = "13248254250"
result = re.match(pattern,phoneStr)
print(result.group())
#-----------------------------------------------------------
#2、匹配原始字符串
#1.匹配"\nabc"
#在给str赋值"\nabc"前加上"r"之后,python解释器会自动给str的值"\nabc"在加上一个"\".
#使str在被打印的时候,能够保持原始字符串的值"\nabc"打印出来
#匹配"\\abc"    r"\\abc"
#----------------------------------------------------------
#3、匹配边界（定义规则匹配str="this is book"）
#定义规则匹配str="this is book"
#1. 以字母开始
#2. 中间有空字符
#3. is两边分别限定匹配单词边界
pattern=r"^\w+\s\bis\b\s\w+"
str = "this is book"
result = re.match(pattern, str)
print(result.group())
#----------------------------------------------------------
#匹配出0-100之间的数字
#首先:正则是从左往又开始匹配
#经过分析: 可以将0-100分为三部分
#1. 0        "0$"
#2. 100      "100$"
#3. 1-99     "[1-9]\d{0,1}$"
#所以整合如下:
pattern=r"100$|[1-9]\d{0,1}$"
result = re.match(pattern, "27")
print(result.group())
#==========================================================
#匹配分组,获取页面<h1>标签中的内容, 爬虫的时候会用到
str = "<h1>hello world!</h1>"
pattern=r"<h1>(.*)</h1>"
result = re.match(pattern, str)
print(result.group())
#==========================================================
#引用分组,精确获取多个标签内的内容
#"\1"是对第一个分组的引用,同理......
str = "<span><h1>hello world!</h1></span>"
pattern=r"<(.+)><(.+)>.*</\2></\1>"
result = re.match(pattern, str)
print(result.group())
#==========================================================
# 分组起别名
str = "<span><h1>hello world!</h1></span>"
pattern=r"<(?P<key1>.+)><(?P<key2>.+)>(?P<key3>.*)</(?P=key2)></(?P=key1)>"
result = re.match(pattern, str)
print(result.group())
#==========================================================
#贪婪模式(尽可能多的匹配字符：匹配：4-235-22-423)
# str = "This is a number 234-235-22-423"
# pattern = r"(.+)(\d+-\d+-\d+-\d+)"
# result = re.match(pattern, str)
# print(result.group())
# #分析
# #由pattern可知str被分成两组,因为默认情况下为贪婪模式,所以
# #    第一组会在保证第二组符合的情况下, 尽可能的匹配多的字符
# #所以推断:
# #    第一组: This is a number 23
# #    第二组: 4-235-22-423
# # 这样既可以是第二组情况符合,而又使得第一组尽可能贪婪地匹配到最多的字符
#非贪婪模式(尽可能少的匹配字符：匹配：234-235-22-423)
str = "This is a number 234-235-22-423"
pattern = r"(.+?)(\d+-\d+-\d+-\d+)"
result = re.match(pattern, str)
print(result.group())
#分析
#由pattern可知str被分成两组,因为默认情况下为贪婪模式,所以
#    第一组会在保证第二组符合的情况下, 尽可能的匹配少的字符
#所以推断:
#    第一组: This is a number
#    第二组: 234-235-22-423
#这样既可以是第二组情况符合,而又使得第一组尽可能贪婪地匹配到最多的字符
#===================================================================
#匹配邮箱
#1、匹配163邮箱
str = "zhangxinwei_user@163.com"
pattern=r"[0-9a-zA-Z_]{0,19}@163.com"
result = re.match(pattern, str)
print(result.group())
#2、匹配任意格式的邮箱
text = "lvzezhang126@126.com"
pattern=r"[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn.net]{1,3}$"
result = re.match(pattern, text)
print(result.group())
#===================================================================
#一般来说，我们填写日期都会写2020年7月7日，但是也有很多人会写成2020/7/7、2020-7-7、2020-07-07等，
# 还有的人可能会写为2020-07或者2020年7月。总之对日期的写法五花八门，
# 那么我们现在需要写一个正则表达式来统一匹配这么多的情况，应该如何来处理呢？
str01 = "xxx高考时间是2020年7月7日"
str02 = "xxx高考时间是2020/7/7"
str03 = "xxx高考时间是2020-7-7"
str04 = "xxx高考时间是2020-07-07"
str05 = "xxx高考时间是2020-07"
str06 = "xxx高考时间是2020年7月"
pattern=".*高考时间是(\d{4}[年/-]\d{1,2}[月/-]|$)(\d{1,2}(日|$)|$))"
print(re.findall(pattern,str06))
# 1、我们从左到右对正则表达式进行分析，首先“.* ”代表的是任意字符出现任意多次，对应原始字符中的“XXX”；“高考时间是”没有什么特别的，
# 就是对应原始字符串中的“高考时间是”。
# 2、接下来是“d
# {4}”代表的是连续出现4个数字，对应原始字符串中的年份“2018”；“[年 / -]”表示取“年”、“ / ”、“-”中的任意一个字符，对应原始字符串中
# 年份“2018”之后所连接的下一个字符。
# 3、继续往后是“d
# {1, 2}”代表的是连续出现1个到2个数字，对应原始字符串中的月份“6”或者“06”；“[月 / -]”表示取“月”、“ / ”、“-”中的任意一个字符，
# 对应原始字符串中月份“6”或者“06”之后所连接的下一个字符，同年份的理解如出一辙。
# 4、接下来就复杂一些了，其中“d
# {1, 2}”的理解同月份的理解一致，关键是关于“日”的提取主要需要注意有的字符串有日期，有的字符串并没有日期，所以需要特殊字符“ | ”来
# 表示“或”的关系，并且用特殊字符“$”来表示结束。
# 5、需要利用特殊字符“ | ”和特殊字符“$”，做一个“或”的选择。
pattern=".*高考时间是(\d{4}[年/-]\d{1,2}([月/-]|$)(\d{1,2}(日|$)|$))"
```

### 2.5 系统编程

1、什么是进程？

```python
进程是程序在计算机中的一次执行过程
	程序是一个可执行的文件，是静态的占有磁盘。
	进程是一个动态的过程描述，占有计算机运行资源，有一定的生命周期。
```

2、进程五态？

```python
- 初始状态：进程刚被创建，由于其他进程正占用CPU所以得不到执行，只能处于初始状态。
- 执行状态：任意时刻处于执行状态的进程只有一个
- 就绪状态：只有处于就绪状态的经过调度才能到执行状态
- 等待状态：进程等待某件事件完成
- 停止状态：进程结束
```

3、进程命令

```shell
ps -aux
USER:进程的创建者
PID：操作系统分配给进程的编号，大于0的整数，系统中每个进程的PID都不重复
%CPU,%MEM:占有的CPU和内存
STAT:进程状态信息，SI表示阻塞状态，R表示就绪状态或者运行状态
START:进程启动时间
COMMAND:通过什么程序启动的进程
```

4、解释一下进程执行现象

```python
新的进程是原有进程的子进程，子进程复制父进程全部内存空间代码段，一个进程可以创建多个子进程。
子进程只执行指定的函数，其余内容均是父进程执行内容，但是子进程也拥有其他父进程资源。
各个进程在执行上互不影响，也没有先后顺序关系。
进程创建后，各个进程空间独立，相互没有影响。
multiprocessing 创建的子进程中无法使用标准输入（input）。
```

5、什么是孤儿进程和僵尸进程？

```python
孤儿进程 ： 父进程先于子进程退出，此时子进程成为孤儿进程。
	特点： 孤儿进程会被系统进程收养，此时系统进程就会成为孤儿进程新的父进程，孤儿进程退出该进程会自动处理。

僵尸进程 ： 子进程先于父进程退出，父进程又没有处理子进程的退出状态，此时子进程就会成为僵尸进程。
	特点： 僵尸进程虽然结束，但是会存留部分进程信息资源在内存中，大量的僵尸进程会浪费系统的内存资源。
```

6、如何避免僵尸进程产生？

```
1.  使用join()回收
2.  在父进程中使用signal方法处理
from signal import *
signal(SIGCHLD,SIG_IGN)
```

7、什么是多线程竞争？

```
线程是非独立的，同一个进程里线程是数据共享的，当各个线程访问数据资源时会出现竞争状态即：数据几乎同步会被多个线程占用，造成数据混乱，即所谓的线程不安全
那么怎么解决多线程竞争问题？---锁
锁的好处： 确保了某段关键代码（共享数据资源）只能由一个线程从头到尾完整地执行能解决多线程资
源竞争下的原子操作问题。
锁的坏处： 阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了锁的致命问题: 死锁
```

8、什么是死锁？

```
死锁是指两个或者两个以上的线程，在执行过程中由于资源竞争或者由于彼此通信而造成的一种阻塞的现象，若无外力推动，他们将无法执行下去，此时称系统处于死锁状态或系统产生了死锁
```

9、死锁产生条件

```
互斥条件：指线程使用了互斥方法，使用一个资源时其他线程无法使用
请求和保持条件：指线程已经保持至少一个资源，但又提出了新的资源请求，在获取到新的资源前不会释放自己保持的资源。
不剥夺条件：不会受到线程外部的干扰，如系统强制终止线程等。
环路等待条件：指在发生死锁时，必然存在一个线程——资源的环形链，如 T0正在等待一个T1占用的资源；T1正在等待T2占用的资源，……，Tn正在等待已被T0占用的资源
```

10、如何避免死锁

```
* 逻辑清晰，不要同时出现上述死锁产生的四个条件
* 通过测试工程师进行死锁检测
```

11、GIL问题(Global Interpreter Lock)

```
什么是GIL问题 （全局解释器锁）

由于python解释器设计中加入了解释器锁，导致python解释器同一时刻只能解释执行一个线程，大大降低了线程的执行效率

导致后果：
因为遇到阻塞时线程会主动让出解释器，去解释其他线程。所以python多线程在执行多阻塞任务时可以提升程序效率，其他情况并不能对效率有所提升

结论 

* GIL问题与Python语言本身并没什么关系，属于解释器设计的历史问题。
* 在无阻塞状态下，多线程程序程序执行效率并不高，甚至还不如单线程效率。
* Python多线程只适用于执行有阻塞延迟的任务情形。
```

12、谈谈你对多进程，多线程，以及协程的理解，项目是否用？

```
进程：一个运行的程序就是一个进程，没有运行的代码叫程序，进程是系统资源分配的最小单位，进程拥有自己独立的内存空间，所有进程间数据不共享，开销大
线程：CPU调度执行的最小单位，也叫执行路径，不能独立存在，依赖进程存在，一个进程至少有一个线程，叫主线程，而多格线程共享内存（数据共享，共享全局变量），从而极大的提高了程序的运行效率
协程：是一种用户态的轻量级线程，协程的调度完全由用户控制，协程拥有自己的寄存器上下文和栈。协程调度时，将寄存器上下文和栈保存到其他地方，再切回来的时候，回复先前保存的寄存器上下文和栈，直接操作栈则基本没有内核切换的开销，可以不加锁的访问全局变量，所以上下文切换非常快
```

13、请介绍一下Python的线程同步？

```python
1、setDaemon(False)
当一个进程启动之后，会默认产生一个主线程，因为线程是程序执行的最小单位，当设置多线程时，主
线程会创建多个子线程，在Python中，默认情况下就是setDaemon(False),主线程执行完自己的任务以后，就退出了，此时子线程会继续执行自己的任务，直到自己的任务结束。
2、setDaemon（True)
当我们使用setDaemon(True)时，这是子线程为守护线程，主线程一旦执行结束，则全部子线程被强制
终止
3、join（线程同步)
join 所完成的工作就是线程同步，即主线程任务结束以后，进入堵塞状态，一直等待所有的子线程结束
以后，主线程再终止。
import threading
import time
def thread():
	time.sleep(2)
	print('---子线程结束---')
def main():
	t1 = threading.Thread(target=thread)
	t1.setDaemon(True)
	t1.start()
	t1.join(timeout=1)
    #1 线程同步，主线程堵塞1s 然后主线程结束，子线程继续执行
#2 如果不设置timeout参数就等子线程结束主线程再结束
#3 如果设置了setDaemon=True和timeout=1主线程等待1s后会强制杀死子线程，然后主线程结束
	print('---主线程结束---')
if __name__=='__main___':
	main()
```

14、多线程交互访问数据，如果访问到了就不访问了？

```
怎么避免重读？
创建一个已访问数据列表，用于存储已经访问过的数据，并加上互斥锁，在多线程访问数据的时候先查看数据是否在已访问的列表中，若已存在就直接跳过。
```

15、什么是线程安全，什么是互斥锁？

```
每个对象都对应于一个可称为’互斥锁‘的标记，这个标记用来保证在任一时刻，只能有一个线程访问该对象。
同一进程中的多线程之间是共享系统资源的，多个线程同时对一个对象进行操作，一个线程操作尚未结束，另一线程已经对其进行操作，导致最终结果出现错误，此时需要对被操作对象添加互斥锁，保证每个线程对该对象的操作都得到正确的结果。
```

16、说说下面几个概念：同步，异步，阻塞，非阻塞？

```
同步： 多个任务之间有先后顺序执行，一个执行完下个才能执行。
异步：多个任务之间没有先后顺序，可以同时执行，有时候一个任务可能要在必要的时候获取另一个同时执行的任务的结果，这个就叫回调。
阻塞：如果卡住了调用者，调用者就不嫩那个继续往下执行，就说明调用者阻塞了。
非阻塞：如果不会卡住，可以继续执行。就是说非阻塞的。
```

15、为什么有全局解释器锁了，还需要互斥锁？

```python
lock.acquire()
n -= 1
lock.release()
在执行python代码时，经常把一条语句拆分成2条或者多条语句去执行，
正常情况：
n=5000
x=n+1
n=x
x=n-1
n=x
非正常情况：
n=5000
x=n+1
上锁之后再上锁就阻塞了，互斥锁是对需要操作的数据加了一把锁，保证数据一次操作完成再对数据进行其他操作
```

17、python中进程与线程的使用场景？

```
cpu密集型，适用于多进程
IO密集型，适用于多线程
cpu密集和io密集：多进程+协程
```

18、线程是并发还是并行，进程是并发还是并行？

```
线程是并发，进程是并行;
```

19、并行(parallel)和并发（concurrency)?

```
并行： 同一时刻多个任务同时在运行
并发： 不会在同一时刻同时运行，存在交替执行的情况
实现并行的库有： multiprocessing
实现并发的库有: threading
程序需要执行较多的读写、请求和回复任务的需要大量的IO操作，IO密集型操作使用并发更好。
CPU运算量大的程序，使用并行会更好
```

20、IO密集型和CPU密集型区别？

```
IO密集型： 系统运行，大部分的状况是CPU在等 I/O（硬盘/内存）的读/写
CPU密集型： 大部分时间用来做计算，逻辑判断等CPU动作的程序称之CPU密集型
```

21、多进程编程基础示例1

```python
创建流程
【1】 将需要新进程执行的事件封装为函数
【2】 通过模块的Process类创建进程对象，关联函数
【3】 可以通过进程对象设置进程信息及属性
【4】 通过进程对象调用start启动进程
【5】 通过进程对象调用join回收进程资源
import multiprocessing
from time import sleep
a = 1
# 进程的执行函数
def fun():
    print('开始运行一个进程')
    sleep(2)
    global a
    print('a=',a)
    a = 10000  #子进程中的变量a
    print('进程执行结束了')
# 实例化进程对象
p = multiprocessing.Process(target=fun)
# 启动进程，自动执行target绑定的函数，进程诞生
p.start()
print('执行另外一个事情')
sleep(3)
print('事情干完了')
# 阻塞等待进程结束后回收
p.join()
print("a: ",a)# 父进程的a还是1
```

22、带参数的多进程编程

```python
"""
进程基础实例2
含有参数的进程函数
"""

from multiprocessing import Process
from time import sleep

# 带有参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working....")

# 创建进程
# p = Process(target=worker,args=(2,"Tom"))
p = Process(target=worker,
            args = (2,),
            kwargs={'name':'Levi'})

p.start()
p.join(3) # 最长等待3秒

print("================================")
#注意 : 启动进程此时target绑定函数开始执行，该函数作为新进程执行内容，此时进程真正被创建
```

23、僵尸进程

```python
"""
僵尸进程
"""

from multiprocessing import Process
from time import sleep
import os
from signal import *

# 带有参数的进程函数
def worker(sec,name):
    for i in range(2):
        sleep(sec)
        print(os.getpid(),"I'm %s"%name)


# 处理僵尸进程
signal(SIGCHLD,SIG_IGN)

# 创建进程
p = Process(target=worker,
            args = (2,),
            kwargs={'name':'Levi'})

p.start()

# p.join() # 防止僵尸产生

while True:
    pass
```

练习

```python
"""
练习1 ： 大文件拆分
将一个 文件拆分为两个小文件

要求： 不清除文件类型 二进制  文本
      拆分的过程按照字节数平均分成两份
      上下两部分同时进行

提示： 两个进程同时拷贝
      os.path.getsize()
"""
from multiprocessing import Process
import os
filename = input("File:")
size = os.path.getsize(filename)
def top():
    fr = open(filename,'rb')
    fw = open("top.jpg",'wb')
    n = size // 2
    while n >=1024:
        fw.write(fr.read(1024))
        n -= 1024
   	else:
        fw.write(fr.read(n))
   	fr.close()
    fw.close()
def bot():
    fr = open(filename,'rb')
    fw = open("bot.jpg",'wb')
    fr.seek(size//2)
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()
jobs = []
for i in [bot,top]:
    p = Process(target=i)
    jobs.append(p)
    p.start()
[i.join() for i in jobs]
```

```python
"""
100000以内质数之和
"""
import time
from multiprocessing import Process
# 装饰器函数求一个函数的运行时间
def timeis(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = f(*args,**kwargs)
        end_time = time.time()
        print("执行时间:",end_time-start_time)
        return res
    return  wrapper
# 判断一个数是不是素数
def isPrime(n):
    if n<=1:
    	return False
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    return True
class Prime(Process):
    def __init__(self,begin,end):
        self.begin = begin # 起始数字
        self.end = end # 结尾数字
        super().__init__()
    # 求和
	def run(self):
        prime = []
        for i in range(self.begin,self.end):
            if is isPrime(i):
                prime.append(i)
        print(sum(prime))
@timeis
def multi_process(n):
    # n表示你想创建几个进程
    tep = 100000 // n
    jobs = []
    # 循环创建进程
    for i in range(1,100001,tep):
        p = Prime(i,i+tep)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs] 
```

24、创建进程类

```python
"""
创建步骤

【1】 继承Process类

【2】 重写`__init__`方法添加自己的属性，使用super()加载父类属性

【3】 重写run()方法
"""
from multiprocessing import Process

# 如果进程执行的时间比较复杂,封装在一个类里
class MyProcess(Process):
    def __init__(self,value):
        self.value = value
        # 同时加载父类属性
        super().__init__()

    def fun(self):
        print("假装干了个大事")

    # start()时run会作为一个新的进程内容执行
    def run(self):
        self.fun()
        print("完事了")

p = MyProcess(2)
p.start() # 启动进程 -->run就会运行
p.join()

```

25、进程池

```python
原理
创建一定数量的进程来处理事件，事件处理完进程不退出而是继续处理其他事件，直到所有事件全都处理完毕统一销毁。增加进程的重复利用，降低资源消耗
from multiprocessing import Pool
from time import sleep,ctime
def worker(msg,sec):
    sleep(sec)
    print(ctime(),'---',msg)
# 创建进程池
pool = Pool(4)
# 向进程池中添加事件
for i in range(10):
    msg = 'Tedu-%d'%i
    pool.apply_async(worker,args=(msg,2))
# 关闭进程池，不能再添加新事件
pool.close()
# 销毁进程池
pool.join()
```

```python
"""
练习2 :  使用进程池完成
拷贝一个指定的文件夹(该文件夹下没有子目录,全是普通文件)

思路提示: os.mkdir("xxx") 创建一个文件夹
         os.listdir('xxx') 获取文件列表

         把每个文件的拷贝作为进程池要执行的一个事件

         本质将源文件夹中所有文件拷贝到新文件夹
"""
from multiprocessing import Pool,Queue
import os 
q = Queue() # 消息队列
def copy(filename,old_folder,new_folder):
    fr.open(old_folder+'/'+filename,'rb')
    fw = open(new_folder+'/'+filename,'wb')
    while True:
        data = fr.read(1024*10):
            if not data:
                break
            n = fw.write(data) #返回值就是写入大小
            q.put(n)# 存入消息队列
#获取文件夹总大小
def get_size(dir):
    total_size = 0
    for file in os.list(dir):
        total_size += os.path.getsize(dir+'/'+file)
    return total_size
# 创建进程池,执行事件
def main():
    # 获取文件列表
    old_folder = input("要拷贝的目录:")
    filelist = os.listdir(old_folder)
    os.mkdir(old_folder+'-备份')
    new_folder = old_folder+'-备份'
    # 文件夹大小
    total_size = get_size(old_folder)
    pool = Pool(4) # 创建进程池
    for file in filelist:
        pool.apply_async(func = copy,
                         args=(file,old_folder,new_folder))
   	pool.close()
    
    copy_size = 0 #　已经拷贝的大小
    while copy_size < total_size:
        copy_size += q.get() # 从消息队列拿到已经拷贝的大小
        print("拷贝 %.2f%%"%(copy_size/total_size*100))
    pool.join()
if __name__ == '__main__':
    main()
```

26、进程通信

```python
必要性： 进程间空间独立，资源不共享，此时在需要进程间数据传输时就需要特定的手段进行数据通信。
消息队列使用
	通信原理： 在内存中开辟空间，建立队列模型，进程通过队列将消息存入，或者从队列取出完成进程间通信。
"""
消息队列通信
"""
from multiprocessing import Process,Queue

#  创建消息队列  必须在父进程创建
q = Queue()

def request():
    name = "Levi"
    passwd = "123"
    # 存入消息队列
    q.put(name)
    q.put(passwd)

def handle():
    # 从消息队列取出消息
    name = q.get()
    passwd = q.get()
    print("用户名:",name)
    print("密  码:",passwd)

p1 = Process(target = request)
p2 = Process(target = handle)
p1.start()
p2.start()
p1.join()
p2.join()
```

实现方法：

```python
from multiprocessing import Queue

q = Queue(maxsize=0)
功能: 创建队列对象
参数：最多存放消息个数
返回值：队列对象

q.put(data,[block,timeout])
功能：向队列存入消息
参数：data  要存入的内容
	block  设置是否阻塞 False为非阻塞
	timeout  超时检测

q.get([block,timeout])
功能：从队列取出消息
参数：block  设置是否阻塞 False为非阻塞
	 timeout  超时检测
返回值： 返回获取到的内容

q.full()   判断队列是否为满
q.empty()  判断队列是否为空
q.qsize()  获取队列中消息个数
q.close()  关闭队列
```

27、进程对象属性

```python
p.name 进程名称
p.pid 对应子进程的PID号
p.is_alive() 查看子进程是否在生命周期
p.daemon 设置父子进程的退出关系
    1、如果设置为True则该子进程会随父进程的退出而结束，子线程为守护线程，主线程一旦执行结束，则全部子线程被强制终止
    2、要求必须在start()前设置
    3、如果daemon设置成True 通常就不会使用 join()
```

28、进程处理细节

```python
进程相关函数：
	os.getpid() #获取一个进程的PID值，返回当前进程的PID
    os.getppid() #获取父进程的PID号，返回父进程的PID
    sys.exit(info) # 退出进程 info表示退出时打印内容
```

29、什么是线程？

```
1、线程被称为轻量级的进程，也是多任务编程方式
2、也可以利用计算机的多cpu资源
3、线程可以理解为进程中再开辟的分支任务
```

30、线程有什么特征？

```
1、一个进程可以包含多个线程，至少包含一个线程，主线程
2、线程也是一个运行行为，消耗计算机资源
3、一个进程中的所有线程共享这个进程的资源
4、多个线程之间的运行同样互不影响各自运行
5、线程的创建和销毁消耗资源远小于进程
```

练习

```python
"""示例代码"""
import os
import threading
from time import sleep

a = 1


def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放:葫芦娃")
    global a
    # 在一个函数中对全局变量进行修改的时候，到底是否需要使用global进行说明，要看是否对全局变量的执行指向进行了修改，如果修改了执行，即让全局变量指向	了一个新的地方，那么必须使用global，如果，仅仅是修改了指向的空间中的数据，此时不用必须使用global
    print("a=", a)
    a = 10000


t = threading.Thread(target=music)
t.start()
for i in range(2):
    sleep(3)
    print(os.getpid(),"播放:中国心")
t.join()
print("a:", a)
```

```python
"""
多线程示例2
"""

from threading import Thread
from time import sleep

# 含有参数的线程函数
def fun(sec,name):
    print("含有参数的线程")
    sleep(sec)
    print("%s 线程执行完毕"%name)

# 创建多个线程
jobs = []
for i in range(5):
    t = Thread(target=fun,
               args=(2,),
               kwargs={'name':"T%d"%i})
    jobs.append(t) # 存储线程对象
    t.start()

# 统一回收线程
for i in jobs:
    i.join()
```

31、线程对象属性

```python
t.setName()#设置线程名称
t.getName()#获取线程名称
t.is_alive()#查看线程是否在生命周期
t.setDaemon()#设置daemon属性值
t.isDaemon()#查看daemon属性值
daemon为True时主线程退出分支线程也退出。要在start前设置，通常不和join一起使用。join为线程同步，主线程结束，阻塞等待分支线程完成一起结束
```

32、线程类创建和使用

```python
"""
自定义线程类
"""
from threading import Thread
import time

class MyThread(Thread):
    def __init__(self,song):
        self.song = song
        super().__init__() # 必须重新加载父类

    # 作为线程的执行内容
    def run(self):
        for i in range(3):
            print("playing %s"%self.song)
            time.sleep(2)

t = MyThread("凉凉")
t.start() # 运行run
t.join()
```

33、什么是同步互斥机制？为什么要有同步互斥机制？

```
共享资源：多个进程或者线程都可以操作的资源称为共享资源。对共享资源的操作代码段称为临界区。
影响 ： 对共享资源的无序操作可能会带来数据的混乱，或者操作错误。此时往往需要同步互斥机制协调操作顺序。
同步 ： 同步是一种协作关系，为完成操作，多进程或者线程间形成一种协调，按照必要的步骤有序执行操作。
互斥 ： 互斥是一种制约关系，当一个进程或者线程占有资源时会进行加锁处理，此时其他进程线程就无法操作该资源，直到解锁后才能操作。
```

34、进程和线程的区别和联系

```python
两者都是多任务编程，都能使用计算机多核资源
进程的创建删除消耗的计算机资源比线程多
进程空间独立，数据互不干扰，有专门通信方法，线程使用全局变量通信
一个进程可以有多个分支线程，两者有包含关系
多线程共享进程资源，在共享资源操作时往往需要同步互斥处理
Python线程存在GIL问题，但是进程没有
```

线程练习

```python
"""
练习1:  模拟一个售票系统
有 500 张门票 记为 T1---T500 存入到一个列表里

创建 10 个线程 同时进行售票 ,知道所有的票都卖完

票需要按照顺序卖出

每出一张打印 w1 --- T256 每出一张票需要sleep(0.1)

"""
from threading import Thread
from time import sleep

# 模拟500张票
ticket = ["T%d"%x for x in range(1,501)]

# 线程函数 w 相当于窗口名
def sell(w):
    while ticket:
        sleep(0.1)
        print("%s -- %s"%(w,ticket.pop(0)))


# 创建线程
jobs = []
for i in range(1,11):
    t = Thread(target=sell,args=("W%d"%i,))
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()
```



### 2.6 网络编程

#### 概述

1、描述一下OSI七层模型并说出每一层的功能

```
从上至下依次为：
	应用层：各种应用程序
	表示层：数据的格式化，数据加密解密，数据的压缩解压缩
	会话层：建立，管理，终止应用之间的会话连接
	传输层：提供端到端的服务
	网络层：逻辑寻址，路由选择
	数据链路层：将分组数据封装成帧
	物理层：在介质上传输比特，提供物理的规约
```

2、TCP/IP协议集

```
应用层：Telnet,FTP,SMTP,DNS,HTTP以及其他应用协议
传输层：TCP UDP
网络层：IP,ARP,RARP,ICMP
网络接口：各种通信网络接口
```

3、常用网络端口号

```python
HTTP 80
HTTPS 443
SOCKS 1080
MYSQL 3306
mongo 27017
redis 6379
FTP 21
SSH 22
Telnet 23
SMTP 25
DNS 53
POP3 110
```

![image-20201210161736251](../图片/image-20201210161736251.png)

#### HTTP

1、长链接与短链接的区别？

```
短连接
连接->传输数据->关闭连接
HTTP 是无状态的，浏览器和服务器每进行一次HTTP 操作，就建立一次连接，但任务结束后就中断连接。短连接是指SOCKET 连接后发送后接收完数据后马上断开连接。
长连接
连接->传输数据->保持连接->传输数据->....->关闭连接
长连接指建立SOCKET 连接后不管是否使用都保持连接，但安全性较差。
```

2、HTTP 协议状态码有什么用，列出你知道的HTTP 协议的状态码，然后讲出他们都表示什么意思。

```
作用：告诉用户当前操作所处的状态
200 OK 服务器成功处理了请求（这个是我们见到最多的）
301/302 Moved Permanently（重定向）请求的URL 已移走。Response 中应该包含一个Location URL, 说明资源现在所处的位置
304 Not Modified（未修改）客户的缓存资源是最新的， 要客户端使用缓存
404 Not Found 未找到资源
501 Internal Server Error 服务器遇到一个错误，使其无法对请求提供服务
```

3、从输入http://www.baidu.com/ 到页面返回，中间都是发生了什么？

```
(浏览器发送一个请求到返回一个页面的具体过程)
第一步，解析域名，找到ip
浏览器会缓存DNS 一段时间，一般2-30 分钟不等，如果有缓存，直接返回ip，否则下一步。缓存中无法找到ip，浏览器会进行一个系统调用，查询hosts 文件。如果找到，直接返回ip，否则下一步。进行1 和2 本地查询无果，只能借助于网络，路由器一般都会有自己的DNS缓存，ISP 服务商DNS 缓存，这时一般都能够得到相应的ip，如果还是无果，只能借助于DNS 递归解析了。
这时ISP 的DNS 服务器就会开始从根域名服务器开始递归搜索，从.com 顶级域名服务器，到baidu 的域名服务器。到这里，浏览器就获得网络ip，在DNS 解析过程中，常常解析出不同的IP。
第二步，浏览器于网站建立TCP 连接
浏览器利用ip 直接网站主机通信，浏览器发出TCP 连接请求，主机返回TCP应答报文，浏览器收到应答报文发现ACK 标志位为1，表示连接请求确认，浏览器返回TCP（）确认报文，主机收到确认报文，三次握手，TCP 连接建立完成。
第三步， 浏览器发起默认的GET 请求
浏览器向主机发起一个HTTP-GET 方法报文请求，请求中包含访问的URL，也就是http://www.baidu.com/还有User-Agent 用户浏览器操作系统信息，编码等，值得一提的是Accep-Encoding 和Cookies 项。Accept-Encoding 一般采用gzip，压缩之后传输html 文件，Cookies 如果是首次访问，会提示服务器简历用户缓存信息，如果不是，可以利用Cookies 对应键值，找到相应缓存，缓存里面存放着用户名，密码和一些用户设置项
第四步，显示页面或返回其他
返回状态码200 OK，表示服务器可以响应请求，返回报文，由于在报头中Content-type 为“text/html”,浏览器以HTML 形式呈现，而不是下载文件。但是对于大型网站存在多个主机站点，往往不会直接返回请求页面，而是重定向。返回的状态码就不是200 OK， 而是301,302 以3 开头的重定向吗。浏览器在获取了重定向响应后，在响应报文中Location 项找到重定向地址，浏览器重新第一步访问即可。
```

4、在浏览器中输入url地址->>显示主页的过程

```
1、DNS解析
2、TCP连接
3、发送HTTP请求
4、服务器处理请求并返回HTTP报文
5、浏览器解析渲染页面
6、连接结束
```

![image-20201210152135014](../图片/image-20201210152135014.png)

5、HTTP和HTTPS的区别

```
1、https协议需要到CA申请证书，一般免费证书较少，因而需要一定费用。

2、http是超文本传输协议，信息是明文传输，https则是具有安全性的ssl/tls加密传输协议。

3、http和https使用的是完全不同的连接方式，用的端口也不一样，前者是80，后者是443。

4、http的连接很简单，是无状态的；HTTPS协议是由SSL/TLS+HTTP协议构建的可进行加密传输、身份认证的网络协议，比http协议安全。
```

#### TCP/UDP

##### UDP

客户端流程

```python
socket()-sendto()-recvfrom()-close()
```

服务端流程

```python
socket()-bind()-recvfrom()-sendto()-close()
```

**重点代码**

```python
"""
udp 客户端
重点代码 ！！！
"""
from socket import *
# 服务器地址
ADDR = ("127.0.0.1",8888)
# 创建udp套接字
udp_socket=socket(AF_INET,SOCK_DGRAM)
# 发送后接收，与服务端配合
while True:
    msg = input(">>")
    if not msg:
        break
    udp_socket.sendto(msg.encode(),ADDR)
    data,addr=udp_socket.recvfrom(1024)
    print('From server',data.decode())
udp_socket.close()
```

```python
"""
udp套接字服务端程序示例
重点代码 ！！！
"""
from socket import *
# 创建udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)
# 绑定地址
udp_socket.bind(('0.0.0.0',8888))
# 接收消息
while True:
    data,addr=udp_socket.recvfrom(1024)
    print('From',addr,":",data.decode())
    # 发送消息
    n = udp_socket.sendto(b'Thanks',addr)
    print("Send %d bytes"%n)
# 关闭套接字
udp_socket.close()
```

2、tcp编程

​	1、简述三次握手与四次挥手

```
三次握手（建立连接）:
	客户端向服务端发送消息报文请求连接
	服务端收到请求后，回复报文确定可以连接
	客户端收到回复，发送最终报文连接建立
客户端–发送带有 SYN 标志的数据包–一次握手–服务端
服务端–发送带有 SYN/ACK 标志的数据包–二次握手–客户端
客户端–发送带有带有 ACK 标志的数据包–三次握手–服务端
四次挥手（断开连接）：
	主动方发送报文请求断开连接
	被动方收到请求后，立即回复，表示准备断开
	被动方准备就绪，再次发送报文表示可以断开
	主动方收到确定，发送最终报文完成断开
客户端-发送一个 FIN，用来关闭客户端到服务器的数据传送
服务器-收到这个 FIN，它发回一 个 ACK，确认序号为收到的序号加1 。和 SYN 一样，一个 FIN 将占用一个序号
服务器-关闭与客户端的连接，发送一个FIN给客户端
客户端-发回 ACK 报文确认，并将确认序号设置为收到序号加1
```

![image-20201210154158580](../图片/image-20201210154158580.png)

3、为什么要三次握手？

![image-20201210161351370](../图片/image-20201210161351370.png)

```
三次握手的目的是建立可靠的通信信道，说到通讯，简单来说就是数据的发送与接收，而三次握手最主要的目的就是双方确认自己与对方的发送与接收是正常的。
第一次握手：Client 什么都不能确认；Server 确认了对方发送正常
第二次握手：Client 确认了：自己发送、接收正常，对方发送、接收正常；Server 确认了：自己接收正常，对方发送正常
第三次握手：Client 确认了：自己发送、接收正常，对方发送、接收正常；Server 确认了：自己发送、接收正常，对方发送接收正常
所以三次握手就能确认双发收发功能都正常，缺一不可。
```

**为什么要传回 SYN**

接收端传回发送端所发送的 SYN 是为了告诉发送端，我接收到的信息确实就是你所发送的信号了

```
SYN 是 TCP/IP 建立连接时使用的握手信号。在客户机和服务器之间建立正常的 TCP 网络连接时，客户机首先发出一个 SYN 消息，服务器使用 SYN-ACK 应答表示接收到了这个消息，最后客户机再以 ACK(Acknowledgement[汉译：确认字符 ,在数据通信传输中，接收站发给发送站的一种传输控制字符。它表示确认发来的数据已经接受无误。 ]）消息响应。这样在客户机和服务器之间才能建立起可靠的TCP连接，数据才可以在客户机和服务器之间传递。
```

**传了 SYN,为啥还要传 ACK**

双方通信无误必须是两者互相发送信息都无误。传了 SYN，证明发送方到接收方的通道没有问题，但是接收方到发送方的通道还需要 ACK 信号来进行验证。

为什么不能用两次握手进行连接？

```
3次握手完成两个重要的功能，既要双方做好发送数据的准备工作(双方都知道彼此已准备好)，也要允许双方就初始序列号进行协商，这个序列号在握手过程中被发送和确认。
```

5、为什么要四次挥手？

![image-20201210161451915](../图片/image-20201210161451915.png)



任何一方都可以在数据传送结束后发出连接释放的通知，待对方确认后进入半关闭状态。当另一方也没有数据再发送的时候，则发出连接释放通知，对方确认后就完全关闭了TCP连接。

###### 为什么客户端最后还要等待2MSL？

```
MSL（Maximum Segment Lifetime），TCP允许不同的实现可以设置不同的MSL值。
    第一，保证客户端发送的最后一个ACK报文能够到达服务器，因为这个ACK报文可能丢失，站在服务器的角度看来，我已经发送了FIN+ACK报文请求断开了，客户端还没有给我回应，应该是我发送的请求断开报文它没有收到，于是服务器又会重新发送一次，而客户端就能在这个2MSL时间段内收到这个重传的报文，接着给出回应报文，并且会重启2MSL计时器。
    第二，防止类似与“三次握手”中提到了的“已经失效的连接请求报文段”出现在本连接中。客户端发送完最后一个确认报文后，在这个2MSL时间中，就可以使本连接持续的时间内所产生的所有报文段都从网络中消失。这样新的连接中不会出现旧连接的请求报文。
```

为什么建立连接是三次握手，关闭连接确是四次挥手呢？

```
建立连接的时候， 服务器在LISTEN状态下，收到建立连接请求的SYN报文后，把ACK和SYN放在一个报文里发送给客户端。
而关闭连接时，服务器收到对方的FIN报文时，仅仅表示对方不再发送数据了但是还能接收数据，而自己也未必全部数据都发送给对方了，所以己方可以立即关闭，也可以发送一些数据给对方后，再发送FIN报文给对方来表示同意现在关闭连接，因此，己方ACK和FIN一般都会分开发送，从而导致多了一次。
```

###### 如果已经建立了连接，但是客户端突然出现故障了怎么办？

```
TCP还设有一个保活计时器，显然，客户端如果出现故障，服务器不能一直等下去，白白浪费资源。服务器每收到一次客户端的请求后都会重新复位这个计时器，时间通常是设置为2小时，若两小时还没有收到客户端的任何数据，服务器就会发送一个探测报文段，以后每隔75秒发送一次。若一连发送10个探测报文仍然没反应，服务器就认为客户端出了故障，接着就关闭连接。
```



##### TCP

服务端：

```
socket()-bind()-listen()-accept()-send/recv()-close()
```

客户端：

```
socket()-connect()-send/recv()-close()
```

```python
"""
tcp客户端基础实例
"""
from socket import *

# 创建tcp套接字 默认就是tcp套接字
tcp_socket = socket()

# 发起链接
tcp_socket.connect(('127.0.0.1',8888))

# 收发消息
msg = input(">>")
tcp_socket.send(msg.encode())

data = tcp_socket.recv(1024)
print("From server:",data.decode())

# 关闭套接字
tcp_socket.close()
```

```python
"""
tcp 服务端基础实例
"""
from socket import *
# 创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)
# 绑定地址
tcp_socket.bind(('0.0.0.0',8888))
# 设置监听
tcp_socket.listen(5)
# 处理客户端链接 (阻塞函数)
print("Waiting for connect...")
connfd,addr = tcp_socket.accept()
print("Connect from",addr)
# 收发消息
data = connfd.recv(1024)
print("接收到：",data.decode())
connfd.send(b"Thanks")
# 关闭套接字
connfd.close()
tcp_socket.close()
```

3、TCP套接字细节

- tcp连接中当一端退出，另一端如果阻塞在recv，此时recv会立即返回一个空字串。
- tcp连接中如果一端已经不存在，仍然试图通过send向其发送数据则会产生BrokenPipeError
- 一个服务端可以同时连接多个客户端，也能够重复被连接

tcp粘包问题

- 产生原因
  - 为了解决数据再传输过程中可能产生的速度不协调问题，操作系统设置了缓冲区
  - 实际网络工作过程比较复杂，导致消息收发速度不一致
  - tcp以字节流方式进行数据传输，在接收时不区分消息边界

也就是说：**接收方不知道该接收多大的数据才算接收完毕，造成粘包。**

4、TCP与UDP对比

- 传输特征:
  - TCP提供可靠的数据传输，但是UDP则不保证传输的可靠性
  - TCP传输数据为字节流，而UDP处理为数据包形式
  - TCP传输需要建立连接才能进行数据传输，效率相对较低，UDP比较自由，无需连接，效率较高

- 套接字编程区别
  - 创建的套接字类型不同
  - tcp套接字会有粘包，udp套接字有消息边界不会粘包
  - tcp套接字依赖listen accept建立连接才能收发消息，udp套接字则不需要
  - tcp套接字使用send，recv收发消息，udp套接字使用sendto，recvfrom

- 使用场景
  - tcp更适合对准确性要求高，传输数据较大的场景
    * 文件传输：如下载电影，访问网页，上传照片
    * 邮件收发
    * 点对点数据传输：如点对点聊天，登录请求，远程访问，发红包
  - udp更适合对可靠性要求没有那么高，传输方式比较自由的场景
    * 视频流的传输： 如直播，视频聊天
    * 广播：如网络广播，群发消息
    * 实时传输：如游戏画面
  - 在一个大型的项目中，可能既涉及到TCP网络又有UDP网络

5、Tcp 协议和udp 协议有什么区别？

```
1、TCP 面向连接（如打电话要先拨号建立连接）;UDP 是无连接的，即发送数据之前不需要建立连接
2、TCP 提供可靠的服务。也就是说，通过TCP 连接传送的数据，无差错，不丢失，不重复，且按序到达;UDP 尽最大努力交付，即不保证可靠交付
3、TCP 面向字节流，实际上是TCP 把数据看成一连串无结构的字节流;UDP 是面向报文的UDP 没有拥塞控制，因此网络出现拥塞不会使源主机的发送速率降低（对实时应用很有用，如IP 电话，实时视频会议等）
4、每一条TCP 连接只能是点到点的;UDP 支持一对一，一对多，多对一和多对多的交互通信
5、TCP 首部开销20 字节;UDP 的首部开销小，只有8 个字节
6、TCP 的逻辑通信信道是全双工的可靠信道，UDP 则是不可靠信道
```

6、知道arp 报文吗？全称叫什么以及有什么作用？

```
ARP (Address Resolution Protocol) 是个地址解析协议。最直白的说法是：
在IP 以太网中，当一个上层协议要发包时，有了该节点的IP 地址，ARP 就能提供该节点的MAC 地址。报文在传输的过程中在路由器中的处理过程
```

7、创建一个简单tcp 服务器需要的流程

```
1.socket 创建一个套接字
2.bind 绑定ip 和port
3.listen 使套接字变为可以被动链接
4.accept 等待客户端的链接
5.recv/send 接收发送数据
```

#### IP

1、有哪些私有（保留）地址？

```
A类：10.0.0.0 - 10.255.255.255
B类：172.16.0.0 - 172.31.255.255
C类：192.168.0.0 - 192.168.255.255
```

2、IP地址分为哪几类？

![image-20201210155931062](../图片/image-20201210155931062.png)

#### ARP

1、简单解释一些ARP协议的工作过程？

```
ARP是地址解析协议，简单语言解释一下工作原理。

1：首先，每个主机都会在自己的ARP缓冲区中建立一个ARP列表，以表示IP地址和MAC地址之间的对应关系。

2：当源主机要发送数据时，首先检查ARP列表中是否有对应IP地址的目的主机的MAC地址，如果有，则直接发送数据，如果没有，就向本网段的所有主机发送ARP数据包，该数据包包括的内容有：源主机 IP地址，源主机MAC地址，目的主机的IP 地址。

3：当本网络的所有主机收到该ARP数据包时，首先检查数据包中的IP地址是否是自己的IP地址，如果不是，则忽略该数据包，如果是，则首先从数据包中取出源主机的IP和MAC地址写入到ARP列表中，如果已经存在，则覆盖，然后将自己的MAC地址写入ARP响应包中，告诉源主机自己是它想要找的MAC地址。

4：源主机收到ARP响应包后。将目的主机的IP和MAC地址写入ARP列表，并利用此信息发送数据。如果源主机一直没有收到ARP响应数据包，表示ARP查询失败。

广播发送ARP请求，单播发送ARP响应
```

![image-20201210160053857](../图片/image-20201210160053857.png)

#### 多任务编程

​	1、多进程并发模型

```python
"""
基于多进程的tcp网络并发模型
    创建网络套接字用于接收客户端请求
    等待客户端连接
    客户端连接，则创建新的进程具体处理客户端请求
    主进程继续等待其他客户端连接
    如果客户端退出，则销毁对应的进程

重点代码 !!!
"""
from multiprocessing import Process
from socket import *
from signal import *
import sys

# 网络地址
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

# 处理客户端事件
def handle(connfd):
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b'ok')
    connfd.close()

# 搭建并发网络
def main():
    # 创建tcp套接字
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)

    print("Listen the port %d"%PORT)
    signal(SIGCHLD,SIG_IGN) # 处理僵尸进程

    # 循环等待客户端链接
    while True:
        try:
            connfd,addr = sock.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            sys.exit("服务结束")

        # 为连接进来的客户端创建新的进程
        p = Process(target=handle,args=(connfd,))
        p.daemon = True # 子进程随父进程退出
        p.start()

if __name__ == '__main__':
    main()
```

2、多线程并发模型

```python
"""
- 创建网络套接字用于接收客户端请求
- 等待客户端连接
- 客户端连接，则创建新的线程具体处理客户端请求
- 主线程继续等待其他客户端连接
- 如果客户端退出，则销毁对应的线程
"""
"""
基于多线程的tcp并发模型

重点代码 !!
"""

from threading import Thread
from socket import *
import sys

# 网络地址
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

# 类用于处理客户端的事件
class MyThread(Thread):
    def __init__(self,connfd):
        # 客户端链接套接字设置为属性
        self.connfd = connfd
        super().__init__()

    # 处理客户端事件
    def run(self):
        while True:
            data = self.connfd.recv(1024)
            if not data:
                break
            print(data.decode())
            self.connfd.send(b'ok')
        self.connfd.close()

# 搭建并发网络
def main():
    # 创建tcp套接字
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)

    print("Listen the port %d"%PORT)

    # 循环等待客户端链接
    while True:
        try:
            connfd,addr = sock.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            sys.exit("服务结束")

        # 为连接进来的客户端创建新的线程
        t = MyThread(connfd)
        t.setDaemon(True)
        t.start()

if __name__ == '__main__':
    main()
```

3、IO并发模型

​	1、什么是IO？

```
在程序中存在读写数据操作行为的事件均是IO行为，比如终端输入输出 ,文件读写，数据库修改和网络消息收发等。
```

```python
"""
基于 select 方法的IO多路复用并发模型

重点代码 !!
"""
from socket import *
from select import select

# 创建监听套接字,作为初始监控对象
sockfd = socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)

# 设置为非阻塞
sockfd.setblocking(False)

# 设置关注列表
rlist = [sockfd] # 关注监听套接字
wlist = []
xlist = []

# 循环监控关注的IO
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    # 遍历就绪的IO列表,分情况讨论 监听套接字和客户端连接套接字
    for r in rs:
        if r is sockfd:
            connfd, addr = r.accept()
            print("Connect from",addr)
            # 将链接进来的客户端链接套接字加入关注的IO
            connfd.setblocking(False)
            rlist.append(connfd)
        else:
            # 某个客户端发送了消息
            data = r.recv(1024).decode()
            if not data:
                # 客户端结束
                rlist.remove(r) # 取消关注
                r.close()
                continue # for循环继续遍历后面的IO
            print(data)
            # r.send(b'OK')
            wlist.append(r) # 加入到写关注列表

    for w in ws:
        w.send(b'ok')
        wlist.remove(w) # 移除
```

2、什么是阻塞IO?

```
定义：在执行IO操作时如果执行条件不满足则阻塞。阻塞IO是IO的默认形态。
效率：阻塞IO效率很低。但是由于逻辑简单所以是默认IO行为。
阻塞情况
	因为某种执行条件没有满足造成的函数阻塞
	e.g.  accept   input   recv
	处理IO的时间较长产生的阻塞状态
	     e.g. 网络传输，大文件读写
```

​	3、什么是非阻塞IO?

```
定义 ：通过修改IO属性行为，使原本阻塞的IO变为非阻塞的状态
```

​	4、什么是IO多路复用？

```
定义：
同时监控多个IO事件，当哪个IO事件准备就绪就执行哪个IO事件。以此形成可以同时处理多个IO的行为，避免一个IO阻塞造成其他IO均无法执行，提高了IO执行效率。
监控对象，而不是监控行为
	select方法 ： windows  linux  unix
	poll方法： linux  unix
	epoll方法： linux
```

​	select方法：

```
rs, ws, xs=select(rlist, wlist, xlist[, timeout])
功能: 监控IO事件，阻塞等待IO发生
参数：rlist  列表  读IO列表，添加等待发生的或者可读的IO事件
      wlist  列表  写IO列表，存放要可以主动处理的或者可写的IO事件
      xlist  列表 异常IO列表，存放出现异常要处理的IO事件
      timeout  超时时间

返回值： rs 列表  rlist中准备就绪的IO
        ws 列表  wlist中准备就绪的IO
	   xs 列表  xlist中准备就绪的IO
```

```python
"""
select io多路复用方法 示例
"""
from select import select
from socket import *

# 搞几个IO 用于监控
tcp_socket = socket()
tcp_socket.bind(('0.0.0.0',8888))
tcp_socket.listen(5)

udp_socket = socket(AF_INET,SOCK_DGRAM)

file = open('my.log','a')

print("对IO进行监控")
rs,ws,xs = select([udp_socket,file],[udp_socket,file],[])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)
```

​	poll方法：

```python
"""
基于 poll 方法的IO多路复用并发模型
"""
from socket import *
from select import *

# 创建监听套接字,作为初始监控对象
sockfd = socket()
sockfd.bind(('0.0.0.0', 8888))
sockfd.listen(5)

# 设置为非阻塞
sockfd.setblocking(False)

# poll对象
p = poll()

# 查找字典 {fileno:sockfd} 与关注的IO保持一致
map = {sockfd.fileno(): sockfd}
# 关注监听套接字
p.register(sockfd, POLLIN)

# 循环监控关注的IO
while True:
    events = p.poll() # events->[(1,2)]
    # 遍历就绪的IO列表,分情况讨论 监听套接字和客户端连接套接字
    for fd, event in events:
        if fd == sockfd.fileno():
            connfd, addr = map[fd].accept()
            print("Connect from", addr)
            # 将链接进来的客户端链接套接字加入关注
            connfd.setblocking(False)
            p.register(connfd, POLLIN)
            # 字典也要维护
            map[connfd.fileno()] = connfd
        elif event == POLLIN:
            # 某个客户端发送了消息
            data = map[fd].recv(1024).decode()
            if not data:
                # 客户端结束
                p.unregister(fd)  # 取消关注
                map[fd].close()
                del map[fd] # 从字典中移除
                continue  # for循环继续遍历后面的IO
            print(data)
            # map[fd].send(b'OK')
            p.register(fd,POLLOUT)
        elif event == POLLOUT:
            map[fd].send(b'OK')
            p.register(fd, POLLIN)

```

​	epoll方法

```python
"""
基于 epoll 方法的IO多路复用并发模型

重点代码　！！
"""
from socket import *
from select import *

# 创建监听套接字,作为初始监控对象
sockfd = socket()
sockfd.bind(('0.0.0.0', 8888))
sockfd.listen(5)

# 设置为非阻塞
sockfd.setblocking(False)

# epoll对象
ep = epoll()

# 查找字典 {fileno:sockfd} 与关注的IO保持一致
map = {sockfd.fileno(): sockfd}
# 关注监听套接字
ep.register(sockfd, EPOLLIN)

# 循环监控关注的IO
while True:
    events = ep.poll()  # events->[(1,2)]
    print("你有新的IO需要处理哦", events)
    # 遍历就绪的IO列表,分情况讨论 监听套接字和客户端连接套接字
    for fd, event in events:
        if fd == sockfd.fileno():
            connfd, addr = map[fd].accept()
            print("Connect from", addr)
            # 将链接进来的客户端链接套接字加入关注
            connfd.setblocking(False)
            # 设置为边缘触发
            ep.register(connfd, EPOLLIN | EPOLLET)
            # 字典也要维护
            map[connfd.fileno()] = connfd
        elif event == EPOLLIN:
            # 某个客户端发送了消息
            data = map[fd].recv(1024).decode()
            if not data:
                # 客户端结束
                ep.unregister(fd)  # 取消关注
                map[fd].close()
                del map[fd]  # 从字典中移除
                continue  # for循环继续遍历后面的IO
            print(data)
            # map[fd].send(b'OK')
            ep.unregister(fd)
            ep.register(fd, EPOLLOUT)
        elif event == POLLOUT:
            map[fd].send(b'OK')
            ep.unregister(fd)
            ep.register(fd, EPOLLIN)

```

**select poll epoll有什么区别？**

```
select:
	支持的操作系统最多，windows,linux,unix
	同时监控IO数量最多1024个
	执行效率一般
poll:
	操作系统：linux,unix
	同时监控IO数量无限制
	执行效率一般
epoll:
	操作系统：unix
	同时监控数量无限制
	执行效率高
select和poll,
1、在应用层整理好要监控的IO，
2、映射到系统层，系统层轮询监控IO,
3、有IO准备就绪，告知应用层处理，但是没有告知哪个就绪，
4、应用层遍历确认，返回给程序，应用层处理，
5、处理完，再提交给系统层，系统层下一次监控
每调用一次select和poll,都会将监控的IO提交给操作系统，重新映射
epoll:
	每当有需要监控的IO就提交给系统层轮询监控，一次监控结束后应用层不用再次提交需要监控的IO，系统层已经记录register过来的，除非unregister
	特点：
		应用层不必遍历，当有IO就绪直接得知是哪一个就绪
		关注的IO直接放在系统层申请的空间，不必每次监控都向系统映射
	
就是select和poll只能通知有fd已经就绪了，但不能知道究竟是哪个fd就绪，所以select和poll就要去主动轮询一遍找到就绪的fd。而epoll则是不但可以知道有fd可以就绪，而且还具体可以知道就绪fd的编号，所以直接找到就可以，不用轮询。
```



* 并发服务实现过程

  【1】将关注的IO准备好，通常设置为非阻塞状态。

  【2】通过IO多路复用方法提交，进行IO监控。

  【3】阻塞等待，当监控的IO有发生时，结束阻塞。

  【4】遍历返回值列表，确定就绪IO事件。

  【5】处理发生的IO事件。

  【6】继续循环监控IO发生。

5、网页访问流程

```
1. 客户端（浏览器）通过tcp传输，发送http请求给服务端
2. 服务端接收到http请求后进行解析
3. 服务端处理请求内容，组织响应内容
4. 服务端将响应内容以http响应格式发送给浏览器
5. 浏览器接收到响应内容，解析展示
```

6、衡量高并发的关键指标

```
- 响应时间(Response Time) ： 接收请求后处理的时间
- 吞吐量(Throughput)： 响应时间+QPS+同时在线用户数量
- 每秒查询率QPS(Query Per Second)： 每秒接收请求的次数
- 每秒事务处理量TPS(Transaction Per Second)：每秒处理请求的次数（包含接收，处理，响应）
- 同时在线用户数量：同时连接服务器的用户的数量
```

## 3.PythonWeb

### 3.1 前端

#### 1.Html

#### 2.Css

#### 3.Javascript

#### 4.Jquery

### 3.2 后端

#### 1.Django

1、Django作为一个重量级的Python Web框架，Django的组件都有哪些？

```
1. 基本配置
2. 路由系统
3. 原生HTML模板系统
4. 视图 view
5. Model模型,数据库连接和ORM数据库管理
6. 中间件
7. Cookie & Seesion
8. 分页
9. 数据库后台管理系统admin
```

2、创建Django项目命令

```python
django-admin startproject mysite1
```

3、说一说setting.py文件中选项

```
1. `BASE_DIR`

   - 用于绑定当前项目的绝对路径(动态计算出来的), 所有文件都可以依懒此路径

2. `DEBUG`

   - 用于配置Django项目的启动模式, 取值:
     1. True 表示开发环境中使用 `调试模式`(用于开发中)
     2. False 表示当前项目运行在`生产环境中`(不启用调试)

3. `ALLOWED_HOSTS`

   - 设置允许访问到本项目的host请求头的值,取值:

     1. [] 空列表,表示只有host请求头为`127.0.0.1`, `localhost`能访问本项目 - DEBUG = True时生效
     2. ['*']，表示任何请求头的host都能访问到当前项目
     3. ['192.168.1.3', '127.0.0.1'] 表示只有当前两个host头的值能访问当前项目

     - 注意:
       - 如果要在局域网其它主机也能访问此主机,启动方式应使用如下模式:

   - `python3 manage.py runserver 0.0.0.0:5000` # 指定网络设备如果内网环境下其他主机想正常访问该站点，需加`ALLOWED_HOSTS = ['内网ip'] 

4. `INSTALLED_APPS`

   - 指定当前项目中安装的应用列表

5. `MIDDLEWARE`

   - 用于注册中间件

6. `TEMPLATES`

   - 用于指定模板的配置信息

7. `DATABASES`

   - 用于指定数据库的配置信息

8. `LANGUAGE_CODE`

   - 用于指定语言配置
   - 取值:
     - 英文 : `"en-us"`
     - 中文 : `"zh-Hans"`

9. `TIME_ZONE`

   - 用于指定当前服务器端时区
   - 取值:
     - 世界标准时间: `"UTC"`
     - 中国时区 : `"Asia/Shanghai"`

10. `ROOT_URLCONF`

    - 用于配置根级 url 配置 'mysite1.urls'
    - 如:
      - `ROOT_URLCONF = 'mysite1.urls'`

> 注: 此模块可以通过 `from django.conf import settings` 导入和使用
```

4、什么是url?url由哪几部分组成？

```
url:统一资源定位符 Uniform Resource Locator
protocol :// hostname[:port] / path [?query][#fragment]
protocol（协议）
hostname（主机名）
port（端口号）
path（路由地址）
query(查询)
fragment（信息片断）
```

5、Django如何处理一个URL对应的请求？

```
1,Django 从配置文件中 根据 ROOT_URLCONF 找到 主路由文件；默认情况下，该文件在 项目同名目录下的urls; 例如 mysite1/mysite1/urls.py
2,Django 加载 主路由文件中的 urlpatterns 变量
3,依次匹配 urlpatterns 中的 URL， 匹配到第一个合适的中断后续匹配
4,匹配成功 - 调用对应的视图函数处理请求，返回响应
5,匹配失败 - 返回404响应
```

6、什么是path()函数？

```
用于描述路由与视图函数的对应关系
path(route, views, name=None)
1. route: 字符串类型，匹配的请求路径
2. views: 指定路径所对应的视图处理函数的名称
3. name: 为地址起别名，在模板中地址反向解析时使用
```

7、什么是path转换器？

```
语法： <转换器类型:自定义名>
作用：若转换器类型匹配到对应类型的数据，则将数据按照关键字传参的方式传递给视图函数
str  匹配除了 '/' 之外的非空字符串
int  匹配0或任何正整数。返回一个 int
slug  匹配任意由 ASCII 字母或数字以及连字符和下划线组成的短标签
path  匹配非空字段，包括路径分隔符 '/'
```

8、什么是re_path函数？

```
在url 的匹配过程中可以使用正则表达式进行精确匹配
re_path(reg, view, name=xxx)
正则表达式为命名分组模式`(?P<name>pattern)` ；匹配提取参数后用关键字传参方式传递给视图函数
```

9、http请求有哪些方法？作用分别是什么？

```
get  请求指定的页面信息，并返回实体主体
head  类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头
post  向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。
PUT  从客户端向服务器传送的数据取代指定的文档的内容
DELETE  请求服务器删除指定的页面
CONNECT  HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。
OPTIONS  允许客户端查看服务器的性能。
TRACE  回显服务器收到的请求，主要用于测试或诊断
```

10、什么是HttpRequest对象？，属性都有哪些？

```
- 视图函数的第一个参数是HttpRequest对象
- 服务器接收到http协议的请求后，会根据请求数据报文创建HttpRequest对象
path_info:URL字符串
method：字符串，表示HTTP请求方法，常用值：'GET'、'POST'
GET：QueryDict查询字典的对象，包含查询字符串的所有数据
book?**bid=10&author=20**查询字符串
POST：QueryDict查询字典的对象，包含post表单提交方式的所有数据
FILES：类似于字典的对象，包含所有的上传文件信息
COOKIES：Python字典，包含所有的cookie，键和值都为字符串 
session：似于字典的对象，表示当前的会话
body: 字符串，请求体的内容(POST或PUT)
scheme : 请求协议('http'/'https')
request.get_full_path() : 请求的完整路径（**包括了查询字符串**）
request.get_host() : 请求的主机
request.META : 请求中的元数据(消息头)
	request.META['REMOTE_ADDR']  : 客户端IP地址
```

11、HTTP响应

1、常见响应码

```
- 200 - 请求成功
- 301 - 永久重定向-资源（网页等）被永久转移到其它URL
  服务器在**Location响应头**中保存新的URL.客户端浏览器收到这个响应，读取url,向这个新url发送GET请求
- 302 - 临时重定向
- 404 - 请求的资源（网页等）不存在
- 500 - 内部服务器错误
```

2、HTTP状态码分类

```
1**信息,服务器收到请求，需要请求者继续执行操作
2**成功,操作被成功接收并处理
3**重定向,需要进一步的操作以完成请求
4**客户端错误,请求包含语法错误或无法完成请求
5**服务器错误,服务器在处理请求的过程中发生了错误
```

12、什么是HttpResponse?

```
HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)
content：表示返回的内容
status_code：返回的HTTP响应状态码(默认为200)
content_type：指定返回数据的的MIME类型(默认为"text/html")
```

13、HttpResponse 子类

```python
HttpResponseRedirect重定向302HttpResponseNotModified未修改304HttpResponseBadRequest错误请求400HttpResponseNotFound没有对应的资源404HttpResponseForbidden请求被禁止403HttpResponseServerError服务器错误500
```

14、GET处理

```python
GET请求动作，一般用于向服务器获取数据
能够产生GET请求的场景：
- 浏览器地址栏中输入URL,回车后
- <a href="地址?参数=值&参数=值">
- form表单中的method为get
GET请求方式中，如果有数据需要传递给服务器，通常会用查询字符串(Query String)传递    【注意：不要传递敏感数据】
服务器获取客户端请求GET请求提交的数据
request.GET['参数名']  # QueryDict
request.GET.get('参数名','默认值')
request.GET.getlist('参数名')
# mypage?a=100&b=200&c=300&b=400
# request.GET=QueryDict({'a':['100'], 'b':['200','400'], 'c':['300']})
# a = request.GET['a']
# b = request.GET['b']  # Error
```

15、POST处理

```
POST请求动作，一般用于向服务器提交大量数据
form 表单的name属性
在form表单控件提交数据时，会自动搜索本表单控件内部的子标签的name属性及相应的值，再将这些名字和值以键-值对的形式提交给action指定的服务器相关位置
服务器端接收参数
通过 request.method 来判断是否为POST请求
使用post方式接收客户端数据
request.POST['参数名']  # request.POST 绑定QueryDict
request.POST.get('参数名','')
request.POST.getlist('参数名')
```

16、对于表单请求：GET和POST的区别？

```
GET:提交的数据以查询字符串的方式填写到地址栏中，不适合提交大数据
POST:提交的数据放到请求体中，所以，表单通常采用POST提交
```

17、POST提交，url可以带查询字符串吗？

```
查询字符串是浏览器向服务器提交数据的一种方式，与采用何种请求方式无关
```

18、request.GET,获取查询字符串数据，request.POST，获取表单数据，两者的类型都是QueryDict,都是字典类型

19、模板的加载方式

​	1、通过 loader 获取模板,通过HttpResponse进行响应

```python
from django.template import loader
# 1.通过loader加载模板
t = loader.get_template("模板文件名")
# 2.将t转化为HTML字符串
html = t.render(字典数据)
# 3.用响应对象将转换的字符串内容返回给浏览器
return HttpResponse(html)
```

​	2、使用render()直接加载并响应模板

```python
from django.shortcuts import render
return render(request,'模板文件名', 字典数据)
```

20、模板的传参

​	1、使用 loader 加载模板

```python
t = loader.get_template('xxx.html')
html = t.render(字典数据)
return HttpResponse(html)
```

​	2、使用render加载模板

```python
return render(request,'xxx.html',字典数据)
```

21、什么是xss？什么是csrf?

```python
xss:cross-site-script,即跨站脚本
原理：将恶意HTML/JavaScript代码注入到受害用户浏览的网页上，从而达到攻击目的
反射型xss:
	定义：发出请求时，XSS代码出现在URL中，作为输入提交到服务器端，服务器端解析后响应，XSS代码随响应内容一起传回给浏览器，最后浏览器解析执行XSS代码。这个过程像一次反射，故叫反射型XSS
存储型xss:
	定义：提交的XSS代码会存储在服务器端（数据库，内存，文件系统等），其他用户请求目标页面时即被攻击
DOM xss:
	定义：DOM XSS的代码无需跟服务器交互，在前端直接触发攻击
    
如何防范：
	**防范XSS攻击的唯一方式就是转义**
import html
# 接收到浏览器发送的数据
content=request.POST['content']
# 在未提交到数据库之前先做转义
contentf=html.escape(content)
# 获取到转义前的数据
s=html.unescape(content)   
    
csrf:cross site request forgery 跨站请求伪造攻击
```

22、模板的标签

​	1、将一些服务器端的功能嵌入到模板中

​	2、if 标签

```
{% if 条件表达式1 %}
...
{% elif 条件表达式2 %}
...
{% elif 条件表达式3 %}
...
{% else %}
...
{% endif %}
```

​	3、for 标签

```
{% for 变量 in 可迭代对象 %}
    ... 循环语句
{% empty %}
    ... 可迭代对象无数据时填充的语句
{% endfor %}
```

​	4、内置变量 

```
forloop.counter    循环的当前迭代（从1开始索引）
forloop.counter0   循环的当前迭代（从0开始索引）
forloop.revcountercounter    值得倒序
forloop.revcounter0revcounter    值的倒序
forloop.first     如果这是第一次通过循环，则为真
forloop.last    如果这是最后一次循环，则为真
forloop.parentloop    当嵌套循环，parentloop 表示外层循环
```

23、过滤器

```
- 在变量输出时对变量的值进行处理
- 可以通过使用 过滤器来改变变量的输出显示。
{{ 变量|过滤器1:参数值1|过滤器2:参数值2 ... }}
lower    将字符串转换为全部小写
upper   将字符串转换为大写形式
safe    默认不对变量内的字符串进行html转义
add: "n"   将value的值增加 n
truncatechars:'n'    如果字符串字符多于指定的字符数量，那么会被截断。 截断的字符串将以可翻译的省略号序列（“...”）结尾。
```

24、模板的继承

​		定义父模板中的块 `block`标签

​		标识出哪些在子模块中是允许被修改的

​		block标签：在父模板中定义，可以在子模板中覆盖

```
{% block block_name %}
定义模板块，此模板块可以被子模板重新定义的同名块覆盖
{% endblock block_name %}
```

​		继承模板 `extends` 标签(写在模板文件的第一行)

​		子模板继承语法标签

​		{% extends '父模板名称' %}

```python
{% block block_name %}
子模板块用来覆盖父模板中 block_name 块的内容
{% endblock block_name %}
```

25、url 反向解析

```
url 反向解析是指在视图或模板中，用path定义的名称来查找或计算出相应的路由
path (route, views, name="别名")
path('page', views.page_view, name="page_url")
```

​		在模板中 ->通过url标签实现地址的反向解析

```
{% url '别名' %}
{% url '别名' '参数值1' '参数值2' %}
ex:
{% url 'pagen' '400' %}
{% url 'person' age='18' name='gxn' %}
```

​		在视图函数中 ->可调用 django中的 reverse 方法进行反向解析

```
from django.urls import reverse
reverse('别名', args=[], kwargs={})
ex:
print(reverse('pagen',args=[300]))
print(reverse('person',kwargs={'name':'xixi','age':18}))
```

26、查询数据

```
all()  查询全部记录,返回QuerySet查询对象  MyModel.objects.all()
get()  查询符合条件的单一记录  
filter()  查询符合条件的多条记录
exclude()  查询符合条件之外的全部记录
```

27、具体用法：

```python
1、all()方法

- 方法: all()
- 用法: MyModel.objects.all()
- 作用: 查询MyModel实体中所有的数据
  - 等同于
    - select * from tabel
- 返回值: QuerySet容器对象,内部存放 MyModel 实例
----------------------------------------------
2、查询返回指定列(字典表示)

- 方法: values('列1', '列2')
- 用法: MyModel.objects.values(...)
- 作用: 查询部分列的数据并返回

  - select 列1,列2 from xxx
- 返回值: QuerySet
  - 返回查询结果容器，容器内存字典，每个字典代表一条数据,
  - 格式为: {'列1': 值1, '列2': 值2}
----------------------------------------------------
3、查询返回指定列（元组表示)

- 方法:values_list('列1','列2')
- 用法:MyModel.objects.values_list(...)
- 作用:

  - 返回元组形式的查询结果
- 返回值: QuerySet容器对象,内部存放 `元组`

  - 会将查询出来的数据封装到元组中,再封装到查询集合QuerySet中
--------------------------------------------------------
4、排序查询

- 方法:order_by
- 用法:MyModel.objects.order_by('-列','列')
- 作用:
  - 与all()方法不同，它会用SQL 语句的ORDER BY 子句对查询结果进行根据某个字段选择性的进行排序
- 说明:
- ​ 默认是按照升序排序,降序排序则需要在列前增加'-'表示
--------------------------------------------------------
5、条件查询 - filter

- 方法: filter(条件)
MyModel.objects.filter(属性1=值1, 属性2=值2)

- 返回值:
  - QuerySet容器对象,内部存放 MyModel 实例
- 说明:
  - 当多个属性在一起时为"与"关系，即当`Books.objects.filter(price=20, pub="清华大学出版社")` 返回定价为20 `且` 出版社为"清华大学出版社"的全部图书
6、条件查询 - exclude

方法: exclude(条件)
MyModel.objects.exclude(条件)
返回不包含此 `条件` 的 全部的数据集
查询 `清华大学出版社，定价等于50` 以外的全部图书
books = Book.objects.exclude(pub="清华大学出版社", price=50)
for book in books:
    print(book)
-------------------------------------------------------
7、条件查询 - get
- 方法: get(条件)
- 语法:
  - MyModel.objects.get(条件)
- 作用：
  - 返回满足条件的唯一一条数据
- 说明:
  - 该方法只能返回一条数据
  - 查询结果多余一条数据则抛出,Model.MultipleObjectsReturned异常
  - 查询结果如果没有数据则抛出Model.DoesNotExist异常
```

28、查询谓词

```python
`__exact` : 等值匹配  Author.objects.filter(id__exact=1)
`__contains` : 包含指定值  Author.objects.filter(name__contains='w')
`__startswith` : 以 XXX 开始  
`__endswith` : 以 XXX 结束
`__gt` : 大于指定值  Author.objects.filer(age__gt=50)
`__gte` : 大于等于 
`__lt` : 小于
`__lte` : 小于等于
`__in` : 查找数据是否在指定范围内  Author.objects.filter(country__in=['中国','日本','韩国'])
`__range`: 查找数据是否在指定的区间范围内  Author.objects.filter(age__range=(35,50))
```

29、修改数据

```python
1、修改单个实体的某些字段值的步骤:
    1. 查
       - 通过 get() 得到要修改的实体对象
    2. 改
       - 通过 对象.属性 的方式修改数据 
    3. 保存
       - 通过 对象.save() 保存数据
    from bookstore.models import Book
    abook = Book.objects.get(id=10)
    abook.market_price = "10.5"
    abook.save()
2、通过 QuerySet 批量修改 对应的全部字段
    - 直接调用QuerySet的update(属性=值) 实现批量修改
    - 返回值：更新数据的数量
    # 将id大于3的所有图书价格定为0元
    books = Book.objects.filter(id__gt=3)
    books.update(price=0)
    # 将所有书的零售价定为100元
    books = Book.objects.all()
    books.update(market_price=100)
3、删除数据
	- 删除记录是指删除数据库中的一条或多条记录
	- 删除单个MyModel对象或删除一个查询结果集(QuerySet)中的全部对象都是调用 delete()方法
1.删除单个对象
- 步骤
  1. 查找查询结果对应的一个数据对象
  2. 调用这个数据对象的delete()方法实现删除
  3. **无需调用save()函数**
try:
    auth = Author.objects.get(id=1)
    auth.delete()
except:
    print(删除失败)
2.删除查询结果集
    - 查找查询结果集中满足条件的全部QuerySet查询集合对象
    - 调用查询集合对象的delete()方法实现删除
# 删除全部作者中，年龄大于65的全部信息
auths = Author.objects.filter(age__gt=65)
auths.delete()
```

30、删除数据

- 删除记录是指删除数据库中的一条或多条记录
- 删除单个MyModel对象或删除一个查询结果集(QuerySet)中的全部对象都是调用 delete()方法

```
1.删除单个对象
- 步骤
  1. 查找查询结果对应的一个数据对象
  2. 调用这个数据对象的delete()方法实现删除
  3. **无需调用save()函数**
try:
    auth = Author.objects.get(id=1)
    auth.delete()
except:
    print(删除失败)
2.删除查询结果集
    - 查找查询结果集中满足条件的全部QuerySet查询集合对象
    - 调用查询集合对象的delete()方法实现删除
# 删除全部作者中，年龄大于65的全部信息
auths = Author.objects.filter(age__gt=65)
auths.delete()
```

31、聚合查询

聚合查询是指对一个数据表中的一个字段的数据进行部分或全部进行统计查询,查bookstore_book数据表中的全部书的平均价格，查询所有书的总个数等,都要使用聚合查询

1、不带分组聚合

- 不带分组的聚合查询是指导将全部数据进行集中统计查询
- 聚合函数【需要导入】:
  - 导入方法: `from django.db.models import *`
  - 聚合函数: 
    - Sum, Avg, Count, Max, Min
- 语法: 

  - MyModel.objects.aggregate(结果变量名=聚合函数('列'))
- 返回结果:
  - 由 结果变量名和值组成的字典
  - 格式为:
    - `{"结果变量名": 值}

```python
# 得到所有书的平均价格
from bookstore.models import Book
from django.db.models import Avg
result = Book.objects.aggregate(myAvg=Avg('price'))
print("平均价格是:", result['myAvg'])
print("result=", result)  # {"myAvg": 58.2}

# 得到数据表里有多少本书
from django.db.models import Count
result = Book.objects.aggregate(mycnt=Count('title'))
print("数据记录总个数是:", result['mycnt'])
print("result=", result)  # {"mycnt": 10}
```

2、分组聚合

- 分组聚合是指通过计算查询结果中每一个对象所关联的对象集合，从而得出总计值(也可以是平均值或总和)，即为查询集的每一项生成聚合。

- 语法: 

  - QuerySet.annotate(结果变量名=聚合函数('列'))

- 用法步骤:

  1. 通过先用查询结果MyModel.objects.values 查找查询要分组聚合的列

     - MyModel.objects.values('列1', '列2')

       ```python
       pub_set = Book.objects.values('pub')
       print(pub_set)  # <QuerySet [{'pub': '清华大学出版社'}, {'pub': '清华大学出版社'}, {'pub_hou {'pub': '机械工业出版社'}, {'pub': '清华大学出版社'}]>
       ```

  2.通过返回结果的 QuerySet.annotate 方法分组聚合得到分组结果

  - QuerySet.annotate(名=聚合函数('列'))

  - 返回 QuerySet 结果集,内部存储结果的字典

    ```python
    pub_count_set = pub_set.annotate(myCount=Count('pub'))
    print(pub_count_set)  # <QuerySet [{'pub': '清华大学出版社', 'myCount': 7}, {'pub': '机械工业出版社', 'myCount': 3}]>
    ```

32、F对象

F对象在数据包 django.db.models 中，使用时需要先导入

`from django.db.models import F`

```python
from django.db.models import F
F('列名') 

- 一个 F() 对象代表了一个model的字段的值
- F对象通常是对数据库中的字段值在不加载到内存中的情况下直接在数据库服务器端进行操作

更新Book实例中所有的零售价涨10元
Book.objects.all().update(market_price=F('market_price')+10)
'UPDATE `bookstore_book` SET `market_price` = (`bookstore_book`.`market_price` + 10) 
# 以上做法好于如下代码
books = Book.objects.all()
for book in books:
    book.market_price=book.marget_price+10
    book.save()
    
对数据库中两个字段的值进行比较，列出哪儿些书的零售价高于定价?
from django.db.models import F
from bookstore.models import Book
books = Book.objects.filter(market_price__gt=F('price'))
'SELECT * FROM `bookstore_book` WHERE `bookstore_book`.`market_price` > (`bookstore_book`.`price`)
for book in books:
    print(book.title, '定价:', book.price, '现价:', book.market_price)
```

33、Q对象

- 当在获取查询结果集 使用复杂的逻辑或  `|` 、 逻辑非 `~` 等操作时可以借助于 Q对象进行操作
- 如: 想找出定价低于20元 或 清华大学出版社的全部书，可以写成

```
Book.objects.filter(Q(price__lt=20)|Q(pub="清华大学出版社"))
```

​	Q对象在 数据包 django.db.models 中。需要先导入再使用

```python
from django.db.models import Q
from django.db.models import Q
Q(条件1)|Q(条件2)  # 条件1成立或条件2成立
Q(条件1)&Q(条件2)  # 条件1和条件2同时成立
Q(条件1)&~Q(条件2)  # 条件1成立且条件2不成立
```

```python
from django.db.models import Q
# 查找清华大学出版社的书或价格低于50的书
Book.objects.filter(Q(market_price__lt=50) | Q(pub_house='清华大学出版社'))
# 查找不是机械工业出版社的书且价格低于50的书
Book.objects.filter(Q(market_price__lt=50) & ~Q(pub_house='机械工业出版社'))
```



**26、面试题**

1、什么是wsgi,uwsgi,uWSGI?

```
WSGI:Web Server Gateway Interface(web服务网关接口),是一套协议，用于接收用户请求并将请求初次封装，然后将请求交给Web框架
实现wsgi协议的模块，wsgiref，本质上就是编写-socket服务端，用于接收用户请求（django）
uwsgi:
与WSGI一样是一种通信协议，它是uWSGI服务器的独占协议，用于定义传输信息的类型。
uWSGI:
是一个web服务器，实现了WSGI的协议，uWSGI协议，http协议
```

2、简述Django请求生命周期

```
一般是用户通过浏览器向我们的服务器发起一个请求(request),这个请求会去访问视图函数，如果不涉及到数据调用，那么这个时候视图函数返回一个模板也就是一个网页给用户）视图函数调用模型去数据库查找数据，然后逐级返回，视图函数把返回的数据填充到模板中空格中，最后返回网页给用户。
1.wsgi ,请求封装后交给web框架（Flask，Django)
2.中间件，对请求进行校验或在请求对象中添加其他相关数据，例如：csrf,request.session
3.路由匹配 根据浏览器发送的不同url去匹配不同的视图函数
4.视图函数，在视图函数中进行业务逻辑的处理，可能涉及到：orm，templates
5.中间件，对响应的数据进行处理
6.wsgi，将响应的内容发送给浏览器
```

![image-20201117222828816](../图片/image-20201117222828816.png)

3、CORS 和 CSRF的区别？

```
什么是CORS？
CORS是一个W3C标准,全称是“跨域资源共享"(Cross-origin resoure sharing).
它允许浏览器向跨源服务器，发出XMLHttpRequest请求，从而客服了AJAX只能同源使用的限制。

什么是CSRF？						
CSRF主流防御方式是在后端生成表单的时候生成一串随机token,内置到表单里成为一个字段，同时，将此串token置入session中。每次表单提交到后端时都会检查这两个值是否一致，以此来判断此次表单提交是否是可信的，提交过一次之后，如果这个页面没有生成CSRF token,那么token将会被清空,如果有新的需求，那么token会被更新。攻击者可以伪造POST表单提交，但是他没有后端生成的内置于表单的token，session中没有token都无济于事。
```

**跨站请求伪造攻击( cross site request forgery) CSRF攻击示意图**

![image-20201118091418160](../图片/image-20201118091418160.png)

**4、简单说说看 Django的CSRF防御机制**

```
Django的CSRF保护主要是通过django.middleware.csrf.CsrfViewMiddleware中间件来实现的。主要流程如下:
Django 第一次响应来自某个客户端的get请求时，会在服务器端随机生成一个 csrftoken(一串64位的随机字符串)，把这个 token 放请求头的 cookie 里返回给用户。
所有通过POST方式提交的表单在渲染时中必须包含一个 csrfmiddlewaretoken 隐藏字段 （在模板中通过{% csrf_token %}标签生成)。
当用户通过POST提交表单时，Django会从请求头cookie取csrftoken这一项的值，再从POST表单里取csrfmiddlewaretoken交由中间件进行校验两者是否一致。如果一致表明这是一个合法请求，否则返回403 Forbidden.

注意csrftoken和csrfmiddlewaretoken并不是简单相等的两个字符串，而是通过算法判断是否一致相等的
```

 **5、Django中使用AJAX发送POST请求时如何通过CSRF认证？**

1. 第一种方式直接在发送数据中加入csrfmiddlewaretoken

```javascript
<script>
  $("#btn").on("click",function () {
        $.ajax({
            url:"/some_url/",
            type:"POST",
            data:{
                csrfmiddlewaretoken:{{ csrf_token }}, //写在模板中，才会被渲染
            },
            success:function (data) {
            }
        })
    })
</script>
```

2、通过jquery选择器获取csrfmiddlewaretoken

```javascript
<script>
  $("#btn").on("click",function () {
        $.ajax({
            url:"/some_url/",
            type:"POST",
            data:{
                csrfmiddlewaretoken:$('[name="csrfmiddlewaretoken"]').val(),
            },
            success:function (data) {
            }
        })
    })
</script>
```

3、使用jquery.cookie.js调用请求头cookie中的csrftoken

```javascript
<script src="/static/jquery.cookie.js"></script> //必须先引入它
<script>
    $("#btn").on("click",function () {
     $.ajax({
        url:"/some_url/",
        type:"POST",
        headers:{"X-CSRFToken":$.cookie('csrftoken')},
        data:$("#f1").serialize()
    }
    )
   })
</script>
```

**跨站脚本(XSS Cross-site Script)攻击示意图**

![image-20201117222555309](../图片/image-20201117222555309.png)

4、xss攻击都有哪些？

```
XSS全称是Cross Site Scripting即跨站脚本

反射型xss定义：发出请求时，XSS代码出现在URL中，作为输入提交到服务器端，服务器端解析后响应，XSS代码随响应内容一起传回给浏览器，最后浏览器解析执行XSS代码。这个过程像一次反射，故叫反射型XSS
以查询字符串形式提交 xss代码
http://127.0.0.1:8000/test_html?t=<script>alert(11)</script>
后端接到查询字符串的值后，显示在页面中
-----------------------------------------------------------
存储型xss
定义：提交的XSS代码会存储在服务器端（数据库，内存，文件系统等），其他用户请求目标页面时即被攻击
博客发表文章时，提交XSS代码，服务器存储代码后，其他用户访问该文章时，被XSS攻击
-----------------------------------------------------------
DOM xss
定义：DOM XSS的代码无需跟服务器交互，在前端直接触发攻击
地址栏提交#内容，例如-http://127.0.0.1:8000/test_html#javascript:alert(11)

页面中添加JS:
<script>
    var hash = location.hash;
    if(hash){
        var url = hash.substring(1);
        location.href = url;
    }
</script>
```

5、怎么防范？

```python
import html
# 接收到浏览器发送的数据
content=request.POST['content']
# 在未提交到数据库之前先做转义
contentf=html.escape(content)
# 获取到转义前的数据
s=html.unescape(content)
```

5、谈一下你对uWSGI和nginx的理解？

```
uWSGI是一个Web服务器，它实现了WSGI协议、uwsgi、http等协议。Nginx中HttpUwsgiModule的作用是与uWSGI服务器进行交换。WSGI是一种Web服务器网关接口。它是一个Web服务器（如nginx，uWSGI等服务器）与web应用（如用Flask框架写的程序）通信的一种规范。
要注意WSGI/uwsgi/uWSGI这三个概念的区分。
WSGI是一种通信协议。
uwsgi是一种线路协议而不是通信协议，在此常用于在uWSGI服务器与其他网络服务器的数据通信。
uWSGI是实现了uwsgi和WSGI两种协议的Web服务器。
nginx 是一个开源的高性能的HTTP服务器和反向代理：
1.作为web服务器，它处理静态文件和索引文件效果非常高
2.它的设计非常注重效率，最大支持5万个并发连接，但只占用很少的内存空间
3.稳定性高，配置简洁。
4.强大的反向代理和负载均衡功能，平衡集群中各个服务器的负载压力应用
```

6、**说说 nginx 和 uWISG 服务器之间如何配合工作的？**

```
首先浏览器发起 http 请求到 nginx 服务器，Nginx 根据接收到请求包，进行 url 分析,
判断访问的资源类型。如果是静态资源，直接读取静态资源返回给浏览器。
如果请求的是动态资源就转交给 uwsgi服务器。
uwsgi 服务器根据自身的uwsgi 和 WSGI 协议，找到对应的 Django 框架。
Django 框架下的应用进行逻辑处理后，将返回值发送到 uwsgi 服务器。
uwsgi 服务器再返回给 nginx，最后 nginx将返回值返回给浏览器进行渲染显示给用户。
```

![image-20201117224424745](../图片/image-20201117224424745.png)

7、**什么是中间件(middleware)，\**中间件(middleware)\**的应用场景**

```
中间件(Middleware)是一个镶嵌到django的request/response处理机制中的一个钩子(hooks) 框架。它是一个可以修改django全局输入或输出的一个底层插件系统。
一个请求HttpRequest在传递给视图View处理前要经过中间件处理，经过View处理后的响应也要经过中间件处理才能返回给用户。我们可以编写自己的中间件实现权限校验，限制用户请求、打印日志、改变输出内容等多种应用场景，比如：
```

8、**Django自带中间件介绍**

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #为request/response提供了几种安全改进，无它不安全
    'django.contrib.sessions.middleware.SessionMiddleware',
    #开启session会话支持，无它无session
    'django.middleware.common.CommonMiddleware',
    #基于APPEND_SLASH和PREPEND_WWW的设置来重写URL，如果APPEND_SLASH设为True，并且初始URL 没有以斜线结尾以及	在URLconf 中没找到对应定义，这时形成一个斜线结尾的新URL；如果PREPEND_WWW设为True，前面缺少 www.的url将会被重定向到相同但是以一个www.开头的url。
    'django.middleware.csrf.CsrfViewMiddleware',
    #添加跨站点请求伪造的保护，通过向POST表单添加一个隐藏的表单字段，并检查请求中是否有正确的值，无它无csrf保护
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #视图函数执行前向每个接收到的user对象添加HttpRequest属性，表示当前登录的用户，无它用不了request.user
    'django.contrib.messages.middleware.MessageMiddleware',
    #MessageMiddleware：开启基于Cookie和会话的消息支持，无它无message
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #XFrameOptionsMiddleware：对点击劫持的保护
]
```

9、**Django的中间件执行顺序**

```
当你在settings.py注册中间件时一定要要考虑中间件的执行顺序，中间件在request到达view之前是从上向下执行的，在view执行完后返回reponse过程中是从下向上执行的，如下图所示。举个例子，如果你自定义的中间件有依赖于request.user（比如判断用户是否登录)，那么你自定义的中间件一定要放在AuthenticationMiddleware的后面。
```

![image-20201117225312544](../图片/image-20201117225312544.png)

10、django中间件的使用？

Django在中间件中预置了六个方法，这六个方法的区别在于不同的阶段执行，对输入或输出进行干预，
方法如下：
1.初始化：无需任何参数，服务器响应第一个请求的时候调用一次，用于确定是否启用当前中间件

```python
def __init__():
	pass
```

2.处理请求前：在每个请求上调用，返回None或HttpResponse对象。

```python
def process_request(request):
	pass
```

3.处理视图前:在每个请求上调用，返回None或HttpResponse对象。

```python
def process_view(request,view_func,view_args,view_kwargs):
	pass
```

4.处理模板响应前：在每个请求上调用，返回实现了render方法的响应对象。

```python
def process_template_response(request,response):
	pass
```

5.处理响应后：所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象。

```python
def process_response(request,response):
	pass
```

6.异常处理：当视图抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象。

```python
def process_exception(request,exception):
	pass
```

![image-20201117225755051](../图片/image-20201117225755051.png)

10、**Django项目中什么时候使用中间件，什么时候使用装饰器？**

```
中间件和装饰器均广泛用于权限校验，缓存和日志。中间件对Django的输入或输出的改变是全局的，而装饰器一般只改变单个视图的输入输出。如果让你希望对Django的输入或输出做出全局性的改变时，需要使用中间件，否则使用装饰器。

举个例子，我们在装饰器一文中介绍了如何使用@login_required装饰器要求用户必须先登录才能访问我们的某个视图函数。试想我们有个网站绝大部分视图函数都需要用户登录，每个视图函数前面都需要加上@login_required装饰器是比较傻的行为。借助于中间件，我们无需使用装饰器即可全局实现：只有登录用户才能访问视图函数，匿名用户跳转到登录页面。实现原理也很简单，在一个request到达视图函数前，我们先对request.user是否验证通过进行判断，然后再进行跳转。
```

11、**post 和 get的区别?**

```
1.GET是从服务器上获取数据，POST是向服务器传送数据
2.在客户端，GET方式在通过URL提交数据，数据在URL中可以看到，POST方式，数据放置在HTML
——HEADER内提交
3.对于GET方式，服务器端用Request.QueryString获取变量的值，对于POST方式，服务器端用
Request.Form获取提交的数据
```

12、**什么是缓存Cache**

```
缓存是一类可以更快的读取数据的介质统称，也指其它可以加快数据读取的存储方式。一般用来存储临时数据，常用介质的是读取速度很快的内存。一般来说从数据库多次把所需要的数据提取出来，要比从内存或者硬盘等一次读出来付出的成本大很多。对于中大型网站而言，使用缓存减少对数据库的访问次数是提升网站性能的关键之一。
```

13、**为什么要使用缓存Cache**

```
在Django中，当用户请求到达视图后，视图会先从数据库提取数据放到模板中进行动态渲染，渲染后的结果就是用户看到的网页。如果用户每次请求都从数据库提取数据并渲染，将极大降低性能，不仅服务器压力大，而且客户端也无法即时获得响应。如果能将渲染后的结果放到速度更快的缓存中，每次有请求过来，先检查缓存中是否有对应的资源，如果有，直接从缓存中取出来返回响应，节省取数据和渲染的时间，不仅能大大提高系统性能，还能提高用户体验。
```

14、**缓存Cache的应用场景**

```
缓存主要适用于对页面实时性要求不高的页面。存放在缓存的数据，通常是频繁访问的，而不会经常修改的数据。我们来举几个应用例子:
博客文章。假设用户一天更新一篇文章，那么可以为博客设置1天的缓存，一天后会刷新。
购物网站。商品的描述信息几乎不会变化，而商品的购买数量需要根据用户情况实时更新。我们可以只选择缓存商品描述信息。
缓存网页片段。比如缓存网页导航菜单和脚部(Footer)。
```

15、**Django缓存设置**

```
数据库缓存
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
文件系统缓存
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',#这个是文件夹的路径
        #'LOCATION': 'c:\foo\bar',#windows下的示例
    }
}
本地内存缓存
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}
```

浏览器缓存分类？

```
强缓存
	不会向服务器发送请求，直接从缓存中读取资源
1,Expires
**缓存过期时间，用来指定资源到期的时间，是服务器端的具体的时间点**
**Expires 是 HTTP/1 的产物，受限于本地时间，如 果修改了本地时间，可能会造成缓存失效**
2, Cache-Control 
在HTTP/1.1中，Cache-Control主要用于控制网页缓存。比如当`Cache-Control:max-age=120  `代表请求创建时间后的120秒，缓存失效

协商缓存
	协商缓存就是强制缓存失效后，浏览器携带缓存标识向服务器发起请求，由服务器根据缓存标识决定是否使用缓存的过程
1、Last-Modified和If-Modified-Since
第一次访问时，服务器会返回 
Last-Modified: Fri, 22 Jul 2016 01:47:00 GMT
浏览器下次请求时 携带If-Modified-Since这个header , 该值为 Last-Modified
服务器接收请求后，对比结果，若资源未发生改变，则返回304， 否则返回200并将新资源返回给浏览器
缺点：只能精确到秒，容易发生单秒内多次修改，检测不到
2，ETag和If-None-Match
Etag是服务器响应请求时，返回当前资源文件的一个唯一标识(由服务器生成)，只要资源有变化，Etag就会重新生成

对比  Last-Modified VS  ETag  
1，精度不一样 -  Etag 高
2，性能上 - Last-Modifi 高
3，优先级 - Etag 高
```

**16、Django代码中如何使用Cache**

```
在视图View中使用cache
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def my_view(request):
    ...

在路由URLConf中使用cache
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('foo/<int:code>/', cache_page(60 * 15)(my_view)),
]

在模板中使用cache
{% load cache %}
{% cache 500 sidebar request.user.username %}
    .. sidebar for logged in user ..
{% endcache %}
```

18、**什么是基于函数的视图（FBV)和基于类的视图（CBV)以及各自的优点**

```
FBV（function base views） 就是在视图里使用函数处理请求。CBV（class base views） 就是在视图里使用类处理请求。Python是一个面向对象的编程语言，如果只用函数来开发，有很多面向对象的优点就错失了（继承、封装、多态）。所以Django在后来加入了Class-Based-View，可以让我们用类写View，这样做的优点主要下面两种：

提高了代码的复用性，可以使用面向对象的技术，比如Mixin（多继承）
可以用不同的函数针对不同的HTTP方法处理，而不是通过很多if判断，提高代码可读性

当然基于函数的视图也有自己的优点，比如对新手更友好。
```

19、Django网络应用开发的**5项基础核心技术**包括[模型（Model）的设计](http://mp.weixin.qq.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247483679&idx=2&sn=9e3db4167e408a2a0c3a1037c4f7266a&chksm=a73c6127904be831aee7abe13980fbea5e2d611ceb48e346dc0fc083c0a8725b52ebb3b8106f&scene=21#wechat_redirect)，[URL的设计与配置](http://mp.weixin.qq.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247483716&idx=2&sn=2c0ac2f977c063c67503a9ff3f8d4d0c&chksm=a73c617c904be86a16e7389c3d66760b86e06dd2f5f2f0f0ef6007b38d32647d8700e2a0a48a&scene=21#wechat_redirect)，View（视图）的编写，Template（模板）的设计和Form(表单)的使用。

20、**什么是View视图? Django的View是如何工作的**

```
Django的Web开发也遵循经典软件设计开发的MVC模式。View (视图) 主要根据用户的请求返回数据，用来展示用户可以看到的内容(比如网页，图片)，也可以用来处理用户提交的数据，比如保存到数据库中。Django的视图(View）通常和URL路由一起工作的。服务器在收到用户通过浏览器发来的请求后，会根据urls.py里的关系条目，去视图View里查找到与请求对应的处理方法，从而返回给客户端http页面数据。
```

21、Django如何处理一个URL对应的请求？

```python
浏览器  http://127.0.0.1:8000/page/2003/

1,Django 从配置文件中 根据 ROOT_URLCONF 找到 主路由文件；默认情况下，该文件在 项目同名目录下的urls; 例如 mysite1/mysite1/urls.py
2,Django 加载 主路由文件中的 urlpatterns 变量
3,依次匹配 urlpatterns 中的 URL， 匹配到第一个合适的中断后续匹配
4,匹配成功 - 调用对应的视图函数处理请求，返回响应
5,匹配失败 - 返回404响应
```

22、 **Django的优点和缺点有哪些?**

```
Django的优点:
1、功能完善、要素齐全：自带大量企业Web开发常用工具和框架（比如分页，auth，权限管理), 适合快速开发企业级网站。
2、完善的文档：经过十多年的发展和完善，Django有广泛的实践案例和完善的在线文档。开发者遇到问题时可以搜索在线文档寻求解决方案。
3、强大的数据库访问组件：Django的Model层自带数据库ORM组件，使得开发者无须学习SQL语言即可对数据库进行操作。
4、Django先进的App设计理念: App是可插拔的，是不可多得的思想。不需要了，可以直接删除，对系统整体影响不大。
自带台管理系统admin：只需要通过简单的几行配置和代码就可以实现一个完整的后台数据管理控制平台。

Django的缺点：
1、大包大揽: 对于一些轻量级应用不需要的功能模块Django也包括了，不如Flask轻便。
2、过度封装: 很多类和方法都封装了，直接使用比较简单，但改动起来就比较困难。
3、性能劣势: 与C, C++性能上相比，Django性能偏低，当然这是python的锅，其它python框架在流量上来后会有同样问题。
4、模板问题: django的模板实现了代码和样式完全分离，不允许模板里出现python代码，灵活度对某些程序员来说可能不够。
```

23、**说说看Django的Queryset有哪些特性**

Django的QuerySet主要有两个特性：一是惰性的(lazy)，二是自带缓存。我们来看个例子。

下例中article_list试图从数据库查询一个标题含有django的全部文章列表。

```
article_list = Article.objects.filter(title__contains="django")
```

但是当我们定义article_list的时候，Django的数据接口QuerySet并没有对数据库进行任何查询。无论你加多少过滤条件，Django都不会对数据库进行查询。只有当你需要对article_list做进一步运算时（比如打印出查询结果，判断是否存在，统计查询结果长度)，Django才会真正执行对数据库的查询(见下例1)。这个过程被称为queryset的执行(evaluation)。Django这样设计的本意是尽量减少对数据库的无效操作，比如查询了结果而不用是计算资源的很大浪费。

```python
# example 1
for article in article_list:
    print(article.title)
```

在例1中，当你遍历queryset(article_list)时，所有匹配的记录会从数据库获取。这些结果会载入内存并保存在queryset内置的cache中。这样如果你再次遍历或读取这个article_list时，Django就不需要重复查询了，这样也可以减少对数据库的查询。

24、**说说看使用基于类的视图(CBV)时get_queryset, get_context_data和get_object方法的作用**

**get_queryset()方法**

正如其名，该方法可以返回一个量身定制的对象列表。当我们使用Django自带的ListView展示所有对象列表时，ListView默认会返回Model.objects.all()。

```python
# Create your views here.
from django.views.generic import ListView
from .models import Article

class IndexView(ListView):

    model = Article
```

然而这可能不是我们所需要的。当我们希望只展示作者自己发表的文章列表且按文章发布时间逆序排列时，我们就可以通过更具体的get_queryset方法来返回一个我们想要显示的对象列表。

```python
# Create your views here.
from django.views.generic import ListView
from .models import Article
from django.utils import timezone

class IndexView(ListView):

    template_name = 'blog/article_list.html'
    context_object_name = 'latest_articles'

    def get_queryset(self):
        return Article.objects.filter(author = self.request.user).order_by('-pub_date')
```

25、**你能列举几个减少数据库查询次数的方法吗？**

```python
1、利用Django queryset的惰性和自带缓存的特性
2、使用select_related和prefetch_related方法在数据库层面进行Join操作
3、使用缓存
```

26、 **Django的模型继承有哪几种方式? 它们有什么区别以及何时使用它们?**【不懂啊】

```
Django的模型继承有如下3种方式:

1. 抽象模型继承(abstract model)
2. 多表模型继承(multi-table inheritance)
3. 代理模型(proxy model)

它们的区别如下:
1、Django不会为抽象模型在数据库中生成自己的数据表。父类Meta中的abstract=True也不会传递给子类。如果你发现多模型有很多共同字段时，需使用抽象模型继承。
2、多表模型继承与抽象模型继承最大的区别在于Django也会为父类模型建立自己的数据表，同时隐式地在父类和子类之间建立一个一对一关系。
3、如果我们只想改变某个模型的行为方法，而不是添加额外的字段或创建额外的数据表，我们就可以使用代理模型(proxy model)。设置一个代理模型，需要在子类模型Meta选项中设置proxy=True， Django不会为代理模型生成新的数据表。
```

27、**说说看如何自定义模型标签(templatetags)和过滤器(filter)?**

首先你要在你的app目录下新建一个叫templatetags的文件夹(不能取其它名字), 里面必需包含__init__.py的空文件。在该目录下你还要新建一个python文件专门存放你自定义的模板标签函数，本例中为blog_extras.py，当然你也可以取其它名字。整个目录结构如下所示:

```
blog/
   __init__.py
   models.py
   templatetags/
       __init__.py
       blog_extras.py
   views.py
```

在模板中使用自定义的模板标签时，需要先使用{% load blog_extras %}载入自定义的过滤器，然后通过{% tag_name %} 使用它。

example:我们将定义3个简单模板标签，一个返回string, 一个给模板context传递变量，一个显示渲染过的模板。我们在blog_extra.py里添加下面代码。

```python
from django import template
import datetime
from blog.models import Article

register = template.Library()

# use simple tag to show string
@register.simple_tag
def total_articles():
    return Article.objects.filter(status='p').count()

# use simple tag to set context variable
@register.simple_tag
def get_first_article():
    return Article.objects.filter(status='p').order_by('-pub_date')[0]

# show rendered template
@register.inclusion_tag('blog/latest_article_list.html')
def show_latest_articles(count=5):
    latest_articles = Article.objects.filter(status='p').order_by('-pub_date')[:count]
    return {'latest_articles': latest_articles, }
```

28、简单说说看**Django的CSRF防御机制**

```
Django的CSRF保护主要是通过django.middleware.csrf.CsrfViewMiddleware中间件来实现的。主要流程如下:
1、Django 第一次响应来自某个客户端的get请求时，会在服务器端随机生成一个 csrftoken(一串64位的随机字符串)，把这	 个 token 放请求头的 cookie 里返回给用户。
2、所有通过POST方式提交的表单在渲染时中必须包含一个 csrfmiddlewaretoken 隐藏字段 （在模板中通过{% csrf_token 	 %}标签生成)。
3、当用户通过POST提交表单时，Django会从请求头cookie取csrftoken这一项的值，再从POST表单里取csrfmiddlewaretoken交由中间件进行校验两者是否一致。如果一致表明这是一个合法请求，否则返回403 Forbidden.
注意csrftoken和csrfmiddlewaretoken并不是简单相等的两个字符串，而是通过算法判断是否一致相等的
```

29、**Django中使用AJAX发送POST请求时如何通过CSRF认证？**

1. 第一种方式直接在发送数据中加入csrfmiddlewaretoken

```javascript
<script>
  $("#btn").on("click",function () {
        $.ajax({
            url:"/some_url/",
            type:"POST",
            data:{
                csrfmiddlewaretoken:{{ csrf_token }}, //写在模板中，才会被渲染
            },
            success:function (data) {
            }
        })
    })
</script>
```

2.通过jquery选择器获取csrfmiddlewaretoken

```javascript
<script>
  $("#btn").on("click",function () {
        $.ajax({
            url:"/some_url/",
            type:"POST",
            data:{
                csrfmiddlewaretoken:$('[name="csrfmiddlewaretoken"]').val(),
            },
            success:function (data) {
            }
        })
    })
</script>
```

3. 使用jquery.cookie.js调用请求头cookie中的csrftoken

   ```javascript
   <script src="/static/jquery.cookie.js"></script> //必须先引入它
   <script>
       $("#btn").on("click",function () {
        $.ajax({
           url:"/some_url/",
           type:"POST",
           headers:{"X-CSRFToken":$.cookie('csrftoken')},
           data:$("#f1").serialize()
       }
       )
      })
   </script>
   ```

30、 如何从数据表中获取一个随机对象？

```python
def get_random_object():
    return MyModel.objects.order_by("?").first()
```

31、**说说看aggregate和annotate方法的作用并举几个例子**

```
aggregate的中文意思是聚合, 源于SQL的聚合函数。Django的aggregate()方法作用是对一组值(比如queryset的某个字段)进行统计计算，并以字典(Dict)格式返回统计计算结果。django的aggregate方法支持的聚合操作有AVG / COUNT / MAX / MIN /SUM 等。
annotate的中文意思是注释，一个更好的理解是分组(Group By)。如果你想要对数据集先进行分组然后再进行某些聚合操作或排序时，需要使用annotate方法来实现。与aggregate方法不同的是，annotate方法返回结果的不仅仅是含有统计结果的一个字典，而是包含有新增统计字段的查询集(queryset）
```

32、**Django中如何使用redis做缓存?**

```
安装好redis后，你需要安装django-redis才能在django中使用redis。django-redis安装命令如下:
pip install django-redis

settings.py中加入以下内容配置缓存。your_host_ip换成你的服务器地址,yourpassword换成你的服务器登陆密码。
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://your_host_ip:6379',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
             "PASSWORD": "yourpassword",
        },
    },
}
你还可以在settings.py设置缓存默认过期时间（非必须)
REDIS_TIMEOUT=7*24*60*60
```

33、**Django项目上传到代码库时是否需要忽略数据库迁移文件?**

```
数据库迁移文件位于每个app文件夹的migrations文件夹里，这些文件记录了模型的创建与改
动。每次当你创建模型或对模型字段进行修改，然后运行python manage.py
makemigrations命令时都会有新的迁移文件产生。Django官方文档特别说明这些迁移文件
属于Django项目代码中很重要的一部分，不应删除或忽略，所以建议上传。
```

34、**如何在模板中获取当前访问url地址**

```
在模板中你可以使用{{ request.path }}获取当前url，如果要获取带querystring的完整url你可以使用{{ request.get_full_path }}。如果你要获取完整绝对路径，你可以使用 {{ request.build_absolute_uri }}。具体使用方法如下所示:https://jackeygao.io/search/?keyword=django
request.path	/search/
request.get_full_path	search/?keyword=django
request.build_absolute_uri   https://jackeygao.io/search/?keyword=django
```

35、**使用F方法更新一个对象或多个对象的某个字段有什么优点?**

```
通常情况下我们在更新数据时需要先从数据库里将原数据取出后放在内存里，然后编辑某些字段或属性，最后提交更新数据库。使用F方法则可以帮助我们避免将所有数据先载入内存，而是直接生成SQL语句更新数据库。

假如我们需要对所有产品的价格涨20%，我们通常做法如下。当产品很少的时候，对网站性能没影响。但如果产品数量非常多，把它们信息全部先载入内存会造成很大性能浪费。
products = Product.objects.all()
for product in products:
    product.price *= 1.2
    product.save()
=====================================================================
使用F方法可以解决上述问题。我们直接可以更新数据库，而不必将所有产品载入内存。
from django.db.models import F
Product.objects.update(price=F('price') * 1.2)
=====================================================================
我们也可以使用F方法更新单个对象的字段，如下所示：
product = Product.objects.get(pk=5009)
product.price = F('price') * 1.2
product.save()
=====================================================================
但值得注意的是当你使用F方法对某个对象字段进行更新后，需要使用refresh_from_db()方法后才能获取最新的字段信息（非常重要！)。如下所示
product.price = F('price') + 1
product.save()
print(product.price)            # <CombinedExpression: F(price) + Value(1)>
product.refresh_from_db()
print(product.price)            # Decimal('13.00')
```

36、**说说 nginx 和 uWISG 服务器之间如何配合工作的？**

```
首先浏览器发起 http 请求到 nginx 服务器，Nginx 根据接收到请求包，进行 url 分析,
判断访问的资源类型。如果是静态资源，直接读取静态资源返回给浏览器。
如果请求的是动态资源就转交给 uwsgi服务器。
uwsgi 服务器根据自身的uwsgi 和 WSGI 协议，找到对应的 Django 框架。
Django 框架下的应用进行逻辑处理后，将返回值发送到 uwsgi 服务器。
uwsgi 服务器再返回给 nginx，最后 nginx将返回值返回给浏览器进行渲染显示给用户。
```

37、**说说看Django信号(Signals)的工作原理, 主要应用场景及内置信号**

```
Django 提供一个了“信号分发器”机制，允许解耦的应用在框架的其它地方发生操作时会被通知到。 通俗而讲Django信号的工作原理就是当某个事件发生的时候会发出一个信号(signals), 而监听这个信号的函数(receivers)就会立即执行。Django信号的应用场景很多，尤其是用于不同模型或程序间的联动。常见例子包括创建User对象实例时创建一对一关系的UserProfile对象实例，或者每当用户下订单时触发给管理员发邮件的动作。
```

38、**什么是中间件(middleware)，\**中间件(middleware)\**的应用场景**

```
中间件(Middleware)是一个镶嵌到django的request/response处理机制中的一个钩子(hooks) 框架。它是一个可以修改django全局输入或输出的一个底层插件系统。

一个请求HttpRequest在传递给视图View处理前要经过中间件处理，经过View处理后的响应也要经过中间件处理才能返回给用户。我们可以编写自己的中间件实现权限校验，限制用户请求、打印日志、改变输出内容等多种应用场景，比如：

禁止特定IP地址的用户或未登录的用户访问我们的View视图函数
对同一IP地址单位时间内发送的请求数量做出限制
在View视图函数执行前记录用户的IP地址
在View视图函数执行前传递额外的变量或参数
在View视图函数执行前或执行后把特定信息打印到log日志
在View视图函数执行后对reponse数据进行修改后返回给用户
```

39、**Django项目如何实现高并发？**

```
可以从如下几个角度讲:
使用nginx进行反向代理和负载均衡
数据库分库和读写分离(含主从复制)
使用nosql数据库比如redis缓存热点数据
耗时任务（比如发邮件或写入操作)交由celery异步处理
使用Gzip或django-compressor压缩静态文件
使用CDN加速静态文件访问
```

40、**什么是wsgi,uwsgi,uWSGI？**

```
WSGI (Web Server Gateway Interface)
Web服务器网关接口,是一套协议。用于接收用户请求并将请求进行初次封装，然后将请求交给web框架。实现wsgi协议的模块有：
1.wsgiref,本质上就是编写一个socket服务端，用于接收用户请求(django)
2.werkzeug,本质上就是编写一个socket服务端，用于接收用户请求(flask)

uwsgi:
与WSGI一样是一种通信协议，它是uWSGI服务器的独占协议,用于定义传输信息的类型

uWSGI:
是一个web服务器,实现了WSGI协议,uWSGI协议,http协议,
```

41、**列举5个常用的Django第三方库**

```
答案不限于：
第三方社交登录: django-allauth
过滤器: django-filter
富文本编辑器：ckeditor
调试debug工具: django-debug-toolbar
快速生成可以用于生产环境的项目目录：cookiecutter
API工具：django rest framework
```

#### 2.Ajax

1、什么是AJAX?优点？使用场合

```
Asynchronous Javascript And Xml
AJAX优点：
    1.异步访问
    2.局部刷新
使用场合：
    1.搜索建议
    2.表单验证
    3.前后端分离
```

2、什么是XMLHttpRequest [简称为 xhr]

```
称为 "异步对象"，代替浏览器向服务器发送异步的请求并接收响应
```

3、jquery如何操作ajax

$.ajax({})

```javascript
参数对象中的属性：
	1.url : 字符串，表示异步请求的地址
	2.type : 字符串，请求方式，GET 或 POST
	3.data : 传递到服务器端的参数[服务器相应给浏览器的数据]
    可以是字符串 ："name=sf.zh&age=18"
		也可以是js对象:
			{
				name:"sf.zh",
				age:18
			}
	4.dataType : 字符串，响应回来的数据的格式
		1.'html'
		2.'xml'
		3.'text' 
		4.'script'
		5.'json'
		6.'jsonp' : 有关跨域的响应格式
	5.success:回调函数，请求和响应成功时回来执行的操作
	6.error : 回调函数，请求或响应失败时回来执行的操作
	7.beforeSend : 回调函数，发送ajax请求之前执行的操作，如果return false，则终止请求
    8.contentType : 当有请求体有数据提交时，标明提交方式，默认值为'application/x-www-form-urlencoded; charset=UTF-8'
```

4、什么是JSON?

```
JavaScript Object Notation 是一种轻量级的数据交换格式
```

5、后台处理JSON

```
1.后台先获取数据
类型允许为：元组|列表|字典
2.在后台将数据转换为符合JSON格式的字符串
3.在后台将JSON格式的字符串进行响应
```

6、Python中的JSON处理？

```python
import json
#序列化-python对象变为json字符串
json_str = json.dumps(元组|列表|字典)
#反序列化-json字符串变为python对象
py_obj = json.loads(json_str)
```

7、Django中的JSON处理

```python
#方法1 使用Django中提供的序列化类来完成QuerySet到JSON字符串的转换
from django.core import serializers
json_str = serializers.serialize('json',QuerySet)
return HttpResponse(json_str)
#方法2
#如果第一个参数是字典类型，不用写第二个参数；
#如果第一个参数是非字典类型，例如：列表元组，第二个参数safe的值设置为False.

d = {'a': 1}
return JsonResponse(d)
```

8、前端中的JSON处理

```javascript
#序列化
JSON字符串JSON.stringify(JSON对象)

#反序列化
JSON对象=JSON.parse(JSON字符串)
```

9、什么是跨域？

```
跨域：非同源的网页，相互发送请求的过程，就是跨域
浏览器的同源策略：
同源：多个地址中，相同协议，相同域名，相同端口被视为是"同源"
在HTTP中，必须是同源地址才能互相发送请求，非同源拒绝请求(<script>和<img>除外)。
```

10、解决方案？

```
通过 <script> 向服务器资源发送请求
由服务器资源指定前端页面的哪个js方法来执行响应的数据
```

11、jquery 的跨域

```javascriptjava
jsonp - json with padding
用户传递一个callback参数给服务端，然后服务端返回数据时会将这个callback参数作为函数名来包裹住JSON数据

ex:
	当前地址： http://127.0.0.1:8000/index
    欲访问地址： http://localhost:8000/data?callback=xxx

	$.ajax({
		url:'xxx',
		type:'get',
		dataType:'jsonp',//指定为跨域访问
		jsonp:'callback',//定义了callback的参数名，以便获取callback传递过去的函数名
		jsonpCallback:'xxx' //定义jsonp的回调函数名
	});

	$.ajax({
		url:'xxx',
		type:'get',
		dataType:'jsonp',//指定为跨域访问
        success: function(data){
            #jquery会自动将后端接收过来的json数据转换为javascript对象
            #前端处理对象即可
        }
	});
```



#### 3.前后端分离

1、什么是前后端分离？

```
前端： 即客户端，负责渲染用户显示界面【如web的js动态渲染页面, 安卓， IOS，pc客户端等】
后端：即服务器端，负责接收http请求，处理数据
API：Application Programming Interface  是一些预先定义的函数，或指软件系统不同组成部分衔接的约定
前后端分离 完整请求过程
1，前端通过http请求后端API
2，后端以json形式返回前端数据
3，前端生成用户显示界面【如html , ios , android】
```

2、优点？

```
1，各司其职
前端：视觉层面，兼容性，前端性能优化
后端：并发，可用性，性能
2，前端可以有效利用客户端处理数据，有效降低服务端压力
3，服务端错误不会直观的反馈到用户
4，后端灵活搭配各类前端 - 如安卓等
5，前端+后端可完全并行开发，加快开发效率
```

3、什么是cookies?session?token?

```
cookie 是一个非常具体的东西，指的就是浏览器里面能永久存储的一种数据，仅仅是浏览器实现的一种数据存储功能。
cookie由服务器生成，发送给浏览器，浏览器把cookie以kv形式保存到某个目录下的文本文件内，下一次请求同一网站时会把该cookie发送给服务器。由于cookie是存在客户端上的，所以浏览器加入了一些限制确保cookie不会被恶意使用，同时不会占据太多磁盘空间，所以每个域的cookie数量是有限的。
=======================================================================================================
session 从字面上讲，就是会话。这个就类似于你和一个人交谈，你怎么知道当前和你交谈的是张三而不是李四呢？对方肯定有某种特征（长相等）表明他就是张三。
session 也是类似的道理，服务器要知道当前发请求给自己的是谁。为了做这种区分，服务器就要给每个客户端分配不同的“身份标识”，然后客户端每次向服务器发请求的时候，都带上这个“身份标识”，服务器就知道这个请求来自于谁了。至于客户端怎么保存这个“身份标识”，可以有很多种方式，对于浏览器客户端，大家都默认采用 cookie 的方式。
服务器使用session把用户的信息临时保存在了服务器上，用户离开网站后session会被销毁。这种用户信息存储方式相对cookie来说更安全，可是session有一个缺陷：如果web服务器做了负载均衡，那么下一个操作请求到了另一台服务器的时候session会丢失。
=======================================================================================================
在Web领域基于Token的身份验证随处可见。在大多数使用Web API的互联网公司中，tokens 是多用户下处理认证的最佳方式。
以下几点特性会让你在程序中使用基于Token的身份验证：
    无状态、可扩展
    支持移动设备
    跨程序调用
    安全
```

#### cookies

1、cookies是保存在客户端浏览器上的存储空间

2、**cookies** 在浏览器上是以**键-值对**的形式进行存储的，键和值都是以**ASCII字符串**的形存储(**不能是中文字符串**)

3、cookies中的数据是**按域存储隔离**的，不同的域之间无法访问

4、cookies 的内部的数据会在每次访问此网址时都会携带到服务器端，如果cookies过大会降低响应速度,cookie的数据，在向服务器发送请求时，客户端浏览器会**自动提交**

#### session 

1、session又名会话控制，是在服务器上开辟一段空间用于保留浏览器和服务器交互时的重要数据

2、实现方式：

​	1.使用 session 需要在浏览器客户端启动 cookie，且用在cookie中存储sessionid

​	2.每个客户端都可以在服务器端有一个独立的Session

​	3.注意：不同的请求者之间不会共享这个数据，与请求者一一对应

3、session存储的过程？

```
首先在django_session表中，存储了key_value,并且将sessionid(对应django_session表中的session_key)使用cookies存储到客户端
下一次提交，浏览器带着sessionid，就可以使用sessionid查询数据库，得到session中保存过的数据
```

4、为什么会出现？

```
- 会话 - 从打开浏览器访问一个网站，到关闭浏览器结束此次访问，称之为一次会话
- HTTP协议是无状态的，导致会话状态难以保持
- 试想一下，如果不保持会话状态，在电商网站购物的场景
  体验？

Cookies和Session就是为了保持会话状态而诞生的两个存储技术
```

![image-20201020144745741](../图片/image-20201020144745741.png)

#### token

```
基于服务器的验证：
我们都是知道HTTP协议是无状态的，这种无状态意味着程序需要验证每一次请求，从而辨别客户端的身份。
在这之前，程序都是通过在服务端存储的登录信息来辨别请求的。这种方式一般都是通过存储Session来完成。
随着Web，应用程序，已经移动端的兴起，这种验证的方式逐渐暴露出了问题。尤其是在可扩展性方面。

基于服务器验证方式暴露的一些问题：
Seesion：每次认证用户发起请求时，服务器需要去创建一个记录来存储信息。当越来越多的用户发请求时，内存的开销也会不断增加。
可扩展性：在服务端的内存中使用Seesion存储登录信息，伴随而来的是可扩展性问题。
CORS(跨域资源共享)：当我们需要让数据跨多台移动设备上使用时，跨域资源的共享会是一个让人头疼的问题。在使用Ajax抓取另一个域的资源，就可以会出现禁止请求的情况。
CSRF(跨站请求伪造)：用户在访问银行网站时，他们很容易受到跨站请求伪造的攻击，并且能够被利用其访问其他的网站。

基于Token的验证原理：
基于Token的身份验证是无状态的，我们不将用户信息存在服务器或Session中。
基于Token的身份验证的过程如下:
1、用户通过用户名和密码发送请求。
2、程序验证。
3、程序返回一个签名的token 给客户端。
4、客户端储存token,并且每次用于每次发送请求。
5、服务端验证token并返回数据。
每一次请求都需要token。token应该在HTTP的头部发送从而保证了Http请求无状态。我们同样通过设置服务器属性Access-Control-Allow-Origin:* ，让服务器能接受到来自所有域的请求。
需要主要的是，在ACAO头部标明(designating)*时，不得带有像HTTP认证，客户端SSL证书和cookies的证书。

Tokens的优势：
无状态、可扩展：
在客户端存储的Tokens是无状态的，并且能够被扩展。基于这种无状态和不存储Session信息，负载负载均衡器能够将用户信息从一个服务传到其他服务器上。
如果我们将已验证的用户的信息保存在Session中，则每次请求都需要用户向已验证的服务器发送验证信息(称为Session亲和性)。用户量大时，可能会造成一些拥堵。
但是不要着急。使用tokens之后这些问题都迎刃而解，因为tokens自己hold住了用户的验证信息。
安全性：
请求中发送token而不再是发送cookie能够防止CSRF(跨站请求伪造)。即使在客户端使用cookie存储token，cookie也仅仅是一个存储机制而不是用于认证。不将信息存储在Session中，让我们少了对session操作。
token是有时效的，一段时间之后用户需要重新验证。我们也不一定需要等到token自动失效，token有撤回的操作，通过token revocataion可以使一个特定的token或是一组有相同认证的token无效。
可扩展性：
Tokens能够创建与其它程序共享权限的程序。例如，能将一个随便的社交帐号和自己的大号(Fackbook或是Twitter)联系起来。当通过服务登录Twitter(我们将这个过程Buffer)时，我们可以将这些Buffer附到Twitter的数据流上(we are allowing Buffer to post to our Twitter stream)。
使用tokens时，可以提供可选的权限给第三方应用程序。当用户想让另一个应用程序访问它们的数据，我们可以通过建立自己的API，得出特殊权限的tokens。
多平台跨域：
我们提前先来谈论一下CORS(跨域资源共享)，对应用程序和服务进行扩展的时候，需要介入各种各种的设备和应用程序。
Having our API just serve data, we can also make the design choice to serve assets from a CDN. This eliminates the issues that CORS brings up after we set a quick header configuration for our application.
只要用户有一个通过了验证的token，数据和资源就能够在任何域上被请求到。
Access-Control-Allow-Origin: *      
基于标准创建token的时候，你可以设定一些选项。我们在后续的文章中会进行更加详尽的描述，但是标准的用法会在JSON Web Tokens体现。
```



![image-20201103100917384](../图片/image-20201103100917384.png)

5、什么是JWT(json-web-token)?

```
三大组成：
1、header
{'alg':'HS256', 'typ':'JWT'}
#alg代表要使用的 算法
#typ表明该token的类别 - 此处必须为 大写的 JWT/该部分数据需要转成json串并用base64 加密
2、payload
公共声明：
	{
	'exp':xxx, # Expiration Time 此token的过期时间的时间戳
 	'iss':xxx，# (Issuer) Claim 指明此token的签发者
 	'aud':xxx, #(Audience) Claim 指明此token的
 	'iat':xxx, # (Issued At) Claim 指明此创建时间的时间戳
 	'aud':xxx, # (Audience) Claim	指明此token签发面向群体
	}此部分均为**可选项**，用户根据自己需求 按需添加key
私有声明：用户可根据自己业务需求，添加自定义的key：
	{'username': 'guoxiaonao'}/公共声明和私有声明均在同一个字典中；转成json串并用base64加密
3、signature 签名【可以认为是消息验证码】
签名规则如下：
	根据header中的alg确定 具体算法，以下用 HS256为例
	HS256(自定义的key ,   base64后的header + '.' + base64后的payload)
	解释：用自定义的key, 对base64后的header + '.' + base64后的payload进行hmac计算
```

6、pyjwt?

```
encode(payload, key, algorithm)
payload/jwt三大组成中的payload,需要组成字典，按需添加公有声明和私有声明/字典格式
key : 自定义的加密key/str类型
algorithm:  需要使用的加密算法HS256/str类型
返回值：token串/返回类型：bytes
==========================================================================
decode(token,key,algorithm)
token:token串/bytes/str类型
key : 自定义的加密key ,需要跟encode中的key保持一致/str类型
algorithm:  同encode
返回值：payload明文/dict类型
```

7、什么是跨域资源共享？

```
Cross-origin resource sharing
允许浏览器向跨源(协议 + 域名 + 端口)服务器，发出XMLHttpRequest请求，从而克服了AJAX只能同源使用的限制
1，浏览器自动完成（在请求头中加入特殊头 或 发送特殊请求）
2，服务器需要支持（响应头中需要有特殊头）
```

8、什么是RESTful？

```
资源（Resources）表现层（Representation）状态转化（State Transfer）
1，每一个URI代表一种资源
2，客户端和服务器端之前传递着资源的某种表现
3，客户端通过HTTP的几个动作 对 资源进行操作 - 发生‘状态转化’
```

9、URI和URL的区别：

```
URI，通一资源标志符(Uniform Resource Identifier， URI)，表示的是web上每一种可用的资源，如 HTML文档、图像、视频片段、程序等都由一个URI进行标识的。
URL是URI的一个子集。它是Uniform Resource Locator的缩写，译为“统一资源定位 符”。
URI和URL都定义了资源是什么，但URL还定义了该如何访问资源。URL是一种具体的URI，它是URI的一个子集，它不仅唯一标识资源，而且还提供了定位该资源的信息。URI 是一种语义上的抽象概念，可以是绝对的，也可以是相对的，而URL则必须提供足够的信息来定位，是绝对的。
```

10、HTTP动词语义？

```
- GET（SELECT）：从服务器取出资源（一项或多项）。
- POST（CREATE）：在服务器新建一个资源。
- PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）。
- PATCH（UPDATE）：在服务器更新资源（客户端提供改变的属性）。
- DELETE（DELETE）：从服务器删除资源。
```

#### 4、celery

1、创建项目+应用

```
django-admin startproject test_celery
python manage.py startapp user
```

2、在settings同目录下创建celery.py

```python
from celery import Celery
from django.conf import settings
import os

# 为celery设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_celery.settings')
# 创建应用
app = Celery("test_celery")

# 配置应用
app.conf.update(
    # 配置broker
    BROKER_URL='redis://:@127.0.0.1:6379/1',)

# 设置app自动加载任务
app.autodiscover_tasks(settings.INSTALLED_APPS)
```

3、在应用模块【user目录下】创建tasks.py文件

```python
from test_celery.celery import app
import time

@app.task
def task_test():
    print("task begin....")
    time.sleep(10)
    print("task over....")
```

4、视图函数编写

```python
from django.http import HttpResponse
from .tasks import task_test
import datetime

def test_celery(request):
    task_test.delay()
	now = datetime.datetime.now()
    html = "return at %s"%(now.strftime('%H:%M:%S'))
    return HttpResponse(html)
```

5、分布式路由下添加 test_celery函数对应路由，此过程略

6、启动django   python3 manage.py runserver

7、创建 celery worker

在项目路径下，即test_celery 下  执行如下

```
celery -A test_celery worker -l info
```

8、浏览器中执行对应url

9、定时任务

```python
from celery.schedules import crontab

app.conf.update(
    CELERYBEAT_SCHEDULE = {
        'sum-task': {
            'task': 'deploy.tasks.add',
            'schedule':  timedelta(seconds=20),
            'args': (5, 6)
        }
        'send-report': {
            'task': 'deploy.tasks.report',
            'schedule': crontab(hour=4, minute=30, day_of_week=1),
        }
    }
)
```

- 定义了两个task：

- - 名字为'sum-task'的task，每20秒执行一次add函数，并传了两个参数5和6
  - 名字为'send-report'的task，每周一早上4：30执行report函数

- timedelta是datetime中的一个对象，需要`from datetime import timedelta`引入，有如下几个参数

- - `days`：天
  - `seconds`：秒
  - `microseconds`：微妙
  - `milliseconds`：毫秒
  - `minutes`：分
  - `hours`：小时

- crontab的参数有：

- - `month_of_year`：月份
  - `day_of_month`：日期
  - `day_of_week`：周
  - `hour`：小时
  - `minute`：分钟

10、task.py文件中添加report方法

```
@shared_task
def report():
    return 5
```

11、启动celery beat，celery启动了一个beat进程一直在不断的判断是否有任务需要执行

```
# celery -A website beat -l info
```

###### 12、Tips

1. 如果你同时使用了异步任务和计划任务，有一种更简单的启动方式`celery -A website worker -b -l info`，可同时启动worker和beat

2. 如果使用的不是rabbitmq做队列那么需要在主配置文件中`website/celery.py`配置broker和backend，如下

   ```python
   # redis做MQ配置
   app = Celery('website', backend='redis', broker='redis://localhost')
   # rabbitmq做MQ配置
   app = Celery('website', backend='amqp', broker='amqp://admin:admin@localhost')
   ```

3、celery不能用root用户启动的话需要在主配置文件中添加`platforms.C_FORCE_ROOT = True`

4、celery在长时间运行后可能出现内存泄漏，需要添加配置`CELERYD_MAX_TASKS_PER_CHILD = 10`，表示每个worker执行了多少个任务就死掉



1、Django 创建项目后，项目文件夹下的组成部分（对mvt 的理
解）？

```
项目文件夹下的组成部分：
manage.py 是项目运行的入口，指定配置文件路径。
与项目同名的目录，包含项目的配置文件
___init.py 是一个空文件，作用是这个目录可以被当作包使用。
settings.py 是项目的整体配置文件。
urls.py 是项目的URL 配置文件。
wsgi.py 是项目与WSGI 兼容的Web 服务器入口
```

13、**Django项目中什么时候使用中间件，什么时候使用装饰器？**

```
中间件和装饰器均广泛用于权限校验，缓存和日志。中间件对Django的输入或输出的改变是全局的，而装饰器一般只改变单个视图的输入输出。如果让你希望对Django的输入或输出做出全局性的改变时，需要使用中间件，否则使用装饰器。

举个例子，我们在装饰器一文中介绍了如何使用@login_required装饰器要求用户必须先登录才能访问我们的某个视图函数。试想我们有个网站绝大部分视图函数都需要用户登录，每个视图函数前面都需要加上@login_required装饰器是比较傻的行为。借助于中间件，我们无需使用装饰器即可全局实现：只有登录用户才能访问视图函数，匿名用户跳转到登录页面。实现原理也很简单，在一个request到达视图函数前，我们先对request.user是否验证通过进行判断，然后再进行跳转。
```

14、**列举5个常用的Django第三方库**

```
第三方社交登录: django-allauth
过滤器: django-filter
富文本编辑器：ckeditor
调试debug工具: django-debug-toolbar
快速生成可以用于生产环境的项目目录：cookiecutter
API工具：django rest framework

1、django-allauth - 用户注册登录管理
2、django-haystack - 全文检索引擎
3、django-ckeditor - 富文本编辑器
4、django-imagekit - 自动化处理图像
5、django-crispy-forms - 快速美化django表单首选
6、django-debug-toolbar - django项目调试利器
7、django-celery - 执行异步任务或定时任务的最佳选择
8、django-rest-framework开发REST API的最佳工具
9、django-xadmin - 更美观更强大的后台
10、django-constance - 常量管理
```

15、django重定向？

**HttpResponseDirect方法**

```
HttpResponseRedirect是django首选的URL重定向方法，在django.http模块里。该方法的第一个参数是必要的，是用来重定向的URL地址。这个URL可以是完整的链接（比如’http://www.baidu.com‘），也可以是一个不包含域名的静态链接（例如‘/index/’）。
```

1. 在视图views.py中利用HttpResponse重新定向至不含参数的URL

   ```
   return HttpResponseRedirect("/index/")
   如果/index/页面有分页功能， 你还可以通过使用HttpResponseRedirect('/index/?page=2')直接获取第2页的文章列表。
   ```

**HttpReponseDirect只支持hard coded urls(硬编码链接), 不能直接使用命名的URL，如使用HttpResponseDirect('blog:article_list‘)是错误的。**在使用URL命名时，我们需要先通过URL反向解析方法reverse先对命名URL(article_list)进行解析，然后再使用HttpReponseRedirect定向(如下面的代码)。背后的逻辑是reverse('blog:article_list')='/index/'。

2.在视图views.py中利用HttpResponseDirect重新定向至包含参数的URL

```
return HttpResponseRedirect(reverse('blog:article_detail', args=[str(article.pk), article.slug]))
```

**redirect方法**

redirect是URL重新定向的便捷方法，在django.shortcuts模块里。**HttpResponseRedirect能支持的URL重定向，redirect都支持。**比如下面3种重定向是redirect的常规用法。

```
1、return redirect('/index/')
2、return redirect('https://www.baidu.com/')
3、return redirect(reverse('blog:article_list'))
```

**redirect真正NB的地方在于，它不仅能根据URL重定向，还可以根据对象Object重定向和根据视图view重定向**，根据视图重定向的时候还可以传递额外的参数。

1. 根据对象Object重定向

   ```
   def my_view(request):
       ...
       obj = MyModel.objects.get(...)
       return redirect(obj)
   ```

2. 根据视图view重定向

   使用该方法的前提已对URL进行了命名，且对应了相应的视图。下面案例中redirect会先根据视图函数的名字查找对应url，在传递额外参数。后台工作还是由reverse方法来完成的。

   ```
   def my_view(request):
       ...
       return redirect('some-view-name', foo='bar')
   ```

   **reverse方法**

   reverse方法的作用是对已命名的URL进行反向解析，还传递相应的参数（args或带key的参数kargs)。该方法位于django.urls模块。reverse方法一般有2种应用场景:

   - 在模型中自定义get_absolute_url时使用，传递参数
   - 在视图中对命名URL进行解析，传递参数，再使用HttpResponseDirect和redict进行重定向

   1. 模型中自定义get_absolute_url，并传递参数args

      ```
      def get_absolute_url(self):
          return reverse('blog:article_detail', args=[str(self.pk), self.slug])
      ```

   2. 在视图中配合URL重定向使用，并传递kargs

      ```
      from django.urls import reverse
      from django.shortcuts import redirect
       
      def my_view(request):
          ...
          return redirect(reverse('admin:app_list', kwargs={'app_label': 'auth'}))
      ```

      

## 4.爬虫

1、什么是网络爬虫？爬虫分类？

```
1、网络蜘蛛、网络机器人，抓取网络数据的程序
2、其实就是用Python程序模仿人点击浏览器并访问网站，而且模仿的越逼真越好
============================
1、通用网络爬虫(搜索引擎使用,遵守robots协议)
https://www.baidu.com/robots.txt
2、聚焦网络爬虫 ：自己写的爬虫程序
```

2、爬虫的常用方法？

```
1、request.get(url,headers,timeout)向目标网站发起请求,并获取响应对象
响应对象属性
    text:字符串
    content:字节流
    status_code：HTTP响应码
    url:实际数据的URL地址
2、request.post()
	参数：data
```

3、爬虫编码模块

​	**urllib.parse模块**

```python
import urllib.parse
from urllib import parse
```

###### 	常用方法urlencode({参数为字典})

```python
import requests
from urllib import parse

# 1. 拼接URL地址
word = input('请输入搜索关键字:')
params = parse.urlencode({'wd':word})
url = 'http://www.baidu.com/s?{}'.format(params)

# 2. 发请求获取响应内容
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
html = requests.get(url=url, headers=headers).text

# 3. 保存到本地文件
filename = '{}.html'.format(word)
with open(filename, 'w', encoding='utf-8') as f:
    f.write(html)
```

​	**quote('参数为字符串')**

```python
import requests
from urllib import parse

# 1. 拼接URL地址
word = input('请输入搜索关键字:')
params = parse.quote(word)
url = 'http://www.baidu.com/s?wd={}'.format(params)

# 2. 发请求获取响应内容
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
html = requests.get(url=url, headers=headers).content.decode('utf-8')

# 3. 保存到本地文件
filename = '{}.html'.format(word)
with open(filename, 'w', encoding='utf-8') as f:
    f.write(html)
```

​	**unquote(string)解码**

4、爬虫的流程？

```
1、确定需要爬取的URL地址
2、由请求模块向URL地址发出请求,并得到网站的响应
3、从响应内容中提取所需数据
4、所需数据,保存
5、页面中有其他需要继续跟进的URL地址,继续第2步去发请求，如此循环1
```

5、**MongoDB介绍**

```
1、MongoDB为非关系型数据库,基于key-value方式存储
2、MongoDB基于磁盘存储,而Redis基于内存
3、MongoDB数据类型单一,就是JSON文档
4、MySQL数据类型:数值类型、字符类型、枚举类型、日期时间类型
5、Redis数据类型:字符串、列表、哈希、集合、有序集合
6、MongoDB数据类型: JSON文档
和MySQL对比
    1、MySQL：  库 - 表   - 表记录
    2、MongoDB：库 - 集合 - 文档
特性
    MongoDB无需提前建库建集合,直接使用即可,会自动创建
```

6、什么是xpath?

```
XPath即为XML路径语言，它是一种用来确定XML文档中某部分位置的语言，同样适用于HTML文档的检索
```

7、xpath常用函数？

```
【1】text() ：获取节点的文本内容
    xpath表达式末尾不加 /text() :则得到的结果为节点对象
    xpath表达式末尾加 /text() 或者 /@href : 则得到结果为字符串
        
【2】contains() : 匹配属性值中包含某些字符串节点
    匹配class属性值中包含 'movie-item' 这个字符串的 div 节点
     //div[contains(@class,"movie-item")]
```

8、什么是增量爬虫？爬取思路是什么样的？

```
【1】原理
    利用Redis集合特性，可将抓取过的指纹添加到redis集合中，根据返回值来判定是否需要抓取
【2】实现(根据sadd的返回值）
	返回值为1 ： 代表之前未抓取过，需要进行抓取
	返回值为0 ： 代表已经抓取过，无须再次抓取
```

9、数据抓取的思路是什么？

```
【1】先确定是否为动态加载网站
【2】找URL规律
【3】正则表达式 | xpath表达式
【4】定义程序框架，补全并测试代码
```

10、有哪几种数据持久化的方式？

#### csv

```python
 import csv
 with open('xxx.csv','w',encoding='utf-8',newline='') as f:
	writer = csv.writer(f)
 	writer.writerow([])
```

**MySQL**

```python
import pymysql

# __init__(self)：
	self.db = pymysql.connect('IP',... ...)
	self.cursor = self.db.cursor()
	
# save_html(self,r_list):
	self.cursor.execute('sql',[data1])
	self.db.commit()
	
# run(self):
	self.cursor.close()
	self.db.close()
```

**MongoDB**

```python
import pymongo

# __init__(self)：
	self.conn = pymongo.MongoClient('localhost', 27017)
	self.db = self.conn['库名']
    self.myset = self.db['集合名']
	
# save_html(self,r_list):
	self.myset.insert_one({})
    
mongo
>show dbs
>use 库名
>show collections
>db.集合名.find().pretty()
>db.集合名.count()
>db.集合名.drop()
>db.dropDatabase()
```

11、lxml解析库

##### 使用流程

```python
1、导模块
   from lxml import etree
2、创建解析对象
   parse_html = etree.HTML(html)
3、解析对象调用xpath
   r_list = parse_html.xpath('xpath表达式')
====================================
【1】基准xpath: 匹配所有电影信息的节点对象列表
   //dl[@class="board-wrapper"]/dd
   [<element dd at xxx>,<element dd at xxx>,...]
    
【2】遍历对象列表，依次获取每个电影信息
   item = {}
   for dd in dd_list:
	 	item['name'] = dd.xpath('..//p[@class="name"]/a/text()').strip()
	 	item['star'] = dd.xpath('..//p[@class="star"]/text()').strip()
	 	item['time'] = dd.xpath('..//p[@class="releasetime"]/text()').strip()
```

12、代理有哪几种？

```
1、定义 : 代替你原来的IP地址去对接网络的IP地址
2、作用 : 隐藏自身真实IP,避免被封

普通代理
代理IP池建立
私密代理+独享代理
```

13、有道翻译破解

```
【1】准备抓包: F12开启控制台，刷新页面
【2】寻找地址
	2.1) 页面中输入翻译单词，控制台中抓取到网络数据包，查找并分析返回翻译数据的地址
        F12-Network-XHR-Headers-General-Request URL
【3】发现规律
	3.1) 找到返回具体数据的地址，在页面中多输入几个单词，找到对应URL地址
	3.2) 分析对比 Network - All(或者XHR) - Form Data，发现对应的规律
【4】寻找JS加密文件
	控制台右上角 ...->Search->搜索关键字->单击->跳转到Sources，左下角格式化符号{} 
【5】查看JS代码
	搜索关键字，找到相关加密方法，用python实现加密算法
【6】断点调试
	JS代码中部分参数不清楚可通过断点调试来分析查看
【7】Python实现JS加密算法
```

14、常见的反爬都有哪些？【重点】

```python
【1】Headers反爬虫
   1.1) 检查: Cookie、Referer、User-Agent
   1.2) 解决方案: 通过F12获取headers,传给requests.get()方法
        
【2】IP限制
   2.1) 网站根据IP地址访问频率进行反爬,短时间内限制IP访问
   2.2) 解决方案: 
        a) 构造自己IP代理池,每次访问随机选择代理,经常更新代理池
        b) 购买开放代理或私密代理IP
        c) 降低爬取的速度
        
【3】User-Agent限制
   3.1) 类似于IP限制，检测频率
   3.2) 解决方案: 构造自己的User-Agent池,每次访问随机选择
        a> fake_useragent模块
        b> 新建py文件,存放大量User-Agent
        c> 程序中定义列表,存放大量的User-Agent
        
【4】对响应内容做处理 - 百度贴吧视频案例
   4.1) 页面结构和响应内容不同
   4.2) 解决方案: 打印并查看响应内容,用xpath或正则做处理
    
【5】JS加密 - 有道翻译案例
   5.1) 抓取到对应的JS文件,寻找加密算法
   5.2) 用Python实现加密算法,生成指定的参数

【6】JS逆向 - 百度翻译案例
   6.1) 抓取到对应的JS文件，寻找加密算法
   6.2) 利用pyexecjs模块执行JS代码

【7】动态加载 - 豆瓣电影、小米应用商店、腾讯招聘
   7.1) F12抓取网络数据包再进行分析,找返回实际json数据的地址
```

15、常见的解析模块?

```python
re正则解析
import re 
pattern = re.compile('正则表达式',re.S)
r_list = pattern.findall(html)
======================================
lxml+xpath解析
from lxml import etree
p = etree.HTML(res.text)
r_list = p.xpath('xpath表达式')

【谨记】只要调用了xpath，得到的结果一定为'列表'
```

16、什么是selenium?

```
selenium是一个开源的Web自动化测试工具
```

17、浏览器对象方法有哪些？

```
【1】driver.get(url=url)   - 地址栏输入url地址并确认
【2】driver.quit()         - 关闭浏览器
【3】driver.close()        - 关闭当前页
【4】driver.page_source    - HTML结构源码
【5】driver.page_source.find('字符串')
    从html源码中搜索指定字符串,没有找到返回：-1,经常用于判断是否为最后一页
【6】driver.maximize_window() - 浏览器窗口最大化
```

18、定位节点八种方法？

```
【1】单元素查找('结果为1个节点对象')
    1.1) 【最常用】driver.find_element_by_id('id属性值')
    1.2) 【最常用】driver.find_element_by_name('name属性值')
    1.3) 【最常用】driver.find_element_by_class_name('class属性值')
    1.4) 【最万能】driver.find_element_by_xpath('xpath表达式')
    1.5) 【匹配a节点时常用】driver.find_element_by_link_text('链接文本')
    1.6) 【匹配a节点时常用】driver.find_element_by_partical_link_text('部分链接文本')
    1.7) 【最没用】driver.find_element_by_tag_name('标记名称')
    1.8) 【较常用】driver.find_element_by_css_selector('css表达式')
```

19、节点对象操作

```python
【1】node.send_keys('')  - 向文本框发送内容
【2】node.click()      - 点击
【3】node.get_attribute('属性名')  -  获取节点的属性值
```

20、selenium爬虫总结

```
【1】特点
	1.1》简单，无需去详细抓取分析网络数据包，使用真实浏览器
	1.2》需要等待页面元素加载，需要时间，效率低

【2】设置无界面模式
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(excutable_path='/home/tarena/chromedriver',options=options)
    
【3】鼠标操作
    from selenium.webdriver import ActionChains
    ActionChains(driver).move_to_element('node').perform()
    
【4】切换句柄 - switch_to.frame(handle)
    all_handles = driver.window_handles
    driver.switch_to.window(all_handles[1])
    
【5】iframe子页面
    driver.switch_to.frame(frame_node)
    
【6】driver执行JS脚本
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    
【7】lxml中的xpath 和 selenium中的xpath的区别
    7.1》lxml中的xpath用法 - 推荐自己手写
        div_list = p.xpath('//div[@class="abc"]/div')
        item = {}
        for div in div_list:
            item['name'] = div.xpath('..//a/@href')[0]
            item['likes'] = div.xpath('..//a/text()')[0]

    7.2》selenium中的xpath用法 - 推荐copy - copy xpath
        div_list = driver.find_elements_by_xpath('//div[@class="abc"]/div')
        item = {}
        for div in div_list:
            item['name'] = div.find_element_by_xpath('..//a').get_attribute('href')
            item['likes'] = div.find_element_by_xpath('..//a').text
```

21、什么是scrapy框架？

```
异步处理框架,可配置和可扩展程度非常高,Python中使用最广泛的爬虫框架
```

22、Scrapy框架五大组件？

```
【1】引擎（Engine）----------整个框架核心
【2】爬虫程序（Spider）------数据解析提取
【3】调度器（Scheduler）-----维护请求队列
【4】下载器（Downloader）----获取响应对象
【5】管道文件（Pipeline）-----数据入库处理


【两个中间件】
    下载器中间件（Downloader Middlewares）
        引擎->下载器,包装请求(随机代理等)
    蜘蛛中间件（Spider Middlewares）
        引擎->爬虫文件,可修改响应对象属性
```

23、scrapy爬虫工作流程？【重点】

```
【1】爬虫项目启动,由引擎向爬虫程序索要第一批要爬取的URL,交给调度器去入队列
【2】调度器处理请求后出队列,通过下载器中间件交给下载器去下载
【3】下载器得到响应对象后,通过蜘蛛中间件交给爬虫程序
【4】爬虫程序进行数据提取：
    4.1) 数据交给管道文件去入库处理
    4.2) 对于需要继续跟进的URL,再次交给调度器入队列，依次循环
```

24、scrapy项目目录结构

```
Baidu                   # 项目文件夹
├── Baidu               # 项目目录
│   ├── items.py        # 定义数据结构
│   ├── middlewares.py  # 中间件
│   ├── pipelines.py    # 数据处理
│   ├── settings.py     # 全局配置
│   └── spiders
│       ├── baidu.py    # 爬虫文件
└── scrapy.cfg          # 项目基本配置文件
```

25、创建爬虫项目步骤？

```
【1】新建项目和爬虫文件
    scrapy startproject 项目名
    cd 项目文件夹
    新建爬虫文件 ：scrapy genspider 文件名 域名
【2】明确目标(items.py)
【3】写爬虫程序(文件名.py)
【4】管道文件(pipelines.py)
【5】全局配置(settings.py)
【6】运行爬虫
    6.1) 终端: scrapy crawl 爬虫名
    6.2) pycharm运行
        a> 创建run.py(和scrapy.cfg文件同目录)
	      from scrapy import cmdline
	      cmdline.execute('scrapy crawl maoyan'.split())
        b> 直接运行 run.py 即可
```

![image-20201129104901557](../图片/image-20201129104901557.png)

26、框架总结

```
【1】五大组件
    1.1) 引擎（Engine）
    1.2) 爬虫程序（Spider）
    1.3) 调度器（Scheduler）
    1.4) 下载器（Downloader）
    1.5) 管道文件（Pipeline）
    1.6) 下载器中间件（Downloader Middlewares）
    1.7) 蜘蛛中间件（Spider Middlewares）
    
【2】工作流程
    2.1) Engine向Spider索要URL,交给Scheduler入队列
    2.2) Scheduler处理后出队列,通过Downloader Middlewares交给Downloader去下载
    2.3) Downloader得到响应后,通过Spider Middlewares交给Spider
    2.4) Spider数据提取：
       a) 数据交给Pipeline处理
       b) 需要跟进URL,继续交给Scheduler入队列，依次循环
    
【3】常用命令
    3.1) scrapy startproject 项目名
    3.2) scrapy genspider 爬虫名 域名
    3.3) scrapy crawl 爬虫名
```

27、必须记住

```
【1】响应对象response属性及方法
    1.1) response.text ：获取响应内容 - 字符串
    1.2) response.body ：获取bytes数据类型
    1.3) response.xpath('')
    1.4) response.xpath('').extract()
    	提取文本内容,将列表中所有元素序列化为Unicode字符串
    1.5) response.xpath('').extract_first()
    	序列化提取列表中第1个文本内容
    1.6) response.xpath('').get() 
    	提取列表中第1个文本内容(等同于extract_first())
    
【2】settings.py中常用变量
    2.1) 设置数据导出编码(主要针对于json文件)
         FEED_EXPORT_ENCODING = 'utf-8'
    2.2) 设置User-Agent
         USER_AGENT = ''
    2.3) 设置最大并发数(默认为16)
         CONCURRENT_REQUESTS = 32
    2.4) 下载延迟时间(每隔多长时间请求一个网页)
         DOWNLOAD_DELAY = 0.5
    2.5) 请求头
         DEFAULT_REQUEST_HEADERS = {'Cookie' : 'xxx'}
    2.6) 添加项目管道
         ITEM_PIPELINES = {'目录名.pipelines.类名' : 优先级}
    2.7) cookie(默认禁用,取消注释-True|False都为开启)
         COOKIES_ENABLED = False
```

28、什么是分布式爬虫？

```
多台主机共享1个爬取队列
```

29、分布式爬虫实现方式

##### 方式一

```
【1】首先完成普通的scrapy爬虫项目
【2】设置settings.py
	1.1 重新指定调度器
	1.2 重新指定去重机制
	1.3 设置不清除请求指纹
	1.4 指定url地址管理的redis的IP地址和端口号
	1.5 如果有需要，则添加redis的管理
【3】把项目拷贝到分布式所有爬虫服务器，并开始运行项目
```

##### 方式二

```python
【1】首先完成普通的scrapy爬虫项目
【2】设置settings.py
	1.1 重新指定调度器
	1.2 重新指定去重机制
	1.3 设置不清除请求指纹
	1.4 指定url地址管理的redis的IP地址和端口号
	1.5 如果有需要，则添加redis的管理
【3】设置爬虫文件
	3.1 更新继承类，继承scrapy_redis的RedisSpider类
	3.2 去掉原来的start_urls
	3.3 添加redis_key,一般以爬虫名：spider命名
【4】把项目拷贝到分布式所有爬虫服务器，并开始运行项目
【5】在Redis命令行，压入第一个要抓取的URL地址，所有服务器开始爬虫redis>LPUSH 爬虫名：spider 第一页的URL地址
```

30、机器视觉与tesseract基本概念？

```
【1】作用
    处理图形验证码

【2】三个重要概念 - OCR、tesseract-ocr、pytesseract
    2.1) OCR
        光学字符识别(Optical Character Recognition),通过扫描等光学输入方式将各种票据、报刊、书籍、文稿及其它印刷品的文字转化为图像信息，再利用文字识别技术将图像信息转化为电子文本

    2.2) tesseract-ocr
        OCR的一个底层识别库（不是模块，不能导入），由Google维护的开源OCR识别库

    2.3) pytesseract
        Python模块,可调用底层识别库，是对tesseract-ocr做的一层Python API封装
```

31、面试问题: 如何处理爬虫中遇到的验证码

```
【1】图形验证码
	简单的图形验证码,我使用tesseract-ocr去处理
	对于一些复杂的验证码,我们使用在线打码(图鉴、云打码)
【2】滑块、缺口验证码
	使用selenium处理
	或者使用人工打码
```

32、分布式爬虫原理

![image-20201129105807829](../图片/image-20201129105807829.png)

33、什么是Hadoop?

```
Hadoop是Yahoo!开发，后贡献给了Apache的一套开源的、可靠的、可扩展的用于分布式计算的框架
```

34、Hadoop有什么优点？

```
- **高可靠性** 
  Hadoop按位存储和数据处理的能力值得信赖
- **高扩展性**
  Hadoop通过可用的计算机集群分配数据，完成存储和计算任务，这些集群可以方便地扩展到数以千计的节点中，具有高扩展性
- **高效性**
  Hadoop能够在节点之间进行动态地移动数据，并保证各个节点的动态平衡，处理速度非常快，具有高效性
- **高容错性**
  Hadoop能够自动保存数据的多个副本（默认是3个），并且能够自动将失败的任务重新分配
```

36、Hadoop有什么缺点？

```
1. 不能做到低延迟，对于低延迟数据访问，不适合hadoop
2. 不适合大量小文件存储，由于namenode将文件系统的元数据存储在内存中，因此该文件系统所能存储的文件总数受限于namenode的内存容量，根据经验，每个文件、目录和数据块的存储信息大约占150字节
3. 对于上传到HDFS上的文件，不支持修改文件，HDFS适合一次写入，多次读取的场景
```

35、Hadoop能做什么？

```
1、大数据量存储
2、日志处理
3、搜索引擎
4、数据挖掘
```

36、Hadoop核心组件？

```
HDFS（Hadoop Distributed File System）分布式存储，解决海量数据的存储
HDFS角色和概念
1、Client
切分文件、访问HDFS、与NameNode交互获取文件位置信息、与DataNode交互读取和写入数据
2、Namenode
Master节点，管理HDFS的名称空间和数据块映射信息，配置副本策略，处理所有客户端请求
3、Secondarynode
定期同步NameNode，紧急情况下，可转正
4、Datanode
数据存储节点，存储实际的数据
汇报存储信息给NameNode
5、Block
每块默认128MB大小
每块可以多个副本
```

37、HDFS原理？

```
1、每个数据块3个副本，分布在两个机架内的节点，2个副本在同一个机架上，另外一个副本在另外的机架上
2、心跳检测，datanode定期向namenode发送心跳消息。查看是否有datanode挂掉了
3、secondary namenode;定期同步元数据映像文件和修改日志，namenode发生故障，secondaryname会成为主namenode
```

38、HDFS写文件流程

```
【1】客户端将文件拆分成固定大小128M的块，并通知namenode
【2】namenode找到可用的datanode返回给客户端
【3】客户端根据返回的datanode，对块进行写入
【4】通过流水线管道流水线复制
【5】更新元数据，告诉namenode已经完成了创建新的数据块，保证namenode中的元数据都是最新的状态
```

39、HDFS读文件流程

```
【1】客户端向namenode发起读请求，把文件名，路径告诉namenode
【2】namenode查询元数据，并把数据返回客户端
【3】此时客户端就明白文件包含哪些块，这些块在哪些datanode中可以找到
```

40、什么是MapReduce？

```
1、MapReduce是Hadoop提供的一套进行分布式计算的框架，用于大规模数据集（大于1TB）的并行运算
2、MapReduce将计算过程拆分为2个阶段：Map(映射)阶段和Reduce(规约)阶段
```

42、什么是Hive?

```
1. Hive是基于Hadoop的一个数据仓库工具。可以将结构化的数据文件映射为一张表，并提供完整的sql查询功能，本质上还是一个文件
2. 底层是将sql语句转换为MapReduce任务进行运行
3. 本质上是一种大数据离线分析工具
4. 学习成本相当低，不用开发复杂的mapreduce应用，十分适合数据仓库的统计分析
5. hive可以用来进行 数据提取、转化、加载，这是一种可以存储、查询和分析存储在hadoop上的数据。
```

43、什么是数据仓库？

```
1. 数据是集成的，数据的来源可能是：MySQL、oracle、网络日志、爬虫数据...... 等多种异构数据源。Hadoop你就可以看成是一个数据仓库，分布式文件系统hdfs就可以存储多种不同的异构数据源
2. 数据仓库不仅要存数据，还要管理数据，即：hdfs 和 mapreduce，从这个角度看之前的hadoop其实就是一个数据仓库，hive其实就是在hadoop之外包了一个壳子，hive是基于hadoop的数据仓库工具，不通过代码操作，通过类sql语言操作数据仓库中的数据。
   底层其实仍然是分布式文件系统和mapreduce，会把sql命令转为底层的代码
3. 数据仓库的特征
   1. 数据仓库是多个异构数据源集成的
   2. 数据仓库存储的一般是历史数据，大多数的应用场景是读数据（分析数据）
   3. 数据库是为捕获数据而设计，而数据仓库是为了分析数据而设计
   4. 数据仓库是弱事务的，因为数据仓库存的是历史数据，一般都读（分析）数据场景
```

44、Hive的特点？

```
优点：
1. 学习成本低，只要会sql就能用hive
2. 开发效率高，不需要编程，只需要写sql
3. 模型简单，易于理解
4. 针对海量数据的高性能查询和分析
5. 与 Hadoop 其他产品完全兼容
缺点：
1. 不支持行级别的增删改
2. 不支持完整的在线事务处理
```

45、Hive应用场景？

```
Hive 构建在基于静态（离线）批处理的Hadoop 之上，Hadoop通常都有较高的延迟并且在作业提交和调度的时候需要大量的开销。因此，Hive 并不能够在大规模数据集上实现低延迟快速的查询因此，Hive并不适合那些需要低延迟的应用
Hive并不提供实时的查询和基于行级的数据更新操作。Hive 的最佳使用场合是大数据集的离线批处理作业，例如，网络日志分析
```

46、Hive总结？

```
【1】hive建立一张表，跟已经存在的结构化的数据文件产生映射关系
	映射成功后，就可以通过写HQL来分析这个结构化的数据文件，避免了写mr程序的麻烦

【2】数据库：和hdfs中 /user/hive/warehouse 下的一个文件夹对应
	表 ：和数据库文件夹下面的子文件夹 /user/hive/warehouse/库名.db/表名
	表的数据位置目前不能随便存放，一定要在指定的数据库表的文件夹下面
	建立表的时候，需要指定分隔符，否则可能会映射不成功

【3】建表的字段个数和字段类型，要跟结构化数据中的个数类型一致

【4】分区表字段不能够在表中已经存在
	分区字段是一个虚拟的字段，不存放任何数据
	分区字段的数据来自于装载分区表数据的时候指定的
	分区表的字段在hdfs上的效果就是在建立表的文件夹下面又创建了子文件夹
	建立分区表的目的把数据的划分更加细致，减少了查询时候全表扫描的成本，只需要按照指定的分区扫描数据并显示结果即可
	分区表就是辅助查询，缩小查询范围，加快数据的检索速度
	
【5】分桶表在创建之前需要开启分桶功能
	分桶表创建时，分桶的字段必须是表中已经存在的字段，即要按照表中的哪个字段进行分桶
	分桶表也是把表所映射的结构数据文件分成更细致的部分，但是更多的是用在join查询提高效率之上，只需要把join的字段在各自表中进行分桶操作
```

## 6.数据分析