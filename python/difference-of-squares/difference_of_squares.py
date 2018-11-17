from math import pow

def square_of_sum(count):
    return pow(sum(range(1, count + 1)), 2)


def sum_of_squares(count):
	return sum(map(lambda c: pow(c, 2), range(1, count + 1)))


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
