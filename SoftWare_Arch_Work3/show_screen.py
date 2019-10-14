#-*-coding:utf-8-*-
import  tkinter as tk
from  tkinter  import ttk
from  SoftWare_Arch_Work3.Number_show import number_show
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
mpl.rcParams['axes.unicode_minus'] = False  # 负号显示


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk #NavigationToolbar2TkAgg
class MainWindow:
    def __init__(self):
        self.frame=tk.Tk()
        self.frame.geometry('800x600')
        self.number_sh=number_show()          #最终数据的接收

        self.contain_cav = tk.Frame(self.frame)  # 创建一个容器
        self.Left_frame = tk.Frame(self.frame)  # 左边容器
        # 基础控件
        self.Var_account=tk.StringVar()
        self.account = tk.Entry(self.Left_frame, text="account",textvariable=self.Var_account, width =20 )
        self.Var_password=tk.StringVar()
        self.password = tk.Entry(self.Left_frame, text="password",textvariable=self.Var_password,show="*",width =20)
        self.logon = tk.Button(self.Left_frame, text="登录", width=5, height=3,command=self.Login_user)
        self.Var_Login_state = tk.StringVar()
        self.Login_state=tk.Label(self.Left_frame,textvariable=self.Var_Login_state)
        #self.free_logon = tk.Button(self.Left_frame, text="免登录", width=10, height=5)
        self.submit = tk.Button(self.Left_frame, text="提交", width=5, height=3,command=self.Submit)
        self.button4 = tk.Button(self.Left_frame, text="button4", width=5, height=5)

        # 创建下拉菜单
        self.cmb_command = ttk.Combobox(self.Left_frame)
        self.cmb_command['value'] = ('Highest_Lowest_Price', 'CloseP_Increase_Ratio')
        self.cmb_command.current(1)
        self.cmb_year = ttk.Combobox(self.Left_frame)
        self.cmb_year['value'] = ('2001','2002','2003','2004','2005','2006','2007',
                                  '2008','2009','2010','2011', '2012','2013',
                                  '2014','2015','2016')
        self.cmb_year.current(1)

        self.photo_shape = ttk.Combobox(self.Left_frame)
        self.photo_shape['value'] = ('折线图','散点图','柱状图')   # 其实还可以加上散状图
        self.photo_shape.current(1)

        # layout
        self.password.grid(row=0, column=1, padx=5, pady=5)
        self.account.grid(row=0, column=0, padx=5, pady=5)                  #嵌套matplotlib图片
        self.logon.grid(row=1, column=0)
        #self.free_logon.grid(row=1, column=1)
        self.Login_state.grid(row=1, column=1)
        self.cmb_year.grid(row=2, column=0,padx=5, pady=5)
        self.cmb_command.grid(row=2, column=1, padx=5, pady=5)
        self.photo_shape.grid(row=3, column=0, padx=5, pady=5)
        self.submit.grid(row=4, column=0, padx=5, pady=5)
        #self.button4.grid(row=2, column=1, padx=5, pady=5)
        self.Left_frame.pack(side='left')
        self.contain_cav.pack(side='right', fill=tk.BOTH, expand=1)

        self.Judge_connect=False    #判断已经登录获得登录成功

        # 画布定位
        self.canvas = FigureCanvasTkAgg(self.number_sh.f, self.contain_cav)  # figure为plot图，self.contain_cav为所在框架
        self.canvas.draw()  # 以前的版本使用show()方法，matplotlib 2.2之后不再推荐show（）用draw代替，但是用show不会报错，会显示警告
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)  # fill=tk.BOTH, ,  expand=1
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)  # , expand=1
        self.frame.mainloop()


    def Login_user(self):                   # 登录
        account=self.Var_account.get()
        password=self.Var_password.get()
        if account and password:
            if self.Judge_connect ==False:
                Judge=self.number_sh.Sign_In(str(account),str(password))
                if Judge:
                    self.Judge_connect=True
                    self.Var_Login_state.set("登录成功")
                else:
                    self.Var_Login_state.set("登录失败")
                    print("登录失败")           #   后期可以做出弹窗之类的
            else :
                    self.Var_Login_state.set("已经登录")
                    print("已经登录")

    def Submit(self):               #还没搞完
        if self.Var_Login_state .get()=='登录成功' or  self.Var_Login_state .get()=='已经登录':
            select_command=(self.cmb_command.get())         #获得指令和年份
            select_year=str(self.cmb_year.get())
            list1,list2,list3=self.number_sh.Send_Request_deal(select_command,select_year)            #选择饼状图，折线图这类的
            self.pare_paint(list1,list2,list3)

    def pare_paint(self,list1=None,list2=None,list3=None):
        # 返回matplotlib所画图形的figure对象
        if self.photo_shape.get() == '折线图': # '折线图','饼状图','柱状图'
            self.figure = self.number_sh.Send_matplotlib_Screeen_broken(self.cmb_command.get(), list1, list2, list3)
        elif self.photo_shape.get() == '柱状图':
            self.figure = self.number_sh.Send_matplotlib_Screeen_Columnar(self.cmb_command.get(), list1, list2, list3)
        elif self.photo_shape.get() == '散点图':
            self.figure = self.number_sh.Send_matplotlib_Screeen_scatter(self.cmb_command.get(), list1, list2, list3)

        self.canvas.draw()

    def paint(self, figure):
        pass
        # 把绘制的图形显示到tkinter窗口上
        # 把matplotlib绘制图形的导航工具栏显示到tkinter窗口上
        # toolbar = NavigationToolbar2Tk(self.canvas,
        #                                self.contain_cav)  # matplotlib 2.2版本之后推荐使用NavigationToolbar2Tk，若使用NavigationToolbar2TkAgg会警告
        # toolbar.update()
        #self.canvas._tkcanvas.pack(side=tk.TOP)#, expand=1












window = MainWindow()