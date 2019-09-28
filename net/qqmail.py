'''
用smtp通过qq邮箱发送邮件
'''

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def send_plain_mail():
    sender = input('请输入你的邮箱：')
    pass_word = input('请输入邮箱的授权码：')
    receivers = ['example@test.com']
    message = MIMEText('你知道你是我的分身，但我们从不接触，从不联系，但从现在开始，我们可以说是开启了一个新纪元，请珍重', 'plain', 'utf-8')
    message['From'] = Header('远方的来客','utf-8')
    message['To'] = Header('我的分身','utf-8')
    message['Subject'] = Header('来自新纪元的接触', 'utf-8')
    smtper = SMTP('smtp.qq.com')
    # 登录
    smtper.login(sender, pass_word)
    # 发送邮件
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成')

def send_rich_mail():
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()

    # 创建文本内容
    text_content = MIMEText(
        '''
        人民有信仰，
        国家有力量，
        民族有希望
        让我们一起努力吧
        ''', 'plain', 'utf-8'
    )
    message['Subject'] = Header('新时代的信仰', 'utf-8')
    # 加上文本信息
    message.attach(text_content)

    # 读文件，将文件添加上邮件对象中
    with open('./img/005BYqpggy1g3jt5iiy7gj31hc0u04aa.jpg', 'rb') as f:
        image = MIMEImage(f.read())
        image.add_header('Content-ID', '<image-1>')
        image.add_header('Content-Type', 'image/jpeg')
        # image['Content-Disposition'] = 'attachment; filename=hello.txt'
        message.attach(image)
        
    # 
    smtper = SMTP('smtp.qq.com')
     # 开启安全连接
    smtper.starttls()
    sender = input('请输入你的邮箱：')
    receivers = ['example@test.com']
    # 登录到SMTP服务器
    pass_word = input('请输入你的授权码：')
    smtper.login(sender, pass_word)
    # 发送邮件
    smtper.sendmail(sender, receivers, message.as_string())
    # 退出
    smtper.quit()
    print('已经发送完成')


    

if __name__ == "__main__":
    # send_plain_mail()
    send_rich_mail()