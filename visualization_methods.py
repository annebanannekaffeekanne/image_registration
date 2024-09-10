# import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# ===================================================================================================================
# create a lineplot for every patient
def plot_patient_fitness_generations(average_fitness_all_generations):
    # create empty dataframe
    data = {
        "generation": [],
        "fitness": [],
        "patient": []
    }
    # fill datafram thourough iterating over the generations and patients
    for generation, fitness_list in enumerate(average_fitness_all_generations):
        for patient_idx, fitness in enumerate(fitness_list):
            data["generation"].append(generation + 1)
            data["fitness"].append(fitness)
            data["patient"].append(f"patient {patient_idx + 1}")

    df = pd.DataFrame(data)

    # create plot
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="generation", y="fitness", hue="patient", data=df, palette="tab20", marker="o")
    plt.title("fitness score evolution of all patients over the generations")
    plt.xlabel("generation")
    plt.ylabel("average fitness")
    plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# -------------------------------------------------------------------------------------------------------------------
# create a lineplot of average fitness of all patients
def plot_total_average_fitness_generations(average_fitness_all_generations):
    # number of patients
    num_patients = len(average_fitness_all_generations[0])

    # calcualte average fitness per generation
    average_fitness_per_generation = [
        sum(fitness_list) / num_patients for fitness_list in average_fitness_all_generations
]

    # create dataframe
    df = pd.DataFrame({
        "generation": range(1, len(average_fitness_per_generation) + 1),
        "average fitness": average_fitness_per_generation
    })

    # create plot
    plt.figure(figsize=(10, 6))
    sns.lineplot(x="generation", y="average fitness", data=df, marker="o")
    plt.title("average fitness of all patients over the generations")
    plt.xlabel("generation")
    plt.ylabel("average fitness")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ===================================================================================================================
def plot_patient_variance_generations(variance_per_image_pair):
    # create empty dataframe
    data = {
        "generation": [],
        "variance": [],
        "patient": []
    }

    # fill dataframe by iterating over the generations and patients
    for patient, variances in variance_per_image_pair.items():
        for generation, variance in enumerate(variances):
            data["generation"].append(generation + 1)
            data["variance"].append(np.mean(variance))  # Assuming variance is a list per generation
            data["patient"].append(patient)

    df = pd.DataFrame(data)
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="generation", y="variance", hue="patient", data=df, palette="tab20", marker="o")
    plt.title("variance evolution of transformation parameters for each patient over the generations")
    plt.xlabel("generation")
    plt.ylabel("average variance")
    plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# -------------------------------------------------------------------------------------------------------------------
def plot_total_average_variance_generations(average_variance_all_generations):
    # calculate the average variance per generation across all patients
    overall_avg_variance_per_generation = [np.mean(variance) for variance in average_variance_all_generations]

    # create dataframe
    df = pd.DataFrame({
        "generation": range(1, len(overall_avg_variance_per_generation) + 1),
        "average variance": overall_avg_variance_per_generation
    })

    # create plot
    plt.figure(figsize=(10, 6))
    sns.lineplot(x="generation", y="average variance", data=df, marker="o")
    plt.title("average variance of transformation parameters across all patients over the generations")
    plt.xlabel("generation")
    plt.ylabel("average variance")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ===================================================================================================================
def plot_mutation_rate(number_generations, mutation_rates):
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, number_generations + 1), mutation_rates, marker='o', linestyle='-')
    plt.title('evolution of the mutation rate over the generations')
    plt.xlabel('generation')
    plt.ylabel('mutation rate')
    plt.grid(True)
    plt.show()

# ===================================================================================================================
def plot_number_selected_individuals(number_generations, count_selected_individuals):
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, number_generations + 1), count_selected_individuals, marker='s', linestyle='-')
    plt.title('evolution of the number of selected individuals over the generations')
    plt.xlabel('generation')
    plt.ylabel('number of selected individuals')
    plt.grid(True)
    plt.show()
