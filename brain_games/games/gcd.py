from random import randint
from math import gcd

DESCRIPTION: str = 'Find the greatest common divisor of given numbers.'
_MIN_RANGE = 1
_MAX_RANGE = 500


def get_round_data() -> tuple[str, str]:
    first_value: int = randint(_MIN_RANGE, _MAX_RANGE)
    second_value: int = randint(_MIN_RANGE, _MAX_RANGE)

    question: str = f'{first_value} {second_value}'
    expected_answer: int = gcd(first_value, second_value)

    return question, str(expected_answer)
