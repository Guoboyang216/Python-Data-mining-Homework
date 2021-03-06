"""
目的：实现多线程报数
作者：徐昭
"""

import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        number_off(self.name)
        # 释放锁，开启下一个线程
        threadLock.release()


def number_off(name):
    count = 0
    while count < 10:
        count += 1
        print(name + "输出" + str(count))
        time.sleep(0.5)


threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(3, "Thread-3", 3)
thread4 = myThread(4, "Thread-4", 4)
thread5 = myThread(5, "Thread-5", 5)

# 开启新线程
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)
threads.append(thread5)

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
