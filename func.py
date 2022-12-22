# 函数可变长参数


# print("str", end='\n\n')
# print("str", end='\n\n')


# 取得参数的个数
# def howlong(first, *other):
#     print(1 + len(other))
#
# howlong(1)
# howlong(1, 2, 3)


# 函数变量的作用域
var1 = 10


def f():
    # 函数作用域内的变量不会影响到外部 除非加global关键字
    global var1
    var1 = 100
    print(var1)


f()
print(var1)
