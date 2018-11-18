import math

from constants import k


def magnitude(vector):
    magnitude = 0
    for coordinate in vector:
        magnitude += (coordinate ** 2)
    return math.sqrt(magnitude)


def sum_vectors(vectors):
    resultant_vector = [0, 0, 0]
    for vector in vectors:
        i = 0
        while i < len(vector):
            resultant_vector[i] += vector[i]
            i += 1
    return resultant_vector


def scale_vector(vector, scalefactor):
    scaled_vector = vector
    i = 0
    while i < len(vector):
        vector[i] *= scalefactor
        i += 1
    return scaled_vector


def distance_vector(point1, point2):
    if type(point1) is list and type(point2) is list:
        pos1 = point1
        pos2 = point2
    elif type(point1) is dict and type(point2) is dict:
        pos1 = point1['position']
        pos2 = point2['position']
    vector = []
    i = 0
    while i < len(pos1):
        vector.append(pos2[i] - pos1[i])
        i += 1
    return vector


def distance(point1, point2):
    return magnitude(distance_vector(point1, point2))


def direction_vector(point1, point2):
    vector = distance_vector(point1, point2)
    length = magnitude(vector)
    return scale_vector(vector, 1 / length)


def electric_force(obj1, obj2):
    length = k * obj1['charge'] * \
        obj2['charge'] / ((distance(obj1, obj2)) ** 2)
    force_vector = scale_vector(direction_vector(obj2, obj1), length)
    return force_vector


def force_to_acceleration(force, mass):
    scalefactor = 1 / mass
    return scale_vector(force, scalefactor)
