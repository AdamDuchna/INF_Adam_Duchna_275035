import numpy
import pyswarms as ps
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt

def f(x):
    n_particles = x.shape[0]
    r = [fitness_func(x[i]) for i in range(n_particles)]
    return numpy.array(r)

def fitness_func(solution):
    S = [1, 2, 3, 6, 10, 17, 25, 29, 30, 41, 51, 60, 70, 79, 80]
    sum1 = numpy.sum(solution * S)
    solution_invert = 1 - solution
    sum2 = numpy.sum(solution_invert * S)
    fitness = numpy.abs(sum1-sum2)
    return fitness

options = {'c1': 0.5, 'c2': 0.3, 'w':0.9 , 'k':2 ,'p':2}
optimizer = ps.discrete.binary.BinaryPSO(n_particles=10, dimensions=15, options=options)

optimizer.optimize(f, iters=30, verbose=True)
cost_history = optimizer.cost_history
plot_cost_history(cost_history)
plt.show()
