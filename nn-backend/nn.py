
import numpy as np
import pathlib
from statistics import mean
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

np.random.seed(42)

def sigmoid(h):
    return 1/(1+np.exp(-h))

def relu(h):
    return np.maximum(0,h)

def sigmoid_backward(h):
    sig = sigmoid(h)
    return sig * (1 - sig)

def relu_backward(dZ, h):
    """Returns d(h_n) * z_n"""
    dh = np.array(dZ, copy = True)
    dh[h <= 0] = 0
    dh[h > 0] = 1
    return dh

class Network:
  """A Neural Network Class to Perform Basic Feedforward algorithm and training"""
  def __init__(self, sizes: list, weight_path: str, bias_path: str, load_existing: bool):
    """Initialize a numpy array or a list of weights an array or list of weights depending on sizes"""
    self.sizes = sizes
    self.num_layers = len(sizes)
    self.weights = []
    self.biases = []

    cwd = pathlib.Path.cwd()
    self.wpath = cwd/weight_path or ""
    self.bpath = cwd/bias_path or ""
    self.load_existing = load_existing or False
    self.__init_params()

    return

  def __init_params(self):
    """Initialize random weights and biases based on size parameters."""
    if self.wpath.exists() and self.bpath.exists() and self.load_existing:
      print("Loading existing model...")
      self.weights = np.load(self.wpath, allow_pickle=True)
      self.biases = np.load(self.bpath, allow_pickle=True)
    else:
      for i in range(1, self.num_layers):
          # X inputs -> Y Ouputs
          in_size = self.sizes[i-1]
          out_size = self.sizes[i]

          # weights.shape = (Y, X), biases.shape = (Y, 1)
          # e.g. 2 -> 3: weights is (2, 3), biases is (1, 3)
          self.weights.append(np.random.randn(out_size, in_size) * 0.3)
          self.biases.append(np.random.randn(out_size, 1) * 0.3)

  def forward(self, x: np.ndarray):
    """
      Perform feedforward algorithm on input vector for all layers

      Input:    x: np.ndarray with shape (1, self.sizes[0])

      Returns:  y: np.ndarray with shape (1, self.sizes[-1])
    """

    # Store inner layers for backward calculation (?)
    x = x.reshape(x.shape[0], 1)

    activations = [x]
    zs = []

    for i in range(self.num_layers-1):
        x = np.matmul(self.weights[i], x) + self.biases[i]
        zs.append(x)
        x = sigmoid(x)
        activations.append(x)
    return x, activations, zs

  def backward(self, x: np.ndarray, y: np.ndarray):

    """Return a tuple ``(delta_w, delta_b)`` representing the
        gradient for the cost function C_x.  ``nabla_b`` and
        ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
        to ``self.biases`` and ``self.weights``."""
    delta_b = [np.zeros(b.shape) for b in self.biases]
    delta_w = [np.zeros(w.shape) for w in self.weights]
    # feedforward
    activation = x
    res, activations, zs = self.forward(activation)

    # backward pass
    delta = (activations[-1] - y) * sigmoid_backward(zs[-1])
    delta_b[-1] = delta
    delta_w[-1] = np.dot(delta, activations[-2].transpose())

    for l in range(2, self.num_layers):
        z = zs[-l]
        sp = sigmoid_backward(z)
        delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
        delta_b[-l] = delta
        delta_w[-l] = np.dot(delta, activations[-l-1].transpose())
    return (delta_w, delta_b)

  def train(self, X_train, y_train, X_test, y_test, epochs=1e6, lr=0.01, verbose=True):
      """Using forward and backward functions, fit the model on an entire training step using gradient descent algorithm."""
      k = 0
      n = X_train.shape[0]
      d_x = X_train.shape[1]
      d_y = y_train.shape[1]

      if self.wpath.exists() and self.bpath.exists():
        print("Existing model found, load it? [Y/N]: ")
        res = input()
        while res.lower() not in {'y', 'n'}:
           print("Please enter [Y/N]:")
           res = input()
        if res.lower() == 'y':
                print("Loading model...")
                self.weights = np.load(self.wpath, allow_pickle=True)
                self.biases = np.load(self.bpath, allow_pickle=True)
                return
      print(f"Training...\nParams: num_epochs: {epochs}, lr: {lr}, normal GD")

      prev_loss = self.calc_squared_loss(X_train, y_train)
      new_loss = prev_loss
      while (k < epochs and (k == 0 or abs(prev_loss - new_loss) > 1e-5)):
        for x, y in zip(X_train, y_train):
          x = x.reshape((d_x, 1))
          y = y.reshape((d_y, 1))
          delta_w, delta_b = self.backward(x, y)
          for i in range(len(self.weights)):
            self.weights[i] -= lr * delta_w[i]
            self.biases[i] -= lr * delta_b[i]

          prev_loss = new_loss
          # new_loss = self.calc_squared_loss(X_train, y_train)

          if verbose:
            print(f"Iteration {k}, mean loss: {new_loss}")
          k+=1

      np.save(self.wpath, np.array(self.weights, dtype=object))
      np.save(self.bpath, np.array(self.biases, dtype=object))

  def sgd_train(self, X_train, y_train, X_test, y_test, epochs=1e6, lr=0.01, batch_size=1, verbose=True, reg=False):
    """Using forward and backward functions, fit the model on an entire training step using gradient descent algorithm."""
    k = 0
    n = X_train.shape[0]
    d_x = X_train.shape[1]
    d_y = y_train.shape[1]

    print(n, d_x, d_y)

    if self.wpath.exists() and self.bpath.exists():
        print("Existing model found, load it? [Y/N]: ")
        res = input()
        while res.lower() not in {'y', 'n'}:
           print("Please enter [Y/N]:")
           res = input()
        if res.lower() == 'y':
                print("Loading model...")
                self.weights = np.load(self.wpath, allow_pickle=True)
                self.biases = np.load(self.bpath, allow_pickle=True)
                return
    print(f"Training...\nParams: num_epochs: {epochs}, lr: {lr}, batch size: {batch_size}, SGD")

    if reg:
        prev_loss = self.calc_squared_loss(X_train, y_train)
        new_loss = prev_loss
    else:
       prev_loss = 1
       new_loss = 0

    while (k < epochs and (k == 0 or abs(prev_loss - new_loss) > 1e-5)):
        rng = np.random.permutation(n)
        for i in range(batch_size):
            x = X_train[rng[i]].reshape((d_x, 1))
            y = y_train[rng[i]].reshape((d_y, 1))
            y = self.cc_one_hot(int(y.item()))

            # print(x.shape,y.shape)

            delta_w, delta_b = self.backward(x, y)
            for i in range(len(self.weights)):
                self.weights[i] -= lr * delta_w[i]
                self.biases[i] -= lr * delta_b[i]
            
        if reg:
            prev_loss = new_loss
            new_loss = self.calc_squared_loss(X_train, y_train)

        if verbose and reg:
            print(f"Epoch {k}, mean loss: {new_loss}")
        elif verbose:
            acc = self.evaluate(X_test, y_test)
            print(f"Epoch {k}, accuracy: {acc*100}%")
        k+=1

    np.save(self.wpath, np.array(self.weights, dtype=object))
    np.save(self.bpath, np.array(self.biases, dtype=object))

  def calc_squared_loss(self, X, y):
    """Helper func to calculate squared loss given by 1/2(y-y')^2."""
    sum = 0
    n = X.shape[0]
    d = X.shape[1]
    for i in range(len(X)):
      y_v, _, _ = self.forward(X[i].reshape(d,1))
      sum += ((y[i] - y_v) ** 2) / 2
    return np.mean(sum) / n
  
  def mnist_one_hot(self, Y):
    one_hot_Y = np.zeros((1, 10))
    one_hot_Y[np.arange(1), Y] = 1
    return one_hot_Y.T
  
  def nid_one_hot(self, Y):
    one_hot_Y = np.zeros((1, 23))
    one_hot_Y[np.arange(1), Y] = 1
    return one_hot_Y.T
  
  def cc_one_hot(self, Y):
    one_hot_Y = np.zeros((1, 2))
    one_hot_Y[np.arange(1), Y] = 1
    return one_hot_Y.T

  def evaluate(self, X_test, y_test):
    correct = 0
    n = X_test.shape[0]
    for x, y in zip(X_test, y_test):
        pred = self.forward(x)[0]
        # print(pred, np.argmax(pred), y)
        if np.argmax(pred) == y:
            correct += 1
    return correct / n

  def cc_evaluate(self, X_test, y_test):
    sum = 0
    n = X_test.shape[0]
    d_x = X_test.shape[1]
    # X_test = X_test.reshape((n, d_x))
    # y_test = y_test.reshape((1, n))
    for x, y in zip(X_test, y_test):
        x = x.reshape((d_x, 1))
        y = y.reshape((1, 1))
        pred, _, _ = self.forward(x)
        # print(x)
        # print(pred, y)
        pred = 1 if pred >= 0.5 else 0
        # print(np.argmax(pred), y)
        if pred == y:
            sum += 1
    return sum / n
          