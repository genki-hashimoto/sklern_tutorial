from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()
print("###raw_data:\n",iris)

df = pd.DataFrame(iris.data,columns=iris.feature_names)
print("###DataFrame:\n",df)


print("===True===")
data,target = datasets.load_iris(True)
print("###data:\n",data)
print("###target:\n",target)
