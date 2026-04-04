from collections import Counter


def full_house(values):
    counter = Counter(values)
    if sorted(dict(counter).values()) == [2, 3]:
        return sum([k * v for k, v in counter.items()])
    return 0


def for_of_a_kind(values):
    counter = Counter(values)
    for k, v in counter.items():
        if v >= 4:
            return k * 4
    return 0


# Score categories
def ONES(values):
    return len(list(filter(lambda v: v == 1, values))) * 1


def TWOS(values):
    return len(list(filter(lambda v: v == 2, values))) * 2


def THREES(values):
    return len(list(filter(lambda v: v == 3, values))) * 3


def FOURS(values):
    return len(list(filter(lambda v: v == 4, values))) * 4


def FIVES(values):
    return len(list(filter(lambda v: v == 5, values))) * 5


def SIXES(values):
    return len(list(filter(lambda v: v == 6, values))) * 6


FULL_HOUSE = full_house
FOUR_OF_A_KIND = for_of_a_kind


def LITTLE_STRAIGHT(values):
    return 30 if [1, 2, 3, 4, 5] == values else 0


def BIG_STRAIGHT(values):
    return 30 if [2, 3, 4, 5, 6] == values else 0


def CHOICE(values):
    return sum(values)


def YACHT(values):
    return 50 if len(set(values)) == 1 else 0


def score(dice, category):
    dice.sort()
    return category(dice)
