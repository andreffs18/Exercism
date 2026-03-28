import math
from typing import Optional
from string import digits


def largest_product(series: Optional[str] = None, size: Optional[int] = None) -> int:
    """
    Calculate the largest product for a contiguous substring of digits.

    Given a string of digits, finds the contiguous substring of the specified
    length that produces the largest product when its digits are multiplied together.

    Args:
        series (str): A string containing only digit characters.
        size (int): The length of the substring to consider.

    Returns:
        int: The largest product of a contiguous substring of the specified size.

    Raises:
        ValueError: If the series contains non-digit characters or if the size
                    is larger than the number of digits in the series.
    """
    if not size:
        return 1

    if not series:
        raise ValueError("Series is empty!")

    if set(series) - set(digits):
        raise ValueError("Series should only be contiguous strings of digits!")

    series_size = len(series)
    if 0 > size or size > series_size:
        raise ValueError("Size must be positive and smaller that the total number of elements in a series!")

    computations = []
    for i in range(series_size):
        if i + size > series_size:
            break
        product = math.prod([int(c) for c in series[i : size + i]])
        computations.append(product)
    return max(computations)
