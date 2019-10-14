#-*-coding:utf-8-*-
import numpy as np
from SoftWare_Arch_Work3.Number_interview import number_interview

class  number_deal:
    def __init__(self):
        self.number_inter=number_interview()
    def Send_Request_interview(self,command):   #发送数据给接受层
        pass

    def Recive_Information_interview(self):
        pass
    def Send_Information_show(self):
        pass
    def Deal_The_data(self):            #觉得变成numpy会好点,便于画图
        pass

    def Recive_Request_show(self,command,year=None):
        # 关闭数据库             Close database
        # 最高价和最低价         Highest_Lowest_Price
        # 收盘价格和涨幅比       CloseP_Increase_Ratio
        #对应年份的东西
        print("命令到达了处理层")
        return_information=None
        if command=='Close database':
            return_information=self.number_inter.Disconnect_SQLServer()
            return  True

        elif year:
            if  command=="Highest_Lowest_Price":
                return_information=self.number_inter.Recive_Request_Deal(command,year)

            elif command =='CloseP_Increase_Ratio':
                return_information=self.number_inter.Recive_Request_Deal(command,year)

        if  return_information==None:
            print("Request Error:数据处理层")
            return "Request Error"
        else:
            print("指令结果返回成功：数据处理层")
            return self.Deal_With_Result(command,return_information)

    def Sign_in(self, account, password):
        judge=self.number_inter.Sign_in(account, password)
        return judge
    #*****************************数据进行处理模块***************************************
    def Deal_With_Result(self,command,result):      #这边还需要继续处理一下
        list1=None          #数据整合
        list2=None
        list3=None
        return_information = None
        # 依据        list1=[i[0] for i in result]            #  提取其中为一列
        # 这是所有年份,对应年份可以是再加上判断
        if command == "Highest_Lowest_Price":  # 调出时间，最高价和最低价格
            list1 = [i[0] for i in result]          # -----------这个还需要微调，比如哪一年那个月
            list2 = np.array([i[1] for i in result],float)     #  这里属于numpy类型，方便Matplotlib展示
            list3 = np.array([i[2] for i in result],float)     #  numpy
            print("是整合这种数据没错：数据处理层")
            return list1, list2, list3

        elif command == 'CloseP_Increase_Ratio':  # 调出收盘价格和涨幅比
            list1 = np.array([i[0] for i in result],float)
            list2 = np.array([i[1] for i in result],float)
            list3 = np.array([i[2] for i in result], float)  # numpy
            return list1, list2,list3
        else :
            return False








