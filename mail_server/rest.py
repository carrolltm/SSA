
import web
import xml.etree.ElementTree as ET
from email.mime.text import MIMEText
from email.header import Header
import smtplib

# Rest 风格
# https://www.cnblogs.com/zhangmingcheng/p/8194741.html

tree = ET.parse('users.xml')
root = tree.getroot()

urls = (
    '/users', 'list_users',
    '/users/(.*)', 'get_user'
)
app = web.application(urls, globals())

class get_user:
    def GET(self, email):
        print(email)

        # for child in root:
        #     if child.attrib['id'] == user:
        #         return str(child.attrib)
        # 用于发送邮件的邮箱。修改成自己的邮箱
        sender_email_address = "carrolltm@163.com"
        # 用于发送邮件的邮箱的密码。修改成自己的邮箱的密码(密钥)
        sender_email_password_pas = "tm15872114320"
        # 用于发送邮件的邮箱的smtp服务器，也可以直接是IP地址
        # 修改成自己邮箱的sntp服务器地址；qq邮箱不需要修改此值
        smtp_server_host = 'smtp.163.com'
        # 修改成自己邮箱的sntp服务器监听的端口；qq邮箱不需要修改此值
        # PORT ——默认的邮件端口是25（QQ邮箱是：465）
        smtp_server_port = '465'
        # 要发往的邮箱
        receiver_email = email.split('/')[1]
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
        message["Subject"] = Header(message_subject, "utf-8")

        # 连接smtp服务器。如果没有使用SSL，将SMTP_SSL()改成SMTP()即可其他都不需要做改动
        email_client = smtplib.SMTP()
        # email_client = smtplib.SMTP_SSL()
        email_client = smtplib.SMTP_SSL(host=smtp_server_host)
        email_client.connect(host=smtp_server_host, port=smtp_server_port)
        try:
            # 验证邮箱及密码是否正确
            # res = smtp_obj.login(user=FROM, password='tm15872114320')
            email_client.login(sender_email_address, sender_email_password_pas)
            print("smtp----login success, now will send an email to {receiver_email}")
        except:
            print("smtp----sorry, username or password not correct or another problem occur")
        else:
            # 发送邮件
            msg = '\n'.join(['From: {}'.format(sender_email_address), 'To: {}'.format(receiver_email),
                             'Subject: {}'.format(message_subject), '', message_context])
            email_client.sendmail(sender_email_address, receiver_email, msg=msg.encode('utf-8'))
            print(f"smtp----send email to {receiver_email} finish")
            return  "the send is success"
        finally:
            # 关闭连接
            email_client.close()
        return  "the send is fail"


class list_users:
    def GET(self):
        output = 'users:['
        for child in root:
            print('child', child.tag, child.attrib)
            output = output+  str(child.attrib) + ','
        output  =output+   ']'
        return output



if __name__ == '__main__':
    app.run()