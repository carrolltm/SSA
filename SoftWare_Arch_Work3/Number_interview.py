#-*-coding:utf-8-*-
import pyodbc
import  numpy as np
class number_interview:
    def __init__(self):
        # 数据库服务器信息   后期可以变成输入（在表现层中输入，方便多机）   现在是本地
        self.driver = 'SQL Server Native Client 11.0'  # 因版本不同而异
        self.server = '残夜'
        self.user = None#'sa'                                      # 后期需要删除
        self.password = None#'1314'
        self.database = 'Northwind'
        self.conn=None     #数据库连接
        self.cursor=None    #游标
        self.rows=None       #从数据库获得的消息
        self.year=None          # 返回的时间
        self.highest=None       #  返回当天的最高价
        self.Lowest=None        #   返回当天的最低价


    def Connect_SQLServer(self):
        self.conn = pyodbc.connect(driver=self.driver, server=self.server, user=self.user, password=self.password, database=self.database)
        if self.conn:    #后期可以尝试显示到界面上
            print("the database is connected")
            return True
        else:
            print("connect  the database is failed")
            return False
    def Send_SQL_SQLServer(self,sql):
        self.cursor = self.conn.cursor()   #获得游标。
        self.cursor.execute(sql)           # 传递sql语句给数据库。
        self.rows = self.cursor.fetchall()  # list
        return  self.rows

    # def Recive_SQL_SQLServer_All(self):     #获得所有消息
    #     self.rows = self.cursor.fetchall()        # list
    #     print(self.rows)
    def change_data_SQLServer(self):
        self.conn.commit()   #(适合增删改除) 操作提交，如果中途出错，或连接中断，则会发生数据回流，不会影响到数据库原有数据。

    def Disconnect_SQLServer(self):     #Delete_connect
        self.conn.close()
        return "关闭数据库成功"

    def Send_Request_Deal(self):
        pass
    def Recive_Request_Deal(self,command,year=None):              # 都是Varchar类型
        return_information=None
        if command=="Highest_Lowest_Price":             #  调出时间，最高价和最低价格
            return_information=self.Send_SQL_SQLServer("select LEFT(日期,4),[最高价(元)],[最低价(元)]  from stock "
                                                       "where LEFT(日期,4)='"+year+"'")
        elif command =='CloseP_Increase_Ratio':         #  调出收盘价格和涨幅比
            return_information=self.Send_SQL_SQLServer("select LEFT(日期,4),[收盘价(元)],[涨跌幅(%)]  from stock "
                                                       "where LEFT(日期,4)='"+year+"'")

        print("功能请求：数据接收层")
        if  return_information==None:
            print("Request Error:数据接收层")
            return "Request Error"
        else:
            print("Request Successful:数据接收层")
            return return_information




    def Sign_in(self,account,password):            # 接收展示层消息(账号,密码)之后登陆
        self.user = account
        self.password = password
        judge=self.Connect_SQLServer()       #获得账号和密码之后默认自动连接
        return judge



# if __name__=='__main__':
#     interview=number_interview()
#     interview.Sign_in('sa','1314' )
#     #interview.Send_SQL_SQLServer("select 日期,[最高价(元)]  from stock")
#     interview.Recive_Request_Deal("Highest_Lowest_Price","2011")
#     #interview.Recive_SQL_SQLServer_All()






