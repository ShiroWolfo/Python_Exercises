import math

import numpy as np

LEARNING_STEPS = 10000

x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]
bias = [1, 1, 1, 1]
w = np.random.uniform(-1, 1, (3, 3))
delta_w = np.zeros((3, 3))
previous_step_w = np.zeros((3, 3))

predicted_output = [0, 1, 1, 0]
learning_rate = 2.9
momentum = -2.1
print(w)
for i in range(LEARNING_STEPS):
    for j in range(len(x1)):
        u1 = x1[j] * w[0][0] + x2[j] * w[0][1] + bias[j] * w[0][2]
        u2 = x1[j] * w[1][0] + x2[j] * w[1][1] + bias[j] * w[1][2]

        v1 = 1 / (1 + math.exp(-u1))
        v2 = 1 / (1 + math.exp(-u2))

        u3 = v1 * w[2][0] + v2 * w[2][1] + bias[j] * w[2][2]
        v3 = 1 / (1 + math.exp(-u3))

        delta_2 = (predicted_output[j] - v3) * v3 * (1 - v3)

        delta_w[2][0] = learning_rate * delta_2 * v1
        delta_w[2][1] = learning_rate * delta_2 * v2
        delta_w[2][2] = learning_rate * delta_2 * v3

        delta_0 = delta_2 * w[2][0] * v1 * (1 - v1)

        delta_w[0][0] = learning_rate * delta_0 * x1[j]
        delta_w[0][1] = learning_rate * delta_0 * x2[j]
        delta_w[0][2] = learning_rate * delta_0 * bias[j]

        delta_1 = delta_2 * w[2][1] * v2 * (1 - v2)

        delta_w[1][0] = learning_rate * delta_1 * x1[j]
        delta_w[1][1] = learning_rate * delta_1 * x2[j]
        delta_w[1][2] = learning_rate * delta_1 * bias[j]

        for k in range(3):
            for l in range(3):
                w[k][l] += delta_w[k][l] + momentum * previous_step_w[k][l]

        if i == LEARNING_STEPS - 1:
            print(f"{x1[j]} and {x2[j]} -> {v3}")


print(f"delta after training {w}")
input()