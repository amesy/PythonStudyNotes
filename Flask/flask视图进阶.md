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

```python 

```







标准类视图，必须继承自`flask.views.View`.
必须实现`dipatch_request`方法，以后请求过来后，都会执行这个方法。这个方法的返回值就相当于是之前的函数视图一样。也必须返回`Response`或者子类的对象，或者是字符串，或者是元组。
必须通过`app.add_url_rule(rule,endpoint,view_func)`来做url与视图的映射。`view_func`这个参数，需要使用类视图下的`as_view`类方法类转换：`ListView.as_view('list')`。
如果指定了`endpoint`，那么在使用`url_for`反转的时候就必须使用`endpoint`指定的那个值。如果没有指定`endpoint`，那么就可以使用`as_view(视图名字)`中指定的视图名字来作为反转。
类视图有以下好处：可以继承，把一些共性的东西抽取出来放到父视图中，子视图直接拿来用就可以了。但是也不是说所有的视图都要使用类视图，这个要根据情况而定。









































