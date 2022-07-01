from random import randint

from brain_games.start_game import start_game

__DESCRIPTION = "Answer \"yes\" if given number is prime. " \
                "Otherwise answer \"no\"."
__MIN_RANGE = 0
__RANGE = 100


def __round_data() -> tuple[str, str]:
    question_digit: int = randint(__MIN_RANGE, __RANGE)
    expected_answer: str = 'yes' if __is_prime(question_digit) else 'no'
    question: str = f'{question_digit}'
    return question, expected_answer


def __is_prime(number: int) -> bool:
    result: bool = number > 1
    i: int = 2
    while i < number:
        if number % i == 0:
            result = False
            break
        i += 1
    return result


def main():
    start_game(__DESCRIPTION, __round_data)
