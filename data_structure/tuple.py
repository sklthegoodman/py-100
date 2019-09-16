'''
元组
'''
import sys

def main():
    # 定义元组
    t = ('猪儒',38,True,'广州')
    print(t)
    # 获取元素
    print(t[1])
    print(t[3])
    # 遍历
    for member in t:
        print(member)
     # t[0] = '王大锤'  # TypeError
    # 变量t重新引用了新的元组原来的元组将被垃圾回收
    t = ('王大锤', 20, True, '云南昆明')
    # 将元组转化为列表
    person = list(t)
    print(person)
    # 将列表转为元组
    fruits_list = ['apple','banana','orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)
    print(sys.getsizeof(fruits_list))
    print(sys.getsizeof(fruits_tuple))


if __name__ == '__main__':
    main()