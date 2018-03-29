# 结果按从大到小的顺序排序.
if a > b:
    if b > c:
        print("abc")
    else:
        if a > c:
            print("acb")
        else:
            print("cab")
elif b > c:
    if a > c:
        print("bac")
    else:
        print("bca")
else:
    print("cba")
	
""" 
# 使用三目运算符精简上面代码.
if a > b:
    print("abc") if b > c else print("acb") if a > c else print("cab")
elif b > c:
    print("bac") if a > c else print("bca")
else:
    print("cba")
"""	
