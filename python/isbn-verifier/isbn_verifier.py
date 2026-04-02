from string import ascii_uppercase


def is_valid(isbn: str) -> bool:
    """Verify if a given string is a valid ISBN-10 number.

    ISBN-10 numbers consist of 10 digits where the last digit can also be 'X'
    (representing 10). The validity is determined by calculating a checksum
    where each digit is multiplied by its position (10 for first, 9 for second, etc.)
    and the sum modulo 11 equals 0.

    Args:
        isbn (str): The ISBN string to validate. May contain hyphens which will be ignored.

    Returns:
        bool: True if the ISBN-10 is valid, False otherwise.
    """
    # remove dashes and convert into list of elements
    isbn = list(isbn.replace("-", ""))

    # validation of 10 digit number
    if len(isbn) != 10:
        return False

    # validation of last digit being number or X
    check_char = isbn[-1]
    if check_char in ascii_uppercase:
        if check_char != "X":
            return False
        isbn[-1] = 10

    # validation, every item on isbn must be able to convert to integer
    try:
        isbn = list(map(int, isbn))
    except ValueError:
        return False

    # run factorial multiplication and sum its terms
    isbn = sum(map(lambda x: x[0] * x[1], zip(range(10, 0, -1), isbn)))
    # calculate mod 11
    return isbn % 11 == 0
