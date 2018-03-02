[TOC]

## 数字的处理函数

| 函数名         | 作用                                       |
| ----------- | :--------------------------------------- |
| sqrt()      | 取数字的平方根,返回值类型为float. (例如:import math; math.sqrt(9) -> 3.0). |
| divmod(x,y) | 这个函数也可以获得商和余数, 比如divmod(5,2)，返回的值为(2,1)，其中2为商，1为余数. |
| bin()       | 二进制.                                     |
| oct()       | 八进制.                                     |



## 列表, 链表, queue(队列), stack(栈)的差异:

**列表: ** 

根据索引查找比较快，从最后追加也很快，命中cpu缓存概率比较大. 插入很慢，删除也很慢.

**链表:** 

非线性结构,由前一个元素来获知下一元素的位置,不能使用索引. 

查找很慢,但空间不必连续. 插入,插入,尾部追加很快.

**队列: **

队列是一个先入先出的的数据结构, 类似于银行排队. 【pop(0)和append】

**栈: **

栈是一个后入先出/先入后出的数据结构,类似于洗碗堆盘子. 【append和pop()】



## 列表

列表元素可以是任意对象(数字,字符串,对象,列表等). 

列表内元素有顺序,可以使用索引. 

是一种线性的数据结构.

列表内元素可变, 使用[]表示.



**方法 - 增 **

L.append(object)    原地修改.  时间复杂度O(1).

L.insert(index, object)   原地修改.  

​	insert 时间复杂度不确定,但会引起内存结构变化,索引超界会将元素追加到开头或最后.  

​	链表适合插入操作, 因为不需要挪动位置.

L.extend(iterable)   原地修改. 

'+'  ---> list   连接两个列表,产生新的列表. 

'*'  --->  list  将本列表元素重复n次,重复操作,产生新的列表.   

**方法 - 删**



**方法 - 改**   



**方法 - 查**







```python 
In [123]: res1.sort(key=None, reverse=False)

TypeError Traceback (most recent call last)
<ipython-input-123-16bd8c3d3c94> in <module>()
----> 1 res1.sort(key=None, reverse=False)

TypeError: unorderable types: int() < str()

In [124]: res1.sort(key=str, reverse=False)

In [125]: res1
Out[125]: [1, 2, 3, 4, 5, 6, 7, 8, 'a', 'asd', 'b']

## In [127]: sorted(res1, key=int, reverse=False)

ValueError                                Traceback (most recent call last)
<ipython-input-127-b1e784651af8> in <module>()
----> 1 sorted(res1, key=int, reverse=False)

ValueError: invalid literal for int() with base 10: 'a'

In [128]: sorted(res1, key=str, reverse=False)
Out[128]: [1, 2, 3, 4, 5, 6, 7, 8, 'a', 'asd', 'b']

In [129]:
```







append、 reverse是O(1), 类似于双向列表。

len() 是O(1), 因为它内部有个字段是计数器。

'=='用值作比较. 
is用内存id作比较.

In [1]: a = 'aaa'

In [2]: b = 'aaa'

In [3]: id(a) is id(b)
Out[3]: False

In [4]: id(a) == id(b)
Out[4]: True

In [5]: id(a)
Out[5]: 2061831307192

In [6]: id(b)
Out[6]: 2061831307192

In [7]:

> > > id(id(a)) is id(id(b))  # False.



列表复制: L.copy() -> list — a shallow copy of L. 

```
shadow copy: 影子拷贝，也叫浅拷贝，遇到引用类型，只是复制了一个引用而已. 
```

深拷贝: copy模块提供了 deepcopy方法.
注: 浅拷贝在内存中只额外创建第一层数据.
深拷贝在内存中将所有的数据重新创建一份（排除最后一层,即: python内部对字符串和数字的优化）
注意引用类型. 

```
list定义: 赋值即定义(即动态语言和静态语言的差别)
list是可变的,所以不能被hash. 
list赋值等同于浅拷贝.

In [130]: res1
Out[130]: [1, 2, 3, 4, 5, 6, 7, 8, 'a', 'asd', 'b']

In [131]: import copy

In [132]: res = copy.deepcopy(res1)

In [133]: res
Out[133]: [1, 2, 3, 4, 5, 6, 7, 8, 'a', 'asd', 'b']

In [134]:
```

​	

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

### 元组

1. 一个有序的元素组成的集合. 
   2.使用小括号()表示. 
   3.元组是不可变对象(里面的引用类型可变).
   4.可理解为只读.
   支持索引(下标).

tuple() -> empty tuple 
tuple(iterable) -> tuple initialized from iterable's items. 

In [7]: ttt = (1,)  # 构造一个元素的元组时,不加逗号会被误认为其他类型,此处只是以数字为例.

元组只读，增删改的方法都没有 
支持： 

```
查找元素: T.index(value, [start, [stop]]) -> integer -- return first index of value.
注: 匹配到第一个就立即返回索引,匹配不到则报错ValueError.
统计次数: T.count(value) -> integer -- return number of occurrences of value. 
	注: 返回元组中匹配value的次数. 
时间复杂度: index和count方法都是O(n),随着元组规模增大,效率下降. 
len(tuple): 返回元组中元素的个数. 
```

命名元组： 
collections.namedtuple(typename, field_names, verbose=False, rename=False)  

typename：此元组的名称； 
field_names: 元祖中元素的名称,此字段有多种表达方式. 
rename:如果元素名称中含有python的关键字，则必须设置为rename=True.
verbose:默认就好；

# 其中field_names 有多种表达方式，如下

student=collections.namedtuple('student','name age sex')
student=cpllections.namedtuple('student',['name','age','sex'])
student=cpllections.namedtuple('student','name,age,sex')

In [1]: from collections import namedtuple

In [2]: student = namedtuple('student', ['name', 'age', 'sex'])

In [3]: student
Out[3]: __main__.student

In [4]: res = student(name = 'zhangsan', age = 22, sex = 'male')

In [5]: res
Out[5]: student(name='zhangsan', age=22, sex='male')

In [6]: "My name is %s, age is %s, sex is %s" % res
Out[6]: 'My name is zhangsan, age is 22, sex is male'

In [7]:

rename参数的作用：如果元素名称中含有python的关键字，则必须设置为rename=True.

In [29]: from collections import namedtuple

In [30]: color = namedtuple('color', 'all kind of  class color', rename = True)  # class是python关键字。

In [31]: other_color = namedtuple('color', 'all age and age',rename = True)  # and是python关键字，重复的age被重命名。

In [32]: color._fields
Out[32]: ('all', 'kind', 'of', '_3', 'color')

In [33]: other_color._fields
Out[33]: ('all', 'age', '_2', '_3')

In [34]:

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Point = namedtuple(‘Point’, [‘x’, ‘y’], verbose=True)

class Point(tuple):

```
'Point(x, y)'
```

```
__slots__ = ()
```

```
_fields = ('x', 'y')
```

```
def __new__(_cls, x, y):
    'Create new instance of Point(x, y)'
    return _tuple.__new__(_cls, (x, y))

@classmethod
def _make(cls, iterable, new=tuple.__new__, len=len):
    'Make a new Point object from a sequence or iterable'
    result = new(cls, iterable)
    if len(result) != 2:
        raise TypeError('Expected 2 arguments, got %d' % len(result))
    return result

def __repr__(self):
    'Return a nicely formatted representation string'
    return 'Point(x=%r, y=%r)' % self

def _asdict(self):
    'Return a new OrderedDict which maps field names to their values'
    return OrderedDict(zip(self._fields, self))

def _replace(_self, **kwds):
    'Return a new Point object replacing specified fields with new values'
    result = _self._make(map(kwds.pop, ('x', 'y'), _self))
    if kwds:
        raise ValueError('Got unexpected field names: %r' % kwds.keys())
    return result

def __getnewargs__(self):
    'Return self as a plain tuple.  Used by copy and pickle.'
    return tuple(self)

__dict__ = _property(_asdict)

def __getstate__(self):
    'Exclude the OrderedDict from pickling'
    pass

x = _property(_itemgetter(0), doc='Alias for field number 0')

y = _property(_itemgetter(1), doc='Alias for field number 1')
```

# ---------------------------------------------------------------------------------------------------------------------------------------------

冒泡算法。 
时间复杂度: O(n2).

字符串 str

```
S.strip([chars]) -> str
注: strip用于从字符串两端去除指定的字符串集chars中的所有字符.
	如果chars没有指定,则默认去除两端的空白字符.
从右开始: S.rstrip([chars]) -> str 
从左开始: S.lstrip([chars]) -> str

join连接字符串: S.join(iterable) -> str
注: 将可迭代对象连接起来,使用string作为分隔符.
可迭代对象元素本身都是字符串.
返回一个新的字符串.
In [19]: '@'.join('amesy')
Out[19]: 'a@m@e@s@y'

字符串分割 
		split系:
			S.split(sep=None, maxsplit=-1) -> list of strings
			注: 将字符串按照分隔符分割成若干字符串,并返回列表.
				从左至右
				sep指定分割字符串,缺省的情况下以空白字符串作为分隔符. 
				maxsplit指定分割的次数,-1表示遍历整个字符串.
			S.rsplit(sep=None, maxsplit=-1) -> list of strings 
			注: 从右往左, 其余和split用法一样. 
			S.splitlines([keepends]) -> list of strings
			注: 按照行来切分字符串. 
				keepends指是否保留行分隔符.
				行分隔符包括: \n, \r\n, \r等. 
				
			In [16]: name = 'amesyllsey'

			In [17]: name.split('es')
			Out[17]: ['am', 'yllsey']
```

```
		partition系:
			S.partition(sep) -> (head, sep, tail) 
			注: 将字符串按照分隔符分割成2段,返回这2段和分隔符的元组.
				从左到右,遇到分隔符就把字符串分割成两部分,返回头,分隔符,尾三部分的三元组;如果没有找到分隔符,就返回头,2个空元素的三元组. 
				sep分割字符串,必须指定.
			S.rpartition(sep) -> (head, sep, tail)
				注: 从右往左, 其余和partition用法一样.
				
		In [20]: name
		Out[20]: 'amesyllsey'

		In [21]: name.partition('es')
		Out[21]: ('am', 'es', 'yllsey')
				
	split和partition的区别： split不保留分割字符串,partition保留分割字符串；split后返回一个列表, partition返回一个元组。
```

```
字符串判断 
S.startswith(prefix[, start[, end]]) -> bool
	注: 在指定区间[start, end),字符串是否是prefix开头. 
S.endswith(suffix[, start[, end]]) -> bool 
注: 在指定区间[start, end),字符串是否是suffix结尾.

In [22]: name
Out[22]: 'amesyllsey'

In [23]: name.startswith('ames')
Out[23]: True
```

bytes 和 bytearray 

python3引入的两个新类型: 

```
bytes: 不可变字节序列. 
bytearray: 字节组,可变. 
```

字符串与bytes: 

```
字符串是以字符为单位进行处理的，bytes类型是以字节为单位处理的。
字符串是字符组成的有序序列,字符可以使用编码来理解. 
bytes是字节组成的有序的不可变序列. 
bytearray是字节组成的有序的可变序列.  
```

编码与解码: 

```
字符串按照不同的字符集编码encode返回字节序列bytes. 
	encode(encoding='utf-8', errors='strict') -> bytes. 
字节序列按照不同的字符集解码decode返回字符串. 
	bytes.decode(encoding='utf-8',errors='strict') -> str 
	bytearray.decode(encoding='utf-8',errors='strict') -> str
```

b = b''         # 创建一个空的bytes
b = byte()      # 创建一个空的bytes
b = b'hello'    #  直接指定这个hello是bytes类型
b = bytes('string',encoding='编码类型')  #利用内置bytes方法，将字符串转换为指定编码的bytes
b = str.encode('编码类型')   # 利用字符串的encode方法编码成bytes，默认为utf-8类型

bytes.decode('编码类型')：将bytes对象解码成字符串，默认使用utf-8进行解码。