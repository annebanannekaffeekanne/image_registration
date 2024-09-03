## import necessary libraries
import numpy as np
import cv2

# ===================================================================================================================
def clamp(value, lower, upper):
    return max(lower, min(value, upper))

# ===================================================================================================================
## create general transformation matrix
def transformation_matrix(tx, ty, sx, sy, a, shx, shy):
    # angle as radian
    a = np.radians(a)
    # translation matrix
    T = np.array([[1, 0, tx],
                  [0, 1, ty],
                  [0, 0, 1]])
    # scaling matrix
    S = np.array([[sx, 0, 0],
                  [0, sy, 0],
                  [0, 0, 1]])
    # rotation matrix
    R = np.array([[np.cos(a), -np.sin(a), 0],
                  [np.sin(a), np.cos(a), 0],
                  [0, 0, 1]])
    # shearing matrix
    SH = np.array([[1, shx, 0],
                   [shy, 1, 0],
                   [0, 0, 1]])

    # transformation matrix: np.dot does matrix-multiplication
    transformation_matrix = np.dot(T, np.dot(S, np.dot(R, SH)))
    #print(transformation_matrix)
    return transformation_matrix

# -------------------------------------------------------------------------------------------------------------------
def apply_transformations(image, transformation_matrix):
    height, width = image.shape[:2]
    transformed_image = cv2.warpAffine(image, transformation_matrix[:2], (width, height))

    return transformed_image


# ===================================================================================================================
## decode float parameter into bitstring and reverse
# decode a float parameter (e.g. tx) into a bitstring
def parameter_to_bitstring(parameter, bits, lower_range_value, upper_range_value):
    parameter = clamp(parameter, lower_range_value, upper_range_value)
    normalized_parameter = (parameter - lower_range_value) / (upper_range_value - lower_range_value)
    int_parameter = int(normalized_parameter * (2 ** bits - 1))

    return '{:0{bits}b}'.format(int_parameter, bits=bits)

# -------------------------------------------------------------------------------------------------------------------
# decode a bitstring into a float parameter
def bitstring_to_parameter(bitstring, bits, lower_range_value, upper_range_value):
    int_value = int(bitstring, 2)
    normalized_parameter = int_value / (2 ** bits - 1)
    parameter = normalized_parameter * (upper_range_value - lower_range_value) + lower_range_value

    return parameter

# -------------------------------------------------------------------------------------------------------------------
## decode a whole individual from float parameter into bitstring and reverse
# apply parameter_to_bitstring and transform every single float-parameter-individual into bitstring
def individual_to_bitstring(tx, ty, sx, sy, a, shx, shy):
    tx_bits = parameter_to_bitstring(tx, 8, -20, 20)
    ty_bits = parameter_to_bitstring(ty, 8, -20, 20)
    sx_bits = parameter_to_bitstring(sx, 8, 0.95, 1.10)
    sy_bits = parameter_to_bitstring(sy, 8, 0.95, 1.10)
    a_bits = parameter_to_bitstring(a, 8, -15, 15)
    shx_bits = parameter_to_bitstring(shx, 8, -0.01, 0.01)
    shy_bits = parameter_to_bitstring(shy, 8, -0.01, 0.01)

    return tx_bits + ty_bits + sx_bits + sy_bits + a_bits + shx_bits + shy_bits

# -------------------------------------------------------------------------------------------------------------------
# apply bitstring_to_parameter and retransform every bitstring-individual into float-parameter
def bitstring_to_individual(bitstring):
    tx = bitstring_to_parameter(bitstring[:8], 8, -20, 20)
    ty = bitstring_to_parameter(bitstring[8:16], 8, -20, 20)
    sx = bitstring_to_parameter(bitstring[16:24], 8, 0.95, 1.10)
    sy = bitstring_to_parameter(bitstring[24:32], 8, 0.95, 1.10)
    a = bitstring_to_parameter(bitstring[32:40], 8, -15, 15)
    shx = bitstring_to_parameter(bitstring[40:48], 8, -0.01, 0.01)
    shy = bitstring_to_parameter(bitstring[48:], 8, -0.01, 0.01)

    return tx, ty, sx, sy, a, shx, shy

# ===================================================================================================================
## transform a binary bitstring into a gray-coded-bitstring and reverse
def binary_to_gray(binary_bitstring):
    if not all(c in '01' for c in binary_bitstring):
        raise ValueError(f"Invalid binary bitstring: {binary_bitstring}")
    gray_code = binary_bitstring[0]
    for i in range(1, len(binary_bitstring)):
        gray_code += str(int(binary_bitstring[i - 1]) ^ int(binary_bitstring[i]))

    return gray_code

# -------------------------------------------------------------------------------------------------------------------
def gray_to_binary(gray_code):
    binary_str = gray_code[0]
    for i in range(1, len(gray_code)):
        binary_str += str(int(binary_str[i - 1]) ^ int(gray_code[i]))

    return binary_str

# ===================================================================================================================
def bitstring_to_matrix(bitstring):
    tx, ty, sx, sy, a, shx, shy = bitstring_to_individual(bitstring)

    return transformation_matrix(tx, ty, sx, sy, a, shx, shy)

# -------------------------------------------------------------------------------------------------------------------
def matrix_to_bitstring(matrix):
    tx = matrix[0, 2]
    ty = matrix[1, 2]

    a = np.arctan2(matrix[1, 0], matrix[0, 0])
    sx = matrix[0, 0] / np.cos(a)
    sy = matrix[1, 1] / np.cos(a)

    shx = matrix[0, 1]
    shy = matrix[1, 0] - np.tan(a) * sx

    a = np.degrees(a)

    tx_bits = parameter_to_bitstring(tx, 8, -20, 20)
    ty_bits = parameter_to_bitstring(ty, 8, -20, 20)
    sx_bits = parameter_to_bitstring(sx, 8, 0.95, 1.10)
    sy_bits = parameter_to_bitstring(sy, 8, 0.95, 1.10)
    a_bits = parameter_to_bitstring(a, 8, -15, 15)
    shx_bits = parameter_to_bitstring(shx, 8, -0.01, 0.01)
    shy_bits = parameter_to_bitstring(shy, 8, -0.01, 0.01)

    bitstring = tx_bits + ty_bits + sx_bits + sy_bits + a_bits + shx_bits + shy_bits
    return bitstring
