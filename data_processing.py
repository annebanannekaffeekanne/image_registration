## import necessary methods
from algorithm_code._2_fitness_functions import NMI, NCC, MI, SSD
from data_processing_code.process_images import load_images
from data_processing_code.preprocess_transform_images import transform_images, preprocess_images
from data_processing_code.overlay_images import overlay_images
from data_processing_code.preprocessing_methods import preprocess_all_images, NCC_preprocess_image, NMI_preprocess_image, MI_preprocess_image, SSD_preprocess_image, non_specific_preprocess_images
from test_preprocessing import test_fitness
# ===================================================================================================================
# define directories
RAW_DIRECTORY = '/Users/anne/PycharmProjects/genetic_algorithm/data/raw_data'
PRE_PREPROCESSED_DIRECTORY = '/Users/anne/PycharmProjects/genetic_algorithm/data/pre_preprocessed_data'
PREPROCESSED_DIRECTORY = '/Users/anne/PycharmProjects/genetic_algorithm/data/preprocessed_data'
TRANSFORMED_DIRECTORY = '/Users/anne/PycharmProjects/genetic_algorithm/data/transformed_data'
SLIGHTLY_TRANSFORMED = '/Users/anne/PycharmProjects/genetic_algorithm/data/slightly_transformed'
OVERLAY_BEFORE = '/Users/anne/PycharmProjects/genetic_algorithm/data/overlay_before'
NCC_DATA = '/Users/anne/PycharmProjects/genetic_algorithm/function_specific_data/NCC_data'
NMI_DATA = '/Users/anne/PycharmProjects/genetic_algorithm/function_specific_data/NMI_data'
MI_DATA = '/Users/anne/PycharmProjects/genetic_algorithm/function_specific_data/MI_data'
SSD_DATA = '/Users/anne/PycharmProjects/genetic_algorithm/function_specific_data/SSD_data'

# ===================================================================================================================
## apply (pre-)processing methods
# -------------------------------------------------------------------------------------------------------------------
# load
#images_dict = load_images(PRE_PREPROCESSED_DIRECTORY)
#NCC_dict = load_images(NCC_DATA)
#NMI_dict = load_images(NMI_DATA)
#MI_dict = load_images(MI_DATA)
#SSD_dict = load_images(SSD_DATA)

# -------------------------------------------------------------------------------------------------------------------
# preprocess
#preprocess_images(PRE_PREPROCESSED_DIRECTORY, PREPROCESSED_DIRECTORY, preprocess_all_images)
#preprocess_images(PRE_PREPROCESSED_DIRECTORY, NCC_DATA, NCC_preprocess_image)
#preprocess_images(PRE_PREPROCESSED_DIRECTORY, NMI_DATA, NMI_preprocess_image)
#preprocess_images(PRE_PREPROCESSED_DIRECTORY, MI_DATA, MI_preprocess_image)
#preprocess_images(PRE_PREPROCESSED_DIRECTORY, SSD_DATA, SSD_preprocess_image)

# -------------------------------------------------------------------------------------------------------------------
# test fitness
#fitness_functions = [NCC, NMI, MI, SSD]
#optimization_directions = [True, True, True, False]
#test_fitness(images_dict, fitness_functions, NCC_preprocess_image, optimization_directions)
#test_fitness(images_dict, fitness_functions, NMI_preprocess_image, optimization_directions)
#test_fitness(images_dict, fitness_functions, MI_preprocess_image, optimization_directions)
#test_fitness(images_dict, fitness_functions, SSD_preprocess_image, optimization_directions)
#test_fitness(images_dict, fitness_functions, non_specific_preprocess_images, optimization_directions)
# slightly transform
#transform_images(PREPROCESSED_DIRECTORY, SLIGHTLY_TRANSFORMED)

# -------------------------------------------------------------------------------------------------------------------
# overlay
#overlay_images(PREPROCESSED_DIRECTORY, OVERLAY_BEFORE)
