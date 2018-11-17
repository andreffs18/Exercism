from string import ascii_uppercase


def verify(isbn):
	# remove dashes and convert into list of elements
	isbn = list(isbn.replace("-", ""))

	# validation of 10 digit number
	if len(isbn) != 10:
		return False

	# validation of last digit being number or X
	check_char = isbn[-1]
	if check_char in ascii_uppercase:
		if check_char is not "X":
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
	