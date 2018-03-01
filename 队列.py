# 队列 - 先入先出
import time

# 先入
lst = []
def stack_in(lst, element):
    lst.append(element)

# 先出
def stack_out(lst):
    # res = lst[0]
    # del lst[0]
    # return res
    return lst.pop(0)

print('先入:')
for i in range(10):
    stack_in(lst, i)
    time.sleep(0.5)
    print(i)

print('先出:')
for _ in range(len(lst)):
    time.sleep(0.5)
    print(stack_out(lst))

