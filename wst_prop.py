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

def train_neural_network():
    input_data = np.array([[1, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1]])
    target_output = np.array([0, 1, 1, 0])

    for iteration in range(10000):
        for sample in range(4):
            inputs = input_data[:, sample]
            u1 = calculate_activation(inputs[0], weights[0, 0], inputs[1], weights[0, 1], inputs[2], weights[0, 2])
            v1 = sigmoid_activation(u1)
            u2 = calculate_activation(inputs[0], weights[1, 0], inputs[1], weights[1, 1], inputs[2], weights[1, 2])
            v2 = sigmoid_activation(u2)
            u3 = calculate_activation(v1, weights[2, 0], v2, weights[2, 1], inputs[2], weights[2, 2])
            v3 = sigmoid_activation(u3)
            desired_output = target_output[sample]
            error3 = (desired_output - v3) * v3 * (1 - v3)
            delta_w31 = learning_rate * error3 * v1
            delta_w32 = learning_rate * error3 * v2
            delta_w33 = learning_rate * error3 * inputs[2]
            error2 = error3 * weights[2, 1] * v2 * (1 - v2)
            delta_w21 = learning_rate * error2 * inputs[0]
            delta_w22 = learning_rate * error2 * inputs[1]
            delta_w23 = learning_rate * error2 * inputs[2]
            error1 = error3 * weights[2, 0] * v1 * (1 - v1)
            delta_w11 = learning_rate * error1 * inputs[0]
            delta_w12 = learning_rate * error1 * inputs[1]
            delta_w13 = learning_rate * error1 * inputs[2]
            
            for i in range(3):
                for j in range(3):
                    weights[i, j] = update_weights(i + 1, j + 1, weights[i, j], locals()[f"delta_w{i+1}{j+1}"])
            
            if iteration == 0:
                print(f"XOR przed dla przypadku: ({inputs[0]}, {inputs[1]}) = {v3}")
            if iteration == 9999:
                print(f"XOR po dla przypadku:({inputs[0]}, {inputs[1]}) = {v3}")
        if iteration == 9999:
            print(f"Otrzymany błąd 1:{error1}")
            print(f"Otrzymany błąd 2:{error2}")
            print(f"Otrzymany błąd 3:{error3}")

# Initialize weights
weights = np.random.uniform(-1, 1, (3, 3))

# Set learning rate and momentum
learning_rate = 0.7
momentum = 0.3

# Initialize previous_delta_weights
previous_delta_weights = np.zeros((3, 3))

# Train neural network
train_neural_network()

input("Press Enter to continue...")
