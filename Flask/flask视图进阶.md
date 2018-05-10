## add_url_rule和app.route 

-   `add_url_rule(rule,endpoint=None,view_func=None)`

这个方法用来添加 url 与视图函数的映射。如果没有填写 endpoint，则默认使用 view_func 的名字作为 endpoint 。以后在使用 url_for 的时候，就要看在映射的时候是否传递了 endpoint 参数，如果传递了就应该使用 endpoint 指定的字符串，如果没有传递则应该使用vew_func 的名字。

```python 
@app.route("/", endpoint="index")
def hello_world():
    print(url_for("zhiliao"))
    return "Hello World"

def my_list():
    return "列表页"

app.add_url_rule("/list/", endpoint="zhiliao", view_func=my_list)

# 请求上下文
with app.test_request_context():
    print(url_for("index"))
```

浏览器访问：http://127.0.0.1:8007/list/   ->    my_list()



-   `app.route(rule,**options)`

这是个装饰器，底层也是使用 `add_url_rule` 来实现 url 与视图函数映射的。

```python 
def route(self, rule, **options):
	def decorator(f):
		endpoint = options.pop('endpoint', None)
		self.add_url_rule(rule, endpoint, f, **options)
		return f
	return decorator
```

## 类视图 

之前接触的视图都是函数，所以一般简称视图函数。其实视图也可以基于类来实现。类视图的好处是支持继承，但是类视图不能跟函数视图一样，写完类视图还需要通过`app.add_url_rule(url_rule,view_func)`来进行注册。

示例1：

```python 
from flask import Flask, views, render_template

app = Flask(__name__)
app.config.update({"TEMPLATES_AUTO_RELOAD": True, "DEBUG": True})

class Ads(views.View):
    def __init__(self):
        self.context = {
            "ads": "广告区域"
        }


class Register(Ads):
    def dispatch_request(self):
        return render_template("register.html", **self.context)


class Login(Ads):
    def dispatch_request(self):
        return render_template("login.html", **self.context)

app.add_url_rule("/register/", view_func=Register.as_view("register"))
app.add_url_rule("/login/", view_func=Login.as_view("login"))

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8009
    )
```

示例2：

```python 
from flask import Flask, views, jsonify

app = Flask(__name__)
app.config.update({"TEMPLATES_AUTO_RELOAD": True, "DEBUG": True})

class JsonReverse(views.View):
    def get_data(self):
        raise NotImplementedError

    def dispatch_request(self):
        return jsonify(self.get_data())


class ListView(JsonReverse):
    def get_data(self):
        return {"name": "amesy", "age": 23, "gender": "male"}

app.add_url_rule("/jsonify/", view_func=ListView.as_view("jsonify"))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8010
    )
```

-   标准类视图，必须继承自`flask.views.View`。
-   必须实现`dispatch_request`方法，之后请求过来都会执行这个方法。这个方法的返回值就相当于是之前的函数视图一样。也必须返回`Response`或者子类的对象，或者是字符串、元组。
-   必须通过`app.add_url_rule(rule,endpoint,view_func)`来做url与视图的映射。`view_func`参数需要使用类视图下的`as_view`类方法类转换：`ListView.as_view('list')`。
-   如果指定了`endpoint`，那么在使用`url_for`反转的时候就必须使用`endpoint`指定的那个值。如果没有指定`endpoint`，那么就可以使用`as_view(视图名字)`中指定的视图名字来作为反转。
-   **类视图的优点**：可以通过继承把一些共性的东西抽取出来放到父视图中，子视图直接拿来用就可以了。但是也不是说所有的视图都要使用类视图，这个要根据情况而定。

## 基于调度方法的类视图 

1.  基于方法的类视图是根据请求的`method`来执行不同的方法。如果用户是发送的`get`请求，那么将会执行这个类的`get`方法。如果用户发送的是`post`请求，那么将会执行这个类的`post`方法。其他的method类似，比如`delete`、`put`。

2. 这种方式可以让代码更加简洁。所有和`get`请求相关的代码都放在`get`方法中，所有和`post`请求相关的代码都放在`post`方法中。就不需要跟之前的函数一样通过`request.method == 'GET'`。

```python 
from flask import Flask, views, render_template, request

app = Flask(__name__)
app.config.update(
    {"TEMPLATES_AUTO_RELOAD": True, "DEBUG": True}
)

class ViewMethod(views.MethodView):
    def _render(self, error=None):
        return render_template("login.html", error=error)

    def get(self):
        return self._render()

    def post(self):
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "amesy" and password == "123456":
            return "登录成功"
        else:
            error = "用户名或密码错误！"
            return self._render(error)

app.add_url_rule("/login", view_func=ViewMethod.as_view("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8012)
```

login.html 代码示例： 

```html 
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>login</title>
    </head>
    <body>
        <p>"这是登录页面"</p>
        {{ ads }}
        <form action="" method="post">
            <table>
                <tbody>
                    <tr>
                        <td>用户名：</td>
                        <td><input type="text" name="username"></td>
                    </tr>
                    <tr>
                        <td>密码：</td>
                        <td><input type="password" name="password"></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td><input type="submit" value="立即登录"></td>
                    </tr>
                </tbody>
            </table>
            {% if error %}
                <p style="color: red;">{{ error }}</p>
            {% endif %}
        </form>
    </body>
</html>
```

## 类视图中的装饰器

1.  如果使用的是函数视图，那么自己定义的装饰器必须放在`app.route`下面。否则这个装饰器就起不到任何作用。
2.  类视图的装饰器，需要重写类视图的一个类属性`decorators`，这个类属性是一个列表或者元组都可以，里面装的就是所有的装饰器。

示例1：函数装饰器 

```python 
from flask import Flask, request, views
from functools import wraps

app = Flask(__name__)


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # /settings/?username=xxx
        username = request.args.get('username')
        if username and username == 'amesy':
            return func(*args, **kwargs)
        else:
            return '请先登录'
    return wrapper

# app.route('/settings/')(login_required(settings))
@app.route('/settings/')
@login_required
def settings():
    return '这是设置界面'

if __name__ == '__main__':
    app.run(debug=True)
```

浏览器访问：http://127.0.0.1:5000/settings/?username=amesy

示例2：类装饰器 

```python 
from flask import Flask, request, views
from functools import wraps

app = Flask(__name__)

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # /settings/?username=xxx
        username = request.args.get('username')
        if username and username == 'amesy':
            return func(*args, **kwargs)
        else:
            return '请先登录'
    return wrapper

class ProfileView(views.View):
    decorators = [login_required]
    def dispatch_request(self):
        return '这是个人中心界面'

app.add_url_rule('/profile/', view_func=ProfileView.as_view('profile'))

if __name__ == '__main__':
    app.run(debug=True)

```

浏览器访问：http://127.0.0.1:5000/profile/?username=amesy

## 蓝图 

蓝图的作用就是让我们的 Flask 项目更加模块化，结构更加清晰。可以将相同模块的视图函数放在同一个蓝图下，同一个文件中，方便管理。比如`/user/:id`、`/user/profile/`这样的地址，他们的特点都是以`user`开头的，那么可以将这一类的`url`放在一个模块中，达到项目的模块化。 

步骤： 

1、在蓝图文件中导入Blueprint。

```python 
from flask import Blueprint, request
from functools import wraps

user_bp = Blueprint("user", __name__, url_prefix="/user")

def login_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # http://127.0.0.1:8013/user/profile/?username=amesy&password=123456
        username = request.args.get("username")
        password = request.args.get("password")
        if username == "amesy" and password == "123456":
            return func(*args, **kwargs)
        else:
            "请先登录！"
    return wrapper


@user_bp.route("/profile/")
@login_request
def profile():
    return "个人中心页面"


@user_bp.route("/settings/")
@login_request
def settings():
    return "个人设置页面"

```

2、在主app文件中注册蓝图。

```python 
from blueprints.user import user_bp
app.register_blueprint(user_bp)
```

注： 

-   如果想要某个蓝图下的所有url都有一个url前缀，那么可以在定义蓝图的时候，指定url_prefix参数。

    ```python
    user_bp = Blueprint('user',__name__,url_prefix='/user/')
    ```

    在定义 url_prefix 的时候，要注意后面的斜杠，如果给了，那么以后在定义url与视图函数的时候，就不要再在url前面加斜杠了。

-   蓝图模版文件的查找

    -   如果项目中的templates文件夹中有相应的模版文件，就直接使用。
    -   如果没有相应的模版文件，就到定义蓝图的时候指定的路径中寻找。
    -   蓝图中指定的路径可以为相对路径，相对的是当前这个蓝图文件所在的目录。

    ```python 
    news_bp = Blueprint('news',__name__,url_prefix='/news',template_folder='FILE_PATH')
    ```

**蓝图中静态文件的查找规则**

-   在模版文件中，加载静态文件，如果使用url_for('static')，那么就只会在app指定的静态文件夹目录下查找静态文件。
-   如果在加载静态文件的时候，指定的蓝图的名字，比如`news.static`，那么就会到这个蓝图指定的static_folder下查找静态文件。

```html 
<link rel="stylesheet" href="{{ url_for('static',filename='news_list.css') }}">
```

**url_for反转蓝图中的视图函数为url**

-   如果使用蓝图，那么以后想要反转蓝图中的视图函数为url，那么就应该在使用url_for的时候指定这个蓝图。比如`news.news_list`。否则就找不到这个endpoint。在模版中的url_for同样也是要满足这个条件，即指定蓝图的名字。
-   即使在同一个蓝图中反转视图函数，也要指定蓝图的名字。

```python 
@news_bp.route("/list/")
def news_list():
    # /news/detail/
    print(url_for("news.news_detail"))
    return render_template("news_list.html")

@news_bp.route("/detail/")
def news_detail():
    return "新闻详情页面"
```

**蓝图实现子域名** 

在创建蓝图对象的时候，需要传递一个`subdomain`参数，来指定这个子域名的前缀。

例如：`cms_bp = Blueprint('cms',__name__,subdomain='cms')`。

需要在主app文件中，需要配置app.config的SERVER_NAME参数。

示例： 

```python 
app.config['SERVER_NAME'] = 'amesy.me:8000'
```

>   ip地址不能有子域名。
>   localhost也不能有子域名。

在蓝图文件中传递 subdomain参数： 

```python 
from flask import Blueprint
cms_bp = Blueprint("cms", __name__, subdomain="live")
```

注：

>   本地测试时，可以将域名对应ip加入本机hosts文件中来完成实验。
>
>   hosts PATH：C:\Windows\System32\drivers\etc 



最后，浏览器访问：http://live.amesy.me:8000/


















































