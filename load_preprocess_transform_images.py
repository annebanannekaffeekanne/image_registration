## import necessary libraries
import os
import cv2
import random
import numpy as np
from .transformation_methods import *
from .preprocessing_methods import *

# --------------------------------------------------------------------------------------------------
## load images as dictionaries
def load_images(dir_path):
    images_dict = {}

    # iterate over patients/subdirectories
    for patient_folder in os.listdir(dir_path):
        patient_path = os.path.join(dir_path, patient_folder)

        # ignore non-directories and system files such as DS.store
        if not os.path.isdir(patient_path) or patient_folder.startswith('.'):
            continue

        # Define the expected image filenames
        expected_images = ['ct_image.png', 'pet_image.png']
        images = {img: os.path.join(patient_path, img) for img in expected_images}

        # Check if all expected images are present
        if not all(os.path.exists(img_path) for img_path in images.values()):
            print(f"Error: Missing 'CT' or 'PET' image in patient folder {patient_folder}.")
            continue

        # debug: print which images have been found
        #print(f"Found images in {patient_folder}")

        # read images
        try:
            ct_image = cv2.imread(images['ct_image.png'], cv2.IMREAD_GRAYSCALE)
            pet_image = cv2.imread(images['pet_image.png'], cv2.IMREAD_GRAYSCALE)

            # check if reading of images worked
            if ct_image is None or pet_image is None:
                raise ValueError(f"reading error of image {ct_image_name} or {pet_image_name}.")

            # store images in dictionary
            images_dict[patient_folder] = {'ct': ct_image, 'pet': pet_image}

        # check if reading of a patient folder worked
        except Exception as e:
            print(f"error reading images in patient folder {patient_folder}: {e}")

    print(f"sucessfully loaded all images.")
    print(50 * "_")
    print(" ")
    return images_dict

# ---------------------------------------------------------------------------------------------------
# preprocess the images
def preprocess_images(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    images_dict = load_images(src_dir)

    # iterate over patients/subdirectories
    for patient_folder, images in images_dict.items():
        patient_path = os.path.join(dest_dir, patient_folder)
        if not os.path.exists(patient_path):
            os.makedirs(patient_path)

        pet_image = images['pet']
        ct_image = images['ct']

        try:
            preprocessed_pet_image = preprocess_image(pet_image, is_pet_image=True)

            preprocessed_pet_image_path = os.path.join(patient_path, 'pet_image.png')

            cv2.imwrite(preprocessed_pet_image_path, preprocessed_pet_image)

            preprocessed_ct_image = preprocess_image(ct_image, is_pet_image=False)
            preprocessed_ct_image_path = os.path.join(patient_path, 'ct_image.png')
            cv2.imwrite(preprocessed_ct_image_path, preprocessed_ct_image)

            print(f"preprocessed pet-image and unchanged ct-image for {patient_folder} saved.")
        except Exception as e:
            print(f"error preprocessing images in patient folder {patient_folder}: {e}")
            continue

    print("successfully preprocessed and saved all images.")
    print(50 * "_")
    print(" ")

# -------------------------------------------------------------------------------------------------
# apply artificial transformation on pet image to make it more complex
def transform_images(src_dir, dest_dir, transformations):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    images_dict = load_images(src_dir)

    for patient_folder, images in images_dict.items():
        patient_path = os.path.join(dest_dir, patient_folder)
        if not os.path.exists(patient_path):
            os.makedirs(patient_path)

        pet_image = images['pet']
        ct_image = images['ct']

        try:
            transformed_image = apply_transformations(pet_image, transformations)

            transformed_image_path = os.path.join(patient_path, 'pet_image.png')
            cv2.imwrite(transformed_image_path, transformed_image)

            unchanged_ct_image_path = os.path.join(patient_path, 'ct_image.png')
            cv2.imwrite(unchanged_ct_image_path, ct_image)

            print(f"transformed pet-image and unchanged ct-image for {patient_folder} saved.")
        except Exception as e:
            print(f"error processing images in patient folder {patient_folder}: {e}")
            continue

    print("successfully transformed and saved all images.")
    print(50*"_")
    print(" ")

# -------------------------------------------------------------------------------------------------
# exemplary use of the methods
#transformations = {
#    'translate': (random.randint(-20, 20), random.randint(-20, 20)),
#    'scale': (random.uniform(0.9, 1.5), random.uniform(0.9, 1.5)),
#    'rotate': random.uniform(-30, 30),
#    'shear': (random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5))}

#load_images('/Users/anne/PycharmProjects/genetic_algorithm/data/raw_data')
#preprocess_images('/Users/anne/PycharmProjects/genetic_algorithm/data/raw_data', '/Users/anne/PycharmProjects/genetic_algorithm/data/preprocessed_data')
#transform_images('/Users/anne/PycharmProjects/genetic_algorithm/data/preprocessed_data', '/Users/anne/PycharmProjects/genetic_algorithm/data/transformed_data', transformations)




