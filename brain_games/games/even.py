from random import randint

DESCRIPTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
__MIN_RANGE = 0
__RANGE = 100


def round_data() -> tuple[str, str]:
    question_digit: int = randint(__MIN_RANGE, __RANGE)
    expected_answer: str = 'yes' if question_digit % 2 == 0 else 'no'
    question: str = f'{question_digit}'
    return question, expected_answer
