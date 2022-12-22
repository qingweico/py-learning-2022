# 迭代器和生成器

iterator = iter([1, 2, 3])
print(next(iterator))
print(next(iterator))
print(next(iterator))


# 自定义构建迭代器
def frange(start, end, step):
    x = start
    while x < end:
        yield x
        x += step


for i in frange(1, 5, 0.5):
    print(i)
