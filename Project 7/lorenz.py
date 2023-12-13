################
#
#  Lorenz Attractor
#  By Benjamin Carter and Trevor Pope
#  12/10/2023
#  
#  This program calculates the Lorenz curves with the ability for a user to select an r value.
################

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import time

num_steps = 10000
rVal = 3
dt = 0.01
t = np.arange(0, num_steps + 1, 1)


def lorenz(x, y, z, s=10, r=3, b=2.667):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

def graph(r=28):
    
    # Need one more for the initial values
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)

    # Set initial values
    xs[0], ys[0], zs[0] = (0., 1., 1.05)

    # Step through "time", calculating the partial derivatives at the current point
    # and using them to estimate the next point
    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i],r=r)
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)

    return xs, ys, zs  

def main():
    global rVal
    inStr = input("Enter a value for r, 0 to exit, or enter 'a' to animate: ")
    try:
        rVal = int(inStr)
    except:
        pass
    if(rVal == 0):
        exit()
    # Plot
    fig = plt.figure()
    try:
        ax = fig.add_subplot(projection='3d')
    except:
        print("Warning... your version of Matplotlib is out of date. Please try to update it.")
        ax = fig.gca(projection='3d')
    


    startTime = time.time()
    xs, ys, zs = graph(rVal)
    endTime = time.time()

    timeLength = int((endTime - startTime) * 1000)

    print(f"Calculations took {timeLength / 1000} seconds to run.")
    
    line = ax.plot(xs, ys, zs, lw=0.5)[0]
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title(f"Lorenz Attractor: R={rVal}")

    def updateFrame(frame):
        rValcopy = frame + 3
        #print("Rval", rVal)
        
        startTime = time.time()
        xs, ys, zs = graph(rValcopy)
        endTime = time.time()

        timeLength = int((endTime - startTime) * 1000)

        print(f"Calculations took {timeLength / 1000} seconds to run.")

        line.set_data_3d(xs,ys,zs)
        ax.set_xlim(xs.min(), xs.max())
        ax.set_ylim(ys.min(), ys.max())
        ax.set_zlim(zs.min(), zs.max())
        ax.set_title(f"Lorenz Attractor: R={rValcopy}")
        return line

    if(inStr != 'A' and inStr != 'a'):
        plt.show()

    fig2 = plt.figure()

    ax2 = fig2.add_subplot()
    x2l = ax2.plot(t, xs, lw=0.5)[0]
    ax2.set_xlabel("t")
    ax2.set_ylabel("X - GIF")
    title2 = f"x(t) [GIF] - R={rVal}"
    ax2.set_title(title2)

    def updateFrame2(frame):
        #print("Rval", rVal)
        rValcopy = frame + 3
        xs, ys, zs = graph(rValcopy)
        x2l.set_xdata(t)
        x2l.set_ydata(xs)
        ax2.set_xlim(t.min(), t.max())
        ax2.set_ylim(xs.min(), xs.max())
        ax2.set_title(f"x(t) [GIF] - R={rValcopy}")
        return x2l
    
    if(inStr != 'A' and inStr != 'a'):
        plt.show()

    # Plot
    fig3 = plt.figure()

    ax3 = fig3.add_subplot()
    x3l = ax3.plot(t, ys, lw=0.5)[0]
    ax3.set_xlabel("t")
    ax3.set_ylabel("Y - GIF")
    title3 = f"y(t) [GIF] - R={rVal}"
    ax3.set_title(title3)

    def updateFrame3(frame):
        #print("Rval", rVal)
        rValcopy = frame + 3
        xs, ys, zs = graph(rValcopy)
        x3l.set_xdata(t)
        x3l.set_ydata(ys)
        ax3.set_xlim(t.min(), t.max())
        ax3.set_ylim(ys.min(), ys.max())
        ax3.set_title(f"y(t) [GIF] - R={rValcopy}")
        return x3l

    if(inStr != 'A' and inStr != 'a'):
        plt.show()
    
    # Plot
    fig4 = plt.figure()

    ax4 = fig4.add_subplot()
    x4l = ax4.plot(t, zs, lw=0.5)[0]
    ax4.set_xlabel("t")
    ax4.set_ylabel("Z - GIF")
    title4 = f"z(t) [GIF] - R={rVal}"
    ax4.set_title(title4)

    def updateFrame4(frame):
        #print("Rval", rVal)
        rValcopy = frame + 3
        xs, ys, zs = graph(rValcopy)
        x4l.set_xdata(t)
        x4l.set_ydata(zs)
        ax4.set_xlim(t.min(), t.max())
        ax4.set_ylim(zs.min(), zs.max())
        ax4.set_title(f"z(t) [GIF] - R={rValcopy}")
        return x4l

    if(inStr == 'A' or inStr == 'a'):
        ani = animation.FuncAnimation(fig=fig, func=updateFrame, frames=26, interval=250 )
        ani2 = animation.FuncAnimation(fig=fig2, func=updateFrame2, frames=26, interval=250 )
        ani3 = animation.FuncAnimation(fig=fig3, func=updateFrame3, frames=26, interval=250 )
        ani4 = animation.FuncAnimation(fig=fig4, func=updateFrame4, frames=26, interval=250 )
    plt.show()

    main()
    
if __name__ == "__main__":
    main()
