'''
一个时钟
'''
from time import sleep
import os

class Clock(object):
    '''
    数字时钟
    '''
    def __init__(self, hour=0, minute=0, second=0):
        '''
        初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        '''
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        '''
        走起
        '''
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0 

    def show(self):
        '''
        显示时间
        '''
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


def run_clock():
    clock = Clock(3,22,12)

    while True:
        print(clock.show())
        sleep(1)
        clock.run()
        os.system('clear')






if __name__ == '__main__':
    run_clock()