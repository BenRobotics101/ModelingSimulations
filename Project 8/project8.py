
import math



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


a = -math.pi
b = math.pi

n = 4

def firstEquation(xValue):
    yValue = math.sin(xValue) + 1
    return yValue

print("Left Hand Sum: ", calculateIntegral_LHS(firstEquation, a, b, n))
print("Right Hand Sum: ", calculateIntegral_RHS(firstEquation, a, b, n))
print("Right Hand Sum: ", calculateIntegral_MID(firstEquation, a, b, n))
print("Trapezoid  Sum: ", (calculateIntegral_RHS(firstEquation, a, b, n) + calculateIntegral_LHS(firstEquation, a, b, n)) / 2.0)

