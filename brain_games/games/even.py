from prompt import string as prompt_string
from brain_games.utils import get_random_int_from_range

__DESCRIPTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
__RANGE = 100


def start_game(rounds: int, name: str) -> None:
    print(__DESCRIPTION)
    for i in range(rounds):
        result: bool = __next_round()
        if not result:
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f'Congratulations, {name}!')


def __next_round() -> bool:
    question: int = get_random_int_from_range(0, __RANGE)
    expected_answer: str = 'yes' if question % 2 == 0 else 'no'
    print(f'Question: {question}')
    answer: str = prompt_string('Your answer: ')
    return answer == expected_answer
