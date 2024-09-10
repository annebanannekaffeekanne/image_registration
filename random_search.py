import numpy as np
import random
#from algorithm_code._8_genetic_algorithm import genetic_algorithm
from algorithm_code._2_fitness_functions import NCC
from algorithm_code._4_selection_methods import tournament_selection, rankbased_selection, SUS_selection, roulette_selection
from algorithm_code.apply_algorithm import process_images_and_run_algorithm_for_tuning
from data_processing_code.process_images import load_images
DATA = '/Users/anne/PycharmProjects/genetic_algorithm/data/less_patients'

param_ranges = {
    'population_size': (20, 70),
    'number_selected_individuals': (5, 40),
    'number_generations': (40, 100),
    'crossover_rate': (0.3, 0.9),
    'mutation_rate': (0.01, 0.1),
    'selection_method': [tournament_selection, rankbased_selection, roulette_selection, SUS_selection],  # Ersetze method1, method2 durch deine tatsächlichen Auswahlmethoden
    'crossover_method': ['uniform', 'two_point', 'single_point'],  # Ersetze method1, method2 durch deine tatsächlichen Kreuzungsmethoden
}
def generate_random_parameters():
    # Definiere die Bereiche der Parameter
    population_size = random.randint(20, 70)
    number_selected_individuals = random.randint(5, 40)
    number_generations = random.randint(40, 100)
    crossover_rate = random.uniform(0.3, 0.9)
    mutation_rate = random.uniform(0.01, 0.1)
    selection_method = random.choice([tournament_selection, rankbased_selection, roulette_selection, SUS_selection])  # Ersetze method1, method2 mit deinen Auswahlmethoden
    crossover_method = random.choice(['uniform', 'two_point', 'single_point'])  # Ersetze method1, method2 mit deinen Crossover-Methoden

    return population_size, number_selected_individuals, number_generations, \
           crossover_rate, mutation_rate, selection_method, crossover_method

def random_search(image_dict, maximizing_fitness_function, num_iterations):
    best_score = float('-inf')
    best_params = None
    best_results = None

    for _ in range(num_iterations):
        # Generiere zufällige Parameter
        params = generate_random_parameters()
        print(f"Testing parameters: {params}")

        # Führe die Bilderverarbeitung und den genetischen Algorithmus aus
        results = process_images_and_run_algorithm_for_tuning(image_dict, maximizing_fitness_function, *params)

        # Hier kannst du anpassen, wie du die Ergebnisse bewerten möchtest
        average_fitness_all_generations = results

        # Bewertung der Ergebnisse (beispielhaft)
        # Zum Beispiel: Nutze den durchschnittlichen Fitnesswert der letzten Generation als Bewertung
        last_gen_fitness = average_fitness_all_generations[-1] if average_fitness_all_generations else []
        avg_last_gen_fitness = np.mean(last_gen_fitness) if last_gen_fitness else 0

        # Überprüfe, ob die aktuelle Konfiguration besser ist
        if avg_last_gen_fitness > best_score:
            best_score = avg_last_gen_fitness
            best_params = params
            best_results = results

    print(f"Best parameters: {best_params}")
    print(f"Best score: {best_score}")

    return best_params, best_results


image_dict = load_images(DATA)

maximizing_fitness_function = NCC  # Ersetze durch deine Fitnessfunktion
num_iterations = 50  # Anzahl der Iterationen für die Random Search

best_params, best_results = random_search(image_dict, maximizing_fitness_function, num_iterations)