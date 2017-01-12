import numpy as np


# sigmoid function
def sig(x, deriv=False):
    if (deriv is True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

# input data
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# output data
y = np.array([[0, 0, 1, 1]]).T

np.random.seed(1)
syn0 = 2 * np.random.random((3, 1)) - 1

for iter in range(10000):
    l0 = X
    l1 = sig(np.dot(l0, syn0))
    l1_error = y - l1
    l1_delta = l1_error * sig(l1, True)

    syn0 += np.dot(l0.T, l1_delta)
print("Output After Training:")
print(l1)
