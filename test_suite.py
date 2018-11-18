from functions import *
from constants import *
from atoms import hydrogen1, hydrogen2, oxygen1
import math


def test_magnitude():
    assert magnitude({1, 3, -5}) == math.sqrt(35)


def test_sum_vectors():
    assert sum_vectors([[1, 2, 3], [0, -4, 8]]) == [1, -2, 11]


def test_scale_vector():
    assert scale_vector([1, 4, -3], -2) == [-2, -8, 6]


def test_distance_vector():
    assert distance_vector([1, 4, 3], [0, 1, 1]) == [-1, -3, -2]
    assert distance_vector(hydrogen2, hydrogen1) == [Å, Å, Å]


def test_distance():
    assert distance([1, 2, 3], [3, 2, 1]) == math.sqrt(8)
    assert distance(hydrogen1, oxygen1) == math.sqrt(0.75) * Å
    assert distance(hydrogen1, hydrogen2) == Å * math.sqrt(3)


def test_direction_vector():
    assert direction_vector([1, 1, 1], [7, 5, -3]) == [6 /
                                                       math.sqrt(68), 4 / math.sqrt(68), -4 / math.sqrt(68)]
    m = 1 / math.sqrt(3)
    for component in direction_vector(hydrogen2, hydrogen1):
        assert abs(component - m) < 10 ** (-12)


def test_electric_force():
    m = 4.439972744 * 10 ** (-9)
    for component in electric_force(hydrogen1, hydrogen2):
        assert abs(component - m) < 10 ** (-12)


def test_force_to_acceleration():
    assert force_to_acceleration(
        [4, 3, -1], 5.43) == [4 / 5.43, 3 / 5.43, -1 / 5.43]
