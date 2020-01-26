import socket
import base64

# Mail content
subject = "我是最厉害的我"
contenttype = "text/html"
msg = '''
<h1>你是谁</h1>
<p style="color:red">我是大老鼠</p>
'''

endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver 
mailserver = "smtp.qq.com"

# Auth information (Encode with base64)
u = input('请输入你的用户名：')
username = base64.b64encode(u.encode()).decode()
p = input('请输入你的密码：')
password = base64.b64encode(p.encode()).decode()


# Sender and reciever
fromaddress = u
toaddress = "sun.keliang@foxmail.com"

# 建立一个TC连接
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((mailserver, 25))

# 收到服务器的回应
recv = clientSocket.recv(1024).decode()
print('服务器的首次回应')
print(recv)

# HELO： 打招呼
hello = 'HELO wrynn\r\n'
clientSocket.sendall(hello.encode())
recv = clientSocket.recv(1024).decode()
print('打招呼的回应为：')
if recv[:3] != '250':
    print('250 没有收到')

# AUTH： 鉴权
clientSocket.sendall('AUTH LOGIN\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print('鉴权的回复是：')
print(recv)
if recv[:3] != '334':
    print('334 没有收到')
# AUTH 输入用户名
clientSocket.sendall((username + '\r\n').encode())
recv = clientSocket.recv(1024).decode()
print('输用户名的回复是：')
print(recv)
if (recv[:3] != '334'):
	print('334 没有收到')
# 输入密码
clientSocket.sendall((password + '\r\n').encode())
recv = clientSocket.recv(1024).decode()
print('输密码的回复是：')
print(recv)
if (recv[:3] != '235'):
	print('235 没有收到')

# MAIL FROM 输入发送者
senderSentence = ('MAIL FROM: <' + fromaddress + '>\r\n').encode()
clientSocket.sendall(senderSentence)
recv = clientSocket.recv(1024).decode()
print('输入发送者的回复是：')
print(recv)
if recv[:3] != '250':
    print('250 没有收到')

# RCPT TO 输入接受者
receiveSentence = ('RCPT TO: <' + toaddress + '>\r\n').encode()
clientSocket.sendall(receiveSentence)
recv = clientSocket.recv(1024).decode()
print('输入接收者的回复是：')
print(recv)
if recv[:3] != '250':
    print('250 没有收到')

# DATA 输入内容
clientSocket.sendall('DATA\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '354':
    print('354 没有收到')

message = 'from:' + fromaddress + '\r\n'
message += 'to:' + toaddress + '\r\n'
message += 'subject:' + subject + '\r\n'
message += 'Content-Type:' + contenttype + '\r\n'
message += '\r\n' + msg
# 结束符号
message += '\r\n.\r\n'

clientSocket.sendall(message.encode())
recv = clientSocket.recv(1024).decode()
print('发送内容后收到的数据是：')
print(recv)
if recv[:3] != '250':
    print('250 没有收到')


# QUIT 退出
clientSocket.sendall('QUIT\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print('输入退出之后的收到的数据：')
print(recv)

clientSocket.close()