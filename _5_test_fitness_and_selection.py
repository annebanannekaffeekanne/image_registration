## import necessary libraries and methods
from ._1_coding_decoding import apply_transformations
from ._2_fitness_functions import NCC, SSD, NMI, MI
from ._4_selection_methods import roulette_selection, rankbased_selection, tournament_selection, SUS_selection

# ----------------------------------------------------------------------------------------------------------
def test_fitness_and_select(ct_image, pet_image, maximizing_fitness_function, population_matrix, gray_coded_population, number_selected_individuals, selection_type="roulette", minimize=False):

    ## test fitness
    # make sure the images were loaded
    if ct_image is None or pet_image is None:
        print(f"error: image loading in {patient_folder}")

    # create empty list where the fitness values are saved
    fitness_values = []
    # count variable (not necessary; only for debugging)
    count = 0

    # iterate over populations to calculate the fitness for every transformation
    for individual in population_matrix:
        # raise count by 1
        count += 1
        # apply transformation matrix aka individual on the pet image with the 'apply_transformation' method
        transformed_pet_image = apply_transformations(pet_image, individual)
        # calcualte fitness with the fitness function that is transfered as a parameter in the method
        fitness_value = maximizing_fitness_function(ct_image, transformed_pet_image)
        #print(f"fitness value for {individual}: {fitness_value}")

        # if there's a minimizinf fitness function flip the sign
        if minimize:
            fitness_value = -fitness_value
        # add fitness value to the list
        fitness_values.append(fitness_value)
        #print(f"all fitness values for a population: {fitness_values}")

    ## select
    # differentiate between the selection types and apply the corresponding selection method
    # divide into individuals as matrices and as bitstrings for further processing
    # roulette selection
    if selection_type == "roulette":
        best_individuals = roulette_selection(population_matrix, gray_coded_population, fitness_values, number_selected_individuals)
        best_individuals_matrix = best_individuals[0]
        best_coded_individuals = best_individuals[1]
    # stochastic univerasal sampling
    elif selection_type == "SUS":
        best_individuals = SUS_selection(population_matrix, gray_coded_population, fitness_values, number_selected_individuals)
        best_individuals_matrix = best_individuals[0]
        best_coded_individuals = best_individuals[1]
    # rankbased selection
    elif selection_type == "rankbased":
        best_individuals = rankbased_selection(population_matrix, gray_coded_population, fitness_values, number_selected_individuals)
        best_individuals_matrix = best_individuals[0]
        best_coded_individuals = best_individuals[1]
    # tournament selection
    elif selection_type == "tournament":
        best_individuals = tournament_selection(population_matrix, gray_coded_population, fitness_values, number_selected_individuals)
        best_individuals_matrix = best_individuals[0]
        best_coded_individuals = best_individuals[1]
    # if a wrong parameter is handed over: print error
    else:
        raise ValueError(f"unknown selection type: {selection_type}")
        #print(60 * "-")

    best_individuals_matrix.extend(best_individuals[0])
    best_coded_individuals.extend(best_individuals[1])

    #print(f"fitness values for patient {patient_folder}: {fitness_values}")
    return fitness_values, best_individuals_matrix, best_coded_individuals

#NCC_fitness_scores = test_fitness_and_select(ct_image, pet_image, NCC, population_matrix, gray_coded_population, number_selected_individuals, selection_type="tournament")