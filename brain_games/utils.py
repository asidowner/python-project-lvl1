from random import randint
from prompt import string as prompt_string


def get_random_int_from_range(begin: int, end: int) -> int:
    return randint(begin, end)


def welcome_user() -> str:
    print('Welcome to the Brain Games!')
    name: str = prompt_string('May i have your name? ')
    print(f'Hello, {name}')
    return name
