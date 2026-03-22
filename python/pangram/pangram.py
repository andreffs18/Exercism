from string import ascii_lowercase


def is_pangram(sentence: str) -> bool:
    """Check if a sentence is a pangram (contains all 26 letters of the alphabet).

    Args:
        sentence (str): The sentence to check for pangram status.

    Returns:
        bool: True if the sentence contains all letters of the alphabet, False otherwise.
    """
    return len(set(ascii_lowercase).difference(set(sentence.lower()))) == 0
