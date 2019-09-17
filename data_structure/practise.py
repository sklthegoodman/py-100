'''
一些例子
'''

'''
跑马灯文字
'''
import os,time

def horseLamp():
    content = '我最厉害，我超厉害'
    while True:
        # os.system('cls')
        os.system('clear')
        print(content)
        time.sleep(.2)
        content = content[1:] + content[0]


'''
随机的验证码
'''
import random

def generate_code(code_len=4):
    """
    :param code_len: 验证码的长度

    :return 随机验证码
    """

    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1 
    code = ''
    for _ in range(code_len):
        index = random.randint(0,last_pos)
        code += all_chars[index]
    return code


'''
返回文件的后缀名
'''
def get_suffix(filename,has_dot=False):
    """
    获取文件的后缀名

    :param filename: 文件名
    
    :param has_dot: 返回的后缀是否要带点
    :return 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

# 用字符串方法
def get_suffix2(filename,has_dot=False):
    # print('_'.join(['1','2']))
    split = filename.split('.')
    if(len(split) < 1):
        return ''
    else:
        return '.' + split[-1] if has_dot else split[-1]
    
'''
设计一个函数返回传入的列表中最大和第二大的元素的值。
'''
def max2(x):
    m1, m2 = (x[0],x[1]) if x[0] > x[1] else (x[1],x[0])
    for elem in x[2:]:
        if elem > m1:
            m2 = m1
            m1 = elem
        elif elem > m2:
            m2 = elem
    return m1,m2


'''
计算今天是今年的第几天？
'''
import datetime
# 是否是闰年
def is_leap_year(year):
    """
    判断是不是闰年
    
    :param year 年份
    :return 是否是闰年
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def which_day(year, month, date):
    """
    计算传入的日期是这一边的第几天

    :param year: 年
    :param month: 月
    :param  date: 日
    :return 第几天
    """
    
    days_of_month  = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for elem in days_of_month[0:month-1]:
        total += elem
    return total + date

def cal_now():
    now = datetime.datetime.now()
    return which_day(now.year,now.month,now.day)

if __name__ == '__main__':
    # horseLamp()
    # print(generate_code())
    # print(get_suffix('file.txt',True))
    # print(get_suffix2('file.txt',True))
    # print(max2([1,2,3,8,4,2,8,56,23,45,724,4,8]))
    # print(which_day(2019,9,18))
    print(cal_now())