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
x_adjust = np.linspace(6, 0, 100)  # range of x values
y0 = [6.0, 1.0]

# Solve the differential equation using odeint
y_regular, y_prime = odeint(model, y0, x).T
y_regular2, y_prime2 = odeint(model, y0, x_adjust).T


taylor = model2(x)
    
figure, axis = plt.subplots() 

axis.plot(x+3, y_regular, label = "Real Solution", color = "green")
axis.plot(x_adjust-3, y_regular2, color = "green")
axis.plot(x, taylor, label = "Second Order Taylor Polynomial", color = "red")
axis.set_xlabel('x')
axis.set_ylabel('y')

axis.legend()
axis.set_xlim(0, 6)
axis.set_ylim(-20, 20)
axis.set_title('Taylor Polynomial vs. Real Solution')

plt.show()