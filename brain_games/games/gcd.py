from random import randint
from math import gcd

from brain_games.start_game import start_game

__DESCRIPTION: str = 'Find the greatest common divisor of given numbers.'
__MIN_RANGE = 1
__RANGE = 500


def __round_data() -> tuple[str, str]:
    first_value: int = randint(__MIN_RANGE, __RANGE)
    second_value: int = randint(__MIN_RANGE, __RANGE)

    question: str = f"{first_value} {second_value}"
    expected_answer: int = gcd(first_value, second_value)

    return question, str(expected_answer)


def main():
    start_game(__DESCRIPTION, __round_data)
