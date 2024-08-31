# import necessary libraries and methods
from ._3_initialize_population import initialize_population
from ._5_test_fitness_and_selection import test_fitness_and_select
from ._7_create_next_generation import next_generation
from visualization_code.visualization_methods import save_images, create_output_dirs
from data_processing_code.transformation_methods import apply_transformations
import cv2
import numpy as np

# ----------------------------------------------------------------------------------------------------------------------
# genetic algorithm itself
def genetic_algorithm(ct_image, pet_image, maximizing_fitness_function, population_size, number_selected_individuals,
                      number_generations, crossover_rate, mutation_rate, selection_type="tournament", minimize=False):

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
        #print(50 * "-")
        #rint(f"generation: {generation}:")

        # apply method to test fitness and select the best individuals of each generation
        selected_individuals = test_fitness_and_select(ct_image, pet_image, maximizing_fitness_function, population_matrix,
                                                       gray_coded_population, number_selected_individuals, selection_type, minimize)

        # divide the returns of the method into variables
        fitness_values = selected_individuals[0]
        best_individuals_matrix = selected_individuals[1]
        best_coded_individuals = selected_individuals[2]

        best_individual = best_individuals_matrix[0]

        # apply method to transform the pet image with the matrix of the best individual
        transformed_pet_image = apply_transformations(pet_image, best_individual)

        # apply method to create the next generation
        new_generation = next_generation(best_individuals_matrix, best_coded_individuals, crossover_rate, mutation_rate)
        # divide the returns to have the next generation as matrices and bitstrings
        population_matrix = new_generation[0]
        gray_coded_population = new_generation[1]

        # overlay the images and save in the list
        overlaid_image = cv2.addWeighted(ct_image, 0.5, transformed_pet_image, 0.5, 0)
        overlaid_images.append(overlaid_image)

        average_fitness = sum(fitness_values) / len(fitness_values)
        average_fitness_per_generation.append(average_fitness)

        average_fitness_first_gen = average_fitness_per_generation[0]
        average_fitness_last_gen = average_fitness_per_generation[-1]
        # visualize the progress of image-change over the generations
        cv2.imshow(f'overlaid image -- generation {generation+1}', overlaid_image)
        cv2.waitKey(1)
    cv2.destroyAllWindows()

    #print(f"Average fitness in first generation: {average_fitness_first_gen}")
    #print(f"Average fitness in last generation: {average_fitness_last_gen}")

    return population_matrix, gray_coded_population, overlaid_images, average_fitness_per_generation

# ----------------------------------------------------------------------------------------------------------------------
# apply genetic algorithm on a dict of images and save them
def process_images_and_run_algorithm(image_dict, OUTPUT, maximizing_fitness_function, population_size,
                                     number_selected_individuals, number_generations, crossover_rate, mutation_rate,
                                     selection_type="tournament", minimize=False):

    # sort the dictionary
    sorted_dict = dict(sorted(image_dict.items(), key=lambda item: int(item[0][1:])))

    average_fitness_all_generations = [[] for _ in range(number_generations)]

    # iterate over folders of the sorted dict
    for patient_folder in sorted_dict:
        # define images
        images = image_dict[patient_folder]
        # divide into ct an pet images
        ct_image = images['ct']
        pet_image = images['pet']

        # apply method to create new folders in the output directory
        patient_dir = create_output_dirs(OUTPUT, patient_folder)

        # run genetic algorithm for every image pair of the dict
        population_matrix, gray_coded_population, overlaid_images, average_fitness_per_generation = genetic_algorithm(
            ct_image, pet_image, maximizing_fitness_function, population_size,
            number_selected_individuals, number_generations, crossover_rate, mutation_rate,
            selection_type, minimize)

        for generation, avg_fitness in enumerate(average_fitness_per_generation):
            average_fitness_all_generations[generation].append(avg_fitness)

        # save overlaid image for every generation of an image pair to visualize the registration progress
        for generation, overlaid_image in enumerate(overlaid_images):
            save_images(patient_dir, overlaid_image, generation)

    for generation, fitness_list in enumerate(average_fitness_all_generations):
        overall_avg_fitness = sum(fitness_list) / len(fitness_list)
        print(f"Average fitness for generation {generation + 1} across all patients: {overall_avg_fitness}")

    print("Successfully applied genetic algorithm.")
    return average_fitness_all_generations


