import numpy as np
from scipy.special import softmax

np.seterr(over='ignore')

# funzioni di attivazione
def identity(x):
    return x

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# derivate funzioni di attivazione
def identity_deriv(x):
    return np.ones(x.shape)

def sigmoid_deriv(x):
    z = sigmoid(x)
    return z * (1 - z)

# funzioni di errore
def sum_of_squares(y, t):
    return 0.5 * np.sum(np.power(y - t, 2))

def cross_entropy(y, t, epsilon=1e-15):
    y = np.clip(y, epsilon, 1. - epsilon)
    return - np.sum(t * np.log(y))

def cross_entropy_softmax(y, t):
    softmax_y = softmax(y, axis=0)
    return cross_entropy(softmax_y, t)

# derivate funzioni di errore
def sum_of_squares_deriv(y, t):
    return y - t

# da verificare
def cross_entropy_deriv(y, t):
    return - t / y

def cross_entropy_softmax_deriv(y, t):
    softmax_y = softmax(y, axis=0)
    return softmax_y - t


activation_functions = [sigmoid, identity]
activation_functions_deriv= [sigmoid_deriv, identity_deriv]

error_functions = [cross_entropy, cross_entropy_softmax, sum_of_squares]
error_functions_deriv = [cross_entropy_deriv, cross_entropy_softmax_deriv, sum_of_squares_deriv]
