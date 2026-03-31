from math import pow


def square_of_sum(count: int) -> float:
    """
    Calculate the square of the sum of natural numbers from 1 to count.

    Computes (1 + 2 + ... + count)^2

    Args:
        count (int): The upper limit of the range (inclusive).

    Returns:
        float: The square of the sum of natural numbers from 1 to count.
    """
    return pow(sum(range(1, count + 1)), 2)


def sum_of_squares(count: int) -> float:
    """
    Calculate the sum of squares of natural numbers from 1 to count.

    Computes 1^2 + 2^2 + ... + count^2

    Args:
        count (int): The upper limit of the range (inclusive).
    """
    return sum(map(lambda c: pow(c, 2), range(1, count + 1)))


def difference_of_squares(count: int) -> float:
    """Calculate the difference between the square of sum and sum of squares.

    Computes the difference between (1 + 2 + ... + count)^2 and (1^2 + 2^2 + ... + count^2).

    Args:
        count (int): The upper limit of the range (inclusive).

    Returns:
        float: The difference between square of sum and sum of squares.
    """
    return square_of_sum(count) - sum_of_squares(count)
