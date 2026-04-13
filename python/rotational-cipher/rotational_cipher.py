def rotate(text: str, key: int) -> str:
    if 0 > key > 26:
        raise ValueError("Key needs to be between 0 and 26!")

    new_text = []
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            new_text.append(chr((ord(char) - base + key) % 26 + base))
        else:
            new_text.append(char)

    return "".join(new_text)
