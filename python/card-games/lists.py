"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""

from typing import List


def get_rounds(number: int) -> List:
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return list(range(number, number + 3))


def concatenate_rounds(rounds_1: List, rounds_2: List) -> List:
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds: List, number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    return number in rounds


def card_average(hand: List) -> float:
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand: List) -> bool:
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    quick_avg = (hand[-1] + hand[0]) / 2
    median = hand[len(hand) // 2]
    real_avg = card_average(hand)
    return any([quick_avg == real_avg, median == real_avg])


def average_even_is_average_odd(hand: List) -> bool:
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even = []
    odd = []
    for i, n in enumerate(hand):
        if i % 2 == 0:
            even.append(n)
        else:
            odd.append(n)

    return card_average(even) == card_average(odd)


def maybe_double_last(hand: List) -> List:
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    is_jack = hand[-1] == 11

    if is_jack:
        return hand[:-1] + [22]
    return hand
