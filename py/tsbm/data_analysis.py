import  pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt

csv = pd.read_csv('data/14_data.csv')
csv.info()
# csv[['generator_speed']].plot()
csv.iloc[:,[26]].plot()
plt.show()