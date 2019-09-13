'''
完美数
    - 所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身
'''
import math


def perfect(end):
    perfects = []
    for num in range(1,end):
        total = 0
        for sub_num in range(1,int(math.sqrt(num)) + 1):
            if num % sub_num == 0:
                total += sub_num
                if sub_num > 1 and num // sub_num != sub_num:
                    total += num // sub_num
        if total == num:
            perfects.append(num)
    print(perfects)
            
perfect(10000)