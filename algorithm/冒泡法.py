# coding=utf-8

# 生成20个随机数。
import random
lst = []
for i in range(20):
    lst.append(i)

# 乱序排列。
random.shuffle(lst)
print(lst)

# 排序。
count_num = 0  # 循环次数。
vaild_num = 0  # 循环元素交换次数。
length = len(lst)
for i in range(length):
    flag = True
    count_num += 1
    for j in range(length-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            vaild_num += 1
            flag = False

    if flag:
        break

print('排序完的列表：{}, 共交换：{}次，有效交换：{}次。'.format(lst, count_num, vaild_num))




