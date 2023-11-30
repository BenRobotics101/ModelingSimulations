import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def model(y, x):
    """
    Matrix Method to solve for the actual solution to the differential equation:
    y'' = (x-2)y' - 2y
    """
    y1, y2 = y
    return [y2, (x-2) * y2 - 2 * y1]

def model2(x):
    """
    Second Order Taylor Polynomial solution near x = 3 of the differential equation:
    y'' = (x-2)y' - 2y
    """
    return 6 + (x-3) - 11/2*(x-3)**2


x = np.linspace(0, 6, 100)  # range of x values
y0 = [6.0, 1.0]

# Solve the differential equation using odeint
y_regular, y_prime = odeint(model, y0, x).T

taylor = model2(x)
    
figure, axis = plt.subplots() 

axis.plot(x, y_regular, label = "Real Solution", color = "green")
axis.plot(x, taylor, label = "Second Order Taylor Polynomial", color = "red")
axis.set_xlabel('x')
axis.set_ylabel('y')

axis.legend()
axis.set_xlim(0, 6)
axis.set_title('Part 1B')

plt.show()

#---------------
#    Part 2
#---------------

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
fun1 = odeint(func, [1, -1], x_values)[:,1]

# Calculate the points for the second homogeneous equation
fun2 = func2(x_values)

# Initialise the subplot function using number of rows and columns 
figure1, axis1 = plt.subplots() 
# figure.tight_layout(h_pad=2)

# Graph the plots, starting with Equation 1.
axis1.plot(x_values, fun1, label='Real Solution', linewidth=2.5, color="green")
axis1.plot(x_values, fun2, label='General Solution', linewidth=2.5, color="red")
axis1.set_xlabel('t')
axis1.set_ylabel('Data')
axis1.xaxis.grid(True, which='major')
axis1.yaxis.grid(True, which='major')

axis1.legend()
axis1.set_ylim(-10, 10)
axis1.set_xlim(0, 3)
axis1.set_title("Part 2") 


  
# Combine all the operations and display 
plt.show() 