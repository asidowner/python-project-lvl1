from prompt import string as prompt_string


def welcome_user():
    print('Welcome to the Brain Games!')
    name: str = prompt_string('May i have your name? ')
    print(f'Hello, {name}')
