'''
TCP的客户端
'''
from socket import socket
from threading import Thread

class ConnectTcp(Thread):
    def run(self):
        # 1. 创建套接字对象默认使用IPv4和TCP协议
        client = socket()
        # 2. 连接到服务器（需要指定IP地址和端口）
        client.connect(('127.0.0.1', 6789))
        # 3. 从服务器接受数据
        print(client.recv(1024).decode('utf-8'))
        client.close()

def main():
    # 进行8个连接
    for _ in range(8):
        ConnectTcp().start()

if __name__ == "__main__":
    main()