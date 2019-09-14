'''
字符串
'''

def main():
    str1 = 'hello, world!'
    # 通过len计算长度
    print(len(str1))
    # 首字母大写
    print(str1.capitalize())
    # 全大写
    print(str1.upper())
    # 从字符串查找子串所在位置
    print(str1.find('or'))
    print(str1.find('shit'))
    # index 和find相似，当时如果找不到，回抛出异常，而不是返回-1
    # print(str1.index('or'))
    # print(str1.index('shit'))
    # 检查是否以给定字符串开头
    print(str1.startswith('he'))
    print(str1.startswith('He'))
    # 检查是否以给定字符串结尾
    print(str1.endswith('!'))
    print(str1.endswith('world!'))
    print(str1.endswith('?'))
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(50,'*'))
    # 字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50,'-'))
    # ljust
    print(str1.ljust(50,'-'))

    str2 = 'abc123456'
    # 检查是否由数字组成
    print(str2.isdigit())
    # 是否由字母组成
    print(str2.isalpha())
    # 是否由数字和字母组
    print(str2.isalnum())

    str3 = '    expam@qq.com     '
    print(str3)
    # 修建左边两边的空格
    print(str3.strip())



if __name__ == '__main__':
    main()