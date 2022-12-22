# with 关键字 自动处理异常
# 自定义 with 语句
class WithClazz:
    def __enter__(self):
        print("start")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print("No error")
        else:
            print("error : %s" % exc_tb)
        print("end")


with WithClazz():
    print("something goes")
