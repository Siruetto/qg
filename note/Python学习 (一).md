# *Python学习 (一)*

---

## 一、第一个项目的建立

```python
print("Hello world!")
print("你好 世界！")
```

**Python的打印是靠print关键词进行的，括号里是需要打印的内容，用英文双引号包裹起来。**

运行结果如下:

![b3db63c5c02a15c2f6b3bb8f5d635b6](https://anem0ne.oss-cn-shenzhen.aliyuncs.com/test/20250117221651287.png)

---



## 二、Python程序格式

```python
if 1<2:
    print("1<2")#如果1<2,那么就打印1<2
'''
如果1<2,那么就打印1<2
'''
"""
如果1<2,那么就打印1<2
"""
```

**如上，Python程序格式有缩进、注释**

* print之前是一个缩进，可以使用**单个制表符(Tab)**或**四个空格**来表示一个缩进，Python用**缩进**而不是**{}**表示程序块的**层次关系**;
* print语句后面带有**#**的句子是注释的第**一**种形式：**单行注释**，每行注释加**#**号。当解释器看到**#**,则忽略这一行**#**后面的内容;
* print语句下一行带有**'''**或**"""**的语段是注释的第**二**种形式：**段注释(多行注释)**，使用三个连续单引号**'''**或三个双引号**"""**。当解释器看到**'''**或**"""**，则会扫描到下一个**'''**或**"""**，然后忽略它们之前的内容。
  * 事实上，三个连续引号，其实就是定义了一个**字符串**。只不过，没有**变量指向**，会被当成垃圾回收(知识点：面向对象);

* Python**区分大小写**。

---



## 三、Python之海龟绘图

### 坐标系问题 ###

```python
import turtle # 导入模块

turtle.showturtle() # 显示箭头
turtle.write("你好 世界！")
turtle.forward(300) # 前进300个像素
turtle.color("red") # 改变画笔的颜色
turtle.left(90) # 箭头左转90度
turtle.forward(300)
turtle.goto(0,0) # 回到坐标系的点(0,0)
turtle.penup() # 抬起笔，不画出路径
turtle.goto(0,50)
turtle.pendown() # 放下笔，画出路径
turtle.circle(100) # 画一个半径为100的圆

turtle.done() # 程序结束，可以保持窗口一直存在
```

运行结果如下:

![183d10f90b49ac81fcce8d0060cfa04](https://anem0ne.oss-cn-shenzhen.aliyuncs.com/test/20250117221711951.png)

---

### 绘制奥运五环 ###

```python
import turtle

# 第一个圆
turtle.width(10) # 控制画笔粗度为10
turtle.color("blue")
turtle.circle(50)

# 第二个圆
turtle.penup()
turtle.goto(80,0)
turtle.pendown()
turtle.color("black")
turtle.circle(50)

# 第三个圆
turtle.penup()
turtle.goto(160,0)
turtle.pendown()
turtle.color("red")
turtle.circle(50)

# 第四个圆
turtle.penup()
turtle.goto(40,-60)
turtle.pendown()
turtle.color("yellow")
turtle.circle(50)

# 第五个圆
turtle.penup()
turtle.goto(115,-60)
turtle.pendown()
turtle.color("green")
turtle.circle(50)

turtle.done()
```

> 理解：解决编程问题时，可以将大任务拆分成**若干个小任务**进行解决。

运行结果如下:

![19329c927776cffd0a824b28601c021](https://anem0ne.oss-cn-shenzhen.aliyuncs.com/test/20250118101516315.png)

---



## 四、Python程序之对象 ##

**对象**：Python的对象由**标识(identity)**、**类型(type)**、**值(value)**三部分组成。

* **标识(identity)**：唯一标识对象，通常对应于对象在计算机内存中的地址。使用**内置函数id(obj)**可返回对象的标识。

* **类型(type)**：表示对象存储的”数据“的类型。类型可以限制对象的取值范围以及可以执行的操作。可以使用**type(obj)**获取对象的所属类型。

* **值(value)**：表示对象所存储的数据的信息。使用**print(obj)**可以直接打印出值。

**总结**：对象的**本质**就是一个内存块，拥有特定的值，支持特定类型的相关操作

```python
a = 3
print(a)
print(id(a))
print(type(a))
b = "Hello world"
print(b)
print(id(b))
print(type(b))
```

运行结果如下：

![bc9697c8daded13688c57af810c8baa](https://anem0ne.oss-cn-shenzhen.aliyuncs.com/test/20250118220109371.png)

> 分析：对于a，3是value，140715900996088是标识(系统分配给a的地址)，class 'int’是类型。对于b，Hello world是value，2180586056048是标识(系统分配给b的地址)，class 'str'是类型。

---



## 五、Python之引用的本质

在Python中，变量也称为：对象的**引用(reference)**。变量储存的就是对象的**地址**。变量通过地址引用了”对象“。其中，变量位于**栈内存**，对象位于**堆内存**。

> **注意**：Python是**动态类型**语言，变量不需要显式声明类型。根据变量引用的对象，Python解释器**自动**确定数据类型。

---



## 六、Python之标识符

**标识符有四个原则**：

* 区分**大小写**。
* **第一个**字符必须是**字母**、**下划线**。其后的字符是：字母、数字、下划线。
* **不能**使用**关键字**。比如：‘if’、‘or’、‘while’等。
* 以**双下划线开头和结尾**的名称通常有**特殊**含义，尽量避免这种写法。

> 可以用**help()**来查看Python关键字，然后输入**keywords**即可查看。

**标识符命名规则**：

| 类型       | 规则                                                         | 例子                    |
| ---------- | ------------------------------------------------------------ | ----------------------- |
| 模块和包名 | 全小写字母，尽量简单。多个单词之间用下划线隔开               | math，os，sys           |
| 函数名     | 全小写字母，多个单词之间用下划线隔开                         | phone，my_name          |
| 类名       | 首字母大写，采用驼峰原则。多个单词时，每个单词第一个字母大写，其余部分小写 | Myphone，Myclass，Phone |
| 常量名     | 全大写字母，多个单词使用下划线隔开                           | SPEED，MAX_SPEED        |

---



## 七、Python之变量声明、初始化、垃圾回收机制

**变量的声明和赋值**：用于将一个变量绑定到一个对象上，格式是**变量名 = 表达式**。

> 变量在使用前必须先被**初始化**(先被赋值)。

**删除变量和垃圾回收机制**：

* 可以通过**del**语句删除不再使用的变量。
* 如果对象**没有变量引用**，就会被垃圾回收器**自动**回收清空内存空间。

---



## 八、常量、链式赋值、系列解包赋值

**常量**：Python不支持常量，即**没有语法规则**限制改变一个常量的值。我们只能**约定**常量的命名规则，以及在程序的**逻辑上**不对常量的值作出修改。

```python
MAX_SPEED = 120
print(MAX_SPEED) # 输出120
MAX_SPEED = 140 # 实际是可以改的，只是逻辑上不做修改
print(MAX_SPEED) # 输出140
```

**链式赋值**：用于**同一个对象**赋值给**多个变量**。

```python
x = y = 120 # x与y同时被赋值120
```

**系列解包赋值**：**系列数据**赋值给对应**相同个数**的变量。

> 个数必须保持**一致**。

```python
#使用系列解包赋值实现变量值交换
a,b = 1,2
a,b = b,a # 变量值互换
print(a,b) # 输出2 1
```

---



## 九、内置数据类型和基本算术运算符

**数据类型**：Python中变量**没有类型**，但是对象**都有类型**，其中最基本的**内置**数据类型有四种：

* 整型 int
  * **整数**，如：2345，10。
* 浮点型 float
  * **小数**，如3.14或者科学计数法314e-2。
* 布尔型 bool
  * **表示真假**，仅包含：True、False。
* 字符串型 str
  * **由字符串组成的序列**，如：“abc”，“数据类型”。

```python
a = 123
b = 3.14
b2 = 314e-3
c = True
d = "Hello world"
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print("b2:",str(b2))
```

运行结果如下：

![7d18818d935c3962fefbf813025dce7](https://anem0ne.oss-cn-shenzhen.aliyuncs.com/test/20250118234451660.png)

>  输出浮点数时需要**转换成字符串**输出。

**数字和基本运算符**：Python支持整数(如：50，520)和浮点数(如：3.14，10.0，1.23e2)，我们可以队数字做如下运算。

| 运算符 | 说明       | 示例 | 结果 |
| ------ | ---------- | ---- | ---- |
| +      | 加法       | 3+2  | 5    |
| -      | 减法       | 30-5 | 25   |
| *      | 乘法       | 3*6  | 18   |
| /      | 浮点数除法 | 8/2  | 4.0  |
| //     | 整数除法   | 7//2 | 3    |
| %      | 模（取余） | 7%4  | 3    |
| **     | 幂         | 2**3 | 8    |

> 使用**divmod()函数**可以同时得到商和余数(返回的是一个**元组**)：
>
> ```python
> print(divmod(13,3)) # 输出(4, 1)
> ```

