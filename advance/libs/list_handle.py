'''
heapq
从列表中找到最大/最小的n个元素
堆结构（大根堆/小根堆）
'''

import heapq

list1 = [2,23,23,4,4,5,56,3,47,279,6,34434,12,74,6,3]
list2 = [
    {'name':'IBM','shares':100, 'price':91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# 最大的三个
print(heapq.nlargest(3,list1))
# 最小的两个
print(heapq.nsmallest(3, list1))
# 取特殊的key来对比一下
print(heapq.nlargest(3, list2, key=lambda x: x['price']))
print(heapq.nlargest(3, list2, key=lambda x: x['shares']))


'''
itertools
迭代工具
    - 排列
    - 组合
    - 笛卡尔积
'''

import itertools
a = itertools.permutations('abcd')
print(a)
b = itertools.combinations('ABCDE', 3)
print(b)
c = itertools.product('ABCD', '123')
print(c)


'''
collections下的工具类
'''
from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter)
print(counter['eyes'])
print(counter.most_common(3))