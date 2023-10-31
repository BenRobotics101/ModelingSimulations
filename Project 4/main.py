# CST-305: Principles of Modeling and Simulation
# Project 4: Data Degradation
# Professor Ricardo Citro
# By: Trevor Pope and Ben Carter

# This program graphs out the two solutions found for Part 2 of the Data Degradation assignment.
# The first solution is x(t) = e^(-1/20)t
# The second solution is x(t) = -e^(-1/20)t

import numpy as np
import matplotlib.pyplot as plt

# Initial values
h = 0.1
x0 = 0

MAX_X =30

# Define the equations

def func(x):
    """The first solution found. e^(-1/20)t

    Args:
        x (float): The X values

    Returns:
        y: the Y values
    """
    return np.exp((-1 / 20) * x)

def func2(x):
    """The second solution found. e^(-1/20)t

    Args:
        x (float): The X values

    Returns:
        y: the Y values
    """
    return -1 * np.exp((-1 / 20) * x)


# Create the x-values with a step of h in between each value.
x_values = np.arange(x0, MAX_X+2*h, h)

# Calculate the points for the first homogeneous equation
fun1 = func(x_values)

# Calculate the points for the second homogeneous equation
fun2 = func2(x_values)

# Initialise the subplot function using number of rows and columns 
figure, axis = plt.subplots(2, 1) 
figure.subplots_adjust(hspace=0.5)
# figure.tight_layout(h_pad=2)

# Graph the plots, starting with Equation 1.
axis[0].plot(x_values, fun1, label='EQ1', linewidth=2.5, color="green")
axis[0].set_xlabel('t')
axis[0].set_ylabel('Data')
axis[0].legend()
axis[0].set_ylim(0, 1)
axis[0].set_xlim(0, 30)
axis[0].set_title("Solution 1") 

axis[1].plot(x_values, fun2, label='EQ2', linewidth=2.5, color="green")
axis[1].set_xlabel('t')
axis[1].set_ylabel('Data')
axis[1].legend()
axis[1].set_ylim(-1, 0)
axis[1].set_xlim(0, 30)
axis[1].set_title("Solution 2") 

  
# Combine all the operations and display 
plt.show() 