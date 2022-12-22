# 闭包
def counter(first=0):
    cnt = [first]

    def add_self():
        cnt[0] += 1
        return cnt[0]
    # 返回内部函数的引用
    return add_self


num1 = counter(1)
num10 = counter(10)
print(num1())
print(num1())
print(num1())
print(num1())

print(num10())
print(num10())
print(num10())
print(num10())
