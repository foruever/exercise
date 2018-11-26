import xgboost as xgb
from sklearn import datasets
import pandas as pd
from pandas import *
from sklearn.model_selection import train_test_split

# 特征分布
import matplotlib.pyplot as plt
import seaborn as sns

# 1观察数据
train_data=pd.read_csv('data/train.csv',delimiter=',')
print(train_data.info())
# print(train_data.groupby('Pclass').count())
# print(train_data.head())

# 2 处理缺失值
'''
 a 如果数据集很多，但有很少的缺失值，可以删掉带缺失值的行；
 b 如果该属性相对学习来说不是很重要，可以对缺失值赋均值或者众数。
 c 对于标称属性，可以赋一个代表缺失的值，比如‘U0’。因为缺失本身也可能代表着一些隐含信息。比如船舱号Cabin这一属性，缺失可能代表并没有船舱。
   比如在哪儿上船Embarked这一属性（共有三个上船地点），缺失俩值，可以用众数赋值
 d 使用回归 随机森林等模型来预测缺失属性的值。因为Age在该数据集里是一个相当重要的特征（先对Age进行分析即可得知），
   所以保证一定的缺失值填充准确率是非常重要的，对结果也会产生较大影响。一般情况下，会使用数据完整的条目作为模型的训练集，
   以此来预测缺失值。对于当前的这个数据，可以使用随机森林来预测也可以使用线性回归预测。
   这里使用随机森林预测模型，选取数据集中的数值属性作为特征（因为sklearn的模型只能处理数值属性，
   所以这里先仅选取数值特征，但在实际的应用中需要将非数值特征转换为数值特征）

'''
# 2.1 Age处理


# 2.2 Cabin处理



# 2.3 Embarked处理
# 确实值较少，可以用众数处理
# train_data['Embarked'][train_data.Embarked.isnull()]=train_data.Embarked.dropna().mode().values
train_data.Embarked.fillna(train_data['Embarked'].dropna().mode().max(),inplace=True)