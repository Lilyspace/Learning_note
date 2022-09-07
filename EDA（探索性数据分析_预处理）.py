data = pd.read_csv('D:\项目代码\Corona virus 2019 dataset\covid_19_data.csv')

1. 数据检查及预处理
数据检查：数据的规模与特征数据类型及意义
data.head()
data.shape
data.info()

预处理：缺失处理；异常处理；冗余处理（重复）
缺失值；

样本容量大，缺失信息少，可直接丢弃
data.dropna(axis = 0)删除整行
data.dropna(axis = 1)删除整列

填充
固定值填充:data.fillna({'Age':mean_Age,'Cabin': 'XXX'})
临近值填充:data.fillna(method = 'ffill') 'ffill'/'bfill'用缺失值之前/后的有效值填充 

噪声、干扰、错误
服从正态分布：Z-score,Z-score>3 怀疑异常
不服从正态分布：四分位距Q=q3-q1(q1-第一个四分位距 q3-第三个四分位距),
                x>q3+3Q或者x<q1-3Q则视为极端异常、离群值
对于异常值：判断是错误直接丢弃，如果不能确定则需要增加样本容量

数据冗余（重复）：行重复data.duplicated(),data.drop_duplicates()
                  冗余特征：Datafame.corr函数，
                           当method = pearson时，线性相关系数接近1或-1，则说明两个特征存在强线性正/负相关，有较大冗余
                           线性相关系数接近0，则两个特征之间没有线性相关性

2. 数据初步分析

描述性统计：位置性测度、离散性测度、图形化描述

data.describe():非空元素个数，均值，标准差，最大最小值，分位数

位置性测度：
import pandas as pd
import numpy as np
my_data = pd.read_csv("C:\Python\Scripts\my_data\Titanic.csv")
print('对 Fare 的位置性测度统计结果：')
print('均值：\t\t',my_data[['Fare']].mean()[0])
#mean 这里返回的是 series，可以用方括号序号来访问，下同
print('中位数：\t',my_data[['Fare']].median()[0])
print('第 25 个百分位数：',my_data[['Fare']].quantile(q=0.25)[0])
#q 参数指明第几个百分位数，默认值是 0.5
print('众数：\t\t',my_data[['Fare']].mode().values[0,0])
#mode 返回的是 dataframe，所以用 dataframe 的 values 属性获取值
#values 本身是 ndarray，所以用二维数组的方式访问

离散性测度
print('对 Fare 的离散性测度统计结果：')
print('变化范围：\t [',my_data[['Fare']].min()[0],'\t',my_data[['Fare']].max()[0],']')
print('极差：\t\t',my_data[['Fare']].max()[0]-my_data[['Fare']].min()[0])
print('方差：\t\t',my_data[['Fare']].var()[0])
print('标准差：\t',my_data[['Fare']].std()[0])
print('变异系数：\t',my_data[['Fare']].std()[0]/my_data[['Fare']].mean()[0])
