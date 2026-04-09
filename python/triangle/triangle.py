from typing import List, Union
from collections import Counter


def _is_triangle(sides: List[Union[float, int]]) -> bool:
    """
    For a shape to be a triangle at all,
    * all sides have to be of length > 0, and
    * the sum of the lengths of any two sides must be greater than or equal to the length of the third side.
    """
    valid_lengths = []
    for i in range(len(sides)):
        a = sides[i % len(sides)]
        b = sides[(i + 1) % len(sides)]
        c = sides[(i + 2) % len(sides)]
        valid_lengths.append(a + b >= c)

    return all(map(lambda s: s > 0, sides)) and all(valid_lengths)


def equilateral(sides: List[Union[float, int]]) -> bool:
    """
    An equilateral triangle has all three sides the same length.
    """
    if not _is_triangle(sides):
        return False

    return all(map(lambda s: s == sides[0], sides))


def isosceles(sides: List[Union[float, int]]) -> bool:
    """
    An isosceles triangle has at least two sides the same length.
    (It is sometimes specified as having exactly two sides the same length,
    but for the purposes of this exercise we'll say at least two.)
    """
    if not _is_triangle(sides):
        return False

    same_sides = []
    for i in range(len(sides)):
        for j in range(len(sides)):
            if i != j:
                same_sides.append((sides[i] == sides[j]))

    return Counter(same_sides).get(True, 0) >= 2


def scalene(sides: List[Union[float, int]]) -> bool:
    """
    A scalene triangle has all sides of different lengths.
    """
    if not _is_triangle(sides):
        return False

    return len(set(sides)) == len(sides)
