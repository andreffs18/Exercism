def _is_anagram(word, candidate):
    same_word = word == candidate
    return not same_word and sorted(word) == sorted(candidate)


def find_anagrams(word, candidates):
    output = []
    for candidate in candidates:
        if _is_anagram(word.lower(), candidate.lower()):
            output.append(candidate)
    return output
