import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from nn import Network
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

model = Network([29,40,2], "data/cc_weights.npy", "data/cc_biases.npy", load_existing=False)

path = Path(__file__).parent / "data"
data = pd.read_csv(path / "creditcard_2023.csv")
data = data.drop(['id'], axis=1)

train = np.array(data).T

print("Train/test data loaded")
m, n = train.shape
print(m, n)


X = train[0:m-1].T
Y = train[m-1]


X = preprocessing.minmax_scale(X)
print(X[:][0])
print(Y)
print(X.shape, Y.shape)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.33, shuffle=True, random_state=42)

Y_train = Y_train.reshape(Y_train.shape[0], 1)
print(X_train.shape, Y_train.shape)

model.sgd_train(X_train, Y_train, X_test, Y_test, epochs=29, batch_size=1024, lr=1, verbose=True, reg=False)
acc = model.evaluate(X_test, Y_test)
print(f"Accuracy: {acc*100}%")

