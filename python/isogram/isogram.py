def is_isogram(string: str) -> bool:
    visited_char = []
    for char in string:
        if char in [" ", "-"]:
            continue
        if char.lower() in visited_char:
            return False
        visited_char.append(char.lower())
    return True
