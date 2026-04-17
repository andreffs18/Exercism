BANDS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors):
    return int("".join([str(BANDS.index(c)) for c in colors[:2]]))
