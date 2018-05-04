import inspect
import functools

def typeHints(fn):
    @functools.wraps(fn)
    def wrap(*args, **kwargs):
        sig = inspect.signature(fn)
        params = sig.parameters
		时
        # 处理kwargs：字典
        for k, v in kwargs:
            param = params[k]
            if param.annotation != inspect._empty and not isinstance(v, param.annotation):
                raise TypeError('parameter {} requires {}, but got {}'.format(k, param.annotation, type(v)))
				
        # 处理args：元组
        for i, x in enumerate(args):
            param = list(params.values())[i]
            if param.annotation != inspect._empty and not isinstance(x, param.annotation):
                raise TypeError('parameter {} requires {}, but got {}'.format(param.name, param.annotation, type(x)))
        ret = fn(*args, **kwargs)
        return ret
    return wrap
	
@typeHints
def add(x: int, y: int) -> int:
    return x + y
	
@typeHints
def add1(x, y:int) -> int:
    return x + y
	
print(add(3, 5))	# 输出结果为8
print(add1(1, 2))	# 输出结果为3