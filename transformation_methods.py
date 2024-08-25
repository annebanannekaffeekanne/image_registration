## import necessary libraries
import os
import cv2
import numpy as np
import random

# --------------------------------------------------------------------------------------------------
## transformation methods
# scaling
def scale(image, sx, sy):
    return cv2.resize(image, None, fx=sx, fy=sy)

# translation
def translate(image, tx, ty):
    height, width = image.shape[:2]
    # transformation-Matrix
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    # warpAffine is the size of the output image which should be as big as the input image
    return cv2.warpAffine(image, M, (width, height))

# rotation
def rotate(image, angle):
    height, width = image.shape[:2]
    M = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
    return cv2.warpAffine(image, M, (width, height))

# shearing
def shear(image, shx, shy):
    height, width = image.shape[:2]
    M = np.float32([[1, shx, 0], [shy, 1, 0]])
    return cv2.warpAffine(image, M, (width, height))

# source: https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html

# --------------------------------------------------------------------------------------------------
## apply the transformations
def apply_transformations(image, transformation_matrix):
    height, width = image.shape[:2]
    transformed_image = cv2.warpAffine(image, transformation_matrix[:2], (width, height))

    return transformed_image



    #[tx, ty, sx, sy, angle, shx, shy] = individual

    #if tx is not None and ty is not None:
    #    image = translate(image, tx, ty)

    #if sx is not None and sy is not None:
    #    image = scale(image, sx, sy)

    #if angle is not None:
    #    image = rotate(image, angle)

    #if shx is not None and shy is not None:
    #    image = shear(image, shx, shy)

    #return image

#def apply_transformations(image, transformations):
#    # Prüfe, ob die Transformationen korrekt interpretiert werden
#    print(f"Transformations: {transformations}")

#    if 'translate' in transformations:
#        tx, ty = transformations['translate']
#        image = translate(image, tx, ty)
#    if 'scale' in transformations:
#        sx, sy = transformations['scale']
#        image = scale(image, sx, sy)
#    if 'rotate' in transformations:
#        angle = transformations['rotate']
#        image = rotate(image, angle)
#    if 'shear' in transformations:
#        shx, shy = transformations['shear']
#        image = shear(image, shx, shy)
#    return image



