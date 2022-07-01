from prompt import string as prompt_string

__ROUNDS: int = 3


def start_game(description: str, round_data) -> None:
    name: str = __welcome_user()
    counter: int = 0
    print(description)
    while counter < __ROUNDS:
        result = __next_round(round_data, name)
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


def __next_round(round_data: staticmethod, name: str) -> bool:
    question, expected_answer = round_data()
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
