import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 9, 5

#出力された2d推定結果を読み込み
df= pd.read_csv('./ildoonet-tf-pose-estimation/movie/data/cmu_robot_dance_2ddata.csv')

#2d推定座標をプロット
for i in range(19):
    df1 = df[(df['human'] ==1) & (df['point'] == i)]
    plt.plot(df1['x'], -df1['y'], label=i,marker = 'o')
plt.legend()
plt.show()