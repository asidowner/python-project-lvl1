from random import randint, choice

DESCRIPTION: str = 'What is the result of the expression?'
_OPERATORS: tuple = '-', '+', '*'
_MIN_RANGE = 0
_MAX_RANGE = 25


def get_round_data() -> tuple[str, str]:
    operator: str = choice(_OPERATORS)
    first_value: int = randint(_MIN_RANGE, _MAX_RANGE)
    second_value: int = randint(_MIN_RANGE, _MAX_RANGE)

    if operator == '-':
        expected_answer: int = first_value - second_value
    elif operator == '+':
        expected_answer: int = first_value + second_value
    elif operator == '*':
        expected_answer: int = first_value * second_value
    else:
        raise Exception('Internal error')

    question: str = f'{first_value} {operator} {second_value}'

    return question, str(expected_answer)
