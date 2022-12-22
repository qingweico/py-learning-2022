# pandas
# 安装 pip install pandas
from pandas import Series
# Series 一维数据
obj = Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(obj)
# 根据 index 修改 value
obj['a'] = 100
print(obj)

print('a' in obj)
print('f' in obj)

# 将字典作为参数
dict_data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
series = Series(dict_data)
print(series)
series.index = ['e', 'f', 'g', 'e']
print(series)
