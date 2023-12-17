###############
# Part C Question 1
# Benjamin Carter and Trevor Pope
# 12/16/2023
# 
# This program graphs 
#
############## 

import matplotlib.pyplot as plt
import numpy as np


def calculateIntegral_LHS(function, start, end, subdivisions):
    area = 0
    x = start
    divisions = (end - start) / subdivisions
    while(x < end):
        yValue = function(x)
        area += yValue * divisions
        x += divisions

    return area


def equation(xValue):
    yValue = np.log(xValue)
    return yValue

n = 10000
a = 1
b = np.e

print("Left Hand Sum: ", calculateIntegral_LHS(equation, a, b, n))

X = np.linspace(1, 3, n, endpoint=True)
Y = equation(X)
X_Fill = np.linspace(1, np.e, n, endpoint=True)
Y_Fill = equation(X_Fill)
fig, ax = plt.subplots()
ax.plot(X, Y, color='blue', alpha=1.00)
ax.fill_between(X_Fill, Y_Fill, 0, color='blue', alpha=.1)
ax.set_xlabel("X-Values")
ax.set_ylabel("V-Values")
ax.title.set_text("Left Riemann Sum")
plt.show()

