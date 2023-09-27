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
    requests = M * np.sin(C * t)
    return requests

def requests_t_deriv(t):
    rqin_deriv = M * C * np.cos(C*t)
    return rqin_deriv

def requests_completed_dt(t):
    rqcplt = S - E * requests_t(t)
    return rqcplt

def workers_t_deriv(y,t):

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

maxSolution = np.max(solution)

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
