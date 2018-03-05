from collections import namedtuple

student = namedtuple('student', 'name, age, sex, def', rename=True)
# if rename=False, then ValueError: Type names and field names cannot be a keyword: 'def'。
print(student._fields)  # 'def' 被重命名为'_3'. 并且当元素重名时，也会被重命名。

res = student(name='amesy', age='twenty-two', sex='male', _3='def')
print(res)
print(res.__doc__)

print("My information name: %s, age: %s, sex: %s, def: %s" % res)




