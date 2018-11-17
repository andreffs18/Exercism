def distance(strand_a, strand_b):
	if len(strand_a) != len(strand_b):
		raise ValueError("Both strands must have the same length")

	return len(list(filter(lambda s: s[0] != s[1], zip(strand_a, strand_b))))
