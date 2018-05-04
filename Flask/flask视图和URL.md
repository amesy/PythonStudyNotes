## Web基础
## 开发环境搭建
主要是在windows操作系统下开发，用到的python版本为3.6。编辑器为最新版的pycharm专业版（推荐）。

通过`pip install Flask`安装最新版的Flask。目前为止，最新版本为0.12.2。可以通过以下方式验证是否安装成功：

```python
>>> import flask
>>> flask.__version__
>>> '0.12.2'
```
如果显示0.12.2，则说明已经安装成功。

## 第一个flask程序
用pycharm新建一个flask项目，如下图：

![picture1](https://raw.githubusercontent.com/amesy/PythonStudyNotes/master/images/flask/img01.png)

然后单击"创建"即可。
创建完成后，新建helloworld.py文件编写第一个flask程序：
```python
# 从flask框架中导入Flask类.
from flask import Flask

# 传入__name__初始化一个Flask实例.
app = Flask(__name__)

# app.route装饰器映射URL和要执行的函数。这个设置将根URL映射到了hello_world函数上.
@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    # 运行本项目，自定义host、port和debug模式。默认的host是127.0.0.1，port为5000,debug为False.
    app.run(host="0.0.0.0", port=9000, debug=True)
```

然后在浏览器中输入 http://127.0.0.1:9000 就能看到hello world页面了。

注：app.run这种方式只适合本地开发，如果在生产环境中，应该使用Gunicorn或者uWSGI来启动。如果是在终端运行的，可以按ctrl+c来让服务停止。

**设置DEBUG模式**

1. 代码中如果抛出了异常，在浏览器的页面中可以看到具体的错误信息，以及具体的错误代码位置。方便开发者调试。
2. 在`Python`代码中修改了任何代码，只要按`ctrl+s`，`flask`就会自动的重新加载整个网站。不需要手动点击重新运行。

**配置DEBUG模式的四种方式**
1. 在`app.run()`中传递一个参数`debug=True`就可以开启`debug`模式。
2. 直接在应用对象上设置`app.debug=True`来开启`debug`模式。
3. 通过配置参数的形式设置DEBUG模式：`app.config.update(DEBUG=True)`。
4. 通过配置文件的形式设置DEBUG模式：`app.config.from_object(config)`。

**PIN码**

如果想要在网页上调试代码，则应该输入`PIN`码。
如图在程序中写有bug的代码，执行后在浏览器访问:

```python
from flask import Flask

app = Flask(__name__)
# app.debug=True
app.config.update(DEBUG=True)

@app.route('/')
def hello_world():
    a = 1
    b = 0
    c = a / b
    return c


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000)
```

(![img02](https://raw.githubusercontent.com/amesy/PythonStudyNotes/master/images/flask/img02.png))

然后在弹出的框中输入pycharm的运行状态栏中的Debugger PIN，即可进行调试操作。

(![img03](https://raw.githubusercontent.com/amesy/PythonStudyNotes/master/images/flask/img03.png))

## 配置文件
Flask项目的配置，都是通过`app.config`对象来进行配置的。比如使用`app.config.update(DEBUG=True)`来配置项目处于DEBUG模式。在Flask项目中，有四种方式进行项目的配置：
1. 直接硬编码

```python
app = Flask(__name__)
app.config['DEBUG'] = True
```
2. 通过update方法

因为app.config是flask.config.Config的实例，而Config类是继承自dict，因此可以通过update方法：

```python
app.config.update(
   DEBUG=True,
   SECRET_KEY='...'
)
```
3. 使用专门的配置文件存储配置项

当项目配置项特别多时，可以把所有的配置项都放在一个模块中，然后通过加载模块的方式进行配置，假设有一个settings.py模块，专门用来存储配置项的，此时就可以通过app.config.from_object()方法进行加载，并且该方法既可以接收模块的字符串名称，也可以是模块对象：

```python
# 1. 通过模块字符串
app.config.from_object('settings')
# 2. 通过模块对象
import settings
app.config.from_object(settings)

```
4. 通过app.config.from_pyfile()方法加载配置文件

```python
app.config.from_pyfile('settings.py',silent=True)
# silent=True表示如果配置文件不存在的时候不会抛出异常，默认是为False，会抛出异常。
```
注：  
- settings.py文件的后缀名不能少。
- 这种方式加载配置文件，不局限于只能使用`py`文件，普通的`txt`文件同样也适合。

flask具体的内置配置项，[点这里](http://flask.pocoo.org/docs/0.12/config/#builtin-configuration-values)查看

## URL与视图函数的映射
传递参数的语法：`/<参数名>/`。然后在视图函数中，也要定义同名的参数。

**参数的数据类型**
1. 如果没有指定具体的数据类型，那么默认就是使用`string`数据类型。
2. `int`数据类型只能传递`int`类型。
3. `float`数据类型只能传递`float`类型。
4. `path`数据类型和`string`有点类似，都是可以接收任意的字符串，但是`path`可以接收路径，也就是说可以包含斜杠。
5. `uuid`数据类型只能接收符合`uuid`的字符串。`uuid`是一个全宇宙都唯一的字符串，一般可以用来作为表的主键。
6. `any`数据类型可以在一个`url`中指定多个路径。

**具体示例如下**
```python
@app.route('/')
def hello_world():
    return "Hello World"

@app.route("/list")
def article_list():
    return "article list"

@app.route("/p/<float:article_id>")
def article_detail(article_id):
    return "你请求的文章是：{}".format(article_id)

@app.route("/article/<path:test>/")
def test_article(test):
    return "test article: {}".format(test)

# uuid示例: a8098c1a-f86e-11da-bd1a-00112444be1e.
# uuid问题：https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python
@app.route("/u/<uuid:user_id>/")
def user_detail(user_id):
    return "用户个人中心页面：{}".format(user_id)

# /blog/<id>/
# /user/<id>/
@app.route("/<any(blog, articles):url_path>/<id>/")
def detail(url_path, id):
    if url_path == "blog":
        return "博客详情：{}".format(id)
    else:
        return "文章详情."

# http://127.0.0.1:9000/d?wd=abcdfg&ie=utf8
@app.route("/d")
def d():
    wd = request.args.get("wd")
    ie = request.args.get("ie")
    print("ie: {}".format(ie))
    return '您通过查询字符串的方式传递的参数是：{}'.format(wd)
```
注：如果页面的想要做`SEO`优化，即想要被搜索引擎搜索到，则推荐使用path的形式（将参数嵌入到路径中）。如果不在乎搜索引擎优化，就可以使用查询字符串的形式（?key=value）。

**Python下UUID字符串的生成**
```python
In [1]: import uuid

In [2]: uuid.uuid4()
Out[2]: UUID('177f4749-0a08-4d3f-9423-86c0e996b6e8')

In [3]: uuid.uuid4()
Out[3]: UUID('9850a800-5168-43da-87d4-ccd8a305971e')

In [4]:
```

## 构造URL（url_for）
**url_for的基本使用**  
`url_for`的第一个参数是视图函数的名字的字符串。后面的参数被用来传递给`url`。如果传递的参数之前在`url`中已经定义了，那么这个参数就会被当成`path`的形式给到`url`。如果这个参数之前没有在`url`中定义，那么将变成以查询字符串的形式放到`url`中。
```python
@app.route("/")
def hello_world():
    return url_for('my_list',page=1,count=2)

@app.route('/post/list/<page>/')
def my_list(page):
    return 'my list'
```
浏览器访问：http://127.0.0.1:9000/  -> /post/list/1/?count=2

**url_for的作用**  
- 未来如果修改了`URL`，但没有修改该URL对应的函数名，就不用到处去替换URL了。
- `url_for`会自动的处理那些特殊的字符，不需要手动去处理。

 ```python
 url = url_for('login',next='/')
 # 会自动的将/编码，不需要手动去处理。
 # url=/login/?next=%2F
 ```
最后，强烈建议以后在处理url的时候，使用`url_for`来反转url。

## 自定义URL转换器
自定义URL转换器多用在Flask内置数据类型的转换器不能满足当前需求的情况。

**自定义URL时的注意事项**
- 转换器是一个类，且必须继承自werkzeug.routing.BaseConverter。
- 在转换器类中，实现to_python(self,value)方法，这个方法的返回值将会传递到view函数中作为参数。
- 在转换器类中，实现to_url(self,values)方法，这个方法的返回值将会在调用url_for函数的时候生成符合要求的URL形式。

**示例1：自定义URL匹配手机号码格式转换器**
```python
from flask import Flask
from werkzeug.routing import BaseConverter


app = Flask(__name__)

class TelephoneConveter(BaseConverter):
    regex = r'1[34578]\d{9}'

app.url_map.converters['tel'] = TelephoneConveter

@app.route("/telephone/<tel:my_tel>/")
def my_tel(my_tel):
    return "您的手机号码是：{}".format(my_tel)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
```
浏览器访问：http://127.0.0.1:9000/telephone/13683137989/

**示例2：**
普通方法：
```python
@app.route("/posts/<boards>/")
def posts(boards):
    res = boards.split("+")
    print(res)
    return "提交的结果是：{}".format(res)
```
http://127.0.0.1:9000/posts/a+b/  ->  提交的结果是：['a', 'b']

当有多个视图函数都要实现类似功能时，就要写多次split方法。这时就可以使用自定义URL的方式实现：
```python
from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class ListConveter(BaseConverter):
    def to_python(self, value):
        value = value.split("+")
        return value

app.url_map.converters['list'] = ListConveter

@app.route("/posts/<boards>/")
def posts(boards):
    return "提交的结果是：{}".format(boards)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
```
反转URL：
```python
from flask import Flask, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class ListConveter(BaseConverter):
    def to_url(self, value):
        return "+".join(value)

app.url_map.converters['list'] = ListConveter

@app.route("/")
def helloworld():
    return url_for("posts", boards=['a', 'b'])

@app.route("/posts/<list:boards>/")
def posts(boards):
    return boards

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
```
