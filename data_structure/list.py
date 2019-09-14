'''
列表
'''

'''
使用列表
'''

def basic():
    print('基本操作')

    list1 = [1,3,3,5,7,100]
    print(list1)
    list2 = 'hello'
    print(list2 * 5)
    # 计算长度
    print(len(list1))
    # 下标运算
    print(list1[1])
    print(list1[-1])
    print(list1[-3])
    list1[0] = 1000
    print(list1)
    # 添加元素
    # append
    list1.append(123)
    print(list1)
    # insert
    list1.insert(1,2)
    print(list1)
    # 删除元素
    # remove 通过值删除元素
    list1.remove(3)
    print(list1)
    if 5 in list1:
        list1.remove(5)
    print(list1)
    # del 通过下标删除
    del list1[0]
    print(list1)
    # 清空列表元素
    list1.clear()
    print(list1)

if __name__ == "__main__":
    basic()
    