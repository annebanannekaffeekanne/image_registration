## import necessary libraries
#from algorithm_code.coding_decoding import individual_to_bitstring, bitstring_to_individual, bitstring_to_matrix
from algorithm_code._3_initialize_population import initialize_population
from algorithm_code._2_fitness_functions import NCC
from algorithm_code._5_test_fitness_and_selection import test_fitness_and_select
from algorithm_code._6_crossover_mutation import next_generation
from data_processing_code.load_preprocess_transform_images import load_images
from data_processing_code.transformation_methods import apply_transformations
from visualization_code.visualization_methods import save_images, create_output_dirs
import cv2

# ----------------------------------------------------------------------------------------------------------
# define path
DATA = '/Users/anne/PycharmProjects/genetic_algorithm/data/preprocessed_data'
OUTPUT = '/Users/anne/PycharmProjects/genetic_algorithm/output_images'

# ----------------------------------------------------------------------------------------------------------
## declare variables
population_size = 10
mutation_rate = 0.01
crossover_rate = 0.7
number_selected_individuals = population_size//2
number_generations = 30
image_dict = load_images(DATA)


# ----------------------------------------------------------------------------------------------------------
## final algorithm
def genetic_algorithm(image_dict, maximizing_fitness_function, population_size, number_selected_individuals, number_generations, selection_type="tournament", minimize=False):
    sorted_dict = dict(sorted(image_dict.items(), key=lambda item: int(item[0][1:])))

    # iterate over patients folders
    for patient_folder in sorted_dict:
        images = image_dict[patient_folder]
        # extract ct- and pet-images for each patient
        ct_image = images['ct']
        pet_image = images['pet']

        patient_dir = create_output_dirs(OUTPUT, patient_folder)

        population = initialize_population(population_size)
        population_matrix = population[0]
        gray_coded_population = population[2]

        selected_individuals = test_fitness_and_select(ct_image, pet_image, maximizing_fitness_function, population_matrix, gray_coded_population, number_selected_individuals, selection_type, minimize=False)

        fitness_values = selected_individuals[0]
        best_individuals_matrix = selected_individuals[1]
        best_coded_individuals = selected_individuals[2]

        #print(f"best fitness-values for {patient_folder}: {fitness_values}")
        #print(f"best individual as matrix for {patient_folder}: {best_individuals_matrix}")
        #print(f"beste individual as gray-code for {patient_folder}: {best_coded_individuals}")

        for generation in range(number_generations):
            selected_individuals = test_fitness_and_select(ct_image, pet_image, maximizing_fitness_function, population_matrix, gray_coded_population, number_selected_individuals, selection_type, minimize=False)

            fitness_values = selected_individuals[0]
            best_individuals_matrix = selected_individuals[1]
            best_coded_individuals = selected_individuals[2]

            best_individual = best_individuals_matrix[0]  # Annahme: Das erste Individuum ist das beste
            transformed_pet_image = apply_transformations(pet_image, best_individual)

            # Erzeuge die nächste Generation
            new_generation = next_generation(best_individuals_matrix, best_coded_individuals, crossover_rate,
                                             mutation_rate)
            new_generation_matrix = new_generation[0]
            new_generation_coded = new_generation[1]
            population_matrix = new_generation_matrix
            gray_coded_population = new_generation_coded


            overlaid_image = cv2.addWeighted(ct_image, 0.5, transformed_pet_image, 0.5, 0)
            save_images(patient_dir, overlaid_image, generation_count=generation)
            cv2.imshow('Overlaid Image', overlaid_image)
            cv2.waitKey(1)  # Warte kurz zwischen den Bildern, 1 ms

            #print(f"generation {generation + 1} - best fitness-values for {patient_folder}: {fitness_values}")

genetic_algorithm(image_dict, NCC, population_size, number_selected_individuals, number_generations, selection_type="tournament", minimize=False)

