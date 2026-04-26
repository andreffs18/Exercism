def factors(value):
    divisors = []
    divisor = 2
    while True:
        if value == 1:
            break
        elif value % divisor == 0:
            divisors.append(divisor)
            value = value // divisor
            divisor = 2
        else:
            divisor += 1
    return divisors
