import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch
import numpy as np

def calculateIntegral_LHS(function, start, end, subdivisions):
    area = 0
    x = start
    divisions = (end - start) / subdivisions
    while(x < end):
        yValue = function(x)
        area += yValue * divisions
        x += divisions

    return area

rectangles = []


dataTimeCumulative = [
    0.000,
    0.989,
    1.962,
    2.921,
    3.879,
    4.844,
    5.817,
    6.768,
    7.859,
    8.822,
    9.797,
    10.750,
    11.810,
    12.774,
    15.852,
    16.857,
    17.818,
    18.791,
    19.760,
    20.714,
    21.671,
    22.626,
    23.587,
    24.546,
    25.610,
    26.580,
    27.525,
    28.483,
    29.448,
    30.409
]

widths = [
    0.989,
    0.974,
    0.959,
    0.957,
    0.965,
    0.973,
    0.951,
    1.091,
    0.964,
    0.975,
    0.953,
    1.060,
    0.964,
    3.078,
    1.004,
    0.961,
    0.973,
    0.969,
    0.954,
    0.957,
    0.955,
    0.961,
    0.959,
    1.063,
    0.971,
    0.945,
    0.958,
    0.965,
    0.961,
    0.957
]

heights = [
    77.15902,
    78.35812,
    79.56344,
    79.68010,
    79.04939,
    78.39909,
    80.25433,
    69.92219,
    79.18083,
    78.28821,
    80.04669,
    72.00294,
    79.13513,
    24.78297,
    75.95563,
    79.37404,
    78.40262,
    78.74027,
    79.98472,
    79.73115,
    79.87410,
    79.38077,
    79.51699,
    71.76811,
    78.59000,
    80.74153,
    79.63711,
    79.06629,
    79.39196,
    79.75772

]

for x in range(len(heights)):
    newRectangle = {
        "startX" : dataTimeCumulative[x],
        "width" : widths[x],
        "height" : heights[x]
    }
    rectangles.append(newRectangle)

def function(x):
    
    return 0.000004671590442845150000000000 * (x ** 6) - 0.000362863525824153 * (x ** 5) + 0.00937593627725164 * (x ** 4) - 0.079295569673377 * (x ** 3) - 0.117531465861248 * (x ** 2) + 2.27586137104663 * x + 76.2681550470879
    #return -0.00042255085120313000 * (x ** 4) + 0.0233905429346777 * (x ** 3) - 0.355207095656397 * (x ** 2) + 0.9632569945470100 * x + 80.5928130257807

x_values = np.linspace(0, 31, 100)
y_values = function(x_values)

fig, ax = plt.subplots()
line = ax.plot(x_values, y_values, label = "Polynomial Approximation of Transfer Speed", color = "green", lw=3)
for rectangle in rectangles:
    ax.add_patch(Rectangle((rectangle["startX"], 0), rectangle["width"], rectangle["height"], edgecolor="black", facecolor= (0, 0.6, 0.8, 0.7), lw=1))


# calculate raw area.
rawArea = 0
for rectangle in rectangles:
    rawArea += rectangle["width"] * rectangle["height"]
print("Raw Area: \t\t  ", rawArea, 'Mbit\t', rawArea / 8, "MB")
intArea = calculateIntegral_LHS(function,dataTimeCumulative[0],dataTimeCumulative[-1],30)
print("Riemann of regression: \t  ", calculateIntegral_LHS(function,dataTimeCumulative[0],dataTimeCumulative[-1],30), 'Mbit\t', intArea / 8, "MB")

print("Expected data transferred:", 30 * 10000000 / (1024 * 1024), "MB")

dummyLegendText = Patch(color=(0, 0.6, 0.8, 0.9), label='Raw Download Measurements')
h, l = ax.get_legend_handles_labels()

ax.legend(handles=h + [dummyLegendText])
ax.set_xlabel("Seconds Of Data Transfer")
ax.set_ylabel("Transfer speed in Mbps")
ax.title.set_text(f"Transfer speed over time")
plt.show()