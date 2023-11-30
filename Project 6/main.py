import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def model_1a_deq(y, x):
    """
    Matrix Method to solve for the actual solution to the differential equation:
    y'' = (2*x)y' - 2y
    """
    return [y[1], 2 * x * y[1] - x * x * y[0]]

def model_1a_ans(x):
    return 1 - x - (1/3) * x * x * x - (1/12) * x * x * x * x

def model_1b_deq(y, x):
    """
    Matrix Method to solve for the actual solution to the differential equation:
    y'' = (x-2)y' - 2y
    """
    y1, y2 = y
    return [y2, (x-2) * y2 - 2 * y1]

def model_1b_ans(x):
    """
    Second Order Taylor Polynomial solution near x = 3 of the differential equation:
    y'' = (x-2)y' - 2y
    """
    return 6 + (x-3) - 11/2*(x-3)**2






####### PART 1 A

x_1a = np.linspace(0, 4, 100)
y0_1a = [1, -1]

y_regular_1a, y_prime_1a = odeint(model_1a_deq, y0_1a, x_1a).T

taylor_1a = model_1a_ans(x_1a)

######## PART 1 B

x_1b = np.linspace(0, 6, 100)  # range of x values
x_adjust_1b = np.linspace(6, 0, 100)  # range of x values
y0_1b = [6.0, 1.0]

# Solve the differential equation using odeint
y_regular_1b, y_prime_1b = odeint(model_1b_deq, y0_1b, x_1b).T
y_regular2_1b, y_prime2_1b = odeint(model_1b_deq, y0_1b, x_adjust_1b).T

taylor_1b = model_1b_ans(x_1b)


figure, axis = plt.subplots() 

axis.plot(x_1a, y_regular_1a, label = "Real Solution", color = "green")
axis.plot(x_1a, taylor_1a, label = "Second Order Taylor Polynomial", color = "red")
axis.set_xlabel('x')
axis.set_ylabel('y')

axis.plot(3.5, -29.296875, 'bo')
axis.text(3.5 * 0.7, -29.296875 * (0.95) , "y(-3.5) = -29.296875", fontsize=12)

axis.legend()
axis.set_xlim(0, 4)
axis.set_ylim(-40, 20)
axis.set_title('Taylor Polynomial vs. Real Solution - Part 1A')


figure2, axis2 = plt.subplots() 

axis2.plot(x_1b+3, y_regular_1b, label = "Real Solution", color = "green")
axis2.plot(x_adjust_1b-3, y_regular2_1b, color = "green")
axis2.plot(x_1b, taylor_1b, label = "Second Order Taylor Polynomial", color = "red")
axis2.set_xlabel('x')
axis2.set_ylabel('y')

axis2.legend()
axis2.set_xlim(0, 6)
axis2.set_ylim(-20, 20)
axis2.set_title('Taylor Polynomial vs. Real Solution - Part 1B')

plt.show()