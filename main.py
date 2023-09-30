###----------------###
### ODEINT Program ###
###----------------###

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from math import log
from RKF_Class import RKF

h = 0.1
x0 = 2
y0 = 1

def method(y, x):
    dydx = -y + log(x)
    return dydx

x_values = np.arange(x0, 352.1, h)

solution = odeint(method, y0, x_values)

# Extract the y values from the solution
y_values = solution[:, 0]

for i in range(len(x_values)):
    print(f"X: {x_values[i]:.1f}, Y: {y_values[i]}")


###---------------------###
### Runge-Kutta Program ###
###----------------=----###

rkf = RKF(function=method, x0=x0, y0=y0, h=h)
arrX, arrY = rkf.getArray(3500)

for i in range(len(arrX)):
    print(f"X: {arrX[i]:.1f}, Y: {arrY[i]}")


# Create a figure and axis
fig, ax = plt.subplots()

# Plot the first set of data as a line
ax.plot(x_values, y_values, label='Odeint', linewidth=2.5, color="green")

# Plot the second set of data as a line
ax.plot(arrX, arrY, label='Runge-Kutta', linestyle=(0, (5, 4)), color="red", linewidth=2.5)

# Add labels and a title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title("Runge-Kutta vs. Odeint for Solving ODE's")

# Add a legend to differentiate between the two data sets
ax.legend()

# Display the plot
plt.show()