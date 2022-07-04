from random import randint

DESCRIPTION: str = 'What number is missing in the progression?'
__MIN_LEN_PROGRESSION = 5
__MAX_LEN_PROGRESSION = 10
__MIN_VALUE = 0
__MIN_INCREMENT = 1
__RANGE_FOR_DIFF = 20
__FIRST_VALUE_RANGE = 100


def round_data() -> tuple[str, str]:
    first_value: int = randint(__MIN_VALUE,
                               __FIRST_VALUE_RANGE)
    increment: int = randint(__MIN_INCREMENT,
                             __RANGE_FOR_DIFF)
    len_progression: int = randint(__MIN_LEN_PROGRESSION,
                                   __MAX_LEN_PROGRESSION)

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
