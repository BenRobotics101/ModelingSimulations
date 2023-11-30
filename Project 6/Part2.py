###############
# Part 2 - Taylor Polynomials Project 6
# Benjamin Carter and Trevor Pope
# 11/29/2023
# 
# This program computes the solution to two different differential equations and then
# graphs the result. It also graphs a Taylor polynomial to allow for comparison between the two.
#
############## 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define Functions
def model_2_deq(y, x):
    """
    Matrix Method to solve for the actual solution to the differential equation:
    y'' = (2*x)y' - 2y
    """
    return [y[1], -1 * y[0] / ( x * x + 4) + x / (x * x + 4)]

def model_2_ans(x):
    """
    Second Order Power Series solution near x = 0 of the differential equation:
    y'' = (2*x)y' - 2y
    """
    a = 1
    b = -1
    out = a * (1 - (1/8) * np.power(x,2) + (1/128) * np.power(x,4) - (13/15360) * np.power(x,6) + (961/3440640) * np.power(x,8) - (7657/412876800) * np.power(x,10))
    out += b * (x - (1/24) * np.power(x,3) + (7/1920) * np.power(x,5) - (7/15360) * np.power(x,7) + (301/4423680) * np.power(x,9))
    return out


####### PART 2

x_1a = np.linspace(0, 5, 100)
y0_1a = [1, -1]

y_regular_1a, y_prime_1a = odeint(model_2_deq, y0_1a, x_1a).T

taylor_1a = model_2_ans(x_1a)

# Graph

figure, axis = plt.subplots() 

axis.plot(x_1a, y_regular_1a, label = "Real Solution", color = "green")
axis.plot(x_1a, taylor_1a, label = "Taylor Polynomial", color = "red")
axis.set_xlabel('x')
axis.set_ylabel('y')

axis.plot(3.5, -29.296875, 'bo')
axis.text(3.5 * 0.7, -29.296875 * (0.95) , "y(-3.5) = -29.296875", fontsize=12)

axis.legend()
axis.set_xlim(0, 4.5)
axis.set_ylim(-10, 10)
axis.set_title('Taylor Polynomial vs. Real Solution - Part 2')


plt.show()