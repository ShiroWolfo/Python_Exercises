import random
from back_propagation import back_propagation


class Chromosome:

    def __init__(self, binary=None):
        self.binary = ""
        self.delta = 0
        if self.binary == "":
            for i in range(2):
                number = random.randint(-63, 63)
                self.binary += self.encode(number)
        else:
            self.binary = binary

    @staticmethod
    def encode(number):
        if number < 0:
            binary_representation = bin(number & 0b11111)[2:].zfill(5)
            return '0' + binary_representation
        elif number > 0:
            binary_representation = bin(number & 0b11111)[2:].zfill(5)
            return '1' + binary_representation
        else:
            # Zero case
            return '000000'

    def decode(self):
        holder = []

        for i in range(2):
            start_index = i * 6
            sign_bit = int(self.binary[start_index])
            value_bits = self.binary[start_index + 1: start_index + 6]

            if sign_bit:
                holder.append(int(value_bits, 2))
            else:
                holder.append(-int(value_bits, 2))

        return holder

    def calculate_function(self):
        vars = self.decode()
        results = back_propagation(vars[0] / 10, vars[1] / 10)
        holder = []
        self.delta = 0
        holder.append(abs(0 - results[0]))
        holder.append(abs(1 - results[1]))
        holder.append(abs(1 - results[2]))
        holder.append(abs(0 - results[3]))
        self.delta = max(holder)

    def __add__(self, other):
        index, mutation_index = random.sample(range(0, 12), 2)
        mutation = random.randint(0, 1)
        kid = self.binary[:index] + other.binary[index:]
        kid = kid[:mutation_index] + str(mutation) + kid[mutation_index + 1:]
        return kid


pop = []
for i in range(50):
    ch = Chromosome()
    ch.calculate_function()
    pop.append(ch)

generation = 0

while pop[0].delta > 0.045:

    pop = sorted(pop, key=lambda x: x.delta)
    pop = pop[:30]
    while len(pop) < 50:
        index_1, index_2 = random.sample(range(9), 2)
        pop.append(Chromosome((pop[index_1] + pop[index_2])))

    for i in pop:
        i.calculate_function()
    generation += 1

    pop = sorted(pop, key=lambda x: x.delta)
    print(pop[0].delta)

print(generation)
print(f"learning rate: {pop[0].decode()[0]/10} momentum: {pop[0].decode()[1]/10}")
