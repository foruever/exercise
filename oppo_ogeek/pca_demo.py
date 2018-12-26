import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA


def ana_lable(x):
    if(x=='Iris-setosa'):
        return 0;
    if(x=='Iris-versicolor'):
        return 1;
    if(x=='Iris-virginica'):
        return 2;

train_pd=pd.read_csv('/Users/fasape/project/exercise/oppo_ogeek/oppo_data/iris.train',header=None)
train_pd[4]=train_pd[4].apply(lambda x:ana_lable(x))
features=train_pd[[0,1,2]]
features_array=np.array(features).tolist()
print(features)
pca=PCA(n_components=2)
new_=pca.fit_transform(features)

# 绘图
# 创建散点图+类型
plt.scatter(new_[:,0],new_[:,1])
line=np.array([[-1,-2],[0,-1],[1,0],[2,1],[3,2],[4,3]])
# 创建折线图+类型
plt.plot(line[:,1],line[:,0],'#12ee56')
plt.show()
