from ._6_crossover_mutation import mutation_
from ._5_test_fitness_and_selection import test_fitness_and_select
import random
from ._1_coding_decoding import matrix_to_bitstring, binary_to_gray
import numpy as np

def adaptive_radiation(ct_image, pet_image, population_matrix, gray_coded_population, number_of_niches,
                       initial_mutation_rate, crossover_rate, maximizing_fitness_function, number_selected_individuals,
                       selection_method, minimize=False):
    niche_populations = []

    # Schritt 1: Erstelle Nischen
    niche_size = len(population_matrix) // number_of_niches
    for _ in range(number_of_niches):
        # Zufällig Teile der Population auswählen, um Nischen zu erstellen
        niche_population = random.sample(list(population_matrix), niche_size)
        niche_populations.append(niche_population)

    # Schritt 2: Diversifiziere die Nischen
    diversified_populations = []
    for niche_population in niche_populations:
        diversified_niche = []
        for individual in niche_population:
            mutated_individual = mutation_(np.array(individual), initial_mutation_rate)
            diversified_niche.append(mutated_individual)
        diversified_populations.append(diversified_niche)

    # Schritt 3: Bewerte die Nischen und wähle die besten Individuen
    best_individuals_matrices = []
    best_individuals_bitstrings = []

    for niche_population in diversified_populations:
        niche_bitstring_population = [matrix_to_bitstring(individual) for individual in niche_population]
        niche_gray_coded_population = [binary_to_gray(bitstring) for bitstring in niche_bitstring_population]

        # Fitness-Test und Selektion der besten Individuen in der Nische
        fitness_values, best_individuals_matrix, best_coded_individuals = test_fitness_and_select(
            ct_image, pet_image, maximizing_fitness_function, niche_population, niche_gray_coded_population,
            number_selected_individuals, selection_method, minimize
        )

        # Beste Individuen sammeln
        best_individuals_matrices.extend(best_individuals_matrix)
        best_individuals_bitstrings.extend(best_coded_individuals)

    # Schritt 4: Mischen der besten Individuen aus allen Nischen
    mixed_individuals = mix_niche_individuals(list(zip(best_individuals_matrices, best_individuals_bitstrings)))

    # Überprüfen der Form und sicherstellen, dass sie mit `number_selected_individuals` übereinstimmt
    mixed_individuals_matrices = [matrix for matrix, _ in mixed_individuals][:number_selected_individuals]
    mixed_coded_population = [bitstring for _, bitstring in mixed_individuals][:number_selected_individuals]

    return mixed_individuals_matrices, mixed_coded_population

def mix_niche_individuals(individuals_list):
    # Mische die besten Individuen aus den Nischen
    random.shuffle(individuals_list)  # Zufällige Mischung
    return individuals_list
