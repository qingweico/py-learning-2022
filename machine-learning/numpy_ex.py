# numpy 用于高性能科学计算和数据分析,是常用的高级数据分析库的基础包
# 安装 pip install numpy
import numpy as np

# print(np.array([1, 2, 3]).var())
#
# array = np.array([2, 3, 4])
# print(array * 10)
# 矩阵初始值
# print(np.zeros((3, 5)))
# print(np.ones((3, 5)))
#
# print(np.empty((1, 2, 3)))

# 数字的索引和切片
arr = np.arange(1, 10)
print(arr)
print(arr[3:6])
# 可以直接修改原数组
arr[2:3] = 100
print(arr)

# 副本 不会修改原数组
copy = arr.copy()
copy[:] = 20
print(arr)
print(copy)
