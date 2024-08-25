# import necessary libraries
import os
import cv2

# -----------------------------------------------------------------------------------------
def create_output_dirs(base_dir, patient_folder):
    patient_dir = os.path.join(base_dir, patient_folder)
    if not os.path.exists(patient_dir):
        os.makedirs(patient_dir)

    return patient_dir

# -----------------------------------------------------------------------------------------
def save_images(patient_dir, transformed_image, generation_count):
    output_path = os.path.join(patient_dir, f'registered_image_gen_{generation_count}.png')
    cv2.imwrite(output_path, transformed_image)




