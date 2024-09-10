## import necessary libraries and methods
from data_processing_code.preprocess_transform_images import load_images
from data_processing_code.process_images import save_images, create_output_dirs
from test_preprocessing import test_fitness
from visualization_code.visualization_methods import plot_patient_fitness_generations, plot_total_average_fitness_generations, plot_total_average_variance_generations, plot_patient_variance_generations, plot_mutation_rate, plot_number_selected_individuals
from algorithm_code._2_fitness_functions import NCC, NMI, MI, SSD
from algorithm_code._3_initialize_population import initialize_population
from algorithm_code._4_selection_methods import roulette_selection, rankbased_selection, tournament_selection, SUS_selection
from algorithm_code._5_test_fitness_and_selection import test_fitness_and_select
from algorithm_code._6_crossover_mutation import single_point_crossover, two_point_crossover, uniform_crossover
from algorithm_code._8_genetic_algorithm import genetic_algorithm
from algorithm_code.apply_algorithm import process_images_and_run_algorithm, process_save_images_and_run_algorithm
import cv2
from algorithm_code._9_gendrift_adaptive_radiation import adaptive_radiation


# ===================================================================================================================
## define paths
# for the application on the whole directory
DATA = '/Users/anne/PycharmProjects/genetic_algorithm/data/preprocessed_data'
OUTPUT = '/Users/anne/PycharmProjects/genetic_algorithm/output_data/output_images'
NCC_DATA = '/Users/anne/PycharmProjects/genetic_algorithm/function_specific_data/NCC_data'
NCC_OUTPUT = '/Users/anne/PycharmProjects/genetic_algorithm/function_specific_data/NCC_output'
NMI_DATA = '/Users/anne/PycharmProjects/genetic_algorithm/function_specific_data/NMI_data'
NMI_OUTPUT = '/Users/anne/PycharmProjects/genetic_algorithm/function_specific_data/NMI_output'
MI_DATA = '/Users/anne/PycharmProjects/genetic_algorithm/function_specific_data/MI_data'
MI_OUTPUT = '/Users/anne/PycharmProjects/genetic_algorithm/function_specific_data/MI_output'
SSD_DATA = '/Users/anne/PycharmProjects/genetic_algorithm/function_specific_data/SSD_data'
SSD_OUTPUT = '/Users/anne/PycharmProjects/genetic_algorithm/function_specific_data/SSD_output'
# -------------------------------------------------------------------------------------------------------------------
# for the application of the genetic algorithm on selected images
ct_image_path = '/Users/anne/PycharmProjects/genetic_algorithm/data/slightly_transformed/p1/ct_image.png'
pet_image_path = '/Users/anne/PycharmProjects/genetic_algorithm/data/slightly_transformed/p1/pet_image.png'

# ===================================================================================================================
## read the images
ct_image = cv2.imread(ct_image_path)
pet_image = cv2.imread(pet_image_path)

# -------------------------------------------------------------------------------------------------------------------
## declare variables
population_size = 50
initial_mutation_rate = 0.01
final_mutation_rate = 0.001
crossover_rate = 0.7
number_selected_individuals = 30
final_number_selected = 10
number_generations = 90
image_dict = load_images(DATA)

#NCC_dict = load_images(NCC_DATA)
#NMI_dict = load_images(NMI_DATA)
#MI_dict = load_images(MI_DATA)
#SSD_dict = load_images(SSD_DATA)

# ===================================================================================================================
## final algorithm

variance_per_image_pair, \
average_fitness_all_generations, \
average_variance_all_generations, \
mutation_rates, \
count_selected_individuals = process_images_and_run_algorithm(image_dict, NCC, population_size,
                                                                   number_selected_individuals, final_number_selected,
                                                                  number_generations, crossover_rate,
                                                                  initial_mutation_rate, final_mutation_rate,
                                                                   tournament_selection, "uniform")

#NMI_average_fitness_all_generations = process_images_and_run_algorithm(NMI_dict, NMI_OUTPUT, NMI, population_size,
#                                                                   number_selected_individuals, number_generations,
#                                                                   crossover_rate, mutation_rate,
#                                                                   selection_type="rankbased", minimize=False)

#MI_average_fitness_all_generations = process_images_and_run_algorithm(MI_dict, MI_OUTPUT, MI, population_size,
#                                                                   number_selected_individuals, number_generations,
#                                                                   crossover_rate, mutation_rate,
#                                                                   selection_type="rankbased", minimize=False)

#SSD_average_fitness_all_generations = process_images_and_run_algorithm(SSD_dict, SSD_OUTPUT, SSD, population_size,
#                                                                   number_selected_individuals, number_generations,
#                                                                   crossover_rate, mutation_rate,
#                                                                   selection_type="rankbased", minimize=True)



#genetic_algorithm_new(ct_image, pet_image,  NCC, population_size, number_selected_individuals, final_number_selected, number_generations,
#                  crossover_rate, initial_mutation_rate, final_mutation_rate, tournament_selection, 'uniform', minimize=False)

# -------------------------------------------------------------------------------------------------------------------
## visualize
#fitness score evolution per patient: line for every patient
plot_patient_fitness_generations(average_fitness_all_generations)
# total fitness score evolution: line for all patients (average)
plot_total_average_fitness_generations(average_fitness_all_generations)

plot_patient_variance_generations(variance_per_image_pair)
plot_total_average_variance_generations(average_variance_all_generations)

plot_mutation_rate(number_generations, mutation_rates)
plot_number_selected_individuals(number_generations, count_selected_individuals)

#plot_patient_fitness_generations(NMI_average_fitness_all_generations)
#plot_total_average_fitness_generations(NMI_average_fitness_all_generations)

#plot_patient_fitness_generations(MI_average_fitness_all_generations)
#plot_total_average_fitness_generations(MI_average_fitness_all_generations)

#plot_patient_fitness_generations(SSD_average_fitness_all_generations)
#plot_total_average_fitness_generations(SSD_average_fitness_all_generations)


# -------------------------------------------------------------------------------------------------------------------
## check single methods if they work
#population = initialize_population(population_size)
#pop_matrix = population[0]
#pop_gray_code = population[2]

#test_fitness_and_select(ct_image, pet_image, NCC, pop_matrix, pop_gray_code, number_selected_individuals,
#                        rankbased_selection, minimize=False)
#adaptive_radiation(ct_image, pet_image, pop_matrix, pop_gray_code, 4, initial_mutation_rate, crossover_rate, NCC,
#                   number_selected_individuals, tournament_selection, minimize=False)