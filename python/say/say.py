digits = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

tens = {
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

conversions = {
    1_000: 100,
    10_000: 1_000,
    100_000: 1_000,
    1_000_000: 1_000,
    10_000_000: 1_000_000,
    100_000_000: 1_000_000,
    1_000_000_000: 1_000_000,
    10_000_000_000: 1_000_000_000,
    100_000_000_000: 1_000_000_000,
    1_000_000_000_000: 1_000_000_000,
}

magnitude = {
    100: "hundred",
    1_000: "thousand",
    1_000_000: "million",
    1_000_000_000: "billion",
}


def say(number):
    if 0 > number or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number < 10:
        return digits[number]

    if number < 100:
        if number in tens:
            return tens[number]
        elif number < 20:
            return digits[number % 10] + "teen"

        if number % 10 == 0:
            return tens[number]
        else:
            single = number % 10
            return f"{tens[number - single]}-{digits[single]}"

    for max_bound, scale in conversions.items():
        if number < max_bound:
            order = number // scale
            number = number % scale
            return f"{say(order)} {magnitude[scale]} {'' if not number else say(number)}".strip()
