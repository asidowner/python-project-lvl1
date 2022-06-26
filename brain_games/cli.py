from prompt import string as prompt_string


def welcome_user() -> None:
    print('Welcome to the Brain Games!')
    name: str = prompt_string('May I have your name? ')
    print(f'Hello, {name}')
