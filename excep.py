# 异常处理
# try:
#     a = 10 / 0
# except ZeroDivisionError as e:
#     print("error: %s" % e)
# try:
#     b = int(input(""))
# except Exception as ex:
#     print('%s' % ex)

# 主动抛出异常
try:
    raise NameError("NameError")
except NameError:
    print("NameError")
finally:
    print("finally")
