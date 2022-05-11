import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()

df = pd.read_csv("iris.csv")
labels = df[['class']].replace(['setosa', 'versicolor', 'virginica'], [0, 1, 2])
labels = np.ravel(labels.values)
datasets = train_test_split(df.values[:, 0:4], labels,
                            test_size=0.2)
train_data, test_data, train_labels, test_labels = datasets

scaler = StandardScaler()
scaler.fit(train_data)
train_data = scaler.transform(train_data)
test_data = scaler.transform(test_data)

mlp = MLPClassifier(hidden_layer_sizes=(3,3), max_iter=1000)
mlp.fit(train_data, train_labels)

predictions_train = mlp.predict(train_data)
print(accuracy_score(predictions_train, train_labels))
predictions_test = mlp.predict(test_data)
print(accuracy_score(predictions_test, test_labels))
