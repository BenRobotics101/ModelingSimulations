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
from matplotlib.patches import Rectangle, Patch
import time

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

startTime = time.time()

n = 10000
a = 1
b = np.e

print("Left Hand Sum: ", calculateIntegral_LHS(equation, a, b, n))

X = np.linspace(1, 3, n, endpoint=True)
Y = equation(X)
X_Fill = np.linspace(1, np.e, n, endpoint=True)
Y_Fill = equation(X_Fill)
fig, ax = plt.subplots()
ax.plot(X, Y, label="Function F(x)", color='blue', alpha=1.00)
ax.fill_between(X_Fill, Y_Fill, 0, color=(0, 0.6, 0.8, 0.8), alpha=.5)

dummyLegendText = Patch(color=(0, 0.6, 0.8, 0.8), label='Left Hand Measurements')
h, l = ax.get_legend_handles_labels()

ax.legend(handles=h + [dummyLegendText])
ax.set_xlabel("X-Values")
ax.set_ylabel("V-Values")
ax.title.set_text("Left Riemann Sum")

endTime = time.time()
timeLength = int((endTime - startTime) * 1000)
print(f"Calculations took {timeLength / 1000} seconds to run.")

plt.show()

