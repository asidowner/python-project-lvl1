from random import randint

DESCRIPTION: str = 'What number is missing in the progression?'
_MIN_FIRST_VALUE_RANGE = 0
_MAX_FIRST_VALUE_RANGE = 100
_MIN_INCREMENT_RANGE = 1
_MAX_INCREMENT_RANGE = 20
_MIN_LEN_PROGRESSION = 5
_MAX_LEN_PROGRESSION = 10


def get_round_data() -> tuple[str, str]:
    first_value: int = randint(_MIN_FIRST_VALUE_RANGE,
                               _MAX_FIRST_VALUE_RANGE)
    increment: int = randint(_MIN_INCREMENT_RANGE,
                             _MAX_INCREMENT_RANGE)
    len_progression: int = randint(_MIN_LEN_PROGRESSION,
                                   _MAX_LEN_PROGRESSION)

    result_list: list = __get_progression(first_value,
                                          increment,
                                          len_progression)

    missing_index: int = randint(0, len_progression - 1)
    expected_answer: int = result_list[missing_index]

    question: str = ''
    for value in result_list:
        question += f"{value if value != expected_answer else '..'} "
    question: str = question.strip()

    return question, str(expected_answer)


def __get_progression(first_value: int,
                      increment: int,
                      len_progression: int) -> list:
    result_list: list = []
    value: int = first_value
    for i in range(len_progression):
        result_list.insert(i, value)
        value += increment
    return result_list
