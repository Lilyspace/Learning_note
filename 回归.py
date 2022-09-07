
回归：建立因变量y和自变量x之间的函数关系

线性回归：用量化特征预测连续区间的响应
评价线性回归模型的好坏：r2 回归平方和和样本总平方和之比，也等于1-残差平方和与总平方和之比
                    意义：用模型可解释部分与总离差比较，取值在0到1之间，越接近1，模型可解释部分越多，模型性能越好

逻辑回归：用量化特征预测某事发生的概率（适用于二分类问题）

建模对应训练集，即建立模型时喂给模型的数据
模型应用对于测试集，即模型建立后，用来测试模型性能的数据

一元线性回归例子
import pandas as pd
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import metrics
my_iris=pd.read_csv('C:\Python\Scripts\my_data\iris.csv',sep=',',decimal='.',
header=None,
names=['sepal_length','sepal_width', 'petal_length','petal_width','target'])
feature_cols='petal_length'
#feature_cols='sepal_width'
x=my_iris[[feature_cols]]
y=np.array(my_iris['sepal_length'])
plt.plot(x,y,'o',alpha=0.5)
linreg=LinearRegression()
linreg.fit(x,y)
print('f(x) = ',linreg.intercept_,'+',linreg.coef_[0],'x')
pred_y=linreg.predict(x)
plt.plot(x,pred_y,'g',alpha=0.5)
plt.plot(np.array(x).mean(),y.mean(),'r*',ms=12)
plt.gca().set_xlabel(feature_cols)
plt.gca().set_ylabel('sepal_length')
print('RMSE = ',np.sqrt(metrics.mean_squared_error(y,pred_y)))
print('\n')
f(x) = 4.305565456292049 + 0.4091258984678836 x
RMSE = 0.40435105064202476

print('r_square = ',linreg.score(x,y))
r_square = 0.7599553107783261

print(my_iris[[feature_cols,'sepal_length']].corr())
print('\n') r=np.array(my_iris[[feature_cols,'sepal_length']].corr()[['sepal_length']].
iloc(0)[0])
print('r = ',r)
print('square of r = ',r**2)
petal_length sepal_length
petal_length 1.000000 0.871754
sepal_length 0.871754 1.000000
r = [0.87175416]
square of r = [0.75995531]

逻辑回归的例子
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from scipy import stats
from sklearn.model_selection import train_test_split

bikes=pd.read_csv("C:\Python\Scripts\my_data\\bikeshare.csv") # 注意\b 是转义字符，表示退格，所以\\表示\本身
print(bikes.shape)
(10886, 13)
bikes.head()
feature_cols=['temp'] x=bikes[feature_cols]
bikes['above_average']=bikes['count']>=bikes['count'].mean()
y=bikes['count']>=bikes['count'].mean()
x_train,x_test,y_train,y_test=train_test_split(x,y)
logreg=LogisticRegression()
logreg.fit(x_train,y_train)
#print((y_test.values))
print(pd.DataFrame(np.transpose([y_test.values,logreg.predict(x_test)]),
columns={'真实值','预测值'}))
print('\n')
print('分类准确率是:',logreg.score(x_test,y_test)) # 评分函数

非数值型数据-四季
采用one-hot编码，四位二进制编码，编码长度=类别个数；pd.get_dummies函数
bikes.groupby('season').above_average.mean().plot(kind='bar')
when_dummies=pd.get_dummies(bikes['season'],prefix='season_')
when_dummies.head()
when_dummies=when_dummies.iloc[:,1:] # 去除第一列
when_dummies.head()
#new_bike=pd.concat([bikes[['temp','humidity']],when_dummies],axis=1)
new_bike=pd.concat([bikes[['temp']],when_dummies],axis=1) x=new_bike
x_train,x_test,y_train,y_test=train_test_split(x,y)
logreg=LogisticRegression()
logreg.fit(x_train,y_train)
y_pred=logreg.predict(x_test)
#print(y_pred)
print('用气温、季节同时作为预测自变量，预测的准确率为：',logreg.score(x_test,y_test))
用气温、季节同时作为预测自变量，预测的准确率为： 0.6958119030124909
