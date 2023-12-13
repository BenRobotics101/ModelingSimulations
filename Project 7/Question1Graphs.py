###############
# Part 2 Question 1
# Benjamin Carter and Trevor Pope
# 12/9/2023
# 
# This program graphs the solutions for the queueing model for question 1.
#
############## 



import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

import time
startTime = time.time()


# This is the data calculated in our excel graph.
arrival = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
serviceDur = [2.22, 1.76, 2.13, 0.14, 0.76, 0.70, 0.47, 0.22, 0.18, 2.41, 0.41, 0.46, 1.37, 0.27, 0.27]
serviceStartTime = [1, 3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 10, 12.41, 12.82, 13.28, 14.65, 15]
exitTime = [3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 9.58, 12.41, 12.82, 13.28, 14.65, 14.92, 15.27]
timeInQueue = [0, 1.22, 1.98, 3.11, 2.25, 2.01, 1.71, 1.18, 0.4, 0, 1.41, 0.82, 0.28, 0.65, 0]
systemNumber = [0, 1, 2, 2, 2, 3, 4, 3, 2, 0, 1, 2, 1, 1, 0]
queueNumber = [0, 0, 1, 1, 1, 2, 3, 2, 1, 0, 0, 1, 0, 0, 0]



####### PART 1 A

# Graph the plots

ax = []
labels = []
for x in range(5):
    figure, axis = plt.subplots() 
    ax.append(axis)
    labels.append({})

ax[0].plot(arrival, serviceStartTime, label = "Service Duration", color = "green")
labels[0] = {"y":"Service Start Time", "x":"Arrival Time"}
ax[1].plot(arrival, exitTime, label = "Service Start Time", color = "green")
labels[1] = {"y":"Exit Time", "x":"Arrival Time"}
ax[2].plot(arrival, timeInQueue, label = "Exit Time", color = "green")
labels[2] = {"y":"Time In Queue", "x":"Arrival Time"}
ax[3].plot(arrival, systemNumber, label = "Time In Queue", color = "green")
labels[3] = {"y":"System Number", "x":"Arrival Time"}
ax[4].plot(arrival, timeInQueue, label = "System Number", color = "green")
labels[4] = {"y":"Number In Queue", "x":"Arrival Time"}

for axis in enumerate(ax):
    axis[1].set_xlabel(labels[axis[0]]["x"])
    axis[1].set_ylabel(labels[axis[0]]["y"])
    axis[1].legend()
    axis[1].title.set_text(f"{labels[axis[0]]['y']} vs {labels[axis[0]]['x']}")

endTime = time.time()

timeLength = int((endTime - startTime) * 1000)

print(f"Calculations took {timeLength / 1000} seconds to run.")

plt.show()