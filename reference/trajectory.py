import numpy as np

def generate_trajectory():
    yd = np.zeros(400)
    yd[:200] = 2
    yd[200:] = 0.5
    return yd
