# 生产者消费者模型
import time
from queue import Queue
from threading import Thread, current_thread
import random

# 默认是阻塞的
queue = Queue(10)


class ProducerThread(Thread):
    def run(self):
        thread_name = current_thread().name
        num = range(100)
        global queue
        while True:
            rand = random.choice(num)
            queue.put(rand)
            print("Producer : %s, Produce : %s" % (thread_name, rand))
            t = random.randint(1, 3)
            time.sleep(t)
            print("Producer : %s, Sleep : %s(s)" % (thread_name, t))


class ConsumerThread(Thread):
    def run(self):
        thread_name = current_thread().name
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print("Consumer : %s, Consume : %s" % (thread_name, num))
            t = random.randint(1, 3)
            time.sleep(t)
            print("Consumer : %s, Sleep : %s" % (thread_name, t))


p1 = ProducerThread(name='p1')
p1.start()
c1 = ConsumerThread(name='c1')
c1.start()
c2 = ConsumerThread(name='c2')
c2.start()
