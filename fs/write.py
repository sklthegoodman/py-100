'''
写入文件
    - 写入素数
'''

from math import sqrt


def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main():
    filenames = ['1.txt','2.txt','3.txt']
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1,10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')                    
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as e:
        print(e)
        print('写文件的时候发生错误')
    finally:
        for f in fs_list:
            f.close()
        print('操作完成')

if __name__ == "__main__":
    main()