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
类方法：第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）
静态方法：没有“self”和“cls”参数，不能使用类或实例的任何属性和方法
'''

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
    else:
        print('没法构成三角形')


'''
类方法
    - classmethod
'''
from time import time, localtime, sleep


class Clock2(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)

    def run(self):
        """走字"""
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
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def clock_test():
    # 通过类方法获取
    c = Clock2.now()
    print(c)
    print(c.show())

'''
类与类的关系
    - is-a 继承/泛化 比如学生和人的关系、手机和电子产品的关系都属于继承关系。
    - has-a 关联 比如部门和员工的关系，汽车和引擎的关系都属于关联关系
        - 如果是整体与部分的关联关系，成为 *聚合*
        - 如果整体进一步负责了部分的生命周期（整体和部分是不可分割的，同时同在也同时消亡），那么这种就是最强的关联关系，我们称之为*合成*关系。
    - use-a 依赖 比如司机有一个驾驶的行为（方法），其中（的参数）使用到了汽车，那么司机和汽车的关系就是依赖关系
'''
'''
继承
'''
class Person_(object):
    """人"""

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
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)

class Student(Person_):
    '''
    学生
    '''
    def __init__(self, name, age, grage):
        super().__init__(name, age)
        self._grade = grage

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,grade):
        self._grade = grade
    
    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))

class Teacher(Person_):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))

def test_inherite():
    stu = Student('大锤', 15, '初三')
    stu.study('英语')
    stu.watch_av()
    
    t = Teacher('陈医生', 33, '砖家')
    t.teach('养猪')
    t.watch_av()


'''
元类与多态
'''
import abc
# 表明Pet是个元类，不能实例化
class Pet(object, metaclass=abc.ABCMeta):
    def __init__(self,nick):
        self._nick = nick
    
    # 由该元类创建的类一定要定义这个方法
    @abc.abstractmethod
    def make_voice(self):
        '''发出声音'''
        pass

class Cat(Pet):
    def make_voice(self):
        print('我是%s，我喵喵喵...' % self._nick)

class Dog(Pet):
    def make_voice(self):
        print('我是%s，我汪汪汪...' % self._nick)

def test_polimorphism():
    pets = [Cat('石化鸡蛇'),Dog('旺财'),Cat('猪儒')]
    for p in pets:
        p.make_voice()
    

if __name__ == '__main__':
    # run_clock()
    # get_set_test()
    # slot_test()
    # triangle_test()
    # clock_test()
    # test_inherite()
    test_polimorphism()