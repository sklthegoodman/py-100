'''
多进程
'''
from random import randint
from time import time, sleep
from os import getpid
from multiprocessing import Process

def download_task(name):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载 %s...' % name)
    time_spended = randint(1,5)
    sleep(time_spended)
    print('%s已经下载完成，耗费了%d秒' % (name, time_spended))

def download_in_single_process():
    start = time()
    download_task('最帅的wrynn')
    download_task('猪儒冒险记')
    print('总共耗费了%.2f秒' % (time() - start))
    
def download_in_multi_process():
    start = time()
    p1 = Process(target=download_task, args=('最帅的wrynn',))
    p1.start()
    p2 = Process(target=download_task, args=('猪儒冒险记',))
    p2.start()
    p1.join()
    p2.join()
    print('总共耗费了%.2f秒' % (time() - start))

if __name__ == "__main__":
    # download_in_single_process()
    download_in_multi_process()


'''
我们也可以使用subprocess模块中的类和函数来创建和启动子进程，然后通过管道来和子进程通信，这些内容我们不在此进行讲解，有兴趣的读者可以自己了解这些知识
'''