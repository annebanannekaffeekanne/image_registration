# import necessary libraries
from data_processing_code.load_preprocess_transform_images import *
from data_processing_code.preprocessing_methods import *
import cv2

# -------------------------------------------------------------------------------------------------
# define directories
RAW_DIRECTORY = '/Users/anne/PycharmProjects/genetic_algorithm/data/raw_data'
PREPROCESSED_DIRECTORY = '/Users/anne/PycharmProjects/genetic_algorithm/data/preprocessed_data'
TRANSFORMED_DIRECTORY = '/Users/anne/PycharmProjects/genetic_algorithm/data/transformed_data'
SLIGHTLY_TRANSFORMED = '/Users/anne/PycharmProjects/genetic_algorithm/data/slightly_transformed'
OVERLAY_BEFORE = '/Users/anne/PycharmProjects/genetic_algorithm/data/overlay_before'
ONLY_CROP = '/Users/anne/PycharmProjects/genetic_algorithm/data/only_crop'
CROP_NEGTRANSFORM = '/Users/anne/PycharmProjects/genetic_algorithm/data/crop_negtransform'
NCC_DATA = '/Users/anne/PycharmProjects/genetic_algorithm/function_specific_data/NCC_data'
NMI_DATA = '/Users/anne/PycharmProjects/genetic_algorithm/function_specific_data/NMI_data'
MI_DATA = '/Users/anne/PycharmProjects/genetic_algorithm/function_specific_data/MI_data'
SSD_DATA = '/Users/anne/PycharmProjects/genetic_algorithm/function_specific_data/SSD_data'

# -------------------------------------------------------------------------------------------------
## apply preprocessing methods
# load
images_dict = load_images(RAW_DIRECTORY)

# preprocess
#preprocess_images(RAW_DIRECTORY, ONLY_CROP)

#preprocess_images(RAW_DIRECTORY, CROP_NEGTRANSFORM, preprocess_all_images)
preprocess_images(ONLY_CROP, NCC_DATA, NCC_preprocess_image)
preprocess_images(ONLY_CROP, NMI_DATA, NMI_preprocess_image)
preprocess_images(ONLY_CROP, MI_DATA, MI_preprocess_image)
preprocess_images(ONLY_CROP, SSD_DATA, SSD_preprocess_image)

# slightly transform
#transform_images(PREPROCESSED_DIRECTORY, SLIGHTLY_TRANSFORMED)


# transform
#transform_images(PREPROCESSED_DIRECTORY, TRANSFORMED_DIRECTORY)

# overlay
#overlay_images(PREPROCESSED_DIRECTORY, OVERLAY_BEFORE)

# -----------------------------------------------------------------------------------------------
# gradually apply preprocessing methods for visualization of the preprocessing

#ct_image_path = '/Users/anne/PycharmProjects/genetic_algorithm/data/raw_data/p1/ct_image.png'
#pet_image_path = '/Users/anne/PycharmProjects/genetic_algorithm/data/raw_data/p1/pet_image.png'
#output_path = '/Users/anne/PycharmProjects/genetic_algorithm/output_data/preprocess_steps/cropped_pet_image.png'

#ct_image = cv2.imread(ct_image_path)
#pet_image = cv2.imread(pet_image_path)

#pet_image = negative_transformation(pet_image)
#pet_image = resampling(pet_image, size=(512, 512))
#pet_image = median_filter(pet_image, 5)
#pet_image = gaussian_blur_filter(pet_image)
#pet_image = clahe_contrast_optimization(pet_image)
#pet_image = normalize_image(pet_image)
#pet_image = crop_image(pet_image, (80, 40, 350, 310))

#cv2.imwrite(output_path, pet_image)
