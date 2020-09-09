#!/usr/local/bin/python3

from math import log
import numpy as np
import matplotlib.pyplot as plt

# Vetor de números linearmente espaçados
numbers = np.linspace(1, 10, 100)

labels = [
    'Constant',
    'Logarithmic',
    'Linear',
    'Log linear',
    'Quadratic',
    'Cubic',
    'Exponential'
]

big_o = [
    np.ones(numbers.shape), # Constant
    np.log(numbers), # Logarithmic
    numbers, # Linear
    numbers * np.log(numbers), # Log linear
    numbers ** 2, # Quadratic
    numbers ** 3, # Cubic
    2 ** numbers  # Exponential
]

plt.figure(figsize=(10,8))
plt.ylim(0, 100)
for i in range(len(big_o)):
    plt.plot(numbers, big_o[i], label = labels[i])
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('numbers')