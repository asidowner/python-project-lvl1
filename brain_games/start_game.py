from prompt import string as prompt_string

__ROUNDS: int = 3


def start_game(game) -> None:
    name: str = __welcome_user()
    counter: int = 0
    print(game.DESCRIPTION)
    while counter < __ROUNDS:
        question, expected_answer = game.round_data()
        print(f'Question: {question}')
        answer: str = prompt_string('Your answer: ')
        result = answer == expected_answer
        if not result:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{expected_answer}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print("Correct!")
            if counter == 2:
                print(f'Congratulations, {name}!')
                break
        counter += 1


def __welcome_user() -> str:
    print('Welcome to the Brain Games!')
    name: str = prompt_string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
