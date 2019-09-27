# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 23:39:51 2019

@author: Administrator
"""
#对天气数据进行预处理
import pandas as pd
import re

data=pd.read_csv('weather.csv')
data=data.drop(['Unnamed: 0'],axis=1)

"""数据清洗--处理缺失值"""
mode=data['风力'].mode()
data['风力']=data['风力'].fillna('小于3')


"""数据转换---字符转换为数字"""
#-----------风力处理---------------------
#将微风转换为1-2级,小于3变为1-3,小于3级~3-4级转换为1-4
data['风力'] =data['风力'].apply(lambda x:str(x).replace('微风','1~2级'))
data['风力'] =data['风力'].apply(lambda x:str(x).replace('小于3','1~2'))
data['风力'] =data['风力'].apply(lambda x:str(x).replace('1~2级~3-4级','1~4级'))
data['风力'] =data['风力'].apply(lambda x:str(x).replace('1-2','1~2'))
data['风力'] =data['风力'].apply(lambda x:str(x).replace('3-4','3~4'))
data['风力'] =data['风力'].apply(lambda x:x.split('级',1)[0])
WIND_ORDER = ['1','2','3','4','5','6']
def wind_parser(weather, type='best'):
    indices = [WIND_ORDER.index(i) for i in weather.split('~')]
    if type == 'best':
        return WIND_ORDER[min(indices)]
    elif type == 'worst':
        return WIND_ORDER[max(indices)]
data['最大风力']=data['风力'].apply(lambda x: wind_parser(x,'best'))
data['最小风力']=data['风力'].apply(lambda x: wind_parser(x,'worst'))

#----------------天气处理-----------------

WEATHER_ORDER = ['晴','局部多云','少云','多云','阴','阵雨','小雨','小到中雨','中雨','中到大雨','大雨','雨夹雪','小雪','中雪','大雪','雾','浮尘','扬沙','霾']
WEATHER_ORDER_id = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
#将天气的末尾的~删除
data['天气'] =data['天气'].apply(lambda x:str(x).rstrip('~'))
data['天气'] =data['天气'].apply(lambda x:str(x).replace('转','~'))
data['天气'] =data['天气'].apply(lambda x:str(x).replace('阴天','阴'))

def weather_parser(weather, type='best'):
#    if '转' in str(weather[0]):
#        indices = [WEATHER_ORDER.index(i) for i in weather.split('转')]
#    else:
#        indices = [WEATHER_ORDER.index(i) for i in weather.split('~')]
    indices = [WEATHER_ORDER.index(i) for i in weather.split('~')]
    if type == 'best':
        return WEATHER_ORDER_id[min(indices)]
    elif type == 'worst':
        return WEATHER_ORDER_id[max(indices)]
data['最好天气']=data['天气'].apply(lambda x: weather_parser(x,'best'))
data['最坏天气']=data['天气'].apply(lambda x: weather_parser(x,'worst'))

data.to_csv("data.csv",encoding="utf_8_sig")
