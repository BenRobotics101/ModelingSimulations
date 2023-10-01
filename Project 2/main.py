# CST-305: Principles of Modeling and Simulation
# Project 2: Runge-Kutta-Fehlberg (RKF) for ODE
# Professor Ricardo Citro
# By: Trevor Pope and Ben Carter

# This program calculates the solution to the ODE using both the Runge-Kutta-Fehlburg method and SciPy's Odeint method.
# The program then compares the results of the two and graphs the results to demonstrate the result. The ODE used in this
# program is y' = -y + ln(x). The program uses Matplotlib's pyplot to graph the results. It also uses our own class called
# RKF which we created to do what Runge-Kutta-Fehlburg's method does.

###----------------###
### ODEINT Program ###
###----------------###

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from math import log
from RKF_Class import RKF

# Initial values
h = 0.3
x0 = 2
y0 = 1

MAX_X = 3500

# Define the differential equation
def method(y, x):
    dydx = -y + log(x)
    return dydx

# Create the x-values with a 0.3 step in between each value.
x_values = np.arange(x0, MAX_X+2*h, h)

# Call the odeint function to solve the differential equation for every x-value
solution = odeint(method, y0, x_values)

# Extract the y values from the solution
y_values = solution[:, 0]

###---------------------###
### Runge-Kutta Program ###
###----------------=----###

# Instantiate the RKF
rkf = RKF(function=method, x0=x0, y0=y0, h=h)

# Call the getArray function to get all the answers of the 
arrX, arrY = rkf.getArray(int((MAX_X - x0 + h) / h))

# Print out the values of the runge kutta and ode int methods
for i in range(len(arrX)):
    print(f"X: {arrX[i]:.1f}, Y_rkf: {arrY[i]:.6f}, Y_odeInt: {y_values[i]:.6f}")


# Setup initial values for calculating the difference between the runge kutta and odeint
ctAvg = 0
totlAvg = 0
maxVal = -1000
minVal = 10000
median = 0
diffs = []

# Calculate the difference between the runge kutta and odeint methods for every point
for r in enumerate(y_values):
    odeX = x_values[r[0]]
    odeY = r[1]

    rkfX = arrX[r[0]]
    rkfY = arrY[r[0]]

    diff = odeY - rkfY
    totlAvg += diff
    ctAvg += 1

    if(diff > maxVal):
        maxVal = diff
    
    if(diff < minVal):
        minVal = diff
    
    diffs.append(diff)

diffs.sort()

# Print the comparison between RKF and ODEINT
print("Stats for how different RKF is from ODEINT")
print("AVG: ",totlAvg / ctAvg)
print("MIN: ",minVal)
print("MAX: ",maxVal)
print("MEDIAN: ",diffs[len(diffs)//2])

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