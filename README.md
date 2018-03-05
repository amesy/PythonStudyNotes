[TOC]

## 数字的处理函数

| 函数名         | 功能                                       |
| ----------- | :--------------------------------------- |
| sqrt()      | 取数字的平方根,返回值类型为float  (例如:import math; math.sqrt(9) -> 3.0)。 |
| divmod(x,y) | 该函数也可以获得商和余数, 如divmod(5,2)，返回的值为(2,1)，其中2为商，1为余数。 |
| bin()       | 二进制。                                     |
| oct()       | 八进制。                                     |



## 列表, 链表, queue(队列), stack(栈)的差异

### 列表

根据索引查找比较快，从最后追加也很快，命中cpu缓存概率比较大。插入很慢，删除也很慢。

### 链表

非线性结构,由前一个元素来获知下一元素的位置,不能使用索引。

查找很慢,但空间不必连续。插入,插入,尾部追加很快。

### 队列

队列是一个先入先出的的数据结构, 类似于银行排队。 【pop(0)和append】

### 栈

栈是一个【后入先出/先入后出】的数据结构, 类似于洗碗堆盘子。 【append和pop()】

## 列表 - list

> 使用[ ]表示。
>
> 列表内元素可以是任意对象(数字,字符串,对象,列表等) 。
>
>  元素可变。
>
> 元素有顺序,可以使用索引。 
>
> 是一种线性的数据结构。
>
> list定义: 赋值即定义(即动态语言和静态语言的差别)。
>
> list是可变的,所以不能被hash。
>
> list赋值等同于浅拷贝。

### 方法 - 增
| 方法                      | 功能   | 注释                                       |
| ----------------------- | ---- | ---------------------------------------- |
| L.append(object)        | 增加元素 | 原地修改。时间复杂度O(1),  类似于双向列表。追加元素到列表L末尾。     |
| L.insert(index, object) | 插入元素 | 原地修改。 insert 时间复杂度不确定, 但会引起内存结构变化, 索引超界会将元素追加到开头或最后.链表适合插入操作, 因为不需要挪动位置。 |
| L.extend(iterable)      | 列表扩展 | 原地修改。 iterable可以是 list、str等。             |
| +                       | 连接操作 | 连接操作连接两个列表, 产生新的列表。                      |
| *                       | 重复操作 | 重复操作将本列表元素重复n次, 重复操作, 产生新的列表。            |

### 方法 - 删

| 方法              | 功能          | 注释                                       |
| --------------- | ----------- | ---------------------------------------- |
| L.remove(value) | 根据value删除元素 | 原地修改, 从左到右匹配, 删除完会引起内存结构变化, 需注意效率问题。     |
| L.pop([index])  | 根据索引值删除元素   | 删除完会弹出该index对应的值。从尾部删除效率很高,反之效率低, 删除有返回值,返回值为被删除的对象。 |
| L.clear()       | 清除列表所有元素    | 原地修改。清除完会只剩一空列表, 需注意垃圾回收问题, 清除元素过多,对象释放, 会引发 gc 垃圾回收机制。 |

### 方法 - 改    

| 方法                  | 功能        | 注释      |
| ------------------- | --------- | ------- |
| list[index] = value | 通过索引访问修改。 | 索引不能越界。 |

### 方法 - 查

| 函数                              | 功能           | 注释                                       |
| ------------------------------- | ------------ | ---------------------------------------- |
| L.index(value, [start, [stop]]) | 查找元素对应的索引值。  | 时间复杂度为O(n)。通过value, 从指定区间查找, 匹配到第一个就立即返回, 匹配不到则抛异常 ValueError: xx is not in list。 |
| L.count(value)                  | 匹配列表中元素出现次数。 | 时间复杂度为O(n)。                              |

### 方法 - 翻转

| 方法                                       | 功能      | 注释                                       |
| ---------------------------------------- | ------- | ---------------------------------------- |
| L.reverse()<br>or,<br>reversed(sequence) | 将列表元素反转 | 时间复杂度为O(1)。类似于双向列表。<br>reverse()原地翻转列表被元素。<br>reversed() 结果为可迭代对象。<br>reversed是python的内置函数。 |

### 方法 - 排序
| 方法                                       | 功能       | 注释                                       |
| ---------------------------------------- | -------- | ---------------------------------------- |
| L.sort(key=None, reverse=False)<br>or,<br> sorted(iterable,key=None, reverse=False) | 对列表内元素排序 | 时间复杂度为O(n)。类似于<br>默认升序排列, reverse为True,则降序排列,key指定如何排序。排序会引发效率问题。 <br>sort()原地对元素排序。<br>sorted()不会修改原列表。<br> sorted是python的内置函数。 |

### 方法 - 复制

| 方法              | 功能                                       | 注释                                       |
| --------------- | ---------------------------------------- | ---------------------------------------- |
| L.copy()        | shadow copy: 影子拷贝，也叫浅拷贝，遇到引用类型，只是复制了一个引用而已。 | 浅拷贝在内存中只额外创建第一层数据。                       |
| copy.deepcopy() | 深拷贝, 由copy模块提供, 使用前需先导入。                 | 深拷贝在内存中将所有的数据重新创建一份（排除最后一层,即: python内部对字符串和数字的优化） |

### 统计字符串的长度
| 函数        | 功能            | 注释                                     |
| --------- | ------------- | -------------------------------------- |
| len(list) | 统计list内元素的个数。 | 返回列表元素个数。<br>时间复杂度O(1), 因为它内部有个字段是计数器。 |

### 字符比较 

| 方法        | 功能                        |
| --------- | ------------------------- |
| is <br>== | is用内存id作比较。<br>'=='用值作比较。 |

## 随机数

导入random模块。

| 方法                                 | 功能                                       |
| ---------------------------------- | ---------------------------------------- |
| randint(a, b)                      | 返回[a, b]之间的整数,左右都是闭区间。                   |
| choice(seq)                        | 从非空序列的元素中随机挑选一个元素,取整数。                   |
| randrange([start], stop, [, step]) | 从指定范围内按指定基数递增的集合中获取一个随机数，基数缺省值为1,前闭后开,可取步长。 |
| shuffle(list) -> None              | 就地打乱列表元素。                                |
| sample(population, k)              | 从样本空间或总体(序列或者集合类型)中随机取出k个不同的元素,返回一个新的列表。 |

```python
In [1]: import random

In [2]: lst = [1, 2, 3, 4, 5, 'a', 'b', 'c']

In [3]: random.shuffle(lst)   # 就地打乱列表元素, 无返回值。

In [4]: lst
Out[4]: [2, 3, 5, 'c', 1, 4, 'b', 'a']

In [8]: random.randint(0, 10)  # 返回[0, 10]之间的整数,左右都是闭区间.
Out[8]: 5

In [9]: random.choice(lst)  # 从非空序列的元素中随机挑选一个元素,取整数.
Out[9]: 'a'

In [13]: random.randrange(1, 10)  # 从指定范围内按指定基数递增的集合中获取一个随机数，基数缺省值为1,前闭后开,可取步长. 
Out[13]: 6

In [15]: alpha = bytes(range(97, 123)).decode()

In [16]: alpha
Out[16]: 'abcdefghijklmnopqrstuvwxyz'

In [17]: random.sample(alpha, 10)  # 从样本空间或总体(序列或者集合类型)中随机取出k个不同的元素,返回一个新的列表.
Out[17]: ['f', 'x', 'w', 'v', 'h', 't', 'i', 'b', 'o', 'n']

In [18]:
```

## 元组 - tuple

> 一个有序的元素组成的集合。 
>
> 使用小括号()表示。 
>
> 元组是不可变对象(里面的引用类型可变)。  
>
> 可理解为只读。 
>
> 支持索引(下标)。 

### 初始化 

```python
tuple() ——> empty tuple  

tuple(iterable) ——> tuple initialized from iterable's items.  

In [1]: tuple_element = (1, )  # 构造一个元素的元组时, 不加逗号会被误认为其他类型。
```

### 方法 - 元组只读, 增删改的方法都没有 

### 方法 - 查 

| 方法                              | 功能               | 注释                                       |
| ------------------------------- | ---------------- | ---------------------------------------- |
| T.index(value, [start, [stop]]) | 返回value对应的索引值。   | 时间复杂度是O(n), 随着元组规模增大,效率下降。匹配到第一个就立即返回索引,匹配不到则报错ValueError。 |
| T.count(value)                  | 返回元组中匹配value的次数。 | 时间复杂度是O(n), 随着元组规模增大,效率下降。匹配不到任何一个value就返回0。 |
| len(tuple)                      | 返回元组中元素的个数。      | 时间复杂度O(1)。                               |

### 命名元组 - namedtuple 

namedtuple是继承自tuple的子类。namedtuple创建一个和tuple类似的对象，而且对象拥有可访问的属性。

```python 
from collections import namedtuple

语法： 
namedtuple(typename, field_names, verbose=False, rename=False) 
	Returns a new subclass of tuple with named fields.
    
# typename：此元组的名称;
# field_names: 元祖中元素的名称,此字段有多种表达方式;
# rename:如果元素名称中含有python的关键字，则必须设置为rename=True;
# verbose:在构建之前打印类定义。
```

其中`field_names` 有多种表达方式，如：

```python 
"name age sex"
"name, age, sex"
['name', 'age', 'sex']
```

## 字符串 - str

> 由一个个字符组成的有序的序列, 是字符的集合。
>
> 使用单引号,双引号,三引号引住的字符序列。
>
> 字符串是不可变对象。
>
> Python3起,字符串就是Unicode类型。

### 元素访问 

> 支持索引访问。
>
> 是有序的字符集合,字符序列。 
>
> 可迭代。

### 方法 - 字符串不可变,  增和删的方法都没有 

### 方法 - 改 

| 方法                           | 功能                                 | 注释                                       |
| ---------------------------- | ---------------------------------- | ---------------------------------------- |
| S.replace(old, new[, count]) | 在字符串S中找到匹配值old, 替换为新子串new, 返回新字符串。 | count表示替换几次,不指定就是全部替换。                   |
| S.strip([chars])             | 从字符串两端去除指定的字符串集chars中的所有字符。        | 如果chars没有指定,则默认去除两端的空白字符。<br> 从右开始: S.rstrip([chars]) -> str<br>从左开始: S.lstrip([chars]) -> str |

### 方法 - 查 

| 方法                           | 功能                                       | 注释                                       |
| ---------------------------- | ---------------------------------------- | ---------------------------------------- |
| S.find(sub[, start[, end]])  | 在指定区间[start, end),从左至右查找子串sub,**找到返回索引值,没找到返回-1**。 | 时间复杂度O(n) , 随着字符串数据规模增大,效率下降. <br>从右至左查找子串sub: S.rfind(sub[, start[, end]]) |
| S.index(sub[, start[, end]]) | 在指定区间[start, end),从左至右查找子串sub,找到返回索引值,没找到抛异常ValueError。 | 时间复杂度O(n) <br>从右至左查找子串sub:  S.rindex(sub[, start[, end]]) |
| S.count(sub[, start[, end]]) | 在指定区间[start, end),从左至右,统计子串sub出现的次数。     | 时间复杂度O(n) <br>匹配不到返回0。                   |
| len(str)                     | 返回字符串的长度,即字符的个数。                         | 时间复杂度为O(1),因为它内部有计数机制。                   |

### 方法 - join、split、partition

| 方法               | 功能                         | 注释                                       |
| ---------------- | -------------------------- | ---------------------------------------- |
| S.join(iterable) | 将可迭代对象连接起来, 使用string作为分隔符。 | 可迭代对象元素本身都是字符串.<br>返回一个新的字符串。<br>In [1]: '@'.join('amesy') <br>Out[1]: 'a@m@e@s@y' |
| +                | 将2个字符串连接在一起,返回一个新字符串.      |                                          |

| 方法                             | 功能                                       | 注释                                       |
| ------------------------------ | ---------------------------------------- | ---------------------------------------- |
| S.split(sep=None, maxsplit=-1) | 从左往右, 将字符串按照分隔符分割成若干字符串,并返回**列表**。       | sep指定分割字符串,缺省的情况下以空白字符串作为分隔符。<br>maxsplit指定分割的次数,-1表示遍历整个字符串。<br> 从右往左: S.rsplit(sep=None, maxsplit=-1) |
| S.splitlines([keepends])       | 按照行来切分字符串。                               | keepends指是否保留行分隔符。<br>行分隔符包括: \n, \r\n, \r等。 |
| S.partition(sep)               | 从左往右, 将字符串按照分隔符分割成2段,返回这2段和分隔符的**元组**, (head, sep, tail) | 遇到分隔符就把字符串分割成两部分, 返回头,分隔符, 尾三部分的三元组; 如果没有找到分隔符,就返回头,2个空元素的三元组。<br>sep分割字符串,必须指定。<br> 从右往左: S.rpartition(sep) -> (head, sep, tail) |

**split和partition的区别：**

- split不保留分割字符串,partition保留分割字符串。
- split后返回一个列表, partition返回一个元组。

### 方法 - 字符串判断  

| 方法                                   | 功能     | 注释                                |
| ------------------------------------ | ------ | --------------------------------- |
| S.startswith(prefix[, start[, end]]) | 返回bool | 在指定区间[start, end),字符串是否是prefix开头. |
| S.endswith(suffix[, start[, end]])   | 返回bool | 在指定区间[start, end),字符串是否是suffix结尾. |

### is系列 - 字符串判断

| 函数             | 功能                                       |
| -------------- | ---------------------------------------- |
| isalnum()      | 判断是否是字母和数字组成                             |
| isalpha()      | 检测字符串是否只由字母组成。                           |
| isdecimal()    | 是否只包含十进制数字。                              |
| isdigit()      | 是否全部是数字。                                 |
| isidentifier() | 是否是字母和下划线开头, 其他都是数字,字母,下划线。<br>字符串是否是合法的标识符,实际上这里判断的是变量名是否合法。 |
| islower()      | 是否都是小写。                                  |
| isupper()      | 是否全部大写。                                  |
| isspace()      | 检测字符串是否只由空格组成。                           |

### 方法 - 字符串大小写

| 函数         | 功能     |
| ---------- | ------ |
| upper()    | 全大写。   |
| lower()    | 全小写。   |
| swapcase() | 交互大小写。 |

## bytes 和 bytearray 

> python3引入的两个新类型。 
>
> bytes: 不可变字节序列。
>
> bytearray: 字节组,可变。 

### 字符串与bytes: 

> 字符串是以字符为单位进行处理的，bytes类型是以字节为单位处理的。
>
> 字符串是字符组成的有序序列,字符可以使用编码来理解。
>
> 由一系列不可变的Unicode字符组成的叫string。而一系列不可变的介于0-255之间的数字被称为bytes对象。
>
> bytes是字节组成的有序的不可变序列。 
>
> bytearray是字节组成的有序的可变序列。 

### 编码与解码: 

```
字符串按照不同的字符集编码encode返回字节序列bytes. 
	encode(encoding='utf-8', errors='strict') -> bytes. 
字节序列按照不同的字符集解码decode返回字符串. 
	bytes.decode(encoding='utf-8',errors='strict') -> str 
	bytearray.decode(encoding='utf-8',errors='strict') -> str
	
# encode和decode
Python内部的字符串一般都是 Unicode编码。代码中字符串的默认编码与代码文件本身的编码是一致的。所以要做一些编码转换通常是要以Unicode作为中间编码进行转换的，即先将其他编码的字符串解码（decode）成 Unicode，再从 Unicode编码（encode）成另一种编码。
```

### bytes定义 

> b = b' '         # 创建一个空的bytes。
>
> b = bytes()      # 创建一个空的bytes。
>
> b = b'hello'    #  直接指定这个hello是bytes类型。
>
> b = bytes('string',encoding='编码类型')   # 将字符串转换为指定编码的bytes, 等价于string.encode()。默认为utf-8类型。
>
> bytes(iterable_of_ints) -> bytes[0,255]的int组成的iterable对象。
>
> bytes.decode('编码类型')：将bytes对象解码成字符串，默认使用utf-8进行解码。
>
> 使用b前缀定义: 
>
> 	只允许基本ASCII使用形式b'abc9'. 
> 	使用16进制表示b'\x41\x61'. 

### bytes操作 

两种打印ASCII码的方法: 

```python 
In [1]: p1 = [i for i in bytes(range(97, 123)).decode()] 
In [2]: p2 = [chr(i) for i in range(97, 123)]
```

和str类型类似,都是不可变类型,所以方法很多都一样,只是bytes的方法,输入和输出的都是bytes.

```python
In [1]: b'python'.replace(b'th', b'and')
Out[1]: b'pyandon'

In [2]: b'python'.find(b'th')
Out[2]: 2

In [3]:
```

类方法 bytes.fromhex(string)
	# string必须是2个字符的16进制的形式,'6162 6a 6b',空格将被忽略.
	In [1]: bytes.fromhex('6162 09 6a 6b00')
	Out[1]: b'ab\tjk\x00'
	
	In [2]:
hex() 
	In [1]: 'python'.encode()
	Out[1]: b'python'
	
	In [2]: 'python'.encode().hex()
	Out[2]: '707974686f6e'
	
	In [3]:
索引:
	# 返回该字节对应的数,int类型.  
	In [1]: b'python'[2]
	Out[1]: 116
	
	In [2]:

### bytearray定义 

> bytearray() 空bytearray。
>
> bytearray(int) 指定字节的bytearray,被0填充。
>
> bytearray(iterable_of_ints)  ---> bytearray[0,255]的int组成的iterable对象。 
>
> bytearray(string, encoding[,errors])  ---> bytearray近似于string.encode(),不过返回可变对象。  
>
> **注: b前缀定义的类型是bytes类型。**

### bytearray操作 

```python 
# 和bytes类型的方法相同。 
# 其他操作如下:
append(int) # 尾部追加一个元素。 
insert(index, int)   # 在指定索引位置插入元素。 
extend(iterable_of_ints)   # 将一个可迭代的整数集合追加到当前bytearray。 
pop(index=-1)   # 从指定索引上移除元素,默认从尾部移除。 
remove(value)   # 找到第一个value移除,找不到抛异常ValueError。 
注: 上述方法若使用int类型,值在[0, 255]。 
clear()   # 清空bytearray.  
reverse()   # 翻转bytearray,就地修改.
```

```python 
In [1]: b = bytearray()

In [2]: b.append(97)

In [3]: b
Out[3]: bytearray(b'a')

In [4]: bytearray(range(65, 91)).decode()
Out[4]: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

In [5]: bytearray(range(65, 91)).decode().lower()
Out[5]: 'abcdefghijklmnopqrstuvwxyz'

In [6]:
```

## 封装和解构   

封装： 定义一个元组, 可以省略小括号, 封装出来的一定是元组。

解构： 按照元素顺序, 把线性解构的元素, 赋值给变量。

**元素在左边是解构，元素在右边是封装。**

### python3的解构 

使用 `变量名` 接收,但不能单独使用, 被 `变量名` 收集后组成一个列表。

丢弃变量: 如果不关心一个变量, 就可以定义修改变量的名字为下划线 `_` 。这是一个惯例,是一个不成文的约定,不是标准. 

`_` 是一个合法的标识符,也可以作为一个有效的变量使用,但是定义成下划线就是希望不要被使用,除非你明确的知道这个数据需要被使用。

>  `_` 这个变量本身无任何语义,没有任何可读性,所以不是用来给人使用的。
>
>  python中很多库,都使用这个变量,使用十分广泛, 但是它会导致和库中的产生冲突, 所以不要在不明确变量作用域的情况下使用。 
>
>  [*_, a], _ = lst    # []或()都可以.

```python 
In [1]: _, [*_, a], _ = ['a', 'b', 'c']

In [2]: [*_, a]
Out[2]: ['c', 'b']

In [3]:
```

## 集合 - set 

> **约定:** 
>
> - set 翻译为集合。 
> - collections 翻译为集合类型,是一个大概念。 

### 概念 

> 可变, 无序, 不重复的元素的集合.   
>
> 定义及初始化: 
>
> - set() -> new empty set object. 
> - set(iterable) -> new set object. 
>
> set的元素要求必须可hash。
>
> set元素不可索引, 可迭代。

```python 
In [1]: s1 = set(range(5))

In [2]: s2 = set(list(range(5)))

In [3]: s1
Out[3]: {0, 1, 2, 3, 4}

In [4]: s2
Out[4]: {0, 1, 2, 3, 4}

In [5]: s3 = {(1, 2, 3), [1, 2, 3], {'name': 'amesy', 'sex': 'male'}}
TypeError                                 Traceback (most recent call last)
<ipython-input-9-b2999f24648f> in <module>()
——> 1 s3 = {(1, 2, 3), [1, 2, 3], {'name': 'amesy', 'sex': 'male'}}

TypeError: unhashable type: 'list' # set里面只能放置可哈希元素,list不可哈希,故报错.

In [6]: 
```

### 方法 - 增 

| 方法              | 功能               | 注释                         |
| --------------- | ---------------- | -------------------------- |
| add(elem)       | 增加一个元素elem到set中。 | 如果元素存在, 则什么也不做。            |
| update(*others) | 合并其他元素到set集合中。   | 参数others必须是可迭代对象。<br>原地修改。 |

### 方法 - 删 

| 方法            | 功能            | 注释                                       |
| ------------- | ------------- | ---------------------------------------- |
| remove(elem)  | 从set中移除第一个元素。 | 元素不存在, 则抛出KeyError异常,因为set中的元素被hash过,类似dict中的key。 |
| discard(elem) | 从set中移除一个元素。  | 元素不存在, 什么都不做。                            |
| pop()         | 移除并返回任意的元素。   | 空集则返回KeyError异常。<br>只能由pop随机移除，不能指定移除的元素对象。 |
| clear()       | 移除所有元素        |                                          |

### 方法 - 改, set元素不可重复,故没有修改方法,要么删除,要么加入新的元素. 

### 方法 - 查 

| 方法                                       |
| :--------------------------------------- |
| 非线性结构,无法索引。 <br>遍历: 可以迭代所有元素。<br>成员运算符: in和not in判断元素是否在set中。效率高。<br>list和set关于成员运算符的比较: set要比list效率高。<br>时间复杂度: 可以做到O(1)。set、dict等结构, 内部使用hash值作为key, ,查询时间与数据规模无关。<br>线性结构的查询时间复杂度是O(n), 即随着数据规模的增大而增加耗时。 |

### 集合运算
#### 并集: 

| 方法              | 功能               |
| --------------- | ---------------- |
| union(*others)  | 返回和多个集合合并后的新的集合。 |
| "\|"运算符重载       | 等同于union。        |
| update(*others) | 和多个集合合并,就地修改。    |
| \|=             | 等同于update。       |

#### 交集

| 方法                           | 功能                 |
| ---------------------------- | ------------------ |
| intersection(*others)        | 返回和多个集合的交集。        |
| &                            | 等同于intersection。   |
| intersection_update(*others) | 获取和多个集合的交集,并就地修改。  |
| &=                           | 等同于interse_update。 |

#### 差集
| 方法                         | 功能                    |
| -------------------------- | --------------------- |
| difference(*others)        | 返回和多个集合的差集。           |
| -                          | 等同于difference。        |
| difference_update(*others) | 获取和多个集合的差集并就地修改。      |
| -=                         | 等同于difference_update。 |

#### 对称差集
| 方法                                 | 功能                              |
| ---------------------------------- | ------------------------------- |
| symmetric_difference(other)        | 返回和另一个集合的差集。                    |
| ^                                  | 等同于symmetric_difference。        |
| symmetric_difference_update(other) | 获取和另一个集合的差集并就地修改。               |
| ^=                                 | 等同于symmetric_difference_update。 |

#### 其他操作 

| 方法                    | 功能                            |
| --------------------- | ----------------------------- |
| issubset(other)和"<="  | 判断当前集合是否是另一个集合的子集。            |
| set1 < set2           | 判断set1是否是set2的真子集。            |
| issuperset(other)和">= | 判断当前集合是否是other的真超集。           |
| set1 > set2           | 判断set1是否是set的真超集。             |
| isdisjoint(other)     | 判断当前集合和另一个集合有没有交集,没有交集返回True。 |

## 字典 - dict 

### 基本概念及初始化

基本概念: 

> key-value 键值对的数据的集合。
> 可变, 无序, key 不重复。
> 比 list 占内存。

初始化: 

```python 
d = dict()  或  d = {}      
dict(**kwargs)  # 使用name=value对初始化一个字典。
dict(iterable, **kwargs)  #使用可迭代对象和"name=value对"构造字典,不过可迭代对象的元素必须是一个二元结构。
>>> d = dict(((1,'a'),(2,'b'))) 或 d = dict(([1,'a'],[2,'b'])) 
dict(mapping,**kwarg)  # 使用一个字典构建另一个字典。
>>> d = {'a':10, 'b':20,'c':None,'d':[1,2,3]}   
# 类方法: 
dict.fromkeys(iterable,value) 
>>> d = dict.fromkeys(range(5))
>>> d = dict.fromkeys(range(5),0) 
```

```python 
In [1]: dict(name='amesy')
Out[1]: {'name': 'amesy'}
    
In [2]: dict((('age', 22), ('sex', 'male')))
Out[2]: {'age': 22, 'sex': 'male'}

In [3]: d = dict.fromkeys(range(5))

In [4]: d
Out[4]: {0: None, 1: None, 2: None, 3: None, 4: None}

In [5]: dd = dict.fromkeys(range(5), 'py')

In [6]: dd
Out[6]: {0: 'py', 1: 'py', 2: 'py', 3: 'py', 4: 'py'}

In [7]:
```

### 元素的访问

| 方法                        | 功能              | 注释                                       |
| ------------------------- | --------------- | ---------------------------------------- |
| d[key]                    | 返回key对应的值value。 | key不存在则抛出异常KeyError                      |
| get(key[,default])        | 返回key对应的值value。 | key不存在返回缺省值,如果没有缺省值就返回None。              |
| setdefault(key[,default]) | 返回key对应的值value  | **key不存在则添加kv对**, value为default,缺省值为None |

### 增加和修改元素 

| 方法                      | 功能                     | 注释                                       |
| ----------------------- | ---------------------- | ---------------------------------------- |
| d[key] = value          | 将key对应的值修改为value。      | key不存在则添加新的k/v对。                         |
| update([other]) -> None | 使用另一个字典other的kv对更新本字典。 | 就地修改。<br>key不存在,就添加。<br>key存在,覆盖已存在的key对应的值。 |

### 删除元素 

| 方法                 | 注释                                       |
| ------------------ | ---------------------------------------- |
| pop(key[,default]) | key存在,移除它,并返回它的value。<br> key不存在,返回给定的default。 <br> default未设置,key不存在则抛异常KeyError。 |
| popitem()          | 移除并返回一个任意的键值对。<br> 字典为empty,抛出异常KeyError |
| clear()            | 清空字典。                                    |

### 删除字典 

使用 `del 语句`

### 遍历字典 

`for ... in dict` 

> py3中, keys, values, items方法返回一个类似生成器的可迭代对象, 不会把函数的返回结果复制到内存中。 
>
> py2中,上面的方法会返回一个新的列表,占据新的内存空间.  
>
> 所以python2建议用 iterkeys, itervalues, iteritems 版本, 返回一个迭代器, 而不是一个copy。

```python 
In [1]: d = dict.fromkeys(range(3), 'py')
    
In [2]: d
Out[2]: {0: 'py', 1: 'py', 2: 'py'}

In [3]: [i for i in d]
Out[3]: [0, 1, 2]

In [4]: [i for i in d]
Out[4]: [0, 1, 2]

In [5]: [i for i in d.keys()]
Out[5]: [0, 1, 2]

In [6]: [i for i in d.values()]
Out[6]: ['py', 'py', 'py']

In [7]: [i for i in d.items()]
Out[7]: [(0, 'py'), (1, 'py'), (2, 'py')]

In [8]:
```

### 字典的key 

> 字典的key的要求和set的元素要求一致。
>
> hashable可哈希才能作为key。

### 工厂函数 - defaultdict 缺省字典

> defaultdict是Python内建dict类的一个子类。

```python 
# 用法:  
defaultdict(default_factory[, ...]) ——> dict with default factory.

# 第一个参数是default_factory,缺省是None,它提供一个初始化函数,可以是list,tuple,set和dict等。 
# 它的其他功能与dict相同,当key不存在时,会调用这个工厂函数来生成key对应的value,即提供一个默认值,从而避免KeyError异常. 
```

示例1：迭代1-100, 分类保存到字典中。 

方法1：

```python 
# 常规做法
d = {}
for i in range(100):
    if i > 50:
        if 'k1' not in d:
            d['k1'] = [i]
        else:
            d['k1'].append(i)
    else:
        if 'k2' not in d:
            d['k2'] = [i]
        else:
            d['k2'].append(i)

print(d)
```

方法2： 

```python 
# setdefault
d = {}
for i in range(100):
    if i > 50:
        d.setdefault('k1', [])
        d['k1'].append(i)
    else:
        d.setdefault('k2', [])
        d['k2'].append(i)

print(d)
```

方法3： 

```python 
from collections import defaultdict
d = defaultdict(list)
for i in range(100):
    d['k1'].append(i) if i > 50 else d['k2'].append(i)

print(d)
```

示例2： 

```python 
In [1]: from collections import defaultdict
   ...: lst = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
   ...: d = defaultdict(set)
   ...: for k, v in lst:
   ...:     d[k].add(v)
   ...: print(d)
   ...:
defaultdict(<class 'set'>, {'blue': {2, 4}, 'red': {1, 3}})

In [2]:
```

分析: 

```python 
collections.defaultdict(list)使用起来效果和运用dict.setdefault()比较相似。 
python help也提到了。 
工厂函数这种方法和dict.setdefault()等价，但是要更快。
defaultdict可以利用工厂函数，给初始keyi带来一个默认值,这个默认值也许是空的list[],defaultdict(list);也许是0, defaultdict(int). 
```
### 有序字典 - OrderedDict 

> python中的字典是无序的,因为它是按照hash来存储的,但collections模块自带的子类OrderedDict则可以很好的解决这个问题。

#### 示例

示例1： 

```python 
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])
```

示例2：

```python 
In [1]: from collections import OrderedDict

# regular unsorted dictionary
In [2]: d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# dictionary sorted by key 
In [3]: OrderedDict(sorted(d.items(), key=lambda t: t[0]))
Out[3]: OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

# dictionary sorted by value    
In [4]: OrderedDict(sorted(d.items(), key=lambda t: t[1]))
Out[4]: OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])

# dictionary sorted by length of the key string    
In [5]: OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
Out[5]: OrderedDict([('pear', 1), ('apple', 4), ('banana', 3), ('orange', 2)])

In [6]:
```

#### 方法 -  move_to_end

> Move an existing *key* to either end of an ordered dictionary. The item is moved to the right end if *last* is true (the default) or to the beginning if *last* is false. Raises `KeyError` if the *key* does not exist:

```python 
In [1]: name = 'amesy'

In [2]: '-'.join(name)
Out[2]: 'a-m-e-s-y'

In [3]: from collections import OrderedDict

In [4]: d = OrderedDict.fromkeys('abcde')

In [5]: d
Out[5]: OrderedDict([('a', None), ('b', None), ('c', None), ('d', None), ('e', None)])

In [6]: d.keys()
Out[6]: odict_keys(['a', 'b', 'c', 'd', 'e'])

In [7]: d.move_to_end('b')

In [8]: d
Out[8]: OrderedDict([('a', None), ('c', None), ('d', None), ('e', None), ('b', None)])

In [9]: ''.join(d.keys())
Out[9]: 'acdeb'

In [10]:
```


总结： 

```python 
OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。每次当一个新的元素插入进来的时候,它会被放到链表的尾部。对于一个已经存在的键的重复赋值不会改变键的顺序。
需要注意的是，一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维护着另外一个链表。 所以如果你要构建一个需要大量 OrderedDict 实例的数据结构的时候（比如读取 100,000 行 CSV 数据到一个 OrderedDict 列表中去）， 那么你就得仔细权衡一下是否使用 OrderedDict 带来的好处要大过额外内存消耗的影响。
```

## 解析式/推导式 

**作用** 

```python 
编译器会优化,不会因为简写而影响效率,反而因优化提高了效率。 
减少程序员工作量,减少出错。
简化代码,增强可读性。 
```

### 列表解析式

**语法**

```python 
[返回值 for 元素 in 可迭代对象 if 条件]
[返回值 for 元素 in 可迭代对象 if 条件1 if 条件2] 
[返回值 for 元素 in 可迭代对象 for 元素1 in 可迭代对象1]
# 使用中括号[],内部是for循环,if条件可选。
# 返回一个新的列表。 
```

### 集合解析式

**语法** 

```python 
{返回值 for 元素 in 可迭代对象 if 条件}
# 使用大括号{}。 
# 立即返回一个集合。  

用法: 
{(x,x+1) for x in range(10)} 
{[x] for x in range(10)}
```

### 字典解析式

**语法** 

```python 
{返回值 for 元素 in 可迭代对象 if 条件}
# 使用大括号{}。  
# 使用key:value形式。
# 立即返回一个字典。 

用法:
{x:(x,x+1) for x in range(10)}
{x:[x,x+1] for x in range(10)}
{(x,):[x,x+1] for x in range(10)}
{[x]:[x,x+1] for x in range(10)} 
{chr(0x41+x):x**2 for x in range(10)} 
```

示例： 

```python 
In [1]: {str(x):y for x in range(3) for y in range(4)}
Out[1]: {'0': 3, '1': 3, '2': 3}

In [2]: d = {}
   ...: for x in range(3):
   ...:     for y in range(4):
   ...:         d[str(x)] = y
   ...:

In [3]: d
Out[3]: {'0': 3, '1': 3, '2': 3}
```

## 迭代器

**可迭代对象(Iterable)** ：可重复迭代, 满足如下其中之一的都是iterable。

- 可以使用for循环。
- 可以按index索引的对象, 也就是定义了getitem方法，比如list, str等。
- 定义了iter方法。可以随意返回。
- 可以调用iter(obj)的对象，并且返回一个iterator。

> 可以迭代,但是未必有序,未必可索引. 
> 可迭代对象: list,tuple,str,bytes,bytearray,range,set,dict,iterator. 
> 可以使用成员操作符in和not in,in本质上就是在遍历对象.

**迭代器(Iterator)** ：可被next()函数调用并不断返回下一个值的对象，需满足如下要求。 

- 一定是可迭代对象,具备可迭代对象的特征。


- 定义了**iter**方法，但是必须返回自身，即通过iter方法把一个可迭代对象封装成迭代器。
- 定义了next方法来迭代 迭代器对象,。python3.x中是**next**。用来返回下一个值, 并且当没有数据了, 抛出StopIteration可以保持当前的状态。

迭代器就像一个懒加载的工厂，等到有人需要的时候才给它生成值返回，没调用的时候就处于休眠状态等待下一次调用。

```python 
In [1]: lst = [1, 2, 3]

In [2]: x = iter(lst)

In [3]: y = iter(lst)

In [4]: next(x)
Out[4]: 1

In [5]: next(x)
Out[5]: 2

In [6]: next(y)
Out[6]: 1

In [7]: type(lst)
Out[7]: list

In [8]: type(x)
Out[8]: list_iterator
```

**图示**

![iterator](http://mmbiz.qpic.cn/mmbiz_png/rO1ibUkmNGMmicyvqybd0qMIa0MqjOJ5192yVTFO3w2iczzC0YP3amodXLVX9TdFhZmCRQsMsw9dlKECiaEcDWuIUA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)



## 生成器 

- 带有 **yield** 关键字的的函数在 Python 中被称之为 generator(生成器)。Python 解释器会将带有 **yield** 关键字的函数视为一个 generator 来处理。一个函数或者子程序都只能 return 一次，但是一个生成器能暂停执行并返回一个中间的结果 —— *这就是 yield 语句的功能 : 返回一个中间值给调用者并暂停执行。*
- **生成器其实是一种特殊的迭代器**，不过这种迭代器更加优雅, 这句话反过来不成立。它不需要再像上面的类一样写 `__iter__()`和 `__next__()`方法了，只需要一个 `yiled`关键字。 生成器一定是迭代器（反之不成立），因此任何生成器也是以一种懒加载的模式生成值。



```python 
# generator
def arr(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a+b
        n += 1
res = arr(5)
for _ in range(5):
    print(next(res))
```

**分析：生成器 arr() 的执行过程**

- 执行语句 res = arr(5) 时，并不会马上执行 arr() 函数的代码块，而是首先返回一个 iterable 对象。
- 在 for 循环语句执行时，才会执行 fab() 函数的代码块。 
- 执行到语句 yield b 时，fab() 函数会返回一个迭代值，直到下次迭代前，程序流会回到 yield b 的下一条语句继续执行，然后再次回到 for 循环，如此迭代直到结束。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。 
- 由此可以看出，**生成器通过关键字 yield 不断的将迭代器返回到内存进行处理，而不会一次性的将对象全部放入内存，从而节省内存空间**。从这点看来生成器和迭代器非常相似，但如果更深入的了解的话，其实两者仍存在区别。

## 生成器表达式 

> 生成器表达式是列表解析的扩展，就如上所述：生成器是一个特定的函数, 允许返回一个中间值，然后挂起代码的执行，稍后再恢复执行。列表解析的不足在于，它必须一次性生成所有的数据，用以创建列表对象，所以不适用于迭代大量的数据。 **生成器表达式则通过结合列表解析和生成器来解决这个问题。**

**语法** 

```python 
# 列表解析式 
[expr for iter_var in iterable if cond_expr] 

# 生成器表达式 
(expr for iter_var in iterable if cond_expr)
```

**总结** 

> 两者的语法非常相似，但生成器表达式返回的不是一个列表类型对象，而是一个生成器对象，生成器是一个内存使用友好的结构。在需要迭代一个对象时，应该优先考虑使用生成器替代迭代器，使用生成器表达式替代列表解析。当然这并不是绝对的。迭代器和生成器是 Python 很重要的特性，对其有很好的理解能够写出更加 Pythonic 的代码。

## datetime模块 

### 功能

> 对日期、时间、时间戳的处理。 

### 用途 

> 在开发工作中，经常需要用到日期与时间，如： 
>
> - 作为日志信息的内容输出。
> - 计算某个功能的执行时间。
> - 用日期命名一个日志文件的名称。
> - 记录或展示某文章的发布或修改时间。
> - 其他。

### datetime类 

| 方法                              | 功能                                                         |
| --------------------------------- | ------------------------------------------------------------ |
| today()                           | 返回本地时区当前时间的datetime对象。                         |
| now(tz=None)                      | 返回当前时间的datetime对象, 时间到微妙, 如果tz为None, 返回和today()一样。 |
| utcnow()                          | 没有时区的当前时间。                                         |
| fromtimestamp(timestamp, tz=None) | 根据给定的时间戮, 返回一个datetime对象。                     |

示例： 

```python 
In [1]: import datetime

In [2]: datetime.datetime.now()
Out[2]: datetime.datetime(2018, 3, 5, 12, 43, 41, 76299)

In [3]: datetime.datetime.utcnow()
Out[3]: datetime.datetime(2018, 3, 5, 4, 43, 53, 488395)

In [4]: datetime.datetime.fromtimestamp(2018-3-5)
Out[4]: datetime.datetime(1970, 1, 1, 8, 33, 30)

In [5]:
```

### datetime对象 

> 构造方法: datetime.datetime(2018,3, 4, 11, 29, 43, 79043)
>
> year,  month, day, hour, minute, second, microsecond, 取datetime对象的年月日时分秒及微秒。

| 方法          | 功能                                                         |
| ------------- | ------------------------------------------------------------ |
| timestamp()   | 返回一个到微秒的时间戳。<br>时间戳: 格林威治时间"1970-01-01 00:00"到现在的秒数。 |
| weekday()     | 返回星期的天, 周一 0 ，  周日 6                              |
| isoweekday()  | 返回星期的天, 周一 1 ，  周日 7                              |
| date()        | 返回日期date对象。                                           |
| time()        | 返回时间time对象。                                           |
| replace()     | 修改并返回新的对象。                                         |
| isocalendar() | 返回一个三元组 (年, 周数, 周的天)                            |

```python 
In [1]: import datetime

In [2]: datetime.datetime.now().timestamp()
Out[2]: 1520225470.531848

In [3]: datetime.datetime.now().weekday()
Out[3]: 0

In [4]: datetime.datetime.now().time()
Out[4]: datetime.time(12, 52, 5, 53374)

In [5]: datetime.datetime.now().replace(2018, 3, 1, 9, 21, 55)
Out[5]: datetime.datetime(2018, 3, 1, 9, 21, 55, 569714)

In [6]: datetime.datetime.now().replace(2018-3-3)
Out[6]: datetime.datetime(2012, 3, 5, 12, 53, 55, 799515)

In [7]: datetime.datetime.now().isocalendar()
Out[7]: (2018, 10, 1)

In [8]:
```

### 日期格式化

> 类方法 strptime(date_string, format), 返回datetime对象。 
>
> 对象方法 strftime(format), 返回字符串。
>
> 字符串format函数格式化。

```python 
In [1]: import datetime

In [2]: datetime.datetime.strptime('20180305', '%Y%m%d')
Out[2]: datetime.datetime(2018, 3, 5, 0, 0)

In [3]: datetime.datetime.now().strftime('%Y-%m-%d')
Out[3]: '2018-03-05'

In [4]:
```

### timedelta对象 

datetime.timedelta 对象代表两个时间之间的的时间差，两个date或datetime对象相减时可以返回一个timedelta对象。

**构造函数**

```python 
class datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
# 所有参数可选，且默认都是0，参数的值可以是整数，浮点数，正数或负数。
```

> 内部只存储**days，seconds，microseconds**，其他参数的值会自动按如下规则抓转换：
>
> - 1 millisecond（毫秒） 转换成 1000 microseconds（微秒）
> - 1 minute 转换成 60 seconds
> - 1 hour 转换成 3600 seconds
> - 1 week转换成 7 days

**时间差** 

`total_seconds()` 获取两个时间之间的差的总秒数。 

```python 
In [1]: import datetime

In [2]: t1 = datetime.datetime.strptime("2018-03-05 10:30:00", "%Y-%m-%d %H:%M:%S")

In [3]: t2 = datetime.datetime.strptime("2018-03-05 12:30:00", "%Y-%m-%d %H:%M:%S")

In [4]: total_interval_time = (t2 - t1).total_seconds()

In [5]: total_interval_time
Out[5]: 7200.0

In [6]:
```

### 标准库 - time 

`time.sleep(SECOND)` 将调用线程挂起来等待指定的秒数。 

```python 
In [1]: import time

In [2]: time.sleep(1)  # 将等待1s.

In [3]:
```

## 常用的内建函数 

```python 
标识id: 返回对象的唯一标识,Cpython返回内存地址。  
哈希hash(): 返回一个对象的哈希值。 
类型type(): 返回对象的类型。 
类型转换:
	float(),int(),bin(),hex(),oct(),bool(),list(),tuple(),dict(),set(),bytes(),bytearray()
输入input([prompt]): 接收用户输入,返回一个字符串。 
打印: 
    print(*object,sep='', end='\n',file=sys.stdout,flush=False) 
    打印输出,默认使用空格分割,换行结尾,输出到控制台。
对象长度len(): 返回一个集合类型的元素个数。
isinstance(obj,class_or_tuple): 判断对象obj是否属于某种类型或者元组中列出的某个类型。
    isinstance(True, int)
issubclass(cls,class_or_tuple): 判断类型cls是否是某种类型的子类或元组中列出的耨个类型的子类。
    issubclass(bool, int) 
绝对值obs(x): x为数值。
最大值max(), 最小值min() 
	返回iterable对象中的最大或最小值. 
	返回多个参数中的最大或最小值. 
round(x) 返回浮点数x的四舍五入值。
pow(x, y): 等价于x**y. 
range() 创建一个整数列表，一般用在 for 循环中。
divmod(x, y): 等价于tuple(x//y,x%y) 
sum(iterable[,start]): 求和. 
chr(i): 给一个一定范围的整数返回对应的字符. 如chr(97), chr(2003). 
ord(c): 返回字符对应的整数. 如ord('a'), ord('中'). 
str(), repr(), ascii() 
sorted(): 排序. 
reversed(): 翻转. 
enumerate(): 枚举. 
iter(iterable): 迭代器 
next(iterator): 从一个迭代器中取元素,如果元素都取过了,再次取会抛异常Stopiteration. 
```

### 拉链函数 - zip 

**语法** 

```python 
zip(*iterables) ——> zip object
```

> 像拉链一样,把多个可迭代对象合并在一起,返回一个迭代器。
>
> 将每次从不同对象中取到的元素合并成一个元组。 

**示例** 

```python 
In [1]: x = [1, 2, 3]

In [2]: y = [4, 5, 6]

In [3]: zip(x, y)
Out[3]: <zip at 0x1e3f87272c8>  #　返回迭代器, 可用next()方法迭代。

In [4]: list(zip(x, y))
Out[4]: [(1, 4), (2, 5), (3, 6)]

In [5]:
```

```python
In [1]: list(zip(range(10), range(10), range(5), range(10)))
Out[1]: [(0, 0, 0, 0), (1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3), (4, 4, 4, 4)]

In [2]:
```

注 

> 要求x与y的维数相同，当两者具有相同的行数与列数时，正常组合对应位置元素。
> 当x与y的行数或列数不同时, 取两者结构中最小的行数和列数，依照最小的行数和列数将对应位置的元素进行组合。





**--- 以上, 就是python基础内容的总结。其中内容不完善之处，会不断更新添加修改。**







 