# CST-305: Principles of Modeling and Simulation
# Project 3: Green's Function
# Professor Ricardo Citro
# By: Trevor Pope and Ben Carter

# This program graphs out the homogeneous equation and the equations derived from the Green's function.
# The first equation is y" + 4y = x and the second equation is y" + y = 4. 
# This leaves the homogeneous equation of the first one to be: y = 0  (as subject to y(0) = y'(0) = 0)
# This leaves the homogeneous equation of the second one to also be y = 0

# For the particular solution, (y_h + y_p), the solution for the first equation is:
# y = (-1 / 8) * sin(2x) + (1/4)x

# For the second equation, the solution is:
# y = -4 * cos(x) + 4


import numpy as np
import matplotlib.pyplot as plt

# Initial values
h = 0.1
x0 = 0
y0 = [0, 0]

MAX_X =30

# Define the equations

def func1_H(x):
    """The homogeneous solution for the first equation

    Args:
        x (float): The X values

    Returns:
        y: the Y values
    """
    return 0 * x

def func2_H(x):
    """The homogeneous solution for the second equation

    Args:
        x (float): The X values

    Returns:
        y: the Y values
    """
    return 0 * x

def solution1(x):
    """The green's solution for the first equation

    Args:
        x (float): The X values

    Returns:
        y: the Y values
    """
    y = (-1 / 8) * np.sin(2 * x) + (1 / 4) * x
    return y

def solution2(x):
    """The green's solution for the second equation

    Args:
        x (float): The X values

    Returns:
        y: the Y values
    """
    y = -4 * np.cos(x) + 4
    return y

    

# Create the x-values with a step of h in between each value.
x_values = np.arange(x0, MAX_X+2*h, h)

# Calculate the points for the first homogeneous equation
fun1 = func1_H(x_values)

# Calculate the points for the second homogeneous equation
fun2 = func2_H(x_values)

# Extract the y values from both solutions
y_values = solution1(x_values)
y_values2 = solution2(x_values)

# Initialise the subplot function using number of rows and columns 
figure, axis = plt.subplots(2, 2) 
figure.tight_layout(h_pad=4)

# Graph the plots, starting with Equation 1.
axis[0, 0].plot(x_values, fun1, label='y_h', linewidth=2.5, color="green")
axis[0, 0].set_xlabel('X')
axis[0, 0].set_ylabel('Y')
axis[0, 0].legend()
axis[0, 0].set_title("Homogeneous General Solution EQ 1") 

axis[0, 1].plot(x_values, y_values, label='Green\'s Function Solution', color="red", linewidth=2.5)
axis[0, 1].set_xlabel('X')
axis[0, 1].set_ylabel('Y')
axis[0, 1].legend()
axis[0, 1].set_title("Green's Function Solution EQ 1") 

axis[1, 0].plot(x_values, fun2, label='y_h', linewidth=2.5, color="green")
axis[1, 0].set_xlabel('X')
axis[1, 0].set_ylabel('Y')
axis[1, 0].legend()
axis[1, 0].set_title("Homogeneous General Solution EQ 2") 

axis[1, 1].plot(x_values, y_values2, label='Green\'s Function Solution', color="red", linewidth=2.5)
axis[1, 1].set_xlabel('X')
axis[1, 1].set_ylabel('Y')
axis[1, 1].legend()
axis[1, 1].set_title("Green's Function Solution EQ 2") 
  
# Combine all the operations and display 
plt.show() 