'''
open 参数
    'r'	读取 （默认）
    'w'	写入（会先截断之前的内容）
    'x'	写入，如果文件已经存在会产生异常
    'a'	追加，将内容写入到已有文件的末尾
    'b'	二进制模式
    't'	文本模式（默认）
    '+'	更新（既可以读又可以写）
'''

'''
健壮的读取文件的代码
'''

def robust_read():
    f = None
    try:
        f = open('临江仙.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('没有找到该文件')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件的时候发生了解码错误')
    finally:
        f and f.close()

'''
用with实现的健壮的读取
'''
def robust_read_use_with():
    try:
        with open('临江仙.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('没有找到该文件')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件的时候发生了解码错误')


'''
逐行读取
'''
import time

def readline_use_for_in():
    with open('临江仙.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line,end="")
            time.sleep(.5)

def readline_use_readlines():
    with open('临江仙.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()    
        print(lines)

def readline_use_readline():
    with open('临江仙.txt', 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if line:
                print(line,end='')
                time.sleep(.5)
            else:
                break
                
if __name__ == "__main__":
    # robust_read()
    # robust_read_use_with()
    # readline_use_for_in()
    # readline_use_readlines()
    readline_use_readline()


