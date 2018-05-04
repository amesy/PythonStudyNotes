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

## URL中的传参方式
