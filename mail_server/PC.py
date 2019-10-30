import  tkinter as tk
# from mail_server.send_mail import  operate_email

from suds.client import Client  # 导入suds.client 模块下的Client类
import requests
import _thread


class PC():
    def __init__(self):
        self.wsdl_url = "http://localhost:8000/?wsdl"
        self.frame = tk.Tk()
        self.frame.geometry('300x200')
        self.Left_frame = tk.Frame(self.frame)  # 左边容器
        # 基础控件
        self.Var_account = tk.StringVar()
        self.account = tk.Entry(self.Left_frame, text="account", textvariable=self.Var_account, width=20)
        self.logon = tk.Button(self.Left_frame, text="发送", width=5, height=3,command=self.senmail)

        self.Left_frame.pack()
        self.account.pack()
        self.logon.pack()

        self.frame.mainloop()
    def senmail(self):
        '''
        account=self.account.get()
        main=operate_email()
        main.send_email_by_smtp()
        '''
        account = self.account.get()
        # 开一个线程
        try:
            # soap 风格调用接口
            _thread.start_new_thread(self.say_hello_soap, (self.wsdl_url,account , ))
            # rest调用接口
            # _thread.start_new_thread(self.say_hello_rest,(account,))

        except:
            print("ERROR ：无法启动线程")

    # rest 风格接口
    def say_hello_rest(self,email):
        REQUEST_URL = "http://localhost:8080/users/"
        url = str(REQUEST_URL + "/" + str(email))
        rsp = requests.get(url)
        if rsp.status_code == 200:
            # rspJson = json.loads(rsp.text.encode())
            rspJson = rsp.text
            print(rspJson)

    # soap  风格接口
    def say_hello_soap(self,url,email_account):
        client = Client(url)  # 创建一个webservice接口对象
        # 调用接口
        # client.service.say_hello(name, times)  # 调用这个接口下的getMobileCodeInfo方法，并传入参数
        get_infor=client.service.send_email_by_smtp(email_account)
        if(get_infor[0][0]=='s'):
            req = str(client.last_sent())  # 保存请求报文，因为返回的是一个实例，所以要转换成str
            response = str(client.last_received())  # 保存返回报文，返回的也是一个实例
            print(req)  # 打印请求报文
            print(response)  # 打印返回报文
        else:
            print("the send is fail")






PC()



