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

def func2(y_parts, x):
    dydx = y_parts[1]
    y = y_parts[0]

    return (dydx, 4 - y)

def solution1(x):
    y = (-1 / 8) * np.sin(2 * x) + (1 / 4) * x
    return y

def solution2(x):
    y = -4 * np.cos(x) + 4
    return y

    

# Create the x-values with a 0.3 step in between each value.
x_values = np.arange(x0, MAX_X+2*h, h)

# Call the odeint function to solve the differential equation for every x-value
solutionVal1 = odeint(func1, y0, x_values)

# Call the odeint function to solve the differential equation for every x-value
solutionVal2 = odeint(func2, y0, x_values)

# Extract the y values from the solution
y_values = solutionVal1[:, 0]
y_values2 = solutionVal2[:, 0]

y_values_sol1 = solution1(x_values)
y_values_sol2 = solution2(x_values)

# Initialise the subplot function using number of rows and columns 
figure, axis = plt.subplots(2, 3) 
figure.tight_layout(h_pad=4)

# Plot the first set of data as a line
axis[0, 1].plot(x_values, y_values, label='Odeint', linewidth=2.5, color="green")
axis[0, 1].plot(x_values, y_values_sol1, label='Manual Solution', linestyle=(0, (5, 4)), color="red", linewidth=2.5)
axis[0, 1].set_xlabel('X')
axis[0, 1].set_ylabel('Y')
axis[0, 1].legend()
axis[0, 1].set_title("ODEINT vs Manual Solution Function EQ 1") 

axis[0, 0].plot(x_values, y_values, label='Odeint', linewidth=2.5, color="green")
axis[0, 0].set_xlabel('X')
axis[0, 0].set_ylabel('Y')
axis[0, 0].legend()
axis[0, 0].set_title("ODEINT EQ1") 

axis[0, 2].plot(x_values, y_values_sol1, label='Manual Solution', linestyle=(0, (5, 4)), color="red", linewidth=2.5)
axis[0, 2].set_xlabel('X')
axis[0, 2].set_ylabel('Y')
axis[0, 2].legend()
axis[0, 2].set_title("Manual Solution EQ1") 


axis[1, 1].plot(x_values, y_values2, label='Odeint', linewidth=2.5, color="green")
axis[1, 1].plot(x_values, y_values_sol2, label='Manual Solution', linestyle=(0, (5, 4)), color="red", linewidth=2.5)
axis[1, 1].set_xlabel('X')
axis[1, 1].set_ylabel('Y')
axis[1, 1].legend()
axis[1, 1].set_title("ODEINT vs Manual Solution Function") 

axis[1, 0].plot(x_values, y_values2, label='Odeint', linewidth=2.5, color="green")
axis[1, 0].set_xlabel('X')
axis[1, 0].set_ylabel('Y')
axis[1, 0].legend()
axis[1, 0].set_title("ODEINT EQ2") 

axis[1, 2].plot(x_values, y_values_sol2, label='Manual Solution', linestyle=(0, (5, 4)), color="red", linewidth=2.5)
axis[1, 2].set_xlabel('X')
axis[1, 2].set_ylabel('Y')
axis[1, 2].legend()
axis[1, 2].set_title("Manual Solution EQ2") 
  
# Combine all the operations and display 
plt.show() 