import pygad

gene_space = [0, 1, 2, 3]
Labirynt = \
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
     [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
     [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
     [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
     [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
     [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
     [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
     [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

def fitness_function(solution, solution_idx):
    moveset = Labirynt
    position = [1, 1]
    score = None
    for move in solution:
        if move == 0:
            # LEWO
            if moveset[position[0]][position[1] - 1] == 0:
                position[1] -= 1
            else:
                if score is None:
                    score = -(abs(10 - position[0]) + abs(10 - position[1]))
        if move == 1:
            # PRAWO
            if moveset[position[0]][position[1] + 1] == 0:
                position[1] += 1
            else:
                if score is None:
                    score = -(abs(10 - position[0]) + abs(10 - position[1]))
        if move == 2:
            # DOL
            if moveset[position[0] + 1][position[1]] == 0:
                position[0] += 1
            else:
                if score is None:
                    score = -(abs(10 - position[0]) + abs(10 - position[1]))
        if move == 3:
            # GORA
            if moveset[position[0] - 1][position[1]] == 0:
                position[0] -= 1
            else:
                if score is None:
                    score = -(abs(10 - position[0]) + abs(10 - position[1]))

    if score is None:
        return -(abs(10 - position[0]) + abs(10 - position[1]))
    else:
        return score

sol_per_pop = 50
num_genes = 30
num_parents_mating = 25
num_generations = 300
keep_parents = 12
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 8
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
                       mutation_percent_genes=mutation_percent_genes,
                       stop_criteria="reach_0")

ga_instance.run()

#podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Number of generations passed is {generations_completed}".format(generations_completed=ga_instance.generations_completed))
#wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()