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

![picture1](https://raw.githubusercontent.com/amesy/amesy.github.io/master/assets/_images/flask/img01.png)

然后单击"创建"即可。
创建完成后可以看到，默认已经有了一个app.py文件，直接点击运行。

之后在浏览器中输入 http://127.0.0.1:5000 就能看到hello world了。需要说明一点的是，app.run这种方式只适合本地开发，如果在生产环境中，应该使用Gunicorn或者uWSGI来启动。如果是在终端运行的，可以按ctrl+c来让服务停止。

### 程序代码详解

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
    # 运行本项目，默认的host是127.0.0.1，port为5000,也可以自定义host和port.
    app.run()
    """
    自定义host、port和debug模式
    app.run(host="0.0.0.0", port=9000, debug=True)
    """
```

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

# config笔记：

### 使用`app.config.from_object`的方式加载配置文件：
1. 导入`import config`。
2. 使用`app.config.from_object(config)`。


### 使用`app.config.from_pyfile`的方式加载配置文件：
这种方式不需要`import`，直接使用`app.config.from_pyfile('config.py')`就可以了。
注意这个地方，必须要写文件的全名，后缀名不能少。
1. 这种方式，加载配置文件，不局限于只能使用`py`文件，普通的`txt`文件同样也适合。
2. 这种方式，可以传递`silent=True`，那么这个静态文件没有找到的时候，不会抛出异常。
