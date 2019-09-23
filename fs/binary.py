'''
操作二进制
'''

def read_binary():
    try:
        with open('./test.png','rb',) as f1:
            data = f1.read()
            print(type(data))
        with open('./copy.png','wb') as f2:
            f2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开')
        print(e)
    except IOError as e:
        print('读写文件的时候发生错误')
    print('程序结束')

if __name__ == "__main__":
    read_binary()