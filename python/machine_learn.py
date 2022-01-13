"""Little bit machine learning about."""

import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
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
