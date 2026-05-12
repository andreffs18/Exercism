from copy import deepcopy
from typing import List


def _get_value(garden: List[List[int]], x: int, y: int) -> int:
    if x < 0 or x > len(garden) - 1:
        return 0
    if y < 0 or y > len(garden[0]) - 1:
        return 0
    if garden[x][y] == "*":
        return 1
    else:
        return 0


def annotate(garden):
    new_garden = deepcopy(garden)

    # Garden has rows with different sizes
    if len(set(len(row) for row in garden)) > 1:
        raise ValueError("The board is invalid with current input.")

    # Garden has invalid characters
    if set(sum(map(list, garden), [])).difference({"*", " "}):
        raise ValueError("The board is invalid with current input.")

    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if garden[i][j] == " ":
                count = sum(
                    [
                        _get_value(garden, x=i - 1, y=j - 1),
                        _get_value(garden, x=i - 1, y=j),
                        _get_value(garden, x=i - 1, y=j + 1),
                        _get_value(garden, x=i, y=j - 1),
                        _get_value(garden, x=i, y=j + 1),
                        _get_value(garden, x=i + 1, y=j - 1),
                        _get_value(garden, x=i + 1, y=j),
                        _get_value(garden, x=i + 1, y=j + 1),
                    ]
                )

                if count > 0:
                    new_row = list(new_garden[i])
                    new_row[j] = str(count)
                    new_garden[i] = "".join(new_row)
    return new_garden
