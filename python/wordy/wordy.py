OPERATIONS = [
    ("plus", "+"),
    ("minus", "-"),
    ("divided by", "/"),
    ("multiplied by", "*"),
]


def is_number(parts, x):
    return parts[x].isnumeric() or parts[x][0] == "-" and parts[x][1:].isnumeric()


def answer(question):
    if not question.startswith("What is") and not question.endswith("?"):
        raise ValueError("syntax error")

    question = question[7:-1].strip()
    if not question:
        raise ValueError("syntax error")

    for op in OPERATIONS:
        question = question.replace(*op)
    if any([char.isalpha() for char in question]):
        raise ValueError("unknown operation")

    parts = question.split()
    if len(parts) == 2:
        raise ValueError("syntax error")
    for i in range(len(parts) - 1):
        # Two consecutive numbers or operations are invalid
        if is_number(parts, i) and is_number(parts, i + 1):
            raise ValueError("syntax error")
        if not is_number(parts, i) and not is_number(parts, i + 1):
            raise ValueError("syntax error")

    # Finally add ordering
    parts.insert(0, "(")
    parts.insert(4, ")")
    return eval("".join(parts))
