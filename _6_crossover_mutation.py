## import necessary libraries
import random

# ----------------------------------------------------------------------------------------------------------
# crossover, parents only as bitstrings
def crossover(parent1, parent2):
    # choose a random point which is in the range of the bitstring length (parent-length)
    point = random.randint(1, len(parent1) - 1)

    # child1: take the values from bitstring start till the point from p1 and combine with the values
    # from the point till bitstring end from p2
    child1 = parent1[:point] + parent2[point:]
    # child2: take the values from bitstring start till the point from p2 and combine with the values
    # from the point till bitstring end from p1
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# mutation
def mutation(individual, mutation_rate):
    # new individual is the given individual
    new_individual = list(individual)
    # iterate over the individuals length (=bitstring length) every single number
    for i in range(len(new_individual)):
        # if the mutation_rate is higher than a random value
        if random.random() < mutation_rate:
            # the bit of the bitstring is flipped
            new_individual[i] = '0' if new_individual[i] == '1' else '1'
    return ''.join(new_individual)

