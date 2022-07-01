from random import randint, choice
from brain_games.start_game import start_game

__DESCRIPTION: str = 'What is the result of the expression?'
__OPERATORS: tuple = '-', '+', '*'
__MIN_RANGE = 0
__RANGE = 25


def __round_data() -> tuple[str, str]:
    operator: str = choice(__OPERATORS)
    first_value: int = randint(__MIN_RANGE, __RANGE)
    second_value: int = randint(__MIN_RANGE, __RANGE)

    if operator == '-':
        expected_answer: int = first_value - second_value
    elif operator == '+':
        expected_answer: int = first_value + second_value
    elif operator == '*':
        expected_answer: int = first_value * second_value
    else:
        raise Exception("Internal error")

    question: str = f"{first_value} {operator} {second_value}"

    return question, str(expected_answer)


def main():
    start_game(__DESCRIPTION, __round_data)
