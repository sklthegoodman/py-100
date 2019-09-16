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

'''
切片操作
'''
def split():
    fruits = ['grape','apple','strawberry','waxberry']
    fruits += ['pitaya','pear','mango']
    
    # 循环遍历列表
    for fruit in fruits:
        print(fruit.title(),end='')
    print()
    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)
    # 通过完整切片来复制列表
    fruits3 = fruits[:]
    print(fruits3)
    # 负向切片
    fruits4 = fruits[-3:-1]
    print(fruits4)
    # step
    fruits5 = fruits[1::2]
    print(fruits5)
    # 通过反向切片来获得倒转的列表
    fruits6 = fruits[::-1]
    print(fruits6)

'''
排序
'''
def sort():
    list1 = ['orange','apple','zoo','internationalization','blueberry']
    list2 = sorted(list1)
    print(list2)
    list3 = sorted(list1,reverse=True)
    print(list3)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1,key=len)
    print(list4)

    # 直接调用实例方法，对源列表进行排序
    list1.sort(reverse=True)
    print(list1)

'''
生成器
'''

if __name__ == "__main__":
    basic()
    split()
    sort()
    