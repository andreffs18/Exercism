def square_root(number):
    # Brute force
    for i in range(1000):
        if i * i == number:
            return i

    return None
