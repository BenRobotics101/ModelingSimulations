###############
# Part 1 - Taylor Polynomials Project 6
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


def model_1a_deq(y, x):
    """
    Matrix Method to solve for the actual solution to the differential equation:
    y'' = (2*x)y' - 2y
    """
    return [y[1], 2 * x * y[1] - x * x * y[0]]

def model_1a_ans(x):
    """
    Taylor Polynomial solution near x = 0 of the differential equation:
    y'' = (2*x)y' - 2y
    """
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
    Taylor Polynomial solution near x = 3 of the differential equation:
    y'' = (x-2)y' - 2y
    """
    return 6 + (x-3) - 11/2*(x-3)**2


h = 1
u = 2

# Function to calculate the utilization value.
def funcUtilization(xval):
    return (h * xval) / (u * xval)

# Function to calculate the throughput of jobs.
def throughput(xval):
    return u * xval

# Function to calculate the jobs in the system.
def numSys(xval):
    return h * xval / xval * ( 1 / (u - h))

# Function to calculate the time that the jobs are in the system.
def timeSys(xval):
    return (1 / xval) * (1 / (u - h))



# Graph the plots
ax = []
labels = []
for x in range(4):
    figure, axis = plt.subplots() 
    ax.append(axis)
    labels.append({})


x_values = np.linspace(1, 20, 100)
print(x_values)

ax[0].plot(x_values, funcUtilization(x_values), label = "Utilization", color = "green")
labels[0] = {"y":"Utilization", "x":"K Value", "title":"Utilization as K changes"}
ax[1].plot(x_values, throughput(x_values), label = "Throughput", color = "green")
labels[1] = {"y":"Throughput", "x":"K Value", "title":"Throughput as K changes"}
ax[2].plot(x_values, numSys(x_values), label = "Number System", color = "green")
labels[2] = {"y":"Number System", "x":"K Value", "title":"Number System as K changes"}
ax[3].plot(x_values, timeSys(x_values), label = "Time System", color = "green")
labels[3] = {"y":"Time in System", "x":"K Value", "title":"Time in System"}

for axis in enumerate(ax):
    axis[1].set_xlabel(labels[axis[0]]["x"])
    axis[1].set_ylabel(labels[axis[0]]["y"])
    axis[1].legend()
    axis[1].title.set_text(labels[axis[0]]["title"])

plt.show()
