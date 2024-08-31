## import necessary libraries
import os
import cv2
import numpy as np
import random
from algorithm_code._1_coding_decoding import transformation_matrix

# --------------------------------------------------------------------------------------------------
## transformation methods haben keine verwendung.. oder?
# scaling
#def scale(image, sx, sy):
#    return cv2.resize(image, None, fx=sx, fy=sy)

# translation
#def translate(image, tx, ty):
#    height, width = image.shape[:2]
    # transformation-Matrix
#    M = np.float32([[1, 0, tx], [0, 1, ty]])
    # warpAffine is the size of the output image which should be as big as the input image
#    return cv2.warpAffine(image, M, (width, height))

# rotation
#def rotate(image, angle):
#    height, width = image.shape[:2]
#    M = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
#    return cv2.warpAffine(image, M, (width, height))

# shearing
#def shear(image, shx, shy):
#    height, width = image.shape[:2]
#    M = np.float32([[1, shx, 0], [shy, 1, 0]])
#    return cv2.warpAffine(image, M, (width, height))

# source: https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html

# --------------------------------------------------------------------------------------------------
## apply the transformations
def random_transformation(image_id):
    tx, ty = random.randint(-20, 20), random.randint(-20, 20)
    sx, sy = random.uniform(0.95, 1.10), random.uniform(0.95, 1.10)
    a = random.uniform(-15, 15)
    shx, shy = random.uniform(-0.01, 0.01), random.uniform(-0.01, 0.01)
    return transformation_matrix(tx, ty, sx, sy, a, shx, shy)


def apply_transformations(image, transformation_matrix):
    height, width = image.shape[:2]
    transformed_image = cv2.warpAffine(image, transformation_matrix[:2], (width, height))

    return transformed_image

