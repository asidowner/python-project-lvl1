from prompt import string as prompt_string
from brain_games.games import even
from brain_games.games import calc
from brain_games.games import gcd

__ROUNDS: int = 3
__GAME_DESCRIPTION: dict = {
    'even': even.DESCRIPTION,
    'calc': calc.DESCRIPTION,
    'gcd': gcd.DESCRIPTION
}


def start_game(game_name: str) -> None:
    name: str = __welcome_user()
    counter: int = 0
    print(__GAME_DESCRIPTION[game_name])
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
    name: str = prompt_string('May i have your name? ')
    print(f'Hello, {name}!')
    return name


def __next_round(game_name: str, name: str) -> bool:
    question, expected_answer = __get_round_data(game_name)
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


def __get_round_data(game_name: str) -> tuple[str, str]:
    if game_name == 'even':
        question, expected_answer = even.round_data()
    elif game_name == 'calc':
        question, expected_answer = calc.round_data()
    elif game_name == 'gcd':
        question, expected_answer = gcd.round_data()
    else:
        raise Exception("Unknown game. Let's try again!")
    return question, expected_answer
