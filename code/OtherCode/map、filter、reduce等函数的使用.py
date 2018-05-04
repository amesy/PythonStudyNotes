# 计算列表lst中的以小写字母开头的元素的字母的总个数.
# 结合filter、map、reduce完成.

from functools import reduce

lst = ['fdas', 'Tdfa', 'dfsaf', 'Alddf']

res_filter = filter(lambda x: x[0].islower() is True, lst)
res_map = map(lambda x: len(x), res_filter)
res_reduce = reduce(lambda x, y: x+y, res_map)

print(res_reduce)