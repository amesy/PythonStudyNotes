l1 = [1, 2, 3, 4]
operator_list = ["+", "-", "*", "/"]
l2 = [432, 43243, 543]

def matrix(l1, operator_list, l2, lst=[]):
    a = len(l1)
    b = len(operator_list)
    c = len(l2)

    # 对比较大小后的代码作了精简.
    if a > b:
        res = c if b > c else b
    elif b > c:
        res = c if a > c else  a
    else:
        res = a

    for i in range(res):
        lst.append([])
        lst[i].append(l1[i])
        lst[i].append(operator_list[i])
        lst[i].append(l2[i])
    return iter(lst)

print(list(matrix(l1, operator_list, l2)))


