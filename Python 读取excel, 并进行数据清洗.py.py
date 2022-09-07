import numpy as np 
import pandas as pd
import datetime
import time 
import matplotlib.pyplot as plt
import seaborn
from matplotlib import animation

'''def walkFile(file):
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            print(os.path.join(root, f))

        # 遍历所有的文件夹
        for d in dirs:
            print(os.path.join(root, d))'''

import os
for root, dirs, files in os.walk('D:\项目代码\Corona virus 2019 dataset'):
    for name in files:
        print(os.path.join(root, name))

#处理数据
data = pd.read_csv('D:\项目代码\Corona virus 2019 dataset\covid_19_data.csv')
data.head()
data.shape
data.info()

data['ObservationDate'] = data['ObservationDate'].astype('datetime64')
data['Last Update'] = data['Last Update'].astype('datetime64')
data.info

#处理缺失值
data.isnull().sum()
data = data.drop('Province/State', axis = 1)
data.isnull().sum()

'''df = data.groupby(['ObservationDate','Country/Region']).agg('sum').sort_values(by='Confirmed',ascending=False).reset_index()
Region_list = df['Country/Region'].tolist()
Confirmed_list = df['Confirmed'].tolist()
Date_list = df['ObservationDate'].tolist()'''

#按ObservationDate分组
data1 = data.groupby('ObservationDate')
type(data1)

#数据可视化
