## import necessary libraries
import cv2
import numpy as np

# ===================================================================================================================
## preprocessing methods
# negative transformation
def negative_transformation(image):
    negative_image = cv2.bitwise_not(image)
    return negative_image

# -------------------------------------------------------------------------------------------------------------------
# gauß-filter
def gaussian_blur_filter(image, ksize=(5, 5)):
    blurred_image = cv2.GaussianBlur(image, ksize, 0)
    return blurred_image

# -------------------------------------------------------------------------------------------------------------------
# median-filter
def median_filter(image, ksize):
    if ksize % 2 == 0:
        raise ValueError("kernel size must be odd.")
    filtered_image = cv2.medianBlur(image, ksize)
    return filtered_image

# -------------------------------------------------------------------------------------------------------------------
# contrast-optimization
def clahe_contrast_optimization(image):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_image = clahe.apply(image)
    return clahe_image

# -------------------------------------------------------------------------------------------------------------------
# normalization
def normalize_image(image):
    min_val = np.min(image)
    max_val = np.max(image)
    normalized_image = (image - min_val) / (max_val - min_val) * 255
    return normalized_image.astype(np.uint8)

# -------------------------------------------------------------------------------------------------------------------
# resampling (only applied on pet later)
def resampling(image, size=(512, 512)):
    return cv2.resize(image, size, interpolation=cv2.INTER_NEAREST)

# -------------------------------------------------------------------------------------------------------------------
# crop
def crop_image(image, crop_rect):
    x, y, w, h = crop_rect
    cropped_image = image[y:y+h, x:x+w]
    return cropped_image

# ===================================================================================================================
## apply preprocessing methods in a method
# contains all preprocessing methods from above
def preprocess_images(image):
    if is_pet_image:
        image = resampling(image)
    image = crop_image(image, (80, 40, 350, 310))
    image = gaussian_blur_filter(image)
    image = median_filter(image, 5)
    image = clahe_contrast_optimization(image)
    image = negative_transformation(image)
    image = normalize_image(image)
    return image

def preprocess_all_images(image, is_pet_image=False):
    if is_pet_image:
        image = resampling(image)
    image = crop_image(image, (80, 40, 350, 310))
    return image

def non_specific_preprocess_images(image):
    image = gaussian_blur_filter(image)
    image = median_filter(image, 5)
    image = clahe_contrast_optimization(image)
    image = negative_transformation(image)
    image = normalize_image(image)
    return image

# ===================================================================================================================
## fitness function specific preprocessing
# NCC
def NCC_preprocess_image(image, is_pet_image=False):
    image = gaussian_blur_filter(image)
    image = median_filter(image, 5)
    image = clahe_contrast_optimization(image)
    image = negative_transformation(image)
    return image

# -------------------------------------------------------------------------------------------------------------------
# NMI
def NMI_preprocess_image(image, is_pet_image=False):
    image = gaussian_blur_filter(image)
    image = normalize_image(image)
    image = clahe_contrast_optimization(image)
    image = negative_transformation(image)
    image = median_filter(image, 5)
    return image

# -------------------------------------------------------------------------------------------------------------------
# MI
def MI_preprocess_image(image, is_pet_image=False):
    image = gaussian_blur_filter(image)
    image = normalize_image(image)
    image = clahe_contrast_optimization(image)
    image = negative_transformation(image)
    image = median_filter(image, 5)
    return image

# -------------------------------------------------------------------------------------------------------------------
# SSD
def SSD_preprocess_image(image, is_pet_image=False):
    image = median_filter(image, 5)
    image = gaussian_blur_filter(image)
    return image









