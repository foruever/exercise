import  pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import statsmodels.api as sma
from statsmodels.tsa.arima_model import ARIMAResults

csv = pd.read_csv('data/14_data.csv')
csv.info()
# csv[['generator_speed']].plot()
for index in range(1,27):
    data = csv.iloc[:, [index]]
    # print(data)
    model = sma.tsa.ARMA(data, (1,0)).fit()
    model.save("model/"+str(index)+".model")
    # csv.iloc[:,[index]].plot()
    # plt.plot(data)
    # plt.show()
    # plt.show()