'''
多进程
'''
from random import randint
from time import time, sleep
from os import getpid
from multiprocessing import Process

def download_task(name):
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