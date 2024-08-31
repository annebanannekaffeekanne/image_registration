## import necessary libraries
import numpy as np
import random
from ._1_coding_decoding import transformation_matrix, individual_to_bitstring, binary_to_gray, gray_to_binary

# -----------------------------------------------------------------------------------------------------
## initialize population as binary-, gray-coded-, decoded-bitstring and matrix
def initialize_population(population_size):
    # for lists to differentiate between the different populations
    # as matrix
    population = []
    # as binary bitstring
    population_as_bitstring = []
    # as gray coded bitstring
    population_as_gray_coded_bitstring = []
    # decoded (not necessary)
    population_decoded = []

    # create a population which is made of individuals; as many as the population_size instructs
    for individual in range(population_size):
        ## value ranges are adjustable
        # translation variables
        tx, ty = random.randint(-20, 20), random.randint(-20, 20)
        # scaling factors
        sx, sy = random.uniform(0.95, 1.10), random.uniform(0.95, 1.10)
        # rotation angle
        a = random.uniform(-15, 15)
        # shearing factors
        shx, shy = random.uniform(-0.01, 0.01), random.uniform(-0.01, 0.01)

        # hand the selected transformation parameter over to the method where a transformation matrix is generated
        transformation = transformation_matrix(tx, ty, sx, sy, a, shx, shy)
        # hand the selected transformation parameter over to the method where a bitstring is created
        binary_bitstring = individual_to_bitstring(tx, ty, sx, sy, a, shx, shy)

        # create a gray coded bitstring thourough using to binary_to_gray method
        gray_coded_bitstring = binary_to_gray(binary_bitstring)
        # decode bitstring (not necessary)
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


# apply method
#population_size = 10
#population = initialize_population(population_size)
#pop_as_matrix = population[0]
#print(pop_as_matrix)
