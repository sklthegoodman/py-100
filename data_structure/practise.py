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


if __name__ == '__main__':
    horseLamp()