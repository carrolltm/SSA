import web
from web import form

# Web版的客户端

# https://blog.csdn.net/freeking101/article/details/53020865
# https://blog.csdn.net/hxiaohai/article/details/78469459
render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form(
    form.Textbox("邮箱"))


from suds.client import Client  # 导入suds.client 模块下的Client类
import  _thread


def senmail(sdl_url, account):
    '''
    account=self.account.get()
    main=operate_email()
    main.send_email_by_smtp()
    '''
    account = account.get()
    # 开一个线程
    try:
        _thread.start_new_thread(say_hello_soap, (sdl_url, account,))
    except:
        print("ERROR ：无法启动线程")

    # self.say_hello_test(self.wsdl_url)   # 接口调用

    # soap 接口
def say_hello_soap(url, email_account):
    client = Client(url)  # 创建一个webservice接口对象
    # 调用接口
    # client.service.say_hello(name, times)  # 调用这个接口下的getMobileCodeInfo方法，并传入参数
    get_infor = client.service.send_email_by_smtp(email_account)
    if (get_infor[0][0] == 's'):
        req = str(client.last_sent())  # 保存请求报文，因为返回的是一个实例，所以要转换成str
        response = str(client.last_received())  # 保存返回报文，返回的也是一个实例
        print(req)  # 打印请求报文
        print(response)  # 打印返回报文
        return  "the send is success"
    else:
        print("the send is fail")
        return  "the send is fail"




class index:
    def GET(self):
        form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        # print(form.render())
        return render.formtest(form)

    # post处理函数部分代码
    def POST(self):
        print('<Handle>post')
        webData = web.input()
        print(webData)
        data=None
        if webData:
            data = webData.get('邮箱')
            print(data, type(data))
        url= "http://localhost:8000/?wsdl"
        # 接口调用
        rec_inf = say_hello_soap(url, data)
        return " information: %s" % (rec_inf)

    # def POST(self):
    #     form = myform()
    #     print( type(form.d.boe))
    #     if not form.validates():
    #         print(form.render())
    #         return render.formtest(form)
    #     else:
    #         # form.d.boe and form['boe'].value are equivalent ways of
    #         # extracting the validated arguments from the form.
    #         return "Grrreat success! boe: %s, bax: %s" % (form.d.boe, form['bax'].value)


if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()