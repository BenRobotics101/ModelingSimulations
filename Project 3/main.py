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
import math

# Initial values
h = 0.1
x0 = 0
y0 = [0, 0]

MAX_X = 1.6

# Define the differential equation
def func1(y_parts, x):
    dydx = y_parts[1]
    y = y_parts[0]

    return (dydx,x - 4 * y)

def solution1(x):
    y = (-1 / 8) * np.sin(2 * x) + (1 / 4) * x
    return y
    

# Create the x-values with a 0.3 step in between each value.
x_values = np.arange(x0, MAX_X+2*h, h)

# Call the odeint function to solve the differential equation for every x-value
solution = odeint(func1, y0, x_values)

# Extract the y values from the solution
y_values = solution[:, 0]

y_values_sol = solution1(x_values)

# Initialise the subplot function using number of rows and columns 
figure, axis = plt.subplots(1, 3) 
  

# Plot the first set of data as a line
axis[1].plot(x_values, y_values, label='Odeint', linewidth=2.5, color="green")
axis[1].plot(x_values, y_values_sol, label='Manual Solution', linestyle=(0, (5, 4)), color="red", linewidth=2.5)
axis[1].set_xlabel('X')
axis[1].set_ylabel('Y')
axis[1].legend()
axis[1].set_title("ODEINT vs Manual Solution Function") 

axis[0].plot(x_values, y_values, label='Odeint', linewidth=2.5, color="green")
axis[0].set_xlabel('X')
axis[0].set_ylabel('Y')
axis[0].legend()
axis[0].set_title("ODEINT") 

axis[2].plot(x_values, y_values_sol, label='Manual Solution', linestyle=(0, (5, 4)), color="red", linewidth=2.5)
axis[2].set_xlabel('X')
axis[2].set_ylabel('Y')
axis[2].legend()
axis[2].set_title("Manual Solution Function") 
  
# Combine all the operations and display 
plt.show() 