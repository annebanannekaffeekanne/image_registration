import os
import cv2
import numpy as np

# Definiere den Pfad zum Output-Verzeichnis und zum Verzeichnis für eingefärbte Bilder
OUTPUT_DIR = '/output_data/output_images'
COLORED_OUTPUT_DIR = '/Users/anne/PycharmProjects/genetic_algorithm/colored_images'


def create_colored_dir(base_dir, patient_folder):
    colored_dir = os.path.join(base_dir, patient_folder)
    if not os.path.exists(colored_dir):
        os.makedirs(colored_dir)

    return colored_dir


def apply_color_map(image, color_map=cv2.COLORMAP_JET):
    # Konvertiere das Bild zu einem 8-Bit-Bild, falls es das nicht ist
    if image.dtype != np.uint8:
        image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    # Wende das Farbmapping an
    colored_image = cv2.applyColorMap(image, color_map)

    return colored_image


def process_and_save_colored_images(output_dir, colored_output_dir):
    for patient_folder in os.listdir(output_dir):
        patient_path = os.path.join(output_dir, patient_folder)
        colored_patient_dir = create_colored_dir(colored_output_dir, patient_folder)

        # Liste aller Dateien im Patientenordner
        images = sorted(os.listdir(patient_path))

        if images:
            # Wähle das letzte Bild aus
            last_image_name = images[-1]
            last_image_path = os.path.join(patient_path, last_image_name)
            image = cv2.imread(last_image_path, cv2.IMREAD_GRAYSCALE)

            colored_image = apply_color_map(image)

            # Speichere das eingefärbte letzte Bild
            output_image_path = os.path.join(colored_patient_dir, f'colored_{last_image_name}')
            cv2.imwrite(output_image_path, colored_image)
            print(f"Colored image saved for {patient_folder}: {output_image_path}")


# Führt das Einfärben der Bilder durch
process_and_save_colored_images(OUTPUT_DIR, COLORED_OUTPUT_DIR)
