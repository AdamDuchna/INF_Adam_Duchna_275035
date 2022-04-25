import itertools
import math

import matplotlib.pyplot as plt
import numpy as np
import pygad

gene_space = {"low": 0, "high": 2, "step": 0.001}
particles_count = 21
p0 = 3


def calc_distance(particle_i, particle_j):
    x_i, y_i, z_i = particle_i
    x_j, y_j, z_j = particle_j
    return math.sqrt((x_i - x_j) ** 2 + (y_i - y_j) ** 2 + (z_i - z_j) ** 2)


def fitness_function(solution, solution_idx):
    morse_sum = 0
    particles = [solution[i:i + 3] for i in range(0, len(solution), 3)]
    particle_pairs = list(itertools.combinations(particles, 2))
    for pair in particle_pairs:
        particle_i, particle_j = pair
        euclid_dist = calc_distance(particle_i, particle_j)
        morse_sum += math.exp(p0 * (1 - euclid_dist)) * (math.exp(p0 * (1 - euclid_dist)) - 2)
    return -morse_sum


sol_per_pop = 100
num_genes = particles_count * 3
num_parents_mating = 20
num_generations = 1000
parent_selection_type = "rank"
crossover_type = "single_point"
mutation_type = "random"
mutation_num_genes = 1

ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_num_genes=mutation_num_genes
                       )

ga_instance.run()
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Number of generations passed is {generations_completed}".format(
    generations_completed=ga_instance.generations_completed))

ga_instance.plot_fitness()

particles = [solution[i:i + 3] for i in range(0, len(solution), 3)]
particle_pairs = list(itertools.combinations(particles, 2))
particle_array = np.array(particle_pairs)
particle_array = particle_array.flatten()
x_axis, y_axis, z_axis = [], [], []

for index in range(0, len(solution) - 2, 3):
    x_axis.append(solution[index])
    y_axis.append(solution[index + 1])
    z_axis.append(solution[index + 2])

x, y, z = [], [], []
for index in range(0, len(particle_array) - 2, 3):
    x.append(particle_array[index])
    y.append(particle_array[index + 1])
    z.append(particle_array[index + 2])

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.scatter(x_axis, y_axis, z_axis, c="red")
ax.plot(x, y, z, c="black")
plt.show()
