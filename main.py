import numpy as np
from controller.controller import Controller
from reference.trajectory import generate_trajectory
from output.output import update_y
from estimator.estimator import initialize_phi
from plot.plotter import plot_results

# Initialize parameters
controller = Controller()
phi = initialize_phi()

u = [np.zeros((400, 1)) for _ in range(4)]
e = [np.zeros((401, 1)) for _ in range(4)]
y = [np.zeros((401, 1)) for _ in range(4)]
si = [np.zeros((400, 1)) for _ in range(4)]
yd = generate_trajectory()

for k in range(400):
    # Update phi values
    for i in range(4):
        phi[i][k] = controller.update_phi(k, phi[i], u[i], y[i])
    
    # Update si values
    si1, si2, si3, si4 = controller.update_si(k, yd, y[0], y[1], y[2], y[3])
    si[0][k], si[1][k], si[2][k], si[3][k] = si1, si2, si3, si4
    
    # Update input values
    for i in range(4):
        u[i][k] = controller.update_input(k, u[i], phi[i], si[i])

    # Update y values
    y1_next, y2_next, y3_next, y4_next = update_y(k, u, y)
    y[0][k+1], y[1][k+1], y[2][k+1], y[3][k+1] = y1_next, y2_next, y3_next, y4_next

    # Calculate errors
    for i in range(4):
        e[i][k] = yd[k] - y[i][k]

# Plot results
plot_results(yd, y, e, phi, u)
