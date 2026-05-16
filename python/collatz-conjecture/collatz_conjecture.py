def steps(number: int, acc: int = 0) -> int:
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return acc

    if number % 2 == 0:
        return steps(number=number / 2, acc=acc + 1)
    else:
        return steps(number=number * 3 + 1, acc=acc + 1)
