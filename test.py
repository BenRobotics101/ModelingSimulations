import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

h = 0.1
x0 = 0
y0 = 1

def method(y, x):
    dydx = x * x + y
    return dydx

x_values = np.arange(x0, 1.5, h)

solution = odeint(method, y0, x_values)

# Extract the y values from the solution
y_values = solution[:, 0]

for i in range(len(x_values)):
    print(f"({x_values[i]}, {y_values[i]})")


###---------------------###
### Runge-Kutta Program ###
###----------------=----###