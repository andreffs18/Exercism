def abbreviate(words):
    translation = str.maketrans("_-", "  ")
    return "".join(map(lambda word: word[0].upper(), words.translate(translation).split()))
