# zapisz na wszeli wypadek

# import random
#
# import numpy as np
# from matplotlib import pyplot as plt
#
#
# def f(x, a, b, c, d):
#     return a * x ** 3 + b * x ** 2 + c * x + d
#
# def fitness(individual, points):
#     error = 0
#     for point in points:
#         x, y = point
#         error += (f(x, *individual) - y) ** 2
#     return 1 / (error + 1e-10)
#
# def roulette_selection(population, fitnesses):
#     total_fitness = sum(fitnesses)
#     probabilities = [fitness / total_fitness for fitness in fitnesses]
#     selected_indices = random.choices(range(len(population)), weights=probabilities, k=len(population))
#     selected_population = [population[i] for i in selected_indices]
#     return selected_population
#
# def crossover(parent1, parent2):
#     index = random.randint(0, len(parent1) - 1)
#     child1 = parent1[:index] + parent2[index:]
#     child2 = parent2[:index] + parent1[index:]
#     return child1, child2, index  # Dodano zwracanie punktu krzyÅ¼owania
#
# def mutate(individual, mutation_rate):
#     mutated_individual = individual.copy()
#     for i in range(len(mutated_individual)):
#         if random.random() < mutation_rate:
#             mutated_individual[i] += round(random.uniform(-1, 1))
#             mutated_individual[i] = max(-15, min(15, mutated_individual[i]))
#     return mutated_individual
#
#
# def genetic_algorithm(points, population_size, mutation_rate, generations):
#     population = [[random.randint(-15, 15) for _ in range(4)] for _ in range(population_size)]
#
#     for generation in range(generations):
#         fitnesses = [fitness(individual, points) for individual in population]
#         best_individual = population[fitnesses.index(max(fitnesses))]
#         selected_population = roulette_selection(population, fitnesses)
#
#         new_population = [best_individual]
#         while len(new_population) < population_size:
#             parent1, parent2 = random.choices(selected_population, k=2)
#             child1, child2, crossover_point = crossover(parent1, parent2)
#             child1_mutated = mutate(child1, mutation_rate)
#             child2_mutated = mutate(child2, mutation_rate)
#             new_population.extend([child1_mutated, child2_mutated])
#         population = new_population
#         print("Crossover Point:", crossover_point)
#         print("Parent1: ", parent1)
#         print("Parent2: ", parent2)
#         print("Child1", child1)
#         print("Child2", child2)
#         print("Mutation in Child1: ", child1, " -> ", child1_mutated)
#         print("Mutation in Child2: ", child2, " -> ", child2_mutated)
#
#     return best_individual
#
# points = [(-5, -150), (-4, -77), (-3, -30), (-2, 0), (-1, 10), (1/2, 131/8), (1, 18), (2, 25), (3, 32), (4, 75), (5, 130)]
# best_individual = genetic_algorithm(points, population_size=10, mutation_rate=0.1, generations=10000)
# print(f"Best individual: {best_individual}")
#
#
# x_punkty, y_punkty = zip(*points)
#
# x_values = np.linspace(min(x_punkty), max(x_punkty), 100)
#
# y_values = f(x_values, a=best_individual[0], b=best_individual[1], c=best_individual[2], d=best_individual[3])
#
# plt.plot(x_values, y_values, label=f'funkcja(x) = {best_individual[0]} + {best_individual[1]} + {best_individual[2]} + {best_individual[3]}')
# plt.scatter(x_punkty, y_punkty, color='red', label='Zaznaczone punkty')
#
# plt.xlabel('Wartość x')
# plt.ylabel('Wartość funkcji')
# plt.title('Wykres funkcji')
#
# plt.grid(True)
#
# plt.legend()
#
# plt.show()


import numpy as np

# Krok 1: Inicjalizacja Populacji
def initialize_population(population_size, gene_size):
    return np.random.randint(-15, 16, size=(population_size, gene_size))

# Krok 2: Dekodowanie Chromosomu
def decode_chromosome(chromosome):
    a, b, c, d = chromosome
    return a, b, c, d

# Krok 3: Funkcja Celu
def objective_function(chromosome, points):
    a, b, c, d = decode_chromosome(chromosome)
    errors = [((a * x**3) + (b * x**2) + (c * x) + d - y) for x, y in points]
    return np.sum(np.square(errors))

# Krok 4: Selekcja
def selection(population, fitness):
    selected_indices = np.random.choice(len(population), size=len(population), p=fitness/fitness.sum())
    return population[selected_indices]

# Krok 5: Krzyżowanie
def crossover(parent1, parent2, crossover_prob):
    if np.random.rand() < crossover_prob:
        crossover_point = np.random.randint(1, len(parent1))
        child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
        child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
        return child1, child2
    else:
        return parent1, parent2

# Krok 6: Mutacja
def mutation(child, mutation_prob):
    if np.random.rand() < mutation_prob:
        mutated_gene = np.random.randint(0, len(child))
        child[mutated_gene] = np.random.randint(-15, 16)
    return child

# Krok 7: Zastępowanie Populacji
def replace_population(population, offspring, fitness):
    combined_population = np.vstack((population, offspring))
    sorted_indices = np.argsort(fitness)
    return combined_population[sorted_indices[:len(population)]]

# Algorytm Genetyczny
def genetic_algorithm(population_size, generations, crossover_prob, mutation_prob, points):
    gene_size = 4
    population = initialize_population(population_size, gene_size)

    for generation in range(generations):
        fitness = np.array([objective_function(chromosome, points) for chromosome in population])
        selected_population = selection(population, fitness)

        offspring = []
        for i in range(0, len(selected_population), 2):
            parent1 = selected_population[i]
            parent2 = selected_population[i+1] if i+1 < len(selected_population) else selected_population[i]
            child1, child2 = crossover(parent1, parent2, crossover_prob)
            child1 = mutation(child1, mutation_prob)
            child2 = mutation(child2, mutation_prob)
            offspring.extend([child1, child2])

        population = replace_population(population, offspring, fitness)

    best_chromosome = population[np.argmin(fitness)]
    best_values = decode_chromosome(best_chromosome)
    return best_values

# Punkty
points = [(-5, -150), (4, 77), (-1, -30), (-2, 0), (-1, 10), (1/2, 131/8), (1, 18), (2, 25), (3, 32), (4, 75), (5, 130)]

# Parametry AG
population_size = 100
generations = 100
crossover_prob = 0.7
mutation_prob = 0.1

# Uruchomienie AG
result = genetic_algorithm(population_size, generations, crossover_prob, mutation_prob, points)

# Wyniki
print("Najlepsze wartości a, b, c, d:", result)


# #Nie zapomnij pozmieniać zmiennych
#
# import random
# import numpy as np
# from matplotlib import pyplot as plt
#
#
# def f(x, a, b, c, d):
#     return a * x ** 3 + b * x ** 2 + c * x + d
#
#
# def fitness(individual, points):
#     error = 0
#     for point in points:
#         x, y = point
#         error += (f(x, *individual) - y) ** 2
#     return 1 / (error + 1e-10)
#
#
# def roulette_selection(population, fitnesses):
#     total_fitness = sum(fitnesses)
#     probabilities = [fitness / total_fitness for fitness in fitnesses]
#     selected_indices = random.choices(range(len(population)), weights=probabilities, k=len(population))
#     selected_population = [population[i] for i in selected_indices]
#     return selected_population
#
#
# def crossover(parent1, parent2):
#     index = random.randint(0, len(parent1) - 1)
#     child1 = parent1[:index] + parent2[index:]
#     child2 = parent2[:index] + parent1[index:]
#     return child1, child2, index  # Dodano zwracanie punktu krzyżowania
#
#
# def mutate(individual, mutation_rate):
#     mutated_individual = individual.copy()
#     for i in range(len(mutated_individual)):
#         if random.random() < mutation_rate:
#             mutated_individual[i] += round(random.uniform(-1, 1))
#             mutated_individual[i] = max(-15, min(15, mutated_individual[i]))
#     return mutated_individual
#
#
# def genetic_algorithm(points, population_size, mutation_rate, generations):
#     population = [[random.randint(-15, 15) for _ in range(4)] for _ in range(population_size)]
#
#     for generation in range(generations):
#         fitnesses = [fitness(individual, points) for individual in population]
#         best_individual = population[fitnesses.index(max(fitnesses))]
#         selected_population = roulette_selection(population, fitnesses)
#
#         new_population = [best_individual]
#         while len(new_population) < population_size:
#             parent1, parent2 = random.choices(selected_population, k=2)
#             child1, child2, crossover_point = crossover(parent1, parent2)
#             child1_mutated = mutate(child1, mutation_rate)
#             child2_mutated = mutate(child2, mutation_rate)
#             new_population.extend([child1_mutated, child2_mutated])
#
#         population = new_population
#         best_fitness = max(fitnesses)
#         print(f"Generation: {generation + 1}, Best Fitness: {best_fitness}")
#         print("Crossover Point:", crossover_point)
#         print("Parent1: ", parent1)
#         print("Parent2: ", parent2)
#         print("Child1", child1)
#         print("Child2", child2)
#         print("Mutation in Child1: ", child1, " -> ", child1_mutated)
#         print("Mutation in Child2: ", child2, " -> ", child2_mutated)
#
#     return best_individual
#
#
# points = [(-5, -150), (-4, -77), (-3, -30), (-2, 0), (-1, 10), (1 / 2, 131 / 8), (1, 18), (2, 25), (3, 32), (4, 75),
#           (5, 130)]
# best_individual = genetic_algorithm(points, population_size=10, mutation_rate=0.1, generations=1000)
# print(f"Best individual: {best_individual}")
#
# x_points, y_points = zip(*points)
# x_values = np.linspace(min(x_points), max(x_points), 100)
# y_values = f(x_values, a=best_individual[0], b=best_individual[1], c=best_individual[2], d=best_individual[3])
#
# plt.plot(x_values, y_values,
#          label=f'Function: {best_individual[0]}x^3 + {best_individual[1]}x^2 + {best_individual[2]}x + {best_individual[3]}')
# plt.scatter(x_points, y_points, color='red', label='Selected points')
#
# plt.xlabel('x')
# plt.ylabel('Function Value')
# plt.title('Function Plot')
#
# plt.grid(True)
# plt.legend()
# plt.show()


