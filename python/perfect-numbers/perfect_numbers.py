def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    numbers = []
    for i in range(1, number):
        if number % i == 0:
            numbers.append(i)
    if number == sum(numbers):
        return "perfect"
    elif number < sum(numbers):
        return "abundant"
    elif number > sum(numbers):
        return "deficient"
