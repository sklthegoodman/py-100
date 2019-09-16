'''
集合
'''

def main():
    set1 = {1,3,3,3,2,2}
    print(set1)
    print('Length =',len(set1))
    set2 = set(range(1,10))
    print(set2)
    # 添加到列表
    set1.add(4)
    set1.add(5)
    set2.update([11,12])
    print(set1)
    print(set2)
    # 丢弃
    set2.discard(5)
    print(set2)
    # remove的元素如果不存在会引发KeyError，但discard不会
    if 4 in set2:
        set2.remove(4)
    print(set2)
    # 遍历集合
    for elem in set2:
        print(elem,end='')
    print()
    # 将元组转为集合
    set3 =set((1,2,3,3,2,1))
    print(set3)
    # pop
    set3.pop()
    print(set3)
    # 交集，并集，差集
    print('原数据')
    print(set1)
    print(set2)
    # 交集
    print(set1.intersection(set2))
    print(set1 & set2)
    # 并集
    print(set1.union(set2))
    print(set1 | set2)
    # 差集
    print(set1.difference(set2))
    print(set1 - set2)
    # 对称差
    print(set1.symmetric_difference(set2))
    print(set1 ^ set2)

    # 判断子集和超集
    print('原数据')
    print(set1)
    print(set2)
    print(set3)

    print(set2 <= set1)
    print(set2.issubset(set1))
    
    print(set3 <= set1)
    print(set3.issubset(set1))
    print(set1.issuperset(set3))

    


if __name__ == '__main__':
    main()