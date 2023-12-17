
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Patch


def calculateIntegral_LHS(function, start, end, subdivisions):
    area = 0
    x = start
    divisions = (end - start) / subdivisions
    while(x < end):
        yValue = function(x)
        area += yValue * divisions
        x += divisions

    return area


def calculateIntegral_RHS(function, start, end, subdivisions):
    area = 0
    divisions = (end - start) / subdivisions
    x = start + divisions
    while(x <= end):
        yValue = function(x)
        area += yValue * divisions
        x += divisions

    return area

def calculateIntegral_MID(function, start, end, subdivisions):
    area = 0
    divisions = (end - start) / subdivisions
    x =     start + divisions / 2
    while(x < end):
        yValue = function(x)
        area += yValue * divisions
        x += divisions

    return area


a = -np.pi
b = np.pi

n = 4

def firstEquation(xValue):
    yValue = np.sin(xValue) + 1
    return yValue

def x_values_LHS(start, end, subdivisions):
    xValues = []
    interval = (end - start)/subdivisions
    i = start
    while(i <= end):
        xValues.append(i)
        i += interval
    return np.array(xValues)

print("Left Hand Sum: ", calculateIntegral_LHS(firstEquation, a, b, n))
print("Right Hand Sum: ", calculateIntegral_RHS(firstEquation, a, b, n))
print("Right Hand Sum: ", calculateIntegral_MID(firstEquation, a, b, n))
print("Trapezoid  Sum: ", (calculateIntegral_RHS(firstEquation, a, b, n) + calculateIntegral_LHS(firstEquation, a, b, n)) / 2.0)

xValues = np.arange(-np.pi, np.pi, np.pi/1000)
yValues = firstEquation(xValues)
rectangleX = x_values_LHS(a, b, n)

# Graph the plots
ax = []
labels = []
titles = []
dummyLegendText = []
for x in range(3):
    figure, axis = plt.subplots() 
    ax.append(axis)
    labels.append({})
    titles.append([])
    dummyLegendText.append([])
    ax[x].plot(xValues, yValues, label="Function f(x)", color = "blue", lw=2)

for i in range(4):  
    ax[0].add_patch(Rectangle((rectangleX[i], firstEquation(rectangleX[i])), rectangleX[i + 1] - rectangleX[i], -firstEquation(rectangleX[i]),
            edgecolor = 'black',
            facecolor = (0, 0.6, 0.8, 0.8),
            fill=True,
            lw=1))
for i in range(4):
    ax[1].add_patch(Rectangle((rectangleX[i], firstEquation(rectangleX[i + 1])), rectangleX[i + 1] - rectangleX[i], -firstEquation(rectangleX[i + 1]),
            edgecolor = 'black',
            facecolor = (0, 0.6, 0.8, 0.8),
            fill=True,
            lw=1))
for i in range(4):
    startX = rectangleX[i]
    width = rectangleX[i + 1] - rectangleX[i]
    height = firstEquation(rectangleX[i] + width / 2)

    ax[2].add_patch(Rectangle( (startX, 0.0), width, height, # rectangleX[i + 1] - rectangleX[i], -(firstEquation(rectangleX[i + 1]) + firstEquation(rectangleX[i])) / 2,
            edgecolor = 'black',
            facecolor = (0, 0.6, 0.8, 0.8),
            fill=True,
            lw=1))
    
labels[0] = {"y":"Y-Value", "x":"X-Value"}
labels[1] = {"y":"Y-Value", "x":"X-Value"}
labels[2] = {"y":"Y-Value", "x":"X-Value"}
titles[0] = "Left Riemann Sum"
titles[1] = "Right Riemann Sum"
titles[2] = "Midpoint Riemann Sum"
dummyLegendText[0] = Patch(color=(0, 0.6, 0.8, 0.8), label='Left Hand Measurements')
dummyLegendText[1] = Patch(color=(0, 0.6, 0.8, 0.8), label='Right Hand Measurements')
dummyLegendText[2] = Patch(color=(0, 0.6, 0.8, 0.8), label='Midpoint Measurements')

for axis in enumerate(ax):
    h, l = axis[1].get_legend_handles_labels()
    axis[1].legend(handles=h + [dummyLegendText[axis[0]]])
    axis[1].set_xlabel(labels[axis[0]]["x"])
    axis[1].set_ylabel(labels[axis[0]]["y"])
    axis[1].title.set_text(f"{titles[axis[0]]}")

plt.show()