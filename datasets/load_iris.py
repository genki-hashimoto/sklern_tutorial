from sklearn import datasets

iris = datasets.load_iris()

print(iris)

data,target = datasets.load_iris(True)
print(data)
print(target)
