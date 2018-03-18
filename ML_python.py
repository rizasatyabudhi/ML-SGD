import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math as mt


dataset = pd.read_csv('irisdata.csv')

dataset['class'] = dataset['class'].str.replace('Iris-setosa', '0')
dataset['class'] = dataset['class'].str.replace('Iris-virginica', '1')


dataset = dataset.astype('float64')
# print(dataset)


# Initial Variables

alpha = 0.1
# theta = np.array([0.6,0.4,0.2,0.3])

# User input theta
print("input your theta")
theta = [float(x) for x in input().split()]
theta.array(initial_theta)
print(theta)

bias = 0.9

