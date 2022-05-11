from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7,
                                         random_state=16934)

x = train_set[:, 0:4]
y = train_set[:, 4]

x2 = test_set[:, 0:4]
y2 = test_set[:, 4]
scaler = StandardScaler()
scaler.fit(x)
x = scaler.transform(x)
x2 = scaler.transform(x2)

classifier = KNeighborsClassifier(n_neighbors=11)
classifier.fit(x,y)

y_pred = classifier.predict(x2)

len = test_set.shape[0]
good_predictions = 0
for i in range(len):
    if y_pred[i] == test_set[i, 4]:
        good_predictions = good_predictions + 1

print(good_predictions / len * 100, "%")

#k3 95.55555555555556%
#k5 95.55555555555556%
#k11 93.33333333333333%