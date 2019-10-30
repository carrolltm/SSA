# -*- coding: utf-8 -*-
import json

import requests

# 请求的地址
REQUEST_URL = "http://localhost:8080/users/"
HEADER = {'Content-Type':'application/json; charset=utf-8'}

# 查询Count的值
def getCount(email):
    url=str(REQUEST_URL+"/"+str(email))
    rsp = requests.get(url)
    if rsp.status_code == 200:
        # rspJson = json.loads(rsp.text.encode())
        rspJson =rsp.text
        print(rspJson)



# 程序入口函数
if __name__=="__main__":
    count = getCount("1193997197@qq.com") # 测试查询Count

