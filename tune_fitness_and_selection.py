from algorithm_code._2_fitness_functions import NCC, NMI, MI
from algorithm_code._4_selection_methods import tournament_selection, rankbased_selection, roulette_selection, SUS_selection
from algorithm_code._8_genetic_algorithm import genetic_algorithm
from data_processing_code.process_images import load_images

DATA = '/Users/anne/PycharmProjects/genetic_algorithm/data/preprocessed_data'
OUTPUT = '/Users/anne/PycharmProjects/genetic_algorithm/output_data/output_images'

population_size = 50
mutation_rate = 0.01
crossover_rate = 0.7
number_selected_individuals = population_size // 5
number_generations = 50
crossover_method = "two_point"
image_dict = load_images(DATA)


def tune_fitness_and_selection(image_dict, runs):
    fitness_functions = [NCC, NMI, MI]
    selection_methods = [roulette_selection, rankbased_selection, tournament_selection, SUS_selection]

    result = {}
    for fitness_function in fitness_functions:
        # Berechne min und max für die aktuelle Fitnessfunktion
        best_combination = None
        best_score = float('-inf')
        print(f"testing fitness function: {fitness_function.__name__}")

        for patient_folder, images in image_dict.items():
            # define images
            images = image_dict[patient_folder]
            # divide into ct an pet images
            ct_image = images['ct']
            pet_image = images['pet']

            for selection_method in selection_methods:
                print(
                    f"testing combination: {fitness_function.__name__} with {selection_method.__name__} for patient {patient_folder}")

                fitness_scores = []
                for i in range(runs):
                    _, _, _, average_fitness_per_generation = genetic_algorithm(
                        ct_image, pet_image, fitness_function, population_size,
                        number_selected_individuals, number_generations, crossover_rate, mutation_rate,
                        selection_method, crossover_method, minimize=False)

                    final_fitness_value = average_fitness_per_generation[-1]

                    if isinstance(final_fitness_value, (int, float)):
                        fitness_scores.append(final_fitness_value)
                        print(
                            f"fitness value for {fitness_function.__name__} with {selection_method.__name__}: {final_fitness_value}")
                    else:
                        print(f"unexpected data type in av_fitness_per_gen: {type(final_fitness_value)}")

                if fitness_scores:
                    av_score = sum(fitness_scores) / len(fitness_scores)
                    result[(fitness_function.__name__, selection_method.__name__)] = av_score

                    if av_score > best_score:
                        best_score = av_score
                        best_combination = (fitness_function, selection_method)

        print(f"best selection method for {best_combination[0].__name__}: {best_combination[1].__name__} with an average score of {best_score}")

tune_fitness_and_selection(image_dict, 1)

# beste selektionsmethode für jede fitnessfunktion.. nicht die beste fitnessfunktion an sich