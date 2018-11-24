import xgboost as xgb
from sklearn import datasets
import pandas as pd
from pandas import *
from sklearn.model_selection import train_test_split

# 特征分布
import matplotlib.pyplot as plt
import seaborn as sns

data_src=pd.read_csv('data/train.csv',delimiter=',')
print(data_src.info())