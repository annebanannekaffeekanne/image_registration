## import necessary libraries
import numpy as np
import matplotlib as plt

# -----------------------------------------------------------------------------------------------
## auxiliary methods

# normalized histogram/probability for every intensity value of an image
def P_I(_image):
    # density=True normalizes the histogram so the sum of all bins is 1 in total
    # this is basically the probability of every intensity-value
    hist, _ = np.histogram(_image.flatten(), bins=256, range=(0, 256), density=True)
    return hist

# entropy H of an image I
# use one-dimensional histogram-calculation
def H_I(_image):
    p = P_I(_image)
    # constant to avoid log(0)
    H = -np.sum(p * np.log2(p + 1e-10))
    return H

# normalized histogram/probability for the intensity values of two images
def P_I_J(ct_image, pet_image):
    hist_2d, _, _ = np.histogram2d(ct_image.flatten(), pet_image.flatten(), bins=256, range=[[0,256], [0,256]], density=True)
    return hist_2d

# entropy H of two images I & J
# use two-dimensional histogram-calculation
def H_I_J(ct_image, pet_image):
    p = P_I_J(ct_image, pet_image)
    H = -np.sum(p * np.log2(p + 1e-10))
    return H

# mean-intensity of an image
def mu(_image):
    mu = np.mean(_image.flatten())
    return mu

# standard deviation of the pixel intensities
def sigma(_image):
    sigma = np.std(_image.flatten())
    return sigma

# ----------------------------------------------------------------------------------------------
## methods / fitness functions

# mutual information
# to be maximized
def MI(ct_image, pet_image):
    MI = H_I(ct_image) + H_I(pet_image) - H_I_J(ct_image, pet_image)
    #print(f"mutual information: {MI}")
    return MI

# normalized mutual information
# to be maximized
def NMI(ct_image, pet_image):
    NMI = 2 * MI(ct_image, pet_image)/(H_I(ct_image) + H_I(pet_image))
    #print(f"normalized mutual information: {NMI}")
    return NMI

# sum of squared differences
# to be minimized
def SSD(ct_image, pet_image):
    if ct_image.shape == pet_image.shape:
        ct_image = ct_image.astype(np.uint8)
        pet_image = pet_image.astype(np.uint8)

        SD = np.square(ct_image - pet_image)
        SSD = np.sum(SD)
        #print(f"sum of squared differences: {SSD}")
        return SSD
    else:
        raise ValueError("the images are not having the same size.")

# normalized cross correlation
# to be maximized
def NCC(ct_image, pet_image):
    if ct_image.shape == pet_image.shape:
        mu_I, mu_J = mu(ct_image), mu(pet_image)
        sigma_I, sigma_J = sigma(ct_image), sigma(pet_image)
        NCC = np.sum(((ct_image - mu_I) * (pet_image - mu_J))/(ct_image.size * sigma_I * sigma_J))
        #print(f"normalized cross correlation: {NCC}")
        return NCC
    else:
        raise ValueError("the images are not having the same size.")