import numpy as np

def update_y(k, u, y):
    if k == 1:
        return 0.51, 2.5, 3.5, 4
    else:
        y1_next = (y[0][k] * u[0][k]) / (1 + y[0][k]**2) + u[0][k]
        y2_next = (y[1][k] * u[1][k]) / (1 + y[1][k]**3) + 0.5 * u[1][k]
        y3_next = (y[2][k] * u[2][k]) / (1 + y[2][k]**2) + 0.9 * u[2][k]
        y4_next = (y[3][k] * u[3][k]) / (1 + y[3][k]**5) + 0.8 * u[3][k]
        return y1_next, y2_next, y3_next, y4_next
