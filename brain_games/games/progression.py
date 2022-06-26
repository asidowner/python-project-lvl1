from brain_games.utils import get_random_int_from_range

DESCRIPTION: str = 'What number is missing in the progression?'
__MIN_LEN_PROGRESSION = 5
__MAX_LEN_PROGRESSION = 10
__RANGE_FOR_DIFF = 20
__FIRST_VALUE_RANGE = 100


def round_data() -> tuple[str, str]:
    first_value: int = get_random_int_from_range(0, __FIRST_VALUE_RANGE)
    increment: int = get_random_int_from_range(1, __RANGE_FOR_DIFF)
    len_progression: int = get_random_int_from_range(__MIN_LEN_PROGRESSION,
                                                     __MAX_LEN_PROGRESSION)

    result_list = __get_progression(first_value, increment, len_progression)

    missing_index: int = get_random_int_from_range(0, len_progression - 1)
    expected_answer: int = result_list[missing_index - 1]

    question = ''
    for value in result_list:
        question += f"{value if value != expected_answer else '..'} "
    question = question.strip()

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


round_data()
