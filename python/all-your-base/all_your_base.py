def rebase(input_base: int, digits: list, output_base: int):
    """
    Convert a sequence of digits in one base, representing a number, into a sequence of digits in another base, representing the same number.
    """
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    # another example for input.
    if any(map(lambda d: d < 0 or d >= input_base, digits)):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    in_base_10 = 0
    while digits:
        power = len(digits) - 1
        leading_digit = digits[0]
        in_base_10 += leading_digit * (input_base**power)
        digits = digits[1:]

    digits_in_new_base = []
    while True:
        division = in_base_10 // output_base
        remainder = in_base_10 % output_base

        digits_in_new_base.insert(0, remainder)

        if division == 0:
            break

        in_base_10 = division

    return digits_in_new_base
