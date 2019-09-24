'''
进程通信
    - Queue
'''

from multiprocessing import Process, Queue
import os, time, random

def ping(q):
    print(q.get())
    q.put('sdsd')
    
def pong(q):
    print(q.get())
    q.put('aa')


def main():
    q = Queue()
    
    p1 = Process(target=ping, args=(q,))
    p2 = Process(target=pong, args=(q,))

    p1.start()
    p2.start()

if __name__ == "__main__":
    main()