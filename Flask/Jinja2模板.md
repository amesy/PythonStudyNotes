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
 { # 用来注释 #} <br />
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
html:
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
html:
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
html:
```html
<p>发表时间：{{ create_time|handle_time }}</p>
```

### 模板控制语句

所有的控制语句都是放在`{% ... %}`中，并且有一个语句`{% endxxx %}`来进行结束，`Jinja`中常用的控制语句有`if/for..in..`

#### if条件语句

i条件判断语句必须放在`{% if statement %}`中间，并且还必须有结束的标签`{% endif %}`。

和`python`中的类似，可以使用`>，<，<=，>=，==，!=`来进行判断，也可以通过`and，or，not，()`来进行逻辑合并操作。

示例：

```python
{% if score >= 90 %}
    <p>优秀</p>
{% elif score > 75 and score <90 %}
    <p>良好</p>
{% else %}
    <p>差</p>
{% endif %}
```

#### for循环语句

在jinja2中的for循环，跟python中的for循环一样，也是`for...in...`的形式。并且也可以遍历所有的序列以及迭代器。但唯一不同的是，jinja2中的for循环没有break和continue语句。

示例：

```python
@app.route("/")
def fors():
    info = {
        'books': [
            {
                'name': '三国演义',
                'author': '罗贯中',
                'price': 110
            }, {
                'name': '西游记',
                'author': '吴承恩',
                'price': 109
            }, {
                'name': '红楼梦',
                'author': '曹雪芹',
                'price': 120
            }, {
                'name': '水浒传',
                'author': '施耐庵',
                'price': 119
            }
        ]
    }

    return render_template("fors.html", **info)
```

html：

```html
<body>
    <table>
        <thead>
            <tr>
                <th>序号</th>
                <th>书名</th>
                <th>作者</th>
                <th>价格</th>
                <th>总数</th>
            </tr>
        </thead>
        <tbody>
            {% for book in books %}
                {% if loop.first %}
                    <tr style="background: red;">
                {% elif loop.last %}
                    <tr style="background: pink;">
                {% else %}
                    <tr>
                {% endif %}
                    <td>{{ loop.index0 }}</td>
                    <td>{{ book.name }}</td>
                    <td>{{ book.author }}</td>
                    <td>{{ book.price }}</td>
                    <td>{{ loop.length }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>

```

练习：九九乘法表

```python
<table border="1">
    <tbody>
        {% for x in range(1,10) %}
            <tr>
                {% for y in range(1,10) if y <= x %}
                    <td>{{ y }}*{{ x }}={{ x*y }}</td>
                {% endfor %}
            </tr>
        {% endfor %}
    </tbody>
</table>
```

### 宏和import语句

宏类似常规编程语言中的函数。它们用于把常用行为作为可重用的函数，取代手动重复的工作。

宏渲染表单元素的示例：

```html
<!--定义宏-->
{% macro input(name="", value="", type="text")   %}
    <input type="{{ type }}" name="{{ name }}" value="{{ value }}">
{% endmacro %}

<!--调用宏-->
<h1>用户登录</h1>
<table>
    <tbody>
        <tr>
            <td>用户名：</td>
            <td>{{ input('username') }}</td>
        </tr>
        <tr>
            <td>密码：</td>
            <td>{{ input("password",type="password") }}</td>
        </tr>
        <tr>
            <td></td>
            <td>{{ input(value="提交",type="submit") }}</td>
        </tr>
    </tbody>
</table>
```

**import - 导入宏**

1. `import "宏文件的路径" as xxx`。
2. `from '宏文件的路径' import 宏的名字 [as xxx]`。
3. 宏文件路径，不要以相对路径去寻找，都要以`templates`作为绝对路径去找。
4. 如果想要在导入宏的时候，就把当前模板的一些参数传给宏所在的模板，那么就应该在导入的时候使用`with context`。示例：`from 'xxx.html' import input with context`。

### include语句

`include`语句可以把一个模板引入到另外一个模板中，类似于把一个模板的代码copy到另外一个模板的指定位置。

`include`标签，如果想要使用父模版中的变量，直接用就可以使用，不需要使用`with context`。

`include`的路径，跟`import`一样，直接从`templates`根目录下去找，不要以相对路径去找。

示例：

html

```html
<body>
    {% include "common/header.html" %}
    <div class="content">
        中间的
    </div>
    {% include "common/footer.html" %}
</body>
```

### set语句和with语句

想要在模板中添加变量就需要使用到赋值语句（set）。

示例如下：

html

```html
{% set username='amesy' %}
<p>用户名：{{ username }}</p>
```
>   一旦定义了这个变量，那么在后面的代码中都可以使用这个变量，就类似于Python的变量定义。
>
>   set 还可以赋值列表和元组。

赋值语句创建的变量在其之后都是有效的，如果不想让一个变量污染全局环境，可以使用`with`语句来创建一个内部的作用域，将`set`语句放在其中，这样创建的变量只在`with`代码块中才有效。

示例：

html

```html
{% with classroom = 'first class' %}
<p>班级：{{ classroom }}</p>
{% endwith %}
```

with语句也不一定要跟一个变量，可以定义一个空的with语句，以后在with块中通过set定义的变量，就只能在这个with块中使用了：

```html
{% with %}
    {% set classroom = 'second class' %}
    <p>班级：{{ classroom }}</p>
{% endwith %}
```
### 加载静态文件

Web应用中会出现大量的静态文件来使得网页更加生动美观。静态文件主要包括有`CSS`样式文件、`JavaScript`脚本文件、图片文件、字体文件等静态资源。

加载静态文件使用的是`url_for`函数。然后第一个参数需要为`static`，第二个参数需要为一个关键字参数`filename='路径'`。

示例：

html

```html
<head>
    <meta charset="UTF-8">
    <title>example</title>
    <link rel="stylesheet" href="{{ url_for('static',filename="css/index.css") }}">
    <script src="{{ url_for("static",filename='js/index.js') }}"></script>
</head>
<body>
<img src="{{ url_for("static",filename='imgs/buyudaren.jpg') }}" alt="">
</body>
```

注：路径查找，要以当前项目的`static`目录作为根目录。

### 模板继承

Flask中的模板可以继承。通过继承可以把模板中许多重复出现的元素抽取出来，放在父模板中，并且父模板通过定义block给子模板开一个口，子模板根据需要，再实现这个block。 这样以后修改起来也比较方便。

**模板继承语法**

使用`extends`语句，来指明继承的父模板。父模板的路径，也是相对于`templates`文件夹下的绝对路径。示例代码如下：

```html
{% extends "base.html" %}
```

**block语法**

一般在父模板中会定义一些公共的代码。子模板可能要根据具体的需求实现不同的代码时，父模版就应该有能力提供一个接口给子模板用。从而实现具体业务需求的功能。

在父模板中：

```html
{% block block的名字 %}
{% endblock %}
```

在子模板中：

```html
{% block block的名字 %}
{% endblock %}
```

**调用父模版代码block中的代码**

默认情况下子模板如果实现了父模板定义的block，那么如果子模板block中也实现了与父模板中相同功能的代码，这时子模板就会覆盖掉父模板中的代码。如果想要在子模板中仍然保持父模板中的代码，那么可以使用`{{ super() }}`来实现。

示例如下：

父模板：

```html
{% block body_block %}
        <p style="background: red;">这是父模板中的代码</p>
    {% endblock %}
```

子模板：

```html
{% block body_block %}
    {{ super() }}
    <p style="background: green;">我是子模板中的代码</p>
{% endblock %}
```

**调用另外一个block中的代码**

如果想要在另外一个模版中使用其他模版中的代码。那么可以通过`{{ self.其他block名字() }}`。

示例代码如下：

```html
{% block title %}
    这里是标题
{% endblock %}

{% block body_block %}
    {{ self.title() }}
    <p style="background: green;">我是子模板中的代码</p>
{% endblock %}
```

**其他注意事项**
- 子模板中的代码，第一行应该是`extends`。
- 子模板中，如果要实现自己的代码，应该放到block中。如果放到其他地方，则不会被渲染。

