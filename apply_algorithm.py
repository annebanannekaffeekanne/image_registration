from ._8_genetic_algorithm import genetic_algorithm, genetic_algorithm_for_tuning
from data_processing_code.process_images import create_output_dirs, save_registered_images
import numpy as np

# apply genetic algorithm on a dict of images and save them
def process_save_images_and_run_algorithm(image_dict, OUTPUT, maximizing_fitness_function, population_size,
                                     number_selected_individuals, number_generations, crossover_rate, mutation_rate,
                                     selection_method, crossover_method, minimize=False):
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
            selection_method, crossover_method, minimize)

        for generation, avg_fitness in enumerate(average_fitness_per_generation):
            average_fitness_all_generations[generation].append(avg_fitness)

        # save overlaid image for every generation of an image pair to visualize the registration progress
        for generation, overlaid_image in enumerate(overlaid_images):
            save_registered_images(patient_dir, overlaid_image, generation)

    for generation, fitness_list in enumerate(average_fitness_all_generations):
        overall_avg_fitness = sum(fitness_list) / len(fitness_list)
        print(f"average fitness for generation {generation + 1} across all patients: {overall_avg_fitness}")

    print("successfully applied genetic algorithm.")
    return average_fitness_all_generations

# -------------------------------------------------------------------------------------------------------------------
# apply genetic algorithm on a set of images without saving them
def process_images_and_run_algorithm(image_dict, maximizing_fitness_function, population_size,
                                     number_selected_individuals, final_number_selected, number_generations,
                                     crossover_rate, initial_mutation_rate, final_mutation_rate,
                                     selection_method, crossover_method, minimize=False):
    # sort the dictionary
    sorted_dict = dict(sorted(image_dict.items(), key=lambda item: int(item[0][1:])))
    variance_per_image_pair = {patient: [] for patient in sorted_dict.keys()}
    average_variance_all_generations = [[] for _ in range(number_generations)]
    average_fitness_all_generations = [[] for _ in range(number_generations)]

    # iterate over folders of the sorted dict
    for patient_folder in sorted_dict:
        # define images
        images = image_dict[patient_folder]
        # divide into ct an pet images
        ct_image = images['ct']
        pet_image = images['pet']

        # run genetic algorithm for every image pair of the dict
        population_matrix, gray_coded_population, overlaid_images, average_fitness_per_generation, \
            variances_per_generation, mutation_rates, count_selected_individuals = genetic_algorithm(
            ct_image, pet_image, maximizing_fitness_function, population_size,
            number_selected_individuals, final_number_selected, number_generations, crossover_rate,
            initial_mutation_rate, final_mutation_rate, selection_method, crossover_method, minimize)

        variance_per_image_pair[patient_folder] = variances_per_generation

        for generation, avg_fitness in enumerate(average_fitness_per_generation):
            average_fitness_all_generations[generation].append(avg_fitness)
        for generation, variance in enumerate(variances_per_generation):
            # Calculate the mean variance for this generation and add to the corresponding list
            mean_variance = np.mean(variance)
            average_variance_all_generations[generation].append(mean_variance)

    for generation, fitness_list in enumerate(average_fitness_all_generations):
        overall_avg_fitness = sum(fitness_list) / len(fitness_list)
        print(f"average fitness for generation {generation + 1} across all patients: {overall_avg_fitness}")

    print("successfully applied genetic algorithm.")
    return variance_per_image_pair, average_fitness_all_generations, average_variance_all_generations, mutation_rates, \
        count_selected_individuals


def process_images_and_run_algorithm_for_tuning(image_dict, maximizing_fitness_function, population_size,
                                     number_selected_individuals, number_generations, crossover_rate, mutation_rate,
                                     selection_method, crossover_method, minimize=False):
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

        # run genetic algorithm for every image pair of the dict
        population_matrix, gray_coded_population, overlaid_images, average_fitness_per_generation = genetic_algorithm_for_tuning(
            ct_image, pet_image, maximizing_fitness_function, population_size,
            number_selected_individuals, number_generations, crossover_rate, mutation_rate,
            selection_method, crossover_method, minimize)

        for generation, avg_fitness in enumerate(average_fitness_per_generation):
            average_fitness_all_generations[generation].append(avg_fitness)

        # save overlaid image for every generation of an image pair to visualize the registration progress

    for generation, fitness_list in enumerate(average_fitness_all_generations):
        overall_avg_fitness = sum(fitness_list) / len(fitness_list)
        print(f"average fitness for generation {generation + 1} across all patients: {overall_avg_fitness}")

    print("successfully applied genetic algorithm.")
    return average_fitness_all_generations