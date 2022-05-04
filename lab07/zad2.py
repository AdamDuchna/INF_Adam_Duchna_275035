import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7,
                                         random_state=275035)


def classify_iris(sl, sw, pl, pw):
    if pl >= 4.8:
        return ("virginica")
    elif sl >= 4.4 and pw < 1:
        return ("setosa")
    else:
        return ("versicolor")


len = test_set.shape[0]
good_predictions = 0
for i in range(len):
    if classify_iris(*test_set[i, 0:4]) == test_set[i, 4]:
        good_predictions = good_predictions + 1

print(good_predictions)
print(good_predictions / len * 100, "%")
