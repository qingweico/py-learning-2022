# import threading 导入 threading 中全部的功能
# threading.Thread()
# 导入 threading 中 Thread 模块
from threading import Thread
from threading import current_thread


class Task(Thread):
    def run(self):
        print(current_thread().name)


t = Task()
t.start()
t.join()
print(current_thread().name)
