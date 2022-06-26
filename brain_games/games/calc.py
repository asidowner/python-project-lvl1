from brain_games.utils import get_random_int_from_range

DESCRIPTION: str = 'What is the result of the expression?'
__OPERATORS: tuple = '-', '+', '*'
__RANGE = 25


def round_data() -> tuple[str, str]:
    operator: str = __get_random_operator()
    first_value: int = get_random_int_from_range(0, __RANGE)
    second_value: int = get_random_int_from_range(0, __RANGE)

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


def __get_random_operator() -> str:
    return __OPERATORS[get_random_int_from_range(0, len(__OPERATORS) - 1)]
