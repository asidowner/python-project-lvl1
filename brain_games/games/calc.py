from prompt import string as prompt_string
from brain_games.utils import get_random_int_from_range

__DESCRIPTION: str = 'What is the result of the expression?'
__OPERATORS: tuple = '-', '+', '*'
__RANGE = 25


def start_game(rounds: int, name: str) -> None:
    print(__DESCRIPTION)
    for i in range(rounds):
        result, answer, expected_answer = __next_round()
        if not result:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{expected_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f'Congratulations, {name}!')


def __next_round() -> tuple[bool, str, int]:
    operator: str = __get_random_operator()
    first_value = get_random_int_from_range(0, __RANGE)
    second_value = get_random_int_from_range(0, __RANGE)

    question: str = f"{first_value} {operator} {second_value}"
    print(f'Question: {question}')

    if operator == '-':
        expected_answer: int = first_value - second_value
    elif operator == '+':
        expected_answer: int = first_value + second_value
    elif operator == '*':
        expected_answer: int = first_value * second_value
    else:
        raise Exception("Internal error")

    answer: str = prompt_string('Your answer: ')

    result: bool = False
    try:
        result: bool = int(answer) == expected_answer
    finally:
        return result, answer, expected_answer


def __get_random_operator() -> str:
    return __OPERATORS[get_random_int_from_range(0, len(__OPERATORS) - 1)]
