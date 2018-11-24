# 数据分析过程
# 1 判断 valid 中是否都存在于test
# open("oppo_data/train.")

import xgboost as xgb
from sklearn import datasets
import pandas as pd
from pandas import *
# iris = datasets.load_iris()
# data = iris.data[:100]
# print(type(iris))
def ana_lable(x):
    if(x=='Iris-setosa'):
        return 0;
    if(x=='Iris-versicolor'):
        return 1;
    if(x=='Iris-virginica'):
        return 2;

train_data_src=pd.read_csv('oppo_data/train.txt',header=None,delimiter='	')
# train_data_src[4]=train_data_src[4].apply(lambda x:ana_lable(x))
# print(train_data_src.info())
train_data=train_data_src.loc[:,[0,2,3]]
train_lable=train_data_src[4]
# print(train_lable)

test_data_src=pd.read_csv('oppo_data/valid.txt',header=None,delimiter='	')
# test_data_src[4]=test_data_src[4].apply(lambda x:ana_lable(x))
test_data=train_data_src.loc[:,[0,2,3]]
test_lable=train_data_src[4]
# #
#
dtrain=xgb.DMatrix(train_data,label=train_lable)
dtest=xgb.DMatrix(test_data,label=test_lable)
param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'binary:logistic' }
num_round = 1
bst = xgb.train(param, dtrain, num_round)
preds = bst.predict(dtest)
print(len((Series(preds)!=test_lable)))
print(len(test_lable))
#
# # 计算准确率
# cnt1 = 0
# cnt2 = 0
# for i in range(len(test_lable)):
#     if preds[i] == test_lable[i]:
#         cnt1 += 1
#     else:
#         cnt2 += 1
#
# print("Accuracy: %.4f %%" % (100 * cnt1 / (cnt1 + cnt2)))
# pandas