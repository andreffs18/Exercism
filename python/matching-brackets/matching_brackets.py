def _is_pair(previous_char, next_char):
    return any(
        [
            previous_char == "{" and next_char == "}",
            previous_char == "(" and next_char == ")",
            previous_char == "[" and next_char == "]",
        ]
    )


def _is_open_char(char):
    return char in ["[", "(", "{"]


def _is_close_char(char):
    return char in ["]", ")", "}"]


def _is_special_char(char):
    return _is_open_char(char) or _is_close_char(char)


def is_paired(input_string):
    stack = []
    for char in input_string:
        if not _is_special_char(char):
            continue

        if _is_open_char(char):
            stack.append(char)
            continue

        if _is_close_char(char):
            if len(stack) == 0:
                return False

            prev_char = stack[-1]
            if _is_open_char(prev_char) and _is_pair(prev_char, char):
                stack.pop(-1)
                continue
            else:
                return False

    if len(stack) == 0:
        return True

    return False
