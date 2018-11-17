def largest_product(series, size):
	if len(series) < size:
		raise ValueError("Size can't be bigger than series length!")

	if not isinstance(size, int) or size < 0:
		raise ValueError("Size needs to be non-negative integer.")


	# convert series into integers
	series = map(int, series)
	# slice series into slices of length = size
	series = [series[i: i + size] for i in range(len(series) - size + 1)]
	# store max series
	max_series = -1
	for serie in series:
		# multiply all elements
		total = 1
		for s in serie:
			total *= s
		 
		if total > max_series:
			max_series = total
	return max_series