import random
import numpy as np

def calculate_activation(temp_x1, w1, temp_x2, w2, temp_x3, w3):
    result = temp_x1 * w1 + temp_x2 * w2 + temp_x3 * w3
    return result

def sigmoid_activation(u):
    result = 1 / (1 + np.exp(-u))
    return result

def update_weights(i, j, weight, delta_w):
    result = weight + delta_w + momentum * previous_delta_weights[i-1][j-1]
    previous_delta_weights[i-1][j-1] = delta_w
    return result

def apply_genetic_algorithm(population, fitness_function, crossover_rate=0.8, mutation_rate=0.1, generations=100):
    for generation in range(generations):
        # Evaluate fitness
        fitness_values = [fitness_function(individual) for individual in population]
        sorted_indices = np.argsort(fitness_values)
        sorted_population = [population[i] for i in sorted_indices]

        # Selection
        selected_parents = sorted_population[:int(crossover_rate * len(population))]

        # Crossover
        children = []
        for i in range(0, len(selected_parents), 2):
            parent1 = selected_parents[i]
            parent2 = selected_parents[i + 1]
            crossover_point = random.randint(1, len(parent1) - 1)
            child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
            child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
            children.extend([child1, child2])

        # Mutation
        for i in range(len(children)):
            if random.random() < mutation_rate:
                mutation_point = random.randint(0, len(children[i]) - 1)
                children[i][mutation_point] += random.uniform(-0.1, 0.1)

        # Replace old population with new individuals
        population = selected_parents + children

    # Return the best individual from the final population
    return sorted_population[0]

def genetic_fitness(weights):
    global input_data, target_output
    error = 0
    for sample in range(4):
        inputs = input_data[:, sample]
        u1 = calculate_activation(inputs[0], weights[0], inputs[1], weights[1], inputs[2], weights[2])
        v1 = sigmoid_activation(u1)
        u2 = calculate_activation(inputs[0], weights[3], inputs[1], weights[4], inputs[2], weights[5])
        v2 = sigmoid_activation(u2)
        u3 = calculate_activation(v1, weights[6], v2, weights[7], inputs[2], weights[8])
        v3 = sigmoid_activation(u3)
        desired_output = target_output[sample]
        error += 0.5 * (desired_output - v3)**2
    return -error  # Maximizing negative error is equivalent to minimizing error

def train_neural_network():
    global weights
    # Initialize weights
    initial_population = [np.random.uniform(-1, 1, 9) for _ in range(20)]
    weights = apply_genetic_algorithm(initial_population, genetic_fitness)

    for iteration in range(10000):
        for sample in range(4):
            inputs = input_data[:, sample]
            u1 = calculate_activation(inputs[0], weights[0], inputs[1], weights[1], inputs[2], weights[2])
            v1 = sigmoid_activation(u1)
            u2 = calculate_activation(inputs[0], weights[3], inputs[1], weights[4], inputs[2], weights[5])
            v2 = sigmoid_activation(u2)
            u3 = calculate_activation(v1, weights[6], v2, weights[7], inputs[2], weights[8])
            v3 = sigmoid_activation(u3)
            desired_output = target_output[sample]
            error3 = (desired_output - v3) * v3 * (1 - v3)
            delta_w31 = learning_rate * error3 * v1
            delta_w32 = learning_rate * error3 * v2
            delta_w33 = learning_rate * error3 * inputs[2]
            error2 = error3 * weights[8] * v2 * (1 - v2)
            delta_w21 = learning_rate * error2 * inputs[0]
            delta_w22 = learning_rate * error2 * inputs[1]
            delta_w23 = learning_rate * error2 * inputs[2]
            error1 = error3 * weights[6] * v1 * (1 - v1)
            delta_w11 = learning_rate * error1 * inputs[0]
            delta_w12 = learning_rate * error1 * inputs[1]
            delta_w13 = learning_rate * error1 * inputs[2]

            for i in range(3):
                for j in range(3):
                    weights[i * 3 + j] = update_weights(i + 1, j + 1, weights[i * 3 + j], locals()[f"delta_w{i+1}{j+1}"])

            if iteration == 0:
                print(f"XOR przed dla przypadku: ({inputs[0]}, {inputs[1]}) = {v3}")
            if iteration == 9999:
                print(f"XOR po dla przypadku: ({inputs[0]}, {inputs[1]}) = {v3}")
        if iteration == 9999:
            print(f"Otrzymany błąd 1: {error1}")
            print(f"Otrzymany błąd 2: {error2}")
            print(f"Otrzymany błąd 3: {error3}")

# Initialize weights
weights = np.random.uniform(-1, 1, 9)

# Set learning rate and momentum
learning_rate = 0.7
momentum = 0.3

# Initialize previous_delta_weights
previous_delta_weights = np.zeros((3, 3))

# Train neural network using genetic algorithm
train_neural_network()

input("Press Enter to continue...")
