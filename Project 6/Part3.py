###############
# Part 3 - Taylor Polynomials Project 6
# Benjamin Carter and Trevor Pope
# 11/29/2023
# 

# This program graphs the solution to an ODE that we chose. This ODE represents a webserver that has requests sent into the webserver
# which are then completed by the webserver's "workers". To demonstrate a real webserver, we used a sin function that would demonstrate
# a high number of requests in the middle of the day and a low number of requests at the beginning and end of the day. Our goal was to solve
# the number of resources/workers that the webserver would need in order to complete all of the requests that second. To do that we used this
# differential equation (dr/dt) / (dp/dt) = dw/dt where dr/dt is the rate of change of the number of requests sent in per second, dp/dt is
# the rate of change of the number of requests completed per second, and dw/dt is the rate of change of the number of resources needed at that
# given second.

################

import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import math

####### Initial values

# Time constant
C = math.pi / 86400

# Initial Value at t=0. w(0) = 0, no workers at the start
w0 = 0

# Loss Efficiency. This is the rate that the number of requests per worker drops as requests increase. 
# 0.001 = for every 100 requests, a worker can do one less request per second.
E = 0.001

# Max requests in one instant during a day
M = 500

# Baseline requests per second a worker can do. 
# We will put it at a request every 40 msec
S = 1000 / 50



def requests_t(t):
    """Requests at specific time t

    Args:
        t (float): The time in seconds

    Returns:
        r (float): the value of the function
    """
    requests = M * np.sin(C * t)
    return requests

def requests_t_deriv(t):
    """The derivative of r respect to t

    Args:
        t (float): The time in seconds

    Returns:
        dr/dt (float): the value of the derivative
    """
    rqin_deriv = M * C * np.cos(C*t)
    return rqin_deriv

def requests_completed_dt(t):
    """Requests completed per second

    Args:
        t (float): The time in seconds

    Returns:
        dp/dt (float): The value of the derivative
    """
    rqcplt = S - E * requests_t(t)
    return rqcplt

def workers_t_deriv(w,t):
    """The dw/dt function.

    Args:
        w (float): The worker count
        t (float): The time in seconds.

    Returns:
        dw/dt (float): The value of the differential. 
    """

    # dr/dt - dw/dt * dp/dt >>> dr/dt = dw/dt * dp/dt  >>> (dr/dt) / (dp/dt) = dw/dt

    rqin_deriv = requests_t_deriv(t)
    rqcplt = requests_completed_dt(t)
    dwdt = rqin_deriv/rqcplt
    return dwdt

# Define time span
t = np.linspace(0, 86400)  # Simulate for 24 hours (86400 seconds)

# Solve the ODE
solution = odeint(
    workers_t_deriv,
    w0,
    t
)

# Request Array
requestPoints = requests_t(t)


# Visualize the worker need over time
ax1 = plt.subplot()
ax1.plot(t, solution, label="Workers Spawned")

# find max solution value for computing the y-axis range.
maxSolution = np.max(solution)

# use two axes
ax2 = ax1.twinx()
ax2.plot(t, requestPoints,linestyle='dashed',color='r', label="Requests")

ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

ax1.set_xlabel('Time (s)')
ax2.set_ylabel('Incoming Request Count (n)',color='r')
ax1.set_ylabel('Worker Count (n)')

ax1.set_xlim(0,86500)
ax1.set_ylim(0,maxSolution * 1.5)
ax2.set_ylim(0,M * 1.25)

plt.xticks(np.arange(0,86500 , 60 * 60 * 3)) # a tick every 3 hours
plt.title('Server Performance In One Day')
ax1.grid(True)
plt.show()
