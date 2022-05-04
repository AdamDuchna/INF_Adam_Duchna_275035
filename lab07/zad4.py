from sklearn import tree
from sklearn.metrics import confusion_matrix
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_csv("diabetes.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7,
                                         random_state=275035)


x = train_set[:, 0:8]
y = train_set[:, 8]

x2 = test_set[:, 0:8]
y2 = test_set[:, 8]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

tree.plot_tree(clf)
plt.show()

print(clf.score(x2,y2))
print(confusion_matrix(clf.predict(x2),y2))