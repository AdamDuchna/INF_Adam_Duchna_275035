import math
import numpy as np
import pyswarms as ps
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt

def f(x):
    n_particles = x.shape[0]
    r = [endurance(x[i]) for i in range(n_particles)]
    return np.array(r)

def endurance(arr):
    x, y, z, u, v, w = arr
    return -(math.exp(-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w))

options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}

x_max = np.ones(6)
x_min = np.zeros(6)
bounds = (x_min, x_max)
# Call instance of PSO with bounds argument
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6, options=options, bounds=bounds)

# Perform optimization
cost, pos = optimizer.optimize(f, iters=1000)
cost_history = optimizer.cost_history

plot_cost_history(cost_history)
plt.show()

