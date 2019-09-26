'''
TCP的客户端
'''
from socket import socket
from threading import Thread
import json
from base64 import b64decode

class ConnectTcp(Thread):
    def run(self):
        # 1. 创建套接字对象默认使用IPv4和TCP协议
        client = socket()
        # 2. 连接到服务器（需要指定IP地址和端口）
        client.connect(('127.0.0.1', 6789))
        # 3. 从服务器接受数据
        # 定义一个二进制对象保存二进制数据
        in_data = bytes()
        # 由于不知道传输的数据有多大，每次接受1024
        while True:
            data = client.recv(1024)
            if not data:
                break
            in_data += data
         # 将收到的二进制数据解码成JSON字符串并转换成字典
        my_dict = json.loads(in_data.decode('utf-8'))
        with open('./img_received/' + my_dict['filename'], 'wb') as f:
            # 将base64格式的数据解码成二进制数据并写入文件
            f.write(b64decode(my_dict['fileData']))
        print('图片已经保存')
            

        

def main():
    # 进行8个连接
    for _ in range(8):
        ConnectTcp().start()

if __name__ == "__main__":
    main()