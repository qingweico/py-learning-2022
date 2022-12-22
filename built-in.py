# 内建函数
from functools import reduce
# map
print(list(map(lambda x: x * x, [1, 2, 3])))

# for i in zip((1, 2, 3), (4, 5, 6)):
#     print(i)


# reduce
print(reduce(lambda x, y: x + y, [1, 2, 3], 10))
# key 和 value 对调
# print(dict(zip({'k1': 'v1', 'k2': 'v2'}.values(), {'k1': 'v1', 'k2': 'v2'}.keys())))
