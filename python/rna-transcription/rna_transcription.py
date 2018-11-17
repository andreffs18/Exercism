def to_rna(dna_strand):
	# Correspondence between DNA and RNA strands
	MAP = {
		"G": "C",
		"C": "G",
		"T": "A",
		"A": "U"
	}
	return "".join(map(lambda n: MAP.get(n), list(dna_strand)))
