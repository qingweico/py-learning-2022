# 文件操作
# a 追加写模式
# file = open('data', 'w')
# file.write('python')
# file.close()

file = open('data', 'r')
# 输出当前文件指针的位置
print(file.tell())
# 调整指针位置
# 第二个参数 0表示文件开头偏移 1 表示从当前位置 2 从文件结束位置
file.seek(0, 0)
print(file.read())
file.close()

file = open('data', 'r')
print(file.readline())
file.close()

file = open('data', 'r')
for line in file.readlines():
    print(line)
file.close()
