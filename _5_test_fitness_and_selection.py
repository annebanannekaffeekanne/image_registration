## import necessary libraries and methods
from ._1_coding_decoding import apply_transformations
from ._4_selection_methods import roulette_selection, rankbased_selection, tournament_selection, SUS_selection

# ===================================================================================================================
def test_fitness_and_select(ct_image, pet_image, maximizing_fitness_function, population_matrix, gray_coded_population,
                            number_selected_individuals, selection_method, minimize=False):
    ## test fitness
    fitness_values = []
    count = 0

    # iterate over populations to calculate the fitness for every transformation
    for individual in population_matrix:
        count += 1
        # apply transformation matrix aka individual on the pet image with the 'apply_transformation' method
        transformed_pet_image = apply_transformations(pet_image, individual)
        # calcualte fitness with the fitness function that is transfered as a parameter in the method
        fitness_value = maximizing_fitness_function(ct_image, transformed_pet_image)
        #print(f"fitness value for {individual}: {fitness_value}")

        # if there's a minimizing fitness function flip the sign
        if minimize:
            fitness_value = -fitness_value
        # add fitness value to the list
        fitness_values.append(fitness_value)
        #print(f"all fitness values for a population: {fitness_values}")

    ## select
    # differentiate between the selection types and apply the corresponding selection method
    # divide into individuals as matrices and as bitstrings for further processing
    # roulette selection

    best_individuals = selection_method(population_matrix, gray_coded_population, fitness_values,
                                            number_selected_individuals)
    best_individuals_matrix = best_individuals[0]
    best_coded_individuals = best_individuals[1]

    best_individuals_matrix.extend(best_individuals[0])
    best_coded_individuals.extend(best_individuals[1])

    #print(f"best individuals: {best_individuals_matrix}")
    return fitness_values, best_individuals_matrix, best_coded_individuals
