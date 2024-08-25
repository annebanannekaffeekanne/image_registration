## import necessary libraries
import os
import cv2
import numpy as np

# ----------------------------------------------------------------------------------------------
## preprocessing methods
# negative transformation
def negative_transformation(image):
    negative_image = cv2.bitwise_not(image)
    return negative_image

# gauß-filter
def gaussian_blur_filter(image, ksize=(5, 5)):
    blurred_image = cv2.GaussianBlur(image, ksize, 0)
    return blurred_image

# median-filter
def median_filter(image, ksize):
    if ksize % 2 == 0:
        raise ValueError("kernel size must be odd.")
    filtered_image = cv2.medianBlur(image, ksize)
    return filtered_image

# contrast-optimization
def clahe_contrast_optimization(image):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_image = clahe.apply(image)
    return clahe_image

# normalization
def normalize_image(image):
    min_val = np.min(image)
    max_val = np.max(image)
    normalized_image = (image - min_val) / (max_val - min_val) * 255
    return normalized_image.astype(np.uint8)

# resampling (only applied on pet later)
def resampling(image, size=(512, 512)):
    return cv2.resize(image, size, interpolation=cv2.INTER_NEAREST)

# ------------------------------------------------------------------------------------------------
## apply preprocessing methods in a method
# contains all preprocessing methods from above
def preprocess_image(image, is_pet_image=False):
    image = negative_transformation(image)

    if is_pet_image:
        image = resampling(image)

    image = median_filter(image, 5)
    image = gaussian_blur_filter(image)
    image = clahe_contrast_optimization(image)
    image = normalize_image(image)

    return image

