"""Little bit machine learning about."""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('jill.csv', sep=';')
data = data[['age', 'sex', 'studytime', 'absences', 'G1', 'G2', 'G3']]
data['sex'] = data['sex'].map({'F': 0, 'M': 1})

prediction = 'G3'

X = np.array(data.drop([prediction], 1))
Y = np.array(data[prediction])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

model = LinearRegression()
model.fit(X_train, Y_train)

accuracy = model.score(X_test, Y_test)
print(accuracy)

X_new = np.array([[18, 1, 3, 40, 15, 16]])
Y_new = model.predict(X_new)

print(Y_new)

#1 Visualizing Correlations

plt.title("Correlation")
plt.xlabel("Study Time")
plt.ylabel("Final Grade")
plt.show()

plt.title("Correlation")
plt.xlabel("Second Grade")
plt.ylabel("Final Grade")
plt.show()

#2 Loading data

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
print(data.feature_names)
print(data.target_names)

X = np.array(data.data)
Y = np.array(data.target)
X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.1)

#3 Training and testing

knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train, Y_train)

accuracy = knn.score(X_test, Y_test)
print(accuracy)

#4 The best algorithm

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayers import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

clf1 = KNeighborsClassifier(n_neighbors=5)
clf2 = GaussianNB()
clf3 = LogisticRegression()
clf4 = DecisionTreeClassifier()
clf5 = RandomForestClassifier()

clf1.fit(X_train, Y_train)
clf2.fit(X_train, Y_train)
clf3.fit(X_train, Y_train)
clf4.fit(X_train, Y_train)
clf5.fit(X_train, Y_train)

print(clf1.score(X_test, Y_test))
print(clf2.score(X_test, Y_test))
print(clf3.score(X_test, Y_test))
print(clf4.score(X_test, Y_test))
print(clf5.score(X_test, Y_test))

X_new = np.array([[...]])
Y_new = clf.predict(X_new)

#5 Support verctor machines
# loading data

from sklearn.svn import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

data = load_breast_cancer()

X = data.data
Y = data.target
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=30)

# training and testing

model = SVC(kernel='linear', C=3)
model.ft(X_train, Y_train)

accuracy = model.score(X_test, Y_test)
print(accuracy)

# KNeighborsClassifier with random_state

knn = KNeughborsClassifier(n_neighbors=5)
knn.fit(X_train, Y_train)
knn_accuracy = knn.score(X_test, Y_test)
print(knn_accuracy)

#6 Clustering 
