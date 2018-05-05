## flask模板
在视图函数章节，视图函数只是直接返回文本，而在实际生产环境中很少这样用，因为实际的页面大多是带有样式和复杂逻辑的HTML代码，这可以让浏览器渲染出非常漂亮的页面。目前市面上有非常多的模板系统，其中最知名最好用的就是Jinja2和Mako，这里先简要比较下两个模板的特点和不同：

- Jinja2：Jinja是日本寺庙的意思，并且寺庙的英文是temple和模板的英文template的发音类似。Jinja2是由Flask的作者开发的仿Django模板的一个模板引擎。它速度快且被广泛使用，并且提供了可选的沙箱模板来保证执行环境的安全，它有以下优点：

    * 让前后端开发分离，独立开发。
    * 减少Flask项目代码的耦合性，页面逻辑放在模板中，业务逻辑放在视图函数中，将页面逻辑和业务逻辑解耦有利于代码的维护。
    * 提供了控制语句、继承等高级功能，减少开发的复杂度。

- Marko：Marko是另一个知名的模板。它从Django、Jinja2等模板借鉴了很多语法和API，特点如下：

    * 性能和Jinja2相近，在这里可以看到。
    * 有大型网站使用成功的案例。例如Reddit和豆瓣等公司都在使用。
    * 有知名的web框架支持。Pylons和Pyramid这两个web框架内置模板就是Mako。
    * 支持在模板中写几乎原生的Python语法的代码，对Python工程师比较友好，开发效率高。
    * 自带完整的缓存系统。当然也提供了非常好的扩展借口，很容易切换成其他的缓存系统。

### flask渲染模板

**安装Jinja2模板**

jinja2是flask的一个依赖,安装flask时会一并安装。也可以单独安装：

```shell
> pip install jinja2
```

**渲染Jinja2模板**
Jinja模板是简单的一个纯文本文件（html/xml/csv...），不仅仅是用来产生html文件，后缀名也不固定。当然，尽量命名为模板正确的文件格式，增加可读性。   

1. 模板放在`templates`目录下；
2. 从flask模块中导入`render_template`函数；
3. 在视图函数中,使用`render_template`。
4. 关于路径: 只需填写模板名称,flask会自动找templates文件夹下对应的文件。

示例1：
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/login/")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
```
当访问/login/的时候，login()函数会在当前目录下的templates文件夹下寻找login.html模板文件。如果想更改模板文件地址，应该在创建app的时候给Flask传递一个关键字参数template_folder，然后指定具体的路径，示例如下：

```python
from flask import Flask,render_template

app = Flask(__name__,template_folder=r'C:\templates')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
```
以上例子将会在C盘的templates文件夹中寻找模板文件。

示例2：
```python
@app.route('/')
def index():
    class Person:
        name = 'yangbin'
        age = "23"

    p = Person()

    context = {
        "username": "amesy",
        "age": 21,
        "gender": "male",
        "person": p,
        "websites": {
            'baidu': "baidu.com",
            'google': "google.com"
        }
    }
    return render_template('index.html', **context)
```

index.html代码内容：
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>amesy</title>
</head>
    <body>
        Hello World, 模板由templates渲染.
        <h2> username: {{username}}</h2>
        <h2> age: {{age}}</h2>
        <h2> gender: {{gender}}</h2>

        <br>
        <h3> name: {{person.name}}</h3>
        <h3> age: {{person.age}}</h3>

        <br>
        <h3> baidu: {{websites.baidu}}</h3>
        <h3> google: {{websites.google}}</h3>
    </body>
</html>
```

从以上示例可以看到，在使用`render_template`渲染模版时可以传递关键字参数。然后就可以直接在模版中使用了。如果参数过多，那么可以将所有的参数放到一个字典中，然后在传这个字典参数的时候使用两个星号，将字典解构成关键字参数。

### 模板中使用url_for

模版中的`url_for`和后台视图函数中的`url_for`使用起来基本一样，也是传递视图函数的名字，当然也可以传递参数。
使用的时候，需要在`url_for`左右两边加上一个`{{ url_for('FUNC_NAME') }}`。

示例如下：

```python
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login/<id>/")
def login(id):
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)
```

index.html代码如下：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>index</title>
</head>
	<body>
		这是从模版中渲染的.
		<p><a href="{{ url_for('login',ref='/',id='1') }}">登录</a></p>
	</body>
</html>
```

login.html代码如下：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>login</title>
</head>
    <body>
        <h1>这是登录页面！</h1>
    </body>
</html>
```

模板语法规则:

>{{ 用来存放变量 }} <br />
{# 用来注释 #} <br />
{% 用来执行函数或者逻辑代码 %} <br />

属性访问规则：

1. 比如在模板中有一个变量这样使用：foo.bar，那么在Jinja2中是这样进行访问的：

    - 先去查找foo的bar这个属性，也即通过getattr(foo,'bar')。
    - 如果没有，就去通过foo.__getitem__('bar')的方式进行查找。
    - 如果以上两种方式都没有找到，返回一个undefined。
在模板中有一个变量这样使用：foo['bar']，那么在Jinja2中是这样进行访问：

2. 通过foo.__getitem__('bar')的方式进行查找。
    - 如果没有，就通过getattr(foo,'bar')的方式进行查找。
    - 如果以上没有找到，则返回一个undefined。

### Jinja2模版过滤器

过滤器主要用在模版中对一些变量进行处理，类似于Python中的函数一样，可以将这个值传到函数中，然后做一些操作。在模版中，过滤器相当于是一个函数，把当前的变量传入到过滤器中，然后过滤器根据自己的功能，再返回相应的值，之后再将结果渲染到页面中。

基本语法：`{{ variable|过滤器名字 }}`，使用管道符号`|`进行组合使用。例如：{{ name|length }}，将返回name的长度。过滤器相当于一个函数，把当前的变量传入到过滤器中，然后过滤器根据自己的功能，再返回相应的值，之后再将结果渲染到页面中。Jinja2中内置了许多过滤器，官网如下：
http://jinja.pocoo.org/docs/2.10/templates/#list-of-builtin-filters

部分如下：

-abs(value)：返回一个数值的绝对值。 例如：-1|abs。

-default(value,default_value,boolean=false)：如果当前变量没有值，则会使用参数中的值来代替。name|default('xiaotuo')——如果name不存在，则会使用xiaotuo来替代。boolean=False默认是在只有这个变量为undefined的时候才会使用default中的值，如果想使用python的形式判断是否为false，则可以传递boolean=true。也可以使用or来替换。

-escape(value)或e：转义字符，会将<、>等符号转义成HTML中的符号。例如：content|escape或content|e。

- first(value)：返回一个序列的第一个元素。names|first。

- format(value,*arags,**kwargs)：格式化字符串。例如以下代码：

  `{{ "%s" - "%s"|format('Hello?',"Foo!") }}将输出：Hello? - Foo!`
- last(value)：返回一个序列的最后一个元素。示例：names|last。

- length(value)：返回一个序列或者字典的长度。示例：names|length。

- join(value,d=u'')：将一个序列用d这个参数的值拼接成字符串。

- safe(value)：如果开启了全局转义，safe过滤器会将变量关掉转义。示例：content_html|safe。

- int(value)：将值转换为int类型。

- float(value)：将值转换为float类型。

- lower(value)：将字符串转换为小写。

- upper(value)：将字符串转换为小写。

- replace(value,old,new)： 替换将old替换为new的字符串。

- truncate(value,length=255,killwords=False)：截取length长度的字符串。

- striptags(value)：删除字符串中所有的HTML标签，如果出现多个空格，将替换成一个空格。

- trim：截取字符串前面和后面的空白字符。

- string(value)：将变量转换成字符串。

- wordcount(s)：计算一个长字符串中单词的个数。

示例：

```python
app = Flask(__name__)
# 更改模板时重新加载。
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    context = {
        "position": -9,
        "lst": [1, 3, 5, 7],
        "name": "amesy",
        "age": 20,
        "article": "这是一篇文章的部分内容。",
        "signature": "<script>alert('hello')</script>"
        "create_time": datetime(2017,5,5,18,30,0),
    }

    return render_template("index.html", **context)
```

```html
<body>
    <p>位置的绝对值是：{{ position | abs }}</p>
    <p>该序列的第一个元素是：{{ lst | first }}</p>
    <p>该序列的最后一个元素是：{{ lst | last }}</p>
    <p>该序列的长度是：{{ lst | length }}</p>
    <p>该序列拼接成的字符串是：{{ lst | join("") }}
    <p>修改后的字符串：{{ lst | replace(3, 33)}}
    <p>{{ "我的名字叫：%s" | format(name)}}</p>
    {% if age > 21 %}
        <p>年龄是：{{ age }}, 大于21岁</p>
    {% else %}
        <p>年龄是：{{ age }}, 小于21岁</p>
    {% endif %}
    <p>原字符串为：{{ article }}，截取后的字符串为：{{ article | truncate(length=5) }}</p>
    <p>{{ signature | striptags }}</p>
</body>
```

### 自定义模板过滤器
过滤器本质上就是一个函数。如果在模版中调用这个过滤器，那么就会将这个变量的值作为第一个参数传给过滤器这个函数，然后函数的返回值会作为这个过滤器的返回值。需要使用到一个装饰器：`@app.template_filter`。

```python
@app.template_filter("cut")
def cut(value):
    value = value.replace("hello", "你好")
    return value
```

```html
<p>{{ signature | cut | striptags}}</p>
```

**自定义时间过滤器**

```python
@app.template_filter('handle_time')
def handle_time(time):
    """
    time距离现在的时间间隔
    1. 如果时间间隔小于1分钟以内，那么就显示“刚刚”
    2. 如果是大于1分钟小于1小时，那么就显示“xx分钟前”
    3. 如果是大于1小时小于24小时，那么就显示“xx小时前”
    4. 如果是大于24小时小于30天以内，那么就显示“xx天前”
    5. 否则就是显示具体的时间 2017/10/20 16:15
    """
    if isinstance(time,datetime):
        now = datetime.now()
        timestamp = (now - time).total_seconds()
        if timestamp < 60:
            return "刚刚"
        elif timestamp>=60 and timestamp < 60*60:
            minutes = timestamp / 60
            return "%s分钟前" % int(minutes)
        elif timestamp >= 60*60 and timestamp < 60*60*24:
            hours = timestamp / (60*60)
            return '%s小时前' % int(hours)
        elif timestamp >= 60*60*24 and timestamp < 60*60*24*30:
            days = timestamp / (60*60*24)
            return "%s天前" % int(days)
        else:
            return time.strftime('%Y/%m/%d %H:%M')
    else:
        return time
```

```html
<p>发表时间：{{ create_time|handle_time }}</p>
```
