'''
多线程
'''
from random import randint
from threading import Thread
from time import time, sleep

def download_task(name):
    print('开始下载%s...' % name)
    time_spended = randint(1,5)
    sleep(time_spended)
    print('%s下载完成，耗时%d秒' % (name,time_spended))

def down():
    start = time()
    t1 = Thread(target=download_task, args=('你这笨猪',))
    t1.start()
    t2 = Thread(target=download_task, args=('猪猪侠啊',))
    t2.start()
    t1.join()
    t2.join()
    print('总共花费了%.2f秒...' % (time() - start))



'''
自己建立自己的线程类
'''
class DownlaodTask(Thread):
    
    def __init__(self,filename):
        super().__init__()
        self._filename = filename
    
    def run(self):
        print('开始下载%s...' % self._filename)
        time_spended = randint(1,5)
        sleep(time_spended)
        print('%s下载完成，耗时%d秒' % (self._filename,time_spended))

def download_by_extend():
    start = time()
    t1 = DownlaodTask('杀更大')
    t1.start()
    t2 = DownlaodTask('雷军猪')
    t2.start()
    t1.join()
    t2.join()
    print('总共花费了%.2f秒...' % (time() - start))




if __name__ == "__main__":
    # down()
    download_by_extend()