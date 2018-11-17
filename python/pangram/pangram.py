from string import ascii_lowercase
def is_pangram(sentence):
    return len(set(ascii_lowercase).difference(set(sentence.lower()))) == 0
