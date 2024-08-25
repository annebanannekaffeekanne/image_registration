## import necessary libraries
import random
import numpy as np
from ._3_initialize_population import initialize_population
# --------------------------------------------------------------------------------------------------------------
## fitnessproportional selection methods
# roulette selection
def roulette_selection(population_matrix, population_coded, fitness_scores, number_selected_individuals):
    total_fitness = sum(fitness_scores)
    selection_p = [fitness / total_fitness for fitness in fitness_scores]

    selected_indices = random.choices(range(len(population_matrix)), weights=selection_p, k=number_selected_individuals)


    selected_individuals_matrix = [population_matrix[i] for i in selected_indices]
    selected_individuals_bitstrings = [population_coded[i] for i in selected_indices]

    # debug
    #print(f"selected individuals with roulette selection (matrices): {selected_individuals_matrix}")
    #print(f"as gray coded bitstrings: {selected_individuals_bitstrings}")

    return selected_individuals_matrix, selected_individuals_bitstrings


# stochastic universal sampling
def SUS_selection(population_matrix, gray_coded_population, fitness_scores, number_selected_individuals):
    total_fitness = sum(fitness_scores)
    # distance
    d = total_fitness / number_selected_individuals
    starting_point = random.uniform(0, d)
    points = []
    for i in range(number_selected_individuals):
        point = starting_point + i * d
        points.append(point)

    selected_individuals = []
    sum_fitness = 0
    i = 0

    for point in points:
        while sum_fitness < point:
            sum_fitness += fitness_scores[i]
            i += 1
        selected_individuals.append(i-1)
    selected_individuals_matrix = [population_matrix[i] for i in selected_individuals]
    selected_individuals_bitstrings = [gray_coded_population[i] for i in selected_individuals]

    # debug
    #print(f"selected individuals with SUS-selection (matrices): {selected_individuals_matrix}")
    #print(f"as gray coded bitstrings: {selected_individuals_bitstrings}")

    return selected_individuals_matrix, selected_individuals_bitstrings


# ------------------------------------------------------------------------------------------------------------
## rankbased selection methods
def rankbased_selection(population_matrix, gray_coded_population, fitness_scores, number_selected_individuals):
    sorted_fitness_scores = np.argsort(fitness_scores)
    sorted_population = [population_matrix[i] for i in sorted_fitness_scores]
    sorted_coded_population = [gray_coded_population[i] for i in sorted_fitness_scores]

    ranks = np.arange(1, len(sorted_population) + 1)
    selection_p = ranks / ranks.sum()

    chosen_fitness_scores = np.random.choice(len(sorted_population), size=number_selected_individuals, p=selection_p)
    selected_individuals_matrix = [sorted_population[i] for i in chosen_fitness_scores]
    selected_individuals_bitstrings = [sorted_coded_population[i] for i in chosen_fitness_scores]

    # debug
    #print(f"selected individuals with rank-based selection (matrices): {selected_individuals_matrix}")
    #print(f"as gray coded bitstrings: {selected_individuals_bitstrings}")

    return selected_individuals_matrix, selected_individuals_bitstrings


# ------------------------------------------------------------------------------------------------------------
## tournament selection method
def tournament_selection(population_matrix, gray_coded_population, fitness_scores, number_selected_individuals, tournament_size=3):
    selected_individuals = []
    for i in range(number_selected_individuals):
        tournament = random.sample(range(len(population_matrix)), tournament_size)
        winner = max(tournament, key=lambda i: fitness_scores[i])
        selected_individuals.append(winner)

    selected_individuals_matrix = [population_matrix[i] for i in selected_individuals]
    selected_individuals_bitstrings = [gray_coded_population[i] for i in selected_individuals]

    # debug
    #print(f"selected individuals with tournament selection (matrices): {selected_individuals_matrix}")
    #print(f"as gray coded bitstrings: {selected_individuals_bitstrings}")

    return selected_individuals_matrix, selected_individuals_bitstrings


