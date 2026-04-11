"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it's memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

from typing import List

# Possible sublist categories.
# Change the values as you see fit.
EQUAL = "1"
SUBLIST = "2"
SUPERLIST = "3"
UNEQUAL = "4"


def _isSublist(list_one: List, list_two: List) -> bool:
    for i in range(len(list_two) - len(list_one) + 1):
        if list_one == list_two[i : len(list_one) + i]:
            return True
    return False


def sublist(list_one: List, list_two: List) -> str:
    if list_one == list_two:
        return EQUAL
    elif _isSublist(list_one, list_two):
        return SUBLIST
    elif _isSublist(list_two, list_one):
        return SUPERLIST
    else:
        return UNEQUAL
