# CST-305: Principles of Modeling and Simulation
# Project 4: Data Degradation
# Professor Ricardo Citro
# By: Trevor Pope and Ben Carter

# This program graphs out the two solutions found for Part 2 of the Data Degradation assignment.
# The first solution is x(t) = e^(-1/20)t
# The second solution is x(t) = -e^(-1/20)t

import numpy as np
import matplotlib.pyplot as plt
import scipy

# Initial values
h = 0.1
x0 = 0

MAX_X = 8

# Define the equations

def func(y, x):
    #return [y[1],
    #        2 * x * y[1] - x * x * y[0]
    #        ]

    return [y[1],
            -1 * y[0] / ( x * x + 4) + x / (x * x + 4)
            ]
    


def func2(x):
    #return 1 - x - (1/3) * x * x * x - (1/12) * x * x * x * x
    a = -1
    b = -0.2
    out = a * (1 - (1/8) * np.power(x,2) + (1/128) * np.power(x,4) - (13/15360) * np.power(x,6) + (961/3440640) * np.power(x,8) - (7657/412876800) * np.power(x,10))
    out += b * (x - (1/24) * np.power(x,3) + (7/1920) * np.power(x,5) - (7/15360) * np.power(x,7) + (301/4423680) * np.power(x,9))
    return out
    
# Create the x-values with a step of h in between each value.
x_values = np.arange(x0, MAX_X+2*h, h)

# Calculate the points for the first homogeneous equation
fun1 = scipy.integrate.odeint(func, [1, -1], x_values)[:,1]

# Calculate the points for the second homogeneous equation
fun2 = func2(x_values)

# Initialise the subplot function using number of rows and columns 
figure, axis = plt.subplots() 
# figure.tight_layout(h_pad=2)

# Graph the plots, starting with Equation 1.
axis.plot(x_values, fun1, label='EQ1', linewidth=2.5, color="green")
axis.plot(x_values, fun2, label='EQ2', linewidth=2.5, color="red")
axis.set_xlabel('t')
axis.set_ylabel('Data')
axis.xaxis.grid(True, which='major')
axis.yaxis.grid(True, which='major')

axis.legend()
axis.set_ylim(-10, 10)
axis.set_xlim(0, 3)
axis.set_title("Solutions") 


  
# Combine all the operations and display 
plt.show() 