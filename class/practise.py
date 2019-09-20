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


'''
getter和setter
'''
class Person:
    
    def __init__(self,name,age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修复器 - setter方法
    @age.setter
    def age(self, value):
        self._age = value + 10

    def play(self):
        if self._age <= 16:
            print('%s正在看熊出没' % self._name)
        else:
            print('%s正在看欧冠' % self._name)

def get_set_test():
    kid = Person('Piggy',12)
    adult = Person('Pig',22)

    print(kid.name)
    print(adult.name)

    print('年龄：')
    print(kid.age)
    print(adult.age)
    
    kid.age = 3
    print(kid.age)


if __name__ == '__main__':
    # run_clock()
    get_set_test()