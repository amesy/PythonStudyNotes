## 上传文件 

在模板的form表单中，需要指定`encotype='multipart/form-data`才能上传文件。

```python 
<form action="" method="post" enctype="multipart/form-data">
```

在后台如果想要获取上传的文件，使用`request.files.get('avatar')`来获取。
保存文件之前，先使用`werkzeug.utils.secure_filename`对上传上来的文件名进行一个过滤。这样才能保证不会有安全问题。 
获取到上传上来的文件后，使用`avatar.save(路径)`方法来保存文件。、

```python 
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    else:
        arg = request.form.get("desc")
        avatar = request.files.get("avatar")
        file_name = secure_filename(avatar.filename)
        
        # 此处既可以指定图片存放目录的相对路径(相对于项目根目录)，也可以指定绝对路径。
        
        # 相对路径.
        file_path = pathlib.Path("images/", file_name)
        pathlib.Path(file_path.cwd(), file_path)
        # 绝对路径.
        avatar.save(str(pathlib.Path(file_path.cwd(), file_path)))
        
	    return "文件上传成功！"
```

从服务器上读取文件后定义一个url与视图函数，使用`send_from_directory(directory, filename)`来获取指定的文件。

示例代码如下：

```python 
@app.route("/images/<image_name>")
def images(image_name):
    return send_from_directory("images", image_name)
```

html代码如下： 

```html 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>文件上传</title>
</head>
<body>
    <form action="" method="post" enctype="multipart/form-data">
        <table>
            <tbody>
                <tr>
                    <td>头像：</td>
                    <td>
                        <input type="file" name="avatar">
                    </td>
                </tr>
                <tr>
                    <td>描述信息：</td>
                    <td>
                        <input type="text" name="desc">
                    </td>
                </tr>
                <tr>
                    <td>
                        <input type="submit" value="提交">
                    </td>
                </tr>
            </tbody>
        </table>
    </form>
</body>
</html>
```


## 对上传文件使用表单验证

1.  定义表单的时候，对文件的字段需要采用`FileField`类型。
2.  验证器应该从`flask_wtf.file`中导入。
    -   `flask_wtf.file.FileRequired`是用来验证文件上传是否为空。
    -   `flask_wtf.file.FileAllowed`用来验证上传的文件的后缀名。
3.  在视图文件中，使用`from werkzeug.datastructures import CombinedMultiDict`来把`request.form`与`request.files`来进行合并。再传给表单来验证。

示例代码如下：

forms.py

```python
from wtforms import Form, FileField, StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed

class Uploadform(Form):
    avatar = FileField(validators=[FileRequired(), FileAllowed(['jpg','png','gif'])])
    desc = StringField(validators=[InputRequired()])
```
app.py

```python 
from forms import Uploadform
from werkzeug.datastructures import CombinedMultiDict

form = Uploadform(CombinedMultiDict([request.form, request.files]))
if form.validate():
    # avatar = request.files.get("avatar")
    avatar = form.avatar.data
    ...
```

注： 

>   wtforms 和 flask_wtf 如果没有安装，需要先使用 pip 进行安装。