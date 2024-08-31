## import necessary libraries and methods
from data_processing_code.load_preprocess_transform_images import load_images
from visualization_code.visualization_methods import save_images, create_output_dirs, plot_patient_fitness_generations, plot_total_average_fitness_generations
from algorithm_code._2_fitness_functions import NCC, NMI, MI, SSD
from algorithm_code._3_initialize_population import initialize_population
from algorithm_code._5_test_fitness_and_selection import test_fitness_and_select
from algorithm_code._8_genetic_algorithm import genetic_algorithm, process_images_and_run_algorithm
import cv2


# ----------------------------------------------------------------------------------------------------------
## define paths
# for the application on the whole directory
DATA = '/Users/anne/PycharmProjects/genetic_algorithm/data/preprocessed_data'
OUTPUT = '/Users/anne/PycharmProjects/genetic_algorithm/output_data/output_images'

# for the application of the genetic algorithm on selected images
ct_image_path = '/Users/anne/PycharmProjects/genetic_algorithm/data/slightly_transformed/p1/ct_image.png'
pet_image_path = '/Users/anne/PycharmProjects/genetic_algorithm/data/slightly_transformed/p1/pet_image.png'

# ----------------------------------------------------------------------------------------------------------
## declare variables
population_size = 30
mutation_rate = 0.01
crossover_rate = 0.7
number_selected_individuals = population_size // 4
number_generations = 40
image_dict = load_images(DATA)

# ----------------------------------------------------------------------------------------------------------
## read the images
ct_image = cv2.imread(ct_image_path)
pet_image = cv2.imread(pet_image_path)

# ----------------------------------------------------------------------------------------------------------
## final algorithm
average_fitness_all_generations = process_images_and_run_algorithm(image_dict, OUTPUT, NCC, population_size, number_selected_individuals,
                                 number_generations, crossover_rate, mutation_rate, selection_type="rankbased", minimize=False)


#genetic_algorithm(ct_image, pet_image,  NCC, population_size, number_selected_individuals, number_generations, crossover_rate,
#                  mutation_rate, selection_type="rankbased", minimize=False)

# visualize
# fitness score evolution per patient: line for every patient
plot_patient_fitness_generations(average_fitness_all_generations)
# total fitness score evolution: line for all patients (average)
plot_total_average_fitness_generations(average_fitness_all_generations)


#population = initialize_population(population_size=20)
#pop_matrix = population[0]
#pop_gray_code = population[2]

#test_fitness_and_select(ct_image, pet_image, NCC, pop_matrix, pop_gray_code, number_selected_individuals=10, selection_type="roulette", minimize=False)