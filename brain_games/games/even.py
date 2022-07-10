from random import randint

DESCRIPTION = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'
_MIN_RANGE = 0
_MAX_RANGE = 100


def get_round_data() -> tuple[str, str]:
    question_digit: int = randint(_MIN_RANGE, _MAX_RANGE)
    expected_answer: str = 'yes' if question_digit % 2 == 0 else 'no'
    question: str = f'{question_digit}'
    return question, expected_answer
