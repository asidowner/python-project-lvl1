from brain_games.games import even
from brain_games.games import calc
from brain_games.games import gcd
from brain_games.games import progression
from brain_games.games import prime

__GAME_DESCRIPTION: dict = {
    'even': even.DESCRIPTION,
    'calc': calc.DESCRIPTION,
    'gcd': gcd.DESCRIPTION,
    'progression': progression.DESCRIPTION,
    'prime': prime.DESCRIPTION
}


def get_description(game_name: str) -> str:
    return __GAME_DESCRIPTION.get(game_name)


def get_round_data(game_name: str) -> tuple[str, str]:
    if game_name == 'even':
        question, expected_answer = even.round_data()
    elif game_name == 'calc':
        question, expected_answer = calc.round_data()
    elif game_name == 'gcd':
        question, expected_answer = gcd.round_data()
    elif game_name == 'progression':
        question, expected_answer = progression.round_data()
    elif game_name == 'prime':
        question, expected_answer = prime.round_data()
    else:
        raise Exception("Unknown game. Let's try again!")
    return question, expected_answer
