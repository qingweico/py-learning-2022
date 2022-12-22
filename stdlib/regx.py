# 正则
import re

p = re.compile(r'(\d+)-(\d+)-(\d+)')
year, month, day = p.match('1999-08-04').groups()
print(year)
print(month)
print(day)

# search 与 compile 的区别
# sub() findall() 函数
