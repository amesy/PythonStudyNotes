# 栈 - 先入后出 或 后入先出

import time

# 先入
lst = []
def stack_in(lst, element):
    lst.append(element)

# 后出
def stack_out(lst):
    return lst.pop()

print('先入:')
for i in range(10):
    stack_in(lst, i)
    time.sleep(0.5)
    print(i)

print('后出:')
for _ in range(len(lst)):
    time.sleep(0.5)
    print(stack_out(lst))