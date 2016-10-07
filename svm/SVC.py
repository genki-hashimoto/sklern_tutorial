import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import datasets
import pandas as pd

#irisデータのロード
features,target = datasets.load_iris(True)
#必要な特徴を抜き出し
features = np.array(features[:,2:])

#SVMの学習
clf = svm.SVC(C=1)
clf.fit(features,target)

#トレーニングデータの描画
plt.scatter(features[target==0][:,0],features[target==0][:,1],color="red")
plt.scatter(features[target==1][:,0],features[target==1][:,1],color="blue")
plt.scatter(features[target==2][:,0],features[target==2][:,1],color="green")

#データ範囲にメッシュ状にデータ点を生成
x_min = features[:,0].min()-1
x_max = features[:,0].max()+1
y_min = features[:,1].min()-1
y_max = features[:,1].max()+1
grid_interval=0.02
xx, yy = np.meshgrid(
	np.arange(x_min, x_max, grid_interval),
	np.arange(y_min, y_max, grid_interval),
)

#メッシュ状のデータ点を学習済みSVMで分類
Z = clf.predict(np.c_[xx.ravel(),yy.ravel()])

# 分類結果を表示する
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.bone, alpha=0.2)

# グラフを表示する
plt.autoscale()
plt.grid()
plt.show()
