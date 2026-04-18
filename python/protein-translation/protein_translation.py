CODON_TO_AMINO_ACID = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}


def proteins(strand):
    chain = []

    for i in range(len(strand) // 3):
        codon = strand[i * 3 : (i * 3) + 3]
        amino_acid = CODON_TO_AMINO_ACID.get(codon, None)
        if amino_acid == "STOP":
            break
        chain.append(amino_acid)

    return list(filter(None, chain))
