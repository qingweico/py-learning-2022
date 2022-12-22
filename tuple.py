# 元组
a = (2, 3, 7, 9, 10)
b = 5
# 取出a中小于5的数字
print(list(filter(lambda x: x < b, a)))
