from prompt import string as prompt_string
from brain_games.utils import get_random_int_from_range, welcome_user


def start_even(rounds: int) -> None:
    name: str = welcome_user()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    for i in range(rounds):
        result: bool = next_round()
        if not result:
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f'Congratulations, {name}!')


def next_round() -> bool:
    __RANGE = 100
    question = get_random_int_from_range(0, __RANGE)
    expected_answer = 'yes' if question % 2 == 0 else 'no'
    print(f'Question: {question}')
    answer = prompt_string('Your answer: ')
    return answer == expected_answer
