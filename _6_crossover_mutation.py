## import necessary libraries
import random
from ._1_coding_decoding import bitstring_to_matrix

# ----------------------------------------------------------------------------------------------------------
## single methods
# crossover, parents liegen als bitstrings vor
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutation(individual, mutation_rate):
    new_individual = list(individual)
    for i in range(len(new_individual)):
        if random.random() < mutation_rate:
            new_individual[i] = '0' if new_individual[i] == '1' else '1'
    return ''.join(new_individual)

# ----------------------------------------------------------------------------------------------------------
## apply methods to create the next generation
def next_generation(best_individual_matrix, best_coded_individuals, crossover_rate, mutation_rate):
    next_generation_bitstrings = []

    number_parents = len(best_individual_matrix)
    if number_parents % 2 != 0:
        best_coded_individuals.pop()

    for i in range(0, len(best_coded_individuals), 2):
        parent1 = best_coded_individuals[i]
        parent2 = best_coded_individuals[i + 1]
        #print(f"parent1: {parent1}; parent2: {parent2}")
        if random.random() < crossover_rate:
            child1, child2 = crossover(parent1, parent2)
            #print(f"child1: {child1}; child2: {child2}")
            next_generation_bitstrings.extend([mutation(child1, mutation_rate), mutation(child2, mutation_rate)])
        else:
            next_generation_bitstrings.extend([mutation(parent1, mutation_rate), mutation(parent2, mutation_rate)])

    while len(next_generation_bitstrings) < len(best_coded_individuals):
        next_generation_bitstrings.append(mutation(random.choice(best_coded_individuals), mutation_rate))

    next_generation_matrix = [bitstring_to_matrix(bitstring) for bitstring in next_generation_bitstrings]
    #print(f"next generation as matrices: {next_generation_matrix}")
    #print(f"next generation as bitstrings: {next_generation_bitstrings}")
    return next_generation_matrix, next_generation_bitstrings

# exemplary apply
# next_generation(best_individuals_matrix, best_coded_individuals, crossover_rate, mutation_rate)