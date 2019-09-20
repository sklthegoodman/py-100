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
    print('getter和setter：')

    kid = Person('Piggy',12)
    adult = Person('Pig',22)

    print(kid.name)
    print(adult.name)

    print('年龄：')
    print(kid.age)
    print(adult.age)
    
    kid.age = 3
    print(kid.age)

'''
__slots__魔法
    - 限定绑定属性
'''
class PersonSlot:
    
    # 限定只能绑定_name，_age，_gender属性
    __slots__ = ('_name','_age','_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value + 10

    def play(self):
        if self._age <= 16:
            print('%s正在看熊出没' % self._name)
        else:
            print('%s正在看欧冠' % self._name)

def slot_test():
    print('slot测试：')
    
    p = PersonSlot('崔爷',12)
    p.play()
    # p.is_asshold = True   //会报错


'''
静态方法和类方法
    - @staticmethod
    - 只能通过类访问
'''
from math import sqrt

class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))

def triangle_test():
    a, b, c = 3, 4, 5
    # 静态办法通过类来调用
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        print(t.area())

if __name__ == '__main__':
    # run_clock()
    # get_set_test()
    # slot_test()
    triangle_test()