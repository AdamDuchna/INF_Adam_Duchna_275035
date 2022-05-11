from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pandas as pd

df= pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7,
                                         random_state=16934)

x = train_set[:, 0:4]
y = train_set[:, 4]

x2 = test_set[:, 0:4]
y2 = test_set[:, 4]
gnb = GaussianNB()
y_pred = gnb.fit(x, y).predict(x2)
print("Number of mislabeled points out of a total %d points : %d" % (x.shape[0], (y2 != y_pred).sum()))
