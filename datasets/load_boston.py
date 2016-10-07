from sklearn import datasets
import pandas as pd

boston = datasets.load_boston()
print("###raw_data:\n",boston)
df = pd.DataFrame(boston.data,columns=boston.feature_names)
print("###DataFrame:\n",df)

print("====True===")
data,target = datasets.load_boston(True)
print("###data:\n",data)
print("###target\n:",target)
