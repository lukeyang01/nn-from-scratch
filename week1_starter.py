import numpy as np
import pandas as pd
import math

# Week 1 Dataset
df = pd.read_csv('https://raw.githubusercontent.com/lukeyang01/nn-from-scratch/main/week1_data.csv')
# TODO: First view the input data using head(), then store the top N inputs in a np array
# Hint: List[:x] can extract the first x elements of a python list
inputs = None

# Week 2 Dataset
# df = pd.read_csv('https://raw.githubusercontent.com/lukeyang01/nn-from-scratch/main/week2_data.csv')
# inputs = np.array(df.iloc[:, 0:2])
# labels = np.array(df.iloc[:, 2])

def sigmoid(x: int) -> float:
  """Sigmoid activation function."""
  return 1 / (1 + math.exp(-x))

# OPTIONAL TODO: Try experimenting with other activation functions (Linear, RELU, Tanh are all commonly used)

class Perceptron:
  """Neuron class object representing perceptron."""

  def __init__(self, num_inputs: int) -> None:
    """Init weights and other information."""

    self.num_inputs = num_inputs

    # TODO: declare a variable to store weights similar to how num_inputs is stored
    # Define random weights in shape (1, num_inputs)

  def feed_forward(self, inputs: np.array) -> float:
    """Forward propogation step."""

    output = None

    # TODO: complete feed forward algorithm below

    return output

  def train(self, training_data):
    """Training Step"""
    # training_data should be a list of tuple of input output pairs
    # TODO: For each input output pair in “training_data” adjust the weights vector using the formula we learned.
    # YOU MAY START THIS DURING WEEK 1, BUT THIS WILL BE LARGELY COVERED DURING WEEK 2

def main():
  """Test Perceptron class here."""

  # TODO: Declare your perceptron class below, run your feed_forward algorithm
  out = None

  print(f"Perceptron output after forward propogation: {out:.2f}")

main()