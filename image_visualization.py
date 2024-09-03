# import necessary libraries
import os
import cv2
import numpy as np

# ===================================================================================================================
# define path to output-directory und colored images directory
OUTPUT_DIR = '/output_data/output_images'
COLORED_OUTPUT_DIR = '/Users/anne/PycharmProjects/genetic_algorithm/colored_images'

# ===================================================================================================================
# create directory where colored images are saved
def create_colored_dir(base_dir, patient_folder):
    colored_dir = os.path.join(base_dir, patient_folder)
    if not os.path.exists(colored_dir):
        os.makedirs(colored_dir)

    return colored_dir

# -------------------------------------------------------------------------------------------------------------------
# apply colormap on an image
def apply_color_map(image, color_map=cv2.COLORMAP_JET):
    # make sure it's an 8-bit image
    if image.dtype != np.uint8:
        image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    # apply farbmapping
    colored_image = cv2.applyColorMap(image, color_map)

    return colored_image

# ===================================================================================================================
def process_and_save_colored_images(output_dir, colored_output_dir):
    for patient_folder in os.listdir(output_dir):
        patient_path = os.path.join(output_dir, patient_folder)
        colored_patient_dir = create_colored_dir(colored_output_dir, patient_folder)

        images = sorted(os.listdir(patient_path))

        if images:
            # choose last image
            last_image_name = images[-1]
            last_image_path = os.path.join(patient_path, last_image_name)
            image = cv2.imread(last_image_path, cv2.IMREAD_GRAYSCALE)

            colored_image = apply_color_map(image)

            # save the last colored image
            output_image_path = os.path.join(colored_patient_dir, f'colored_{last_image_name}')
            cv2.imwrite(output_image_path, colored_image)
            print(f"colored image saved for {patient_folder}: {output_image_path}")


# apply method
process_and_save_colored_images(OUTPUT_DIR, COLORED_OUTPUT_DIR)
