import math
import numpy as np
import pyswarms as ps
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt
import itertools


particles_count = 5
dimensions = particles_count * 3
p0 = 10

def f(x):
    n_particles = x.shape[0]
    r = [morse_cluster(x[i]) for i in range(n_particles)]
    return np.array(r)

def morse_cluster(solution):
    morse_sum = 0
    particles = [solution[i:i + 3] for i in range(0, len(solution), 3)]
    particle_pairs = list(itertools.combinations(particles, 2))
    for pair in particle_pairs:
        particle_i, particle_j = pair
        euclid_dist = calc_distance(particle_i, particle_j)
        morse_sum += math.exp(p0 * (1 - euclid_dist)) * (math.exp(p0 * (1 - euclid_dist)) - 2)
    return morse_sum

def calc_distance(particle_i, particle_j):
    x_i, y_i, z_i = particle_i
    x_j, y_j, z_j = particle_j
    return math.sqrt((x_i - x_j) ** 2 + (y_i - y_j) ** 2 + (z_i - z_j) ** 2)

options = {'c1': 0.8, 'c2': 0.2, 'w':0.8}

x_max = np.full(dimensions,2)
x_min = np.zeros(dimensions)
bounds = (x_min, x_max)
# Call instance of PSO with bounds argument
optimizer = ps.single.GlobalBestPSO(n_particles=100, dimensions=dimensions, options=options, bounds=bounds)

# Perform optimization
cost, pos = optimizer.optimize(f, iters=1000)
cost_history = optimizer.cost_history

plot_cost_history(cost_history)
plt.show()