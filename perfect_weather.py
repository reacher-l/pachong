# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 18:31:22 2019

@author: Administrator
"""
#2019,2018,2017,2016,2015
import requests                                                                      
from bs4 import BeautifulSoup                                                        
import pandas as pd

urls=['http://lishi.tianqi.com/xian/201501.html',
 'http://lishi.tianqi.com/xian/201502.html',
 'http://lishi.tianqi.com/xian/201503.html',
 'http://lishi.tianqi.com/xian/201504.html',
 'http://lishi.tianqi.com/xian/201505.html',
 'http://lishi.tianqi.com/xian/201506.html',
 'http://lishi.tianqi.com/xian/201507.html',
 'http://lishi.tianqi.com/xian/201508.html',
 'http://lishi.tianqi.com/xian/201509.html',
 'http://lishi.tianqi.com/xian/201510.html',
 'http://lishi.tianqi.com/xian/201511.html',
 'http://lishi.tianqi.com/xian/201512.html',
      'http://lishi.tianqi.com/xian/201601.html',
 'http://lishi.tianqi.com/xian/201602.html',
 'http://lishi.tianqi.com/xian/201603.html',
 'http://lishi.tianqi.com/xian/201604.html',
 'http://lishi.tianqi.com/xian/201605.html',
 'http://lishi.tianqi.com/xian/201606.html',
 'http://lishi.tianqi.com/xian/201607.html',
 'http://lishi.tianqi.com/xian/201608.html',
 'http://lishi.tianqi.com/xian/201609.html',
 'http://lishi.tianqi.com/xian/201610.html',
 'http://lishi.tianqi.com/xian/201611.html',
 'http://lishi.tianqi.com/xian/201612.html',
      'http://lishi.tianqi.com/xian/201701.html',
 'http://lishi.tianqi.com/xian/201702.html',
 'http://lishi.tianqi.com/xian/201703.html',
 'http://lishi.tianqi.com/xian/201704.html',
 'http://lishi.tianqi.com/xian/201705.html',
 'http://lishi.tianqi.com/xian/201706.html',
 'http://lishi.tianqi.com/xian/201707.html',
 'http://lishi.tianqi.com/xian/201708.html',
 'http://lishi.tianqi.com/xian/201709.html',
 'http://lishi.tianqi.com/xian/201710.html',
 'http://lishi.tianqi.com/xian/201711.html',
 'http://lishi.tianqi.com/xian/201712.html',
      'http://lishi.tianqi.com/xian/201801.html',
 'http://lishi.tianqi.com/xian/201802.html',
 'http://lishi.tianqi.com/xian/201803.html',
 'http://lishi.tianqi.com/xian/201804.html',
 'http://lishi.tianqi.com/xian/201805.html',
 'http://lishi.tianqi.com/xian/201806.html',
 'http://lishi.tianqi.com/xian/201807.html',
 'http://lishi.tianqi.com/xian/201808.html',
 'http://lishi.tianqi.com/xian/201809.html',
 'http://lishi.tianqi.com/xian/201810.html',
 'http://lishi.tianqi.com/xian/201811.html',
 'http://lishi.tianqi.com/xian/201812.html',
 'http://lishi.tianqi.com/xian/201901.html',
 'http://lishi.tianqi.com/xian/201902.html',
 'http://lishi.tianqi.com/xian/201903.html',
 'http://lishi.tianqi.com/xian/201904.html',
 'http://lishi.tianqi.com/xian/201905.html',
 'http://lishi.tianqi.com/xian/201906.html',
 'http://lishi.tianqi.com/xian/201907.html',
 'http://lishi.tianqi.com/xian/201908.html']
       
headers = {
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "lishi.tianqi.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
data_all=[]
for url in urls:
    response = requests.request("GET", url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    tqtongji2=soup.find("div",{"class":"tqtongji2"})
    ul_all=tqtongji2.find_all("ul")
    for i in ul_all:
        li_all=i.find_all("li")
        data=[]
        for j in li_all:
            data.append(j.text)
        data_all.append(data[1:])


weather=pd.DataFrame(data_all)
weather.columns=["日期","最高气温","最低气温","天气","风向","风力"]
weather.drop([0],inplace=True)
weather.to_csv("weather.csv",encoding="utf_8_sig")


