BANDS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
TOLERANCE = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}


def resistor_label(colors):
    if len(colors) < 3 or len(colors) > 5:
        return "0 ohms"

    tolerance = TOLERANCE.get(colors[-1])
    multiplier = 10 ** BANDS.index(colors[-2])

    ohms = sum([10**exp * BANDS.index(color) for exp, color in enumerate(list(reversed(colors[:-2])))]) * multiplier

    prefix = ""
    if ohms >= 1_000_000_000:
        ohms /= 1_000_000_000
        prefix = "giga"
    elif ohms >= 1_000_000:
        ohms /= 1_000_000
        prefix = "mega"
    elif ohms >= 1_000:
        ohms /= 1_000
        prefix = "kilo"

    return f"{ohms:g} {prefix}ohms ±{tolerance}%"
