import itertools
from algorithm_code._2_fitness_functions import NCC, NMI, MI, SSD
from data_processing_code.preprocessing_methods import *
from data_processing_code.load_preprocess_transform_images import load_images

def find_best_combination(images_dict, fitness_functions):
    pre_processing_methods = [negative_transformation, median_filter, gaussian_blur_filter, clahe_contrast_optimization]

    best_results = {}

    for fitness_function in fitness_functions:
        best_combination = None
        best_average_score = float('-inf')

        for r in range(1, len(pre_processing_methods) + 1):
            for combination in itertools.combinations(pre_processing_methods, r):
            # Erzeuge alle Permutationen der gewählten Kombination
                pre_processing_combinations = itertools.permutations(combination)

                for pre_processing_steps in pre_processing_combinations:
                    total_score = 0
                    count = 0

                    for patient, images in images_dict.items():
                        ct_image = images['ct']
                        pet_image = images['pet']
                        #pet_image = resampling(pet_image, (512, 512))
        # Teste jede Kombination der Vorverarbeitungsmethoden und Fitnessfunktionen
                        processed_ct = ct_image.copy()
                        processed_pet = pet_image.copy()

                        for step in pre_processing_steps:
                # Spezifische Behandlung der cropping-Methode
                            #if step == crop_image:
                            #    processed_ct = step(processed_ct, crop_rect=(80, 40, 350, 310))  # Beispielwerte für cropping
                            #    processed_pet = step(processed_pet, crop_rect=(80, 40, 350, 310))  # Beispielwerte für cropping
                            if step == median_filter:
                                processed_ct = step(processed_ct, ksize=5)  # Beispielwert für ksize
                                processed_pet = step(processed_pet, ksize=5)
                            elif step == gaussian_blur_filter:
                                processed_ct = step(processed_ct, ksize=(5, 5))  # Beispielwerte für ksize und sigma
                                processed_pet = step(processed_pet, ksize=(5, 5))
                            else:
                                processed_ct = step(processed_ct)
                                processed_pet = step(processed_pet)


                        score = fitness_function(processed_ct, processed_pet)
                        total_score += score
                        count += 1

                    average_score = total_score / count

                # Aktualisiere die beste Kombination, wenn ein höherer durchschnittlicher Fitnesswert gefunden wird
                    if average_score > best_average_score:
                        best_average_score = average_score
                        best_combination = {
                            'pre_processing_steps': [step.__name__ for step in pre_processing_steps],
                            'average_score': average_score
                                }
        best_results[fitness_function.__name__] = best_combination

    for fitness_name, result in best_results.items():
        print(f"Beste Vorverarbeitungsreihenfolge für {fitness_name}: {result}")

    return best_results


# Beispielaufruf der Funktion
fitness_functions = [NCC, NMI, MI, SSD]
images_dict = load_images('/Users/anne/PycharmProjects/genetic_algorithm/data/only_crop')
best_combination = find_best_combination(images_dict, fitness_functions)