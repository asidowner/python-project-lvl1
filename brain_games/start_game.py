from prompt import string as prompt_string
from brain_games.games import even
from brain_games.games import calc

__ROUNDS: int = 3


def start_game(game_name: str) -> None:
    name: str = __welcome_user()
    if game_name == 'even':
        even.start_game(__ROUNDS, name)
    elif game_name == 'calc':
        calc.start_game(__ROUNDS, name)
    else:
        print(f"Unknown game. Let's try again, {name}!")


def __welcome_user() -> str:
    print('Welcome to the Brain Games!')
    name: str = prompt_string('May i have your name? ')
    print(f'Hello, {name}!')
    return name
