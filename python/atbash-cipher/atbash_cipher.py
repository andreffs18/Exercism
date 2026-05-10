import string


def encode(plain_text):
    encoded_text = ""

    alphabet = string.ascii_lowercase
    cypher = list(reversed(string.ascii_lowercase))

    for char in plain_text.lower():
        if char in alphabet:
            index = alphabet.index(char)
            new_char = cypher[index]
            encoded_text += new_char
        if char in string.digits:
            encoded_text += char

    return " ".join([encoded_text[i : i + 5] for i in range(0, len(encoded_text), 5)])


def decode(ciphered_text):
    encoded_text = ""

    alphabet = list(reversed(string.ascii_lowercase))
    cypher = string.ascii_lowercase

    for char in ciphered_text.lower():
        if char in alphabet:
            index = alphabet.index(char)
            new_char = cypher[index]
            encoded_text += new_char
        if char in string.digits:
            encoded_text += char

    return encoded_text
