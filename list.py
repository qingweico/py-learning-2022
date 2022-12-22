# 列表
int_list = [1, 2, 3, 4, 5, 6]
# object, not index
int_list.remove(1)
print(int_list)
# 列表推导式
alist = [i * i for i in range(1, 11) if (i % 2 == 0)]
print(alist)
