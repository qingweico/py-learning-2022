from os import path
from pathlib import Path

# . 代表当前路径
print(path.abspath('.'))
print(path.exists('C:/Java'))
print(path.isdir('C:/Java'))
print(path.isfile('C:/Java'))

p = Path(".")
# print([x for x in p.iterdir() if x.is_file()])
#
Path.mkdir(p.joinpath("a/b/c"), parents=True)
