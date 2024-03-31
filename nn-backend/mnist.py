import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from nn import Network
from pathlib import Path
from sklearn.model_selection import train_test_split

model = Network([784,700,500,300,10], "nn-backend/data/mnist_weights.npy", "nn-backend/data/mnist_biases.npy")

path = Path(__file__).parent / "data"

train = np.array(pd.read_csv(path / "mnist_train.csv")).T
# test = np.array(pd.read_csv(path / "mnist_test.csv"))

print("Train/test data loaded")
# np.random.shuffle(train)
m, n = train.shape
print(m, n)

X = train[1:n].T
Y = train[0]
X = X / 255

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.6, shuffle=True)

Y_train = Y_train.reshape(Y_train.shape[0], 1)
print(X_train.shape, Y_train.shape)

model.sgd_train(X_train, Y_train, X_test, Y_test, epochs=100, batch_size=2056, lr=0.15, verbose=True)
acc = model.mnist_evaluate(X_test, Y_test)
print(f"Accuracy: {acc*100}%")