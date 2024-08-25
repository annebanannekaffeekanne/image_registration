## import necessary libraries
import numpy as np
import random
from ._1_coding_decoding import transformation_matrix, individual_to_bitstring, binary_to_gray, gray_to_binary

# -----------------------------------------------------------------------------------------------------
## initialize population as binary-, gray-coded-, decoded-bitstring and matrix
def initialize_population(population_size):
    population = []
    population_as_bitstring = []
    population_as_gray_coded_bitstring = []
    population_decoded = []

    for individual in range(population_size):
        # translation variables
        tx, ty = random.randint(-1, 1), random.randint(-1, 1)
        # scaling factors
        sx, sy = random.uniform(0.99, 1.0), random.uniform(0.99, 1.0)
        # rotation angle
        a = random.uniform(-1, 1)
        # shearing factors
        shx, shy = random.uniform(-0.001, 0.001), random.uniform(-0.001, 0.001)

        transformation = transformation_matrix(tx, ty, sx, sy, a, shx, shy)
        binary_bitstring = individual_to_bitstring(tx, ty, sx, sy, a, shx, shy)
        gray_coded_bitstring = binary_to_gray(binary_bitstring)
        decoded_bitstring = gray_to_binary(gray_coded_bitstring)

        population.append(transformation)
        population_as_bitstring.append(binary_bitstring)
        population_as_gray_coded_bitstring.append(gray_coded_bitstring)
        population_decoded.append(decoded_bitstring)

    # debug
    #print(f"population as matrices:{population}")
    #print(f"population as gray-code-bitstrings:{population_as_gray_coded_bitstring}")
    return population, population_as_bitstring, population_as_gray_coded_bitstring, population_decoded


# apply method
#population_size = 10
#population = initialize_population(population_size)
#pop_as_matrix = population[0]
#print(pop_as_matrix)
