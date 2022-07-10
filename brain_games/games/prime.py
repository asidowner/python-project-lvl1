from random import randint

DESCRIPTION = 'Answer \"yes\" if given number is prime. ' \
              'Otherwise answer \"no\".'
_MIN_RANGE = 0
_MAX_RANGE = 100


def get_round_data() -> tuple[str, str]:
    question_digit: int = randint(_MIN_RANGE, _MAX_RANGE)
    expected_answer: str = 'yes' if __is_prime(question_digit) else 'no'
    question: str = f'{question_digit}'
    return question, expected_answer


def __is_prime(number: int) -> bool:
    i: int = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1
    return number > 1
