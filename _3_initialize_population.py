## import necessary libraries
import numpy as np
import random
from ._1_coding_decoding import transformation_matrix, individual_to_bitstring, binary_to_gray, gray_to_binary, matrix_to_bitstring

# ===================================================================================================================
# initialize random transformations to create a population
def random_transformation(individual):
    tx, ty = random.randint(-20, 20), random.randint(-20, 20)
    sx, sy = random.uniform(0.95, 1.10), random.uniform(0.95, 1.10)
    a = random.uniform(-15, 15)
    shx, shy = random.uniform(-0.01, 0.01), random.uniform(-0.01, 0.01)
    return transformation_matrix(tx, ty, sx, sy, a, shx, shy)

# -------------------------------------------------------------------------------------------------------------------
## initialize population as binary-, gray-coded-, decoded-bitstring and matrix
def initialize_population(population_size):
    # four lists to differentiate between the different populations
    population = []
    population_as_bitstring = []
    population_as_gray_coded_bitstring = []
    population_decoded = []

    # create a population which is made of individuals; as many as the population_size instructs
    for individual in range(population_size):
        transformation = random_transformation(individual)
        binary_bitstring = matrix_to_bitstring(transformation)
        gray_coded_bitstring = binary_to_gray(binary_bitstring)
        decoded_bitstring = gray_to_binary(gray_coded_bitstring)

        # create the different populations thourough adding the individuals (transformations) the the lists
        population.append(transformation)
        population_as_bitstring.append(binary_bitstring)
        population_as_gray_coded_bitstring.append(gray_coded_bitstring)
        population_decoded.append(decoded_bitstring)

    # debug
    #print(f"population as matrices:{population}")
    #print(f"population as gray-code-bitstrings:{population_as_gray_coded_bitstring}")
    return population, population_as_bitstring, population_as_gray_coded_bitstring, population_decoded

