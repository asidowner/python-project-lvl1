from prompt import string as prompt_string
from brain_games.game_data import get_round_data, get_description

__ROUNDS: int = 3


def start_game(game_name: str) -> None:
    name: str = __welcome_user()
    counter: int = 0
    print(get_description(game_name))
    while counter < __ROUNDS:
        result = __next_round(game_name, name)
        if not result:
            break
        elif counter == 2:
            print(f'Congratulations, {name}!')
            break
        counter += 1


def __welcome_user() -> str:
    print('Welcome to the Brain Games!')
    name: str = prompt_string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def __next_round(game_name: str, name: str) -> bool:
    question, expected_answer = get_round_data(game_name)
    print(f'Question: {question}')
    answer: str = prompt_string('Your answer: ')
    result: bool = answer == expected_answer
    if not result:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{expected_answer}'.")
        print(f"Let's try again, {name}!")
        return False
    print("Correct!")
    return True
