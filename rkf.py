###----------------###
### ODEINT Program ###
###----------------###

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

h = 0.1
x0 = 0
y0 = 1

def method(y, x):
    dydx = x**2 + y
    return dydx

x_values = np.arange(x0, .5, h)

solution = odeint(method, y0, x_values)

# Extract the y values from the solution
y_values = solution[:, 0]

for i in range(len(x_values)):
    print(f"({x_values[i]}, {y_values[i]})")


###---------------------###
### Runge-Kutta Program ###
###----------------=----###

def rkfmethod(x,y):
    dydx = x**2 + y
    return dydx

def k1method(x,y,h):
    k1 = rkfmethod(x,y)
    return k1

def k2method(x,y,h):
    k2 = rkfmethod(x+h/2, y+h/2*k1method(x,y,h))
    return k2

def k3method(x,y,h):
    k3 = rkfmethod(x+h/2, y+h/2*k2method(x,y,h))
    return k3

def k4method(x,y,h):
    k4 = rkfmethod(x+h, y+h*k3method(x,y,h))
    return k4

def y1method(x,y,h):
    y1 = y0 + h/6 * (k1method(x,y,h) + 2*(k2method(x,y,h)) + 2*(k3method(x,y,h)) + k4method(x,y,h))
    return y1

print(y1method(x0,y0,h))
