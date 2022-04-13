import pygad
import numpy
import math

gene_space = {"low": 0, "high": 2, "step": 0.001}
particles = 5
p0 = 3


def fitness_function(solution, solution_idx):
    [solution[i:i + 3] for i in range(0, len(solution), 3)]
    for x in solution:
        for y in solution:
    return math.exp(p0 * (1 -)) * (math.exp(p0 * (1 -)) - 2)


sol_per_pop = 12
num_genes = particles * 3
num_parents_mating = 6
num_generations = 60
keep_parents = 3
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 14

ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes
                       )

ga_instance.run()

# podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Number of generations passed is {generations_completed}".format(
    generations_completed=ga_instance.generations_completed))

# wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()
