
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

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
    ax = fig.add_subplot(projection='3d')
    xs, ys, zs = graph(rVal)
    line = ax.plot(xs, ys, zs, lw=0.5)[0]
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title(f"Lorenz Attractor: R={rVal}")

    def updateFrame(frame):
        
        rVal = frame + 3
        #print("Rval", rVal)
        xs, ys, zs = graph(rVal)
        line.set_data_3d(xs,ys,zs)
        ax.set_xlim(xs.min(), xs.max())
        ax.set_ylim(ys.min(), ys.max())
        ax.set_zlim(zs.min(), zs.max())
        ax.set_title(f"Lorenz Attractor: R={rVal}")
        return line


    if(inStr == 'A' or inStr == 'a'):
        ani = animation.FuncAnimation(fig=fig, func=updateFrame, frames=26, interval=250 )

    plt.show()

    if(inStr != 'A' and inStr != 'a'):
        fig = plt.figure()

        plt.plot(t, xs, lw=0.5)
        plt.xlabel("t")
        plt.ylabel("X - GIF")
        title = f"x(t) [GIF] - r: {rVal}"
        plt.title(title)

        plt.show()

        # Plot
        fig = plt.figure()

        plt.plot(t, ys, lw=0.5)
        plt.xlabel("t")
        plt.ylabel("Y - GIF")
        title = f"y(t) [GIF] - r: {rVal}"
        plt.title(title)

        plt.show()

        # Plot
        fig = plt.figure()

        plt.plot(t, zs, lw=0.5)
        plt.xlabel("t")
        plt.ylabel("Z - GIF")
        title = f"z(t) [GIF] - r: {rVal}"
        plt.title(title)

        plt.show()

    main()
    
if __name__ == "__main__":
    main()
