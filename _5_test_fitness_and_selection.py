## import necessary libraries and methods
from ._2_fitness_functions import NCC, SSD, NMI, MI
from ._4_selection_methods import roulette_selection, rankbased_selection, tournament_selection, SUS_selection
from data_processing_code.transformation_methods import apply_transformations

# ----------------------------------------------------------------------------------------------------------
def test_fitness_and_select(ct_image, pet_image, maximizing_fitness_function, population_matrix, gray_coded_population, number_selected_individuals, selection_type="roulette", minimize=False):
    if ct_image is None or pet_image is None:
        print(f"error: image loading in {patient_folder}")

    fitness_values = []
    count = 0

    # iterate over populations to calculate the fitness for every transformation
    for individual in population_matrix:
        # raise count by 1
        count += 1
        # apply transformation matrix aka individual on the pet image with the 'apply_transformation' method
        transformed_pet_image = apply_transformations(pet_image, individual)
        # calcualte fitness with the fitness function that is transfered as a parameter in the method
        fitness_value = maximizing_fitness_function(ct_image, transformed_pet_image)
        if minimize:
            fitness_value = -fitness_value
        fitness_values.append(fitness_value)

    if selection_type == "roulette":
        best_individuals = roulette_selection(population_matrix, gray_coded_population, fitness_values, number_selected_individuals)
        best_individuals_matrix = best_individuals[0]
        best_coded_individuals = best_individuals[1]
    elif selection_type == "SUS":
        best_individuals = SUS_selection(population_matrix, gray_coded_population, fitness_values, number_selected_individuals)
        best_individuals_matrix = best_individuals[0]
        best_coded_individuals = best_individuals[1]
    elif selection_type == "rankbased":
        best_individuals = rankbased_selection(population_matrix, gray_coded_population, fitness_values, number_selected_individuals)
        best_individuals_matrix = best_individuals[0]
        best_coded_individuals = best_individuals[1]
    elif selection_type == "tournament":
        best_individuals = tournament_selection(population_matrix, gray_coded_population, fitness_values, number_selected_individuals)
        best_individuals_matrix = best_individuals[0]
        best_coded_individuals = best_individuals[1]
    else:
        raise ValueError(f"unknown selection type: {selection_type}")
        #print(60 * "-")
    best_individuals_matrix.extend(best_individuals[0])
    best_coded_individuals.extend(best_individuals[1])
    #print(f"fitness values for patient {patient_folder}: {fitness_values}")
    return fitness_values, best_individuals_matrix, best_coded_individuals

#NCC_fitness_scores = test_fitness_and_select(ct_image, pet_image, NCC, population_matrix, gray_coded_population, number_selected_individuals, selection_type="tournament")