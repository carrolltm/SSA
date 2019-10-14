#-*-coding:utf-8-*-
import numpy  as np
import matplotlib.pyplot as plt
from  SoftWare_Arch_Work3.Number_deal import  number_deal



class number_show:
    def __init__(self):
        self.number_de=number_deal()                 #初始化数据处理
        self.f = plt.figure( dpi=80, facecolor="pink", edgecolor='green', frameon=True) # figsize=(8, 8),

    def Send_Request_deal(self,command,year=None):
        # 关闭数据库             Close database
        # 最高价和最低价         Highest_Lowest_Price
        # 收盘价格和涨幅比       CloseP_Increase_Ratio
        # 哪一年的对比200  --2016
        list1=None
        list2=None
        list3=None
        if command=="Close database":
            self.number_de.Recive_Request_show(command)
        elif command == "Highest_Lowest_Price":
            list1,list2,list3=self.number_de.Recive_Request_show(command,year)
        elif command == 'CloseP_Increase_Ratio':
            list1,list2,list3=self.number_de.Recive_Request_show(command,year)
        return list1,list2,list3


    def Sign_In(self,account,password):        #  get account and password to sign in
        judge=self.number_de.Sign_in(account,password)
        return judge                           # True or False
    # *********************8界面展示模块*******************888

    #折线图
    def Send_matplotlib_Screeen_broken(self,command,list1,list2,list3):   # 这是散点图
        # 创建绘图对象f
        # 脱线编号不断迭代然后方便删除前面一个
        self.f.clf()
        self.a = self.f.add_subplot(111)
        self.ax1 = self.a.twinx()
        x = np.linspace(1, np.size(list2), np.size(list2))
        #list1 = np.array(list1, int).T
        self.a.plot(x, list2, 'g-')  # green, solid line
        self.ax1.plot(x, list3, 'b-')  # blue
        self.a.set_xlabel('Year')
        if command=='Highest_Lowest_Price':
            self.a.set_ylabel('Highest Price', color='g')
            self.ax1.set_ylabel('Lowest_Price', color='b')
        else:
            self.a.set_ylabel('收盘率%', color='g')
            self.ax1.set_ylabel('增长速%', color='b')
            #x = np.linspace(1, np.size(list2),np.size(list2))
        #self.a .scatter(x, list2, s=75, alpha=.5)
        return self.f

    def Send_matplotlib_Screeen_scatter(self,command, list1, list2, list3):         # 散点图吧，饼状图想不出什么
        self.f.clf()
        self.a = self.f.add_subplot(111)
        x = np.linspace(1, np.size(list2), np.size(list2))
        self.a.scatter(x, list2, alpha=.5)
        self.a.set_xlabel('Year')
        self.ax1 = self.a.twinx()
        if command == 'Highest_Lowest_Price':
            self.a.set_ylabel('Highest Price', color='g')
            self.ax1.set_ylabel('Lowest_Price', color='b')
        else:
            self.a.set_ylabel('收盘率%', color='g')
            self.ax1.set_ylabel('增长速%', color='b')
        return self.f



    def Send_matplotlib_Screeen_Columnar(self, command,list1, list2, list3):    # 柱状图  出现负数的话就不好看
        self.f.clf()
        self.a = self.f.add_subplot(111)
        # x = np.linspace(1, np.size(list2), np.size(list2))
        n=12
        x = np.arange(n)
        self.a.bar(x, +list2[:n],facecolor='#9999ff', edgecolor='white')  # green, solid line
        self.a.bar(x, -list3[:n],facecolor='#ff9999', edgecolor='white')  # blue
        # self.a.xlim(0,5)
        # self.a.xticks(())
        # self.a.ylim(0, 20)
        # self.a.yticks(())
        # 加上数值
        print(list3.shape)
        # add data to the photo
        X=zip(x, list2[:n])
        Y=zip(x, list3[:n])
        for x, y in  X:
            # ha: horizontal alignment
            # va: vertical alignment
            self.a.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
        for x, y in Y:
            # ha: horizontal alignment
            # va: vertical alignment
            self.a.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')
        return self.f

#
# if __name__=='__main__':
#     number_show=number_show()
#     number_show.Sign_In('sa','1314' )
#     #这个地方应该就要开一个多线程，一个展示，一个数据交互



