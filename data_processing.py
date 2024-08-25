from data_processing_code.load_preprocess_transform_images import *

RAW_DIRECTORY = '/Users/anne/PycharmProjects/genetic_algorithm/data/raw_data'
PREPROCESSED_DIRECTORY = '/Users/anne/PycharmProjects/genetic_algorithm/data/preprocessed_data'
TRANSFORMED_DIRECTORY = '/Users/anne/PycharmProjects/genetic_algorithm/data/transformed_data'


# Define transformations
transformations = {
    'translate': (random.randint(-20, 20), random.randint(-20, 20)),
    'scale': (random.uniform(0.9, 1.5), random.uniform(0.9, 1.5)),
    'rotate': random.uniform(-30, 30),
    'shear': (random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5))
}

## apply methods
# load
images_dict = load_images(RAW_DIRECTORY)

for patient_folder, images in images_dict.items():
    ct_image = images['CT']
    pet_image = images['PET']

# preprocess
preprocess_images(RAW_DIRECTORY, PREPROCESSED_DIRECTORY)

# transformation
transform_images(PREPROCESSED_DIRECTORY, TRANSFORMED_DIRECTORY, transformations)