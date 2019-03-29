import  pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import statsmodels.api as sma
from statsmodels.tsa.arima_model import ARIMAResults


data_path='data/wind_speed'
data = pd.read_csv(data_path)
print(data.index)
# data.plot()

# 正常显示中文标签
# plt.rcParams["font.sans-serif"] = ['SimHei']
# plt.show()

# 自相关图
from statsmodels.graphics.tsaplots import plot_acf
# plot_acf(data,lags=200).show()

# 平稳性检验
from statsmodels.tsa.stattools import adfuller as ADF
# print(ADF(data[u'wind_speed']))

D_data=data.diff().dropna()
# D_data.plot()
# plt.show()
plot_acf(D_data,lags=200).show()
# print(ADF(D_data[u'wind_speed']))
# model_2_0 = sma.tsa.ARMA(data, (1,0)).fit()
# plt.plot(data)
# plt.plot(model_2_0.fittedvalues, color='red')
# plt.show()
# predict = model_2_0.predict(100, 10000002, dynamic=True)
# print(predict)
# predict_data = model_2_0.predict(start=163732, end=163734, dynamic=True)
# model_2_0.save('1.pkl')
# load_model = ARIMAResults.load('1.pkl')
# predict_data = model_2_0.forecast(steps=86400)[0]
# print(predict_data)
# predict_data = model_2_0.predict(start=163732, end=163734, dynamic=True)
# data.append(predict_data,ignore_index=True)
# new_data=data+predict_data
# print(data)
# print(predict_data)
# plt.plot(predict_data)
# plt.show()
