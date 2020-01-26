import socket
import time

serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 延时最多一秒
clientSocket.settimeout(1)

for i in range(0, 10):
    sendTime = time.time()
    message = ('Ping %d %s' % (i, sendTime)).encode()
    try:
        clientSocket.sendto(message, (serverName, serverPort))
        modifiedMessage, addr = clientSocket.recvfrom(1024)
        rtt = time.time() - sendTime
        print('Sequence: %d: Reply from %s RTT = %.3fs' % (i+1, serverName, rtt))
    except Exception as e:
        print('Sequence %d: Request timed out' % (i+1))

clientSocket.close()