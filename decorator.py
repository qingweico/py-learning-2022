# 装饰器
import time


def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[%s] cost time : %ss' % (func.__name__, end - start))

    return wrapper


@timer
def some_task():
    time.sleep(2)


some_task()
