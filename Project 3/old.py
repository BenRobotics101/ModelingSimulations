
# Plot the first set of data as a line
axis[0, 1].plot(x_values, y_values, label='Odeint', linewidth=2.5, color="green")
axis[0, 1].plot(x_values, y_values_sol1, label='Manual Solution', linestyle=(0, (5, 4)), color="red", linewidth=2.5)
axis[0, 1].set_xlabel('X')
axis[0, 1].set_ylabel('Y')
axis[0, 1].legend()
axis[0, 1].set_title("ODEINT vs Manual Solution Function EQ 1") 

axis[0, 0].plot(x_values, y_values, label='Odeint', linewidth=2.5, color="green")
axis[0, 0].set_xlabel('X')
axis[0, 0].set_ylabel('Y')
axis[0, 0].legend()
axis[0, 0].set_title("ODEINT EQ1") 

axis[0, 2].plot(x_values, y_values_sol1, label='Manual Solution', linestyle=(0, (5, 4)), color="red", linewidth=2.5)
axis[0, 2].set_xlabel('X')
axis[0, 2].set_ylabel('Y')
axis[0, 2].legend()
axis[0, 2].set_title("Manual Solution EQ1") 


axis[1, 1].plot(x_values, y_values2, label='Odeint', linewidth=2.5, color="green")
axis[1, 1].plot(x_values, y_values_sol2, label='Manual Solution', linestyle=(0, (5, 4)), color="red", linewidth=2.5)
axis[1, 1].set_xlabel('X')
axis[1, 1].set_ylabel('Y')
axis[1, 1].legend()
axis[1, 1].set_title("ODEINT vs Manual Solution Function") 

axis[1, 0].plot(x_values, y_values2, label='Odeint', linewidth=2.5, color="green")
axis[1, 0].set_xlabel('X')
axis[1, 0].set_ylabel('Y')
axis[1, 0].legend()
axis[1, 0].set_title("ODEINT EQ2") 

axis[1, 2].plot(x_values, y_values_sol2, label='Manual Solution', linestyle=(0, (5, 4)), color="red", linewidth=2.5)
axis[1, 2].set_xlabel('X')
axis[1, 2].set_ylabel('Y')
axis[1, 2].legend()
axis[1, 2].set_title("Manual Solution EQ2") 