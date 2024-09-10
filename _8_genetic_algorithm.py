## import necessary libraries and methods
from ._1_coding_decoding import apply_transformations, binary_to_gray, matrix_to_bitstring
from ._3_initialize_population import initialize_population
from ._4_selection_methods import adjust_selection_size
from ._5_test_fitness_and_selection import test_fitness_and_select
from ._6_crossover_mutation import single_point_crossover, two_point_crossover, uniform_crossover, adjust_mutation_rate
from ._7_create_next_generation import next_generation
from ._9_gendrift_adaptive_radiation import adaptive_radiation
from data_processing_code.process_images import save_registered_images, create_output_dirs
import cv2
import matplotlib.pyplot as plt
import numpy as np

# ===================================================================================================================
def calculate_variance_of_parameters(population_matrix):
    # Assume population_matrix is a list of transformation matrices
    # Stack all transformation matrices into a 3D array
    population_array = np.array(population_matrix)

    # Calculate variance along the axis corresponding to the population
    # (i.e., across all individuals for each parameter)
    variance_per_parameter = np.var(population_array, axis=0)

    return variance_per_parameter


# genetic algorithm itself
def genetic_algorithm(ct_image, pet_image, maximizing_fitness_function, population_size, number_selected_individuals,
                      final_number_selected, number_generations, crossover_rate, initial_mutation_rate,
                      final_mutation_rate, selection_method, crossover_method, minimize=False):
    # Initialisiere die Population
    population = initialize_population(population_size)
    population_matrix = population[0]
    gray_coded_population = population[2]

    overlaid_images = []
    average_fitness_per_generation = []
    variances_per_generation = []
    mutation_rates = []
    count_selected_individuals = []

    for generation in range(number_generations):
        print(f"\n--- Generation {generation + 1} ---")

        # Anpassung der Mutationsrate und Anzahl der Individuen
        mutation_rate = adjust_mutation_rate(generation, number_generations, initial_mutation_rate, final_mutation_rate)
        mutation_rates.append(mutation_rate)
        #number_selected_individuals = adjust_selection_size(generation, number_generations, number_selected_individuals,
        #                                                    final_number_selected)
        count_selected_individuals.append(number_selected_individuals)
        print(f"Mutationsrate: {mutation_rate}")
        print(f"Anzahl ausgewählter Individuen: {number_selected_individuals}")

        # Teste Fitness und wähle die besten Individuen
        selected_individuals = test_fitness_and_select(ct_image, pet_image, maximizing_fitness_function,
                                                       population_matrix, gray_coded_population,
                                                       number_selected_individuals, selection_method, minimize)

        fitness_values = selected_individuals[0]
        best_individuals_matrix = selected_individuals[1]
        best_coded_individuals = selected_individuals[2]

        best_individual = best_individuals_matrix[0]
        transformed_pet_image = apply_transformations(pet_image, best_individual)

        # Evaluierung der Konvergenz durch Varianz der Fitnesswerte
        fitness_variance = np.var(fitness_values)
        variances_per_generation.append(fitness_variance)
        print(f"Varianz der Fitnesswerte: {fitness_variance}")

        # Schwellenwert für die adaptive Radiation
        convergence_threshold = 0.01  # Beispielwert, anpassbar

        # Überprüfe, ob die adaptive Radiation aktiviert wird
        if fitness_variance < convergence_threshold:
            print("Adaptive Radiation wird aktiviert. Niedrige Varianz der Fitnesswerte erkannt.")
            population_matrix, gray_coded_population = adaptive_radiation(
                ct_image, pet_image, population_matrix, gray_coded_population, 4, mutation_rate, crossover_rate,
                maximizing_fitness_function, number_selected_individuals, selection_method, minimize)
        else:
            print("Adaptive Radiation wird nicht aktiviert.")

        # Erstelle die nächste Generation
        new_generation = next_generation(best_individuals_matrix, best_coded_individuals,
                                         crossover_rate, mutation_rate, crossover_method)
        population_matrix = new_generation[0]
        gray_coded_population = new_generation[1]

        # Visualisiere überlagerte Bilder
        overlaid_image = cv2.addWeighted(ct_image, 0.5, transformed_pet_image, 0.5, 0)
        overlaid_images.append(overlaid_image)

        average_fitness = sum(fitness_values) / len(fitness_values)
        average_fitness_per_generation.append(average_fitness)
        print(f"Durchschnittliche Fitness: {average_fitness}")
        # Zeige das Bild für die aktuelle Generation
        cv2.imshow(f'Überlagerte Bilder für Generation {generation + 1}', overlaid_image)
        cv2.waitKey(1)

    cv2.destroyAllWindows()

    print("\n--- Algorithmus abgeschlossen ---")
    print("Gesamtübersicht der durchschnittlichen Fitness pro Generation:")
    print(average_fitness_per_generation)
    print("Gesamtübersicht der Varianzen pro Generation:")
    print(variances_per_generation)

    return population_matrix, gray_coded_population, overlaid_images, average_fitness_per_generation, \
        variances_per_generation, mutation_rates, count_selected_individuals



# ===================================================================================================================


def genetic_algorithm_for_tuning(ct_image, pet_image, maximizing_fitness_function, population_size, number_selected_individuals,
                      number_generations, crossover_rate, mutation_rate, selection_method, crossover_method, minimize=False):
    # apply method to initialize a population
    population = initialize_population(population_size)
    # divide into population as matrices and as coded bitstrings (method returns different populations)
    population_matrix = population[0]
    gray_coded_population = population[2]

    # create an emty list to save overlaid images in
    overlaid_images = []
    average_fitness_per_generation = []

    # iterate over the generations
    for generation in range(number_generations):
        # apply method to test fitness and select the best individuals of each generation
        selected_individuals = test_fitness_and_select(ct_image, pet_image, maximizing_fitness_function,
                                                       population_matrix,gray_coded_population,
                                                       number_selected_individuals, selection_method, minimize)

        # divide the returns of the method into variables
        fitness_values = selected_individuals[0]
        best_individuals_matrix = selected_individuals[1]
        best_coded_individuals = selected_individuals[2]

        best_individual = best_individuals_matrix[0]

        # apply method to transform the pet image with the matrix of the best individual
        transformed_pet_image = apply_transformations(pet_image, best_individual)

        # apply method to create the next generation
        new_generation = next_generation(best_individuals_matrix, best_coded_individuals,
                                         crossover_rate, mutation_rate, crossover_method)
        # divide the returns to have the next generation as matrices and bitstrings
        population_matrix = new_generation[0]
        gray_coded_population = new_generation[1]

        # overlay the images and save in the list
        overlaid_image = cv2.addWeighted(ct_image, 0.5, transformed_pet_image, 0.5, 0)
        overlaid_images.append(overlaid_image)

        average_fitness = sum(fitness_values) / len(fitness_values)
        average_fitness_per_generation.append(average_fitness)

        #average_fitness_first_gen = average_fitness_per_generation[0]
        #average_fitness_last_gen = average_fitness_per_generation[-1]
        # visualize the progress of image-change over the generations
        cv2.imshow(f'overlaid image for generation {generation+1}', overlaid_image)
        cv2.waitKey(1)
    cv2.destroyAllWindows()

    #print(f"Average fitness in first generation: {average_fitness_first_gen}")
    #print(f"Average fitness in last generation: {average_fitness_last_gen}")

    return population_matrix, gray_coded_population, overlaid_images, average_fitness_per_generation

