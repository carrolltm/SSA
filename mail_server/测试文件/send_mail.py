
import smtplib
import poplib
import imaplib
from email.mime.text import MIMEText
from email.header import Header
import smtplib


#  独立的通过163/qq发送邮件
# reference
# https://www.jb51.net/article/155176.htm
# https://www.cnblogs.com/lsdb/p/9419036.html
# https://www.cnblogs.com/cymwill/p/8311591.html
class operate_email:
    # 此函数通过使用smtplib实现发送邮件
    def send_email_by_smtp(self):
        # 用于发送邮件的邮箱。修改成自己的邮箱
        sender_email_address = "carrolltm@163.com"
        # 用于发送邮件的邮箱的密码。修改成自己的邮箱的密码
        sender_email_password = "t15872114320"
        sender_email_password_pas="tm15872114320"
        # 用于发送邮件的邮箱的smtp服务器，也可以直接是IP地址
        # 修改成自己邮箱的sntp服务器地址；qq邮箱不需要修改此值
        smtp_server_host = 'smtp.163.com'
        # 修改成自己邮箱的sntp服务器监听的端口；qq邮箱不需要修改此值
        # PORT ——默认的邮件端口是25（QQ邮箱是：465）
        smtp_server_port ='465'
        # 要发往的邮箱
        receiver_email = "1193997197@qq.com"
        # 要发送的邮件主题
        message_subject = "Python smtp测试邮件"
        # 要发送的邮件内容
        message_context = "这是一封通过Python smtp发送的测试邮件..."

        # 邮件对象，用于构建邮件
        message = MIMEText(message_context, 'plain', 'utf-8')
        # 设置发件人（声称的）
        message["From"] = Header(sender_email_address, "utf-8")
        # 设置收件人（声称的）
        message["To"] = Header(receiver_email, "utf-8")
        # 设置邮件主题
        message["Subject"] = Header(message_subject,"utf-8")

        # 连接smtp服务器。如果没有使用SSL，将SMTP_SSL()改成SMTP()即可其他都不需要做改动
        email_client = smtplib.SMTP()
        # email_client = smtplib.SMTP_SSL()
        email_client = smtplib.SMTP_SSL(host=smtp_server_host)
        email_client.connect(host=smtp_server_host, port= smtp_server_port)
        try:
            # 验证邮箱及密码是否正确
            # res = smtp_obj.login(user=FROM, password='tm15872114320')
            email_client.login(sender_email_address, sender_email_password_pas)
            print("smtp----login success, now will send an email to {receiver_email}")
        except:
            print("smtp----sorry, username or password not correct or another problem occur")
        else:
            # 发送邮件
            msg = '\n'.join(['From: {}'.format(sender_email_address), 'To: {}'.format(receiver_email ), 'Subject: {}'.format(message_subject), '', message_context ])
            email_client.sendmail(sender_email_address, receiver_email, msg=msg.encode('utf-8'))
            print(f"smtp----send email to {receiver_email} finish")
        finally:
            # 关闭连接
            email_client.close()

    # 此函数通过使用poplib实现接收邮件
    # 收到的是第一篇，这里163和qq都可以
    def recv_email_by_pop3(self):
        # 要进行邮件接收的邮箱。改成自己的邮箱
        email_address = "carrolltm@163.com"
        # email_address = "1193997197@qq.com"
        # 要进行邮件接收的邮箱的密码。改成自己的邮箱的密码(准确来说是密钥)
        # 163 和qq
        email_password = "tm15872114320"
        # email_password = "tqipayydapdfijfd"
        # 邮箱对应的pop服务器，也可以直接是IP地址
        # 改成自己邮箱的pop服务器；qq邮箱不需要修改此值
        pop_server_host = "pop.163.com"
        # pop_server_host = "pop.qq.com"
        # 邮箱对应的pop服务器的监听端口。改成自己邮箱的pop服务器的端口；qq邮箱不需要修改此值
        pop_server_port = 995

        try:
            # 连接pop服务器。如果没有使用SSL，将POP3_SSL()改成POP3()即可其他都不需要做改动
            email_server = poplib.POP3_SSL(host=pop_server_host, port=pop_server_port, timeout=10)
            print("pop3----connect server success, now will check username")
        except:
            print("pop3----sorry the given email server address connect time out")
            exit(1)
        try:
            # 验证邮箱是否存在
            email_server.user(email_address)
            print("pop3----username exist, now will check password")
        except:
            print("pop3----sorry the given email address seem do not exist")
            exit(1)
        try:
            # 验证邮箱密码是否正确
            email_server.pass_(email_password)
            print("pop3----password correct,now will list email")
        except:
            print("pop3----sorry the given username seem do not correct")
            exit(1)

        # 邮箱中其收到的邮件的数量(取第一篇)
        email_count = len(email_server.list()[1])
        print( len(email_server.list()[1]))
        # 通过retr(index)读取第index封邮件的内容；这里读取最后一封，也即最新收到的那一封邮件
        resp, lines, octets = email_server.retr(email_count)
        # lines是邮件内容，列表形式使用join拼成一个byte变量
        email_content = b'\r\n'.join(lines)
        # 再将邮件内容由byte转成str类型
        email_content = email_content.decode()
        print(email_content)

        # 关闭连接
        email_server.close()

    # 此函数通过使用imaplib实现接收邮件
    def recv_email_by_imap4(self):
        # 要进行邮件接收的邮箱。改成自己的邮箱
        email_address = "1193997197@qq.com"
        # 要进行邮件接收的邮箱的密码。改成自己的邮箱的密码
        email_password = "tqipayydapdfijfd"
        # 邮箱对应的imap服务器，也可以直接是IP地址
        # 改成自己邮箱的imap服务器；qq邮箱不需要修改此值
        imap_server_host = "imap.qq.com"
        # 邮箱对应的pop服务器的监听端口。改成自己邮箱的pop服务器的端口；qq邮箱不需要修改此值
        imap_server_port = 993

        try:
            # 连接imap服务器。如果没有使用SSL，将IMAP4_SSL()改成IMAP4()即可其他都不需要做改动
            email_server = imaplib.IMAP4_SSL(host=imap_server_host, port=imap_server_port)
            print("imap4----connect server success, now will check username")
        except:
            print("imap4----sorry the given email server address connect time out")
            exit(1)
        try:
            # 验证邮箱及密码是否正确
            email_server.login(email_address,email_password)
            print("imap4----username exist, now will check password")
        except:
            print("imap4----sorry the given email address or password seem do not correct")
            exit(1)

        # 邮箱中其收到的邮件的数量
        email_server.select()
        email_count = len(email_server.search(None, 'ALL')[1][0].split())
        # 通过fetch(index)读取第index封邮件的内容；这里读取最后一封，也即最新收到的那一封邮件
        typ, email_content = email_server.fetch(f'{email_count}'.encode(), '(RFC822)')
        # 将邮件内存由byte转成str
        email_content = email_content[0][1].decode()
        print(email_content)
        # 关闭select
        email_server.close()
        # 关闭连接
        email_server.logout()


if __name__ == "__main__":
    # 实例化
    email_client = operate_email()
    # 调用通过smtp发送邮件的发送函数
    # email_client.send_email_by_smtp()
    # 调用通过pop3接收邮件的接收函数
    # email_client.recv_email_by_pop3()
    # 调用通过imap4接收邮件的接收函数
    email_client.recv_email_by_imap4()

