import string

VOWELS = {"a", "e", "i", "o", "u"}
CONSONANTS = set(string.ascii_lowercase).difference(VOWELS)


def translate(text: str) -> str:
    # Its a sentence, so we split the words and call the translate function on each one
    if len(text.split()) > 1:
        return " ".join([translate(word) for word in text.split()])

    # 1st rule
    if any([text[0] in VOWELS, text.startswith("xr"), text.startswith("yt")]):
        return text + "ay"

    for i in range(1, len(text)):
        if text[i - 1] not in CONSONANTS:
            break

        # 3rd rule
        if text[i - 1 :].startswith("qu"):
            before, after = text.split("qu")
            return after + before + "quay"

        # 4th rule
        if text[i] == "y":
            before, after = text.split("y")
            return "y" + after + before + "ay"

    # 2nd rule
    if text[0] in CONSONANTS:
        prefix = ""
        for char in text:
            if char not in CONSONANTS:
                break
            prefix += char

        _, after = text.split(prefix)
        return after + prefix + "ay"

    # fallback
    return text
