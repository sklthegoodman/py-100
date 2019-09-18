'''
综合实践
'''

'''
双色球选号
'''
from random import randrange, randint, sample

def display(balls):
    '''
    输出列表的双色球号码
    '''
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()

def random_select():
    ''''
    随机选一组号码
    '''
    red_balls = [x for x in range(1,34)]
    selected_ball = sample(red_balls,6)
    selected_ball.sort()
    selected_ball.append(randint(1,16))
    return selected_ball

def double_color_ball():
    # n = int(input('机选几注：'))
    for _ in range(3):
        display(random_select())



"""
约瑟夫环
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""

def joseph_round():
    # 所有人的环
    person = [True] * 30
    
    counter = index = number = 0
    # 如果已经有15个了就退出
    while counter < 15:
        if person[index]:
            number += 1
            if number == 9:
                person[index] = False
                counter += 1
                number = 0
        index += 1
        # 当超过数组的长度的时候，重新开始
        index %= len(person)

    for p in person:
        print('基' if p else '非',end='|')


if __name__ == '__main__':
    # double_color_ball()
    joseph_round()