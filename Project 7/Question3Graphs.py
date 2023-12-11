###############
# Part 2 Question 3
# Benjamin Carter and Trevor Pope
# 12/9/2023
# 
# This program graphs how changes in k affect the rest of the parameters in queuing theory.
#
############## 


import numpy as np
import matplotlib.pyplot as plt


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
