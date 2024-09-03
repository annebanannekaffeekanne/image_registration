# import necessary libraries and methods
import random
from ._1_coding_decoding import bitstring_to_matrix
from ._6_crossover_mutation import single_point_crossover, two_point_crossover, uniform_crossover, mutation

# ===================================================================================================================
## create the next generation
def next_generation(best_individual_matrix, best_coded_individuals, crossover_rate, mutation_rate, crossover_method):
    # empty list for the generation as bitstrings
    next_generation_bitstrings = []
    # select number of parents which is the length of the chosen individuals (=return of method: test_fitness_and_select)
    number_parents = len(best_individual_matrix)
    # make sure that number of parents remains odd
    if number_parents % 2 != 0:
        # if number is not dividable with 2, drop the rest
        best_coded_individuals.pop()

    # iterate over the individuals in 2 step
    for i in range(0, len(best_coded_individuals), 2):
        # define parents
        parent1 = best_coded_individuals[i]
        parent2 = best_coded_individuals[i + 1]
        #print(f"parent1: {parent1}; parent2: {parent2}")

        # choose a random value; if it's smaller than the crossover rate
        if random.random() < crossover_rate:
            # apply the crossover method to create children
            if crossover_method == 'single_point':
                child1, child2 = single_point_crossover(parent1, parent2)
            elif crossover_method == 'two_point':
                child1, child2 = two_point_crossover(parent1, parent2)
            elif crossover_method == 'uniform':
                child1, child2 = uniform_crossover(parent1, parent2, crossover_rate)
            else:
                raise ValueError("Unbekannte Crossover-Methode.")
            #print(f"child1: {child1}; child2: {child2}")

            # and apply the mutation method on both of the children and add them to the list
            next_generation_bitstrings.extend([mutation(child1, mutation_rate), mutation(child2, mutation_rate)])
        else:
            # otherwise apply the mutation method on the parents
            next_generation_bitstrings.extend([mutation(parent1, mutation_rate), mutation(parent2, mutation_rate)])

    # make sure, that the number of individuals per population remains constant
    while len(next_generation_bitstrings) < len(best_coded_individuals):
        # add random chosen and mutated individuals to the next generation
        next_generation_bitstrings.append(mutation(random.choice(best_coded_individuals), mutation_rate))

    # create the individuals of the next generation as matrices thourough applying the bitstring_to_matrix method
    next_generation_matrix = [bitstring_to_matrix(bitstring) for bitstring in next_generation_bitstrings]

    #print(f"next generation as matrices: {next_generation_matrix}")
    #print(f"next generation as bitstrings: {next_generation_bitstrings}")
    return next_generation_matrix, next_generation_bitstrings
