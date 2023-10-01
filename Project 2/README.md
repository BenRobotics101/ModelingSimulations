# CST-305: Principles of Modeling and Simulation
## Project 2 - Runge-Kutta-Fehlberg (RKF) for ODE
## By: Trevor Pope and Ben Carter

### Description

This program calculates the solution to the ODE using both the Runge-Kutta-Fehlburg method and SciPy's Odeint method.
The program then compares the results of the two and graphs the results to demonstrate the result. The ODE used in this
program is y' = -y + ln(x). The program uses Matplotlib's pyplot to graph the results. It also uses our own class called
RKF which we created to do what Runge-Kutta-Fehlburg's method does.

### Files included:

- main.py: This is the main python file which runs scipy's odeint to solve the ODE and creates an instance of the RKF class to solve the ODE that way.
- RKF_Class.py: This is the file that holds the RKF class.
- RKF_Flowchart.png: This is the flowchart describing the program execution logic.

### How to run the program:

There are a couple steps to run this program. If you have any python interpreter installed, you can install matplotlib using "pip install matplotlib" and then you can install scipy using "pip install scipy". After you have done that, ensure you have the RKF_Class.py file in the same directory as the main.py file. When all these are done you can simply run the program.
