def is_armstrong_number(number: int) -> bool:
    """
    An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
    """

    return sum(int(n) ** len(str(number)) for n in str(number)) == number
