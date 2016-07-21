from sklearn.preprocessing import scale
import numpy as np
import pandas as pd


dim1_nparray = np.array([1,2,3,4,5])
dim1_df = pd.Series([1,2,3,4,5])
dim1_array = [1,2,3,4,5]

s_dim1_nparray = scale(dim1_nparray)
s_dim1_array = scale(dim1_array)
s_dim1_df = scale(dim1_df)
print("array")
print(dim1_array)
print(s_dim1_array)
print(s_dim1_array.mean(), s_dim1_array.var())
print(dim1_nparray)
print(s_dim1_nparray)
print(s_dim1_nparray.mean(), s_dim1_nparray.var())
print(dim1_df)
print(s_dim1_df)
print(s_dim1_df.mean(), s_dim1_df.var())

dim2_array = [[1,2],[2,3],[3,4],[4,5],[5,6]]
s_dim2_array = scale(dim2_array)
print(dim2_array)
print(s_dim2_array)
print(s_dim2_array.mean(),s_dim2_array.var())
