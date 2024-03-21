import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

from sklearn.discriminant_analysis import StandardScaler
from nn import Network
from pathlib import Path
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# def generate_data():
#     # Define correlation values
#     corr_a = 0.8
#     corr_b = 0.4
#     corr_c = -0.2
    
#     # Generate independent features
#     a = np.random.normal(0, 1, size=100000)
#     b = np.random.normal(0, 1, size=100000)
#     c = np.random.normal(0, 1, size=100000)
#     d = np.random.randint(0, 4, size=100000)
#     e = np.random.binomial(1, 0.5, size=100000)
    
#     # Generate target feature based on independent features
#     target = 50 + corr_a*a + corr_b*b + corr_c*c + d*10 + 20*e + np.random.normal(0, 10, size=100000)
    
#     # Create DataFrame with all features
#     df = pd.DataFrame({'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'target': target})
#     return df

# df = generate_data()

# # Separate the features and target
# X = df.drop('target', axis=1)
# y = df['target']

# scaler = StandardScaler()
# X = scaler.fit_transform(X)

# # Split the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# y_train = y_train.to_numpy().reshape(-1,1)
# y_test = y_test.to_numpy().reshape(-1,1)

# model = Network([X_train.shape[1],10,10,1])

# print(X_train.shape, y_train.shape)
# model.train(X_train, y_train, epochs=20, lr=0.0001, batch_size=32, verbose=True)


# y_pred = model.predict(X_test)

# model.plot_learning()

# print("Test error: ", mean_squared_error(y_test, y_pred))


model = Network([2,3,3,1])

path = Path(__file__).parent.parent / "week2_data.csv"

train = np.array(pd.read_csv(path))
                 
m, n = train.shape
print(m, n)

X = train[:, [0,1]]
y = train[:, 2]

X_train, X_test, Y_train, Y_test = train_test_split(X, y , train_size=0.6, shuffle=True)

print(X_train.shape, Y_train.shape)
Y_train = Y_train.reshape(Y_train.shape[0], 1)
model.train(X_train, Y_train, epochs=100, lr=0.0001, verbose=True)



