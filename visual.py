# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:52:24 2019

@author: Administrator
"""
import re
import csv
import lxml.html
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import requests                                                                      
from bs4 import BeautifulSoup 
import pandas as pd  
import lxml.html


#可视化温度      
def myplot(path):  
    data=pd.read_csv(path)
    data=data.drop(['Unnamed: 0'],axis=1)    
    datetime=data['日期']
    datatime=np.array(datetime)
    highs =data['最高气温'].apply(lambda x:int(x))
    lows =data['最低气温'].apply(lambda x:int(x))
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(datatime, highs, c='red', label='最高温')
    plt.plot(datatime, lows, c='blue', label="最低温")
    plt.show()


if __name__ == '__main__':
    path='data.csv'
    myplot(path)