'''
TCP套接字
    - 创建一个提供时间的服务器
'''
from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime
from base64 import b64encode
from time import sleep
from threading import Thread
from json import dumps
from random import randint

class FileTransferHandler(Thread):
    
    def __init__(self, cclient, data):
        super().__init__()
        self._client = cclient
        self._data = data
    
    def run(self):
        my_dict = {}
        my_dict['filename'] = 'test'
        my_dict['fileData'] = self._data
        json_str = dumps(my_dict)
        '''
        5.发送数据
        '''
        # 模拟需要处理1s
        sleep(randint(1,4))
        self._client.send(json_str.encode('utf-8'))
        '''
        6.断开连接  
        '''
        self._client.close()

def main():
    '''
    1.创建套接字对象并指定使用哪种传输服务
    family=AF_INET - IPv4地址
    family=AF_INET6 - IPv6地址
    type=SOCK_STREAM - TCP套接字
    type=SOCK_DGRAM - UDP套接字
    type=SOCK_RAW - 原始套接字
    '''
    server = socket(family=AF_INET, type=SOCK_STREAM)
    '''
    2.绑定ip和端口
    '''
    server.bind(('127.0.0.1', 6789))
    '''
    3.开启监听 - 监听客户端连接到服务器
    参数512可以理解为连接队列的大小
    '''
    server.listen(512)
    print('服务器开始监听...')
    # 打开一个图片
    with open('./img/005BYqpggy1g1ut8y6c4lj31c00u0gp8.jpg', 'rb') as f:
        # 将二进制数据处理成base64再解码成字符串
        data = b64encode(f.read())
        data = data.decode('utf-8')
    while True:
        '''
        4.通过循环接收客户端的连接并作出相应的处理(提供服务)
        accept方法是一个阻塞方法如果没有客户端连接到服务器，代码不会向下执行
        accept方法返回一个元组：
            - 第一个是客户端对象
            - 第二个是连接到服务器的的客户端的地址
        '''
        client, addr = server.accept()
        print(str(addr) + '；连接到服务器。')
        
        FileTransferHandler(client, data).start()


if __name__ == "__main__":
    main()