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

## URL唯一
Flask的URL规则是基于`Werkzeug`的路由模块。这个模块的思想是基于Apache以及更早的HTTP服务器的主张，希望保证优雅且唯一的URL。

在定义url的时候，一定要记得在最后加一个斜杠(/)。
- 如果加了斜杠，在浏览器中访问这个url时结尾不加斜杠，会被重定向到带斜线的URL上去。这样有助于避免搜索引擎搜索同一个页面两次。
- 如果不加斜杠，在浏览器中访问这个url时结尾加了斜杠，就会产生一个404（"Not Found"）错误。这样用户体验不太好。
- 搜索引擎会将不加斜杠的和加斜杠的视为两个不同的url。而其实加和不加斜杠的都是同一个url，这样就会给搜索引擎造成误解。加了斜杠，就不会出现没有斜杠的情况。

## 指定HTTP请求
在网络请求中有许多请求方式，比如：GET、POST、DELETE、PUT等。最常用的就是`GET`和`POST`请求。
- `GET`请求：只会在服务器上获取资源，不会更改服务器的状态。这种请求方式推荐使用`GET`请求。
- `POST`请求：会给服务器提交一些数据或者文件。一般POST请求是会对服务器的状态产生影响，这种请求推荐使用`POST`请求。

- 关于参数传递：
    * `GET`请求：把参数放到`url`中，通过`?key=value`的形式传递。因为会把参数放到url中，不太安全。

    * `POST`请求：把参数放到`Form Data`中。避免了被偷瞄的风险，但是如果别人想要偷看你的密码，其实可以通过抓包的形式。因为POST请求可以提交一些数据给服务器，比如可以发送文件，那么这就增加了安全风险。所以POST请求，对于那些有经验的黑客来讲，其实是更不安全的。说它安全是相对于GET请求而言的。

- 在Flask中，`route`方法默认只能使用`GET`的方式请求这个url，如果想要设置自己的请求方式，那么应该传递一个`methods`参数。

注：method参数是一个列表的形式。
```python
@app.route('/login/',methods=['GET','POST'])
def login():
    pass
```
以上装饰器将让login的URL既能支持GET又能支持POST。

## 页面跳转和重定向
重定向分为永久性重定向和临时性重定向，在页面上体现的操作就是浏览器会从一个页面自动跳转到另外一个页面。比如用户访问了一个需要权限的页面，但是该用户当前并没有登录，因此我们应该给他重定向到登录页面。

- 永久性重定向：http的状态码是301，多用于旧网址被废弃了要转到一个新的网址确保用户的访问，最经典的就是京东网站，你输入www.jingdong.com的时候，会被重定向到www.jd.com，因为jingdong.com这个网址已经被废弃了，被改成jd.com，所以这种情况下应该用永久重定向。
- 临时性重定向：http的状态码是302，表示页面的临时性跳转。比如访问一个需要权限的网址，如果当前用户没有登录，应该重定向到登录页面，这种情况下，应该用临时性重定向。

在flask中，重定向通过flask.redirect(location,code=302)这个函数来实现，location表示需要重定向到的URL，应该配合之前讲的url_for()函数来使用，code表示采用哪个重定向，默认是302也即临时性重定向，可以修改成301来实现永久性重定向。

```python
from flask import Flask, url_for, request, redirect
from werkzeug.routing import BaseConverter


app = Flask(__name__)

@app.route("/login/", methods=["get", "post"])
def login():
    return "login page"


@app.route("/profile/", methods=["get", "post"])
def profile():
    name = request.args.get("name")
    if not name:
        return redirect(url_for("login"))
    else:
        return name


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
```
http://127.0.0.1:9000/profile/?name=amesy  -> amesy

## 响应（Response）
视图函数的返回值会被自动转换为一个响应对象，Flask的转换逻辑如下：

- 如果返回的是一个合法的响应对象，则直接返回。

- 如果返回的是一个字符串，那么Flask会重新创建一个`werkzeug.wrappers.Response`对象，Response将该字符串作为主体，状态码为200，MIME类型为text/html，然后返回该Response对象。

- 如果返回的是一个元组，元组中的数据类型是(response,status,headers)。status值会覆盖默认的200状态码，headers可以是一个列表或者字典，作为额外的消息头。元组内不一定三个元素都要写。返回的元组，其实在底层也是包装成了一个`Response`对象。

- 如果以上条件都不满足，Flask会假设返回值是一个合法的WSGI应用程序，并通过`Response.force_type(rv,request.environ)`转换为一个请求对象。

**示例1：直接使用Response创建**

```python
from werkzeug.wrappers import Response

@app.route('/about/')
def about():
    resp = Response(response='about page',status=200,content_type='text/html;charset=utf-8')
    return resp
```
**示例2：使用make_response函数来创建Response对象**

这个方法可以设置额外的数据，比如设置cookie，header信息等。

```python
from flask import make_response

@app.route('/about/')
def about():
    return make_response('about page')
```
**示例3：通过返回元组的形式**

```python
@app.errorhandler(404)
def not_found():
    return 'not found',404
```

**示例4：自定义响应**

- 必须继承自Response类。
- 实现类方法force_type(cls,rv,environ=None)。
- 必须指定app.response_class为你自定义的Response。

注：`Restful API`都是通过JSON的形式进行传递，如果你的后台跟前台进行交互，所有的URL都是发送JSON数据，此时就可以自定义一个叫做JSONResponse的类来代替Flask自带的Response类。

```python
from flask import Flask, Response, jsonify, render_template

# flask = werkzeug+sqlalchemy+jinja2

app = Flask(__name__)

# 将视图函数中返回的字典，转换成json对象，然后返回。
# restful-api
class JSONResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        """
        这个方法只有视图函数返回非字符、非元组、非Response对象才会调用.
        response：视图函数的返回值.
        """
        if isinstance(response, dict):
            # jsonify除了将字典转换成json对象，还将改对象包装成了一个Response对象
            response = jsonify(response)
        return super(JSONResponse, cls).force_type(response, environ)

app.response_class = JSONResponse

@app.route("/")
def hello_world():
    # Response("Hello World!", status=200, mimetype="text/html")
    return "Hello World"

@app.route("/list1/")
def list1():
    resp = Response("list1")
    resp.set_cookie('country', 'china')
    return resp

@app.route("/list2/")
def list2():
    return "list", 200, {"X-NAME": "x-name"}

@app.route("/list3/")
def list3():
    return {"username": "amesy", "age": 18}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
```

注意以上例子，如果不写`app.response_class = JSONResponse`，将不能正确的将字典返回给客户端。因为字典不在Flask的响应类型支持范围中，那么将调用`app.response_class`这个属性的`force_type`类方法，而`app.response_class`的默认值为Response，因此会调用`Response.force_class()`这个类方法，它有一个默认的转换成字符串的算法，但是这个算法不能满足我们的需求。因此，我们要设置`app.response_class=JSONResponse`，然后重写JSONResponse中的force_type类方法，在这个方法中将字典转换成JSON格式的字符串后再返回。
