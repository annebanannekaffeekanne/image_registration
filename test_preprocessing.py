## import necessary libraries and methods
import itertools
from algorithm_code._2_fitness_functions import NCC, NMI, MI, SSD
from data_processing_code.preprocessing_methods import clahe_contrast_optimization, median_filter, gaussian_blur_filter, normalize_image, negative_transformation
from data_processing_code.process_images import load_images
import math

# ===================================================================================================================
def find_best_combination(images_dict, fitness_functions, optimization_directions):
    pre_processing_methods = [negative_transformation,
                              median_filter,
                              gaussian_blur_filter,
                              normalize_image,
                              clahe_contrast_optimization]
    best_results = {}

    for fitness_function, optimize_for_max in zip(fitness_functions, optimization_directions):
        best_combination = None
        best_average_score = float('-inf') if optimize_for_max else float('inf')

        for r in range(1, len(pre_processing_methods) + 1):
            for combination in itertools.combinations(pre_processing_methods, r):
                pre_processing_combinations = itertools.permutations(combination)

                for pre_processing_steps in pre_processing_combinations:
                    total_score = 0
                    count = 0

                    for patient, images in images_dict.items():
                        ct_image = images['ct']
                        pet_image = images['pet']

                        processed_ct = ct_image.copy()
                        processed_pet = pet_image.copy()

                        for step in pre_processing_steps:
                            if step == median_filter:
                                processed_ct = step(processed_ct, ksize=5)
                                processed_pet = step(processed_pet, ksize=5)
                            elif step == gaussian_blur_filter:
                                processed_ct = step(processed_ct, ksize=(5, 5))
                                processed_pet = step(processed_pet, ksize=(5, 5))
                            else:
                                processed_ct = step(processed_ct)
                                processed_pet = step(processed_pet)

                        score = fitness_function(processed_ct, processed_pet)
                        total_score += score
                        count += 1

                    average_score = total_score / (count + 1.99*math.e**-18)

                    if (optimize_for_max and average_score > best_average_score) or (
                            not optimize_for_max and average_score < best_average_score):
                        best_average_score = average_score
                        best_combination = {
                            'pre_processing_steps': [step.__name__ for step in pre_processing_steps],
                            'average_score': average_score
                        }

        best_results[fitness_function.__name__] = best_combination

                    # Print the best preprocessing sequence for each fitness function
    for fitness_name, result in best_results.items():
        print(f"Best preprocessing sequence for {fitness_name}: {result}")
    return best_results

# ===================================================================================================================
def test_fitness(images_dict, fitness_functions, preprocessing_function, optimization_directions):
    best_results = {}
    for fitness_function, optimize_for_max in zip(fitness_functions, optimization_directions):
        total_score = 0
        count = 0

        best_average_score = float('-inf') if optimize_for_max else float('inf')

        for patient, images in images_dict.items():
            ct_image = images['ct']
            pet_image = images['pet']

            pre_processing_ct = preprocessing_function(ct_image)
            pre_processing_pet = preprocessing_function(pet_image)

            score = fitness_function(pre_processing_ct, pre_processing_pet)
            total_score += score
            count += 1

        average_score = total_score / (count + 1.99*math.e**-18)

        if (optimize_for_max and average_score > best_average_score) or (
                not optimize_for_max and average_score < best_average_score):
            best_average_score = average_score

        print(f"Average score for {fitness_function.__name__}: {best_average_score}")
        best_results[fitness_function.__name__] = best_average_score
    print(50*'_')
    return best_results

# exemplary apply of the methods
#fitness_functions = [NCC, NMI, MI, SSD]
#optimization_directions = [True, True, True, False]
#image_path = '/Users/anne/PycharmProjects/genetic_algorithm/data/pre_preprocessed_data'
#images_dict = load_images(image_path)
#best_combination = find_best_combination(images_dict, fitness_functions, optimization_directions)
#test_fitness(images_dict, fitness_functions, non_specific_preprocess_images)