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


if __name__ == '__main__':
    double_color_ball()