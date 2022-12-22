from pandas import Series, DataFrame
from numpy import nan
import numpy as np

# DataFrame (二)多维数据
# data = {'city': ['北京', '广州', '上海', '深圳', '杭州'],
#         'year': [2016, 2017, 2018, 2017, 2018],
#         'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

# frame = DataFrame(data)
# print(frame)
# frame2 = DataFrame(data, columns=['year', 'city', 'pop'])
# print(frame2)
# print(frame.city)
# print(frame['year'])

# 增加新的列
# frame['salary'] = ['18000', '15000', '13000', '20000', '14000']
# print(frame)

# data = {'name': {'k1': 'v1', 'k2': 'v2'},
#         'id': {'k1': 'v3', 'k2': 'v4'}}
# frame = DataFrame(data)
# print(frame)
# # 转置(行列互换)
# print(frame.T)
#
# obj4 = Series([4.5, 7.2, -5.3, 3.6], index=['b', 'd', 'c', 'a'])
# # 重建索引 使用0填充NaN
# obj5 = obj4.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
#
# print(obj5)

# 填充数据
# obj6 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
# print(obj6)
# # bfill 和 ffill
# print(obj6.reindex(range(6), method='bfill'))

# 删除缺失值 NaN
# data = Series([1, nan, 2])
# print(data.dropna())

# 删除缺失值
data = DataFrame([[1., 6.5, 3], [1., nan, nan], [nan, nan, nan]])
# data[4] = nan
# print(data)
# # axis=1指删除某列都是nan的列,how=all指某行都是nan才删除
# print(data.dropna(axis=1, how='all'))

# 填充缺失值
# inplace=True 在原来数据上修改,不创建副本
data.fillna(0, inplace=True)
print(data)

# 层次化索引
data = Series(np.random.randn(10),
              index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                     [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])

# unstack 转换为 Dataframe
# stack 转换为 Series
print(data.unstack().stack())

print(data['b':'c'])
