from brain_games.utils import get_random_int_from_range

DESCRIPTION: str = 'Find the greatest common divisor of given numbers.'
__RANGE = 100


def round_data() -> tuple[str, str]:
    first_value: int = get_random_int_from_range(0, __RANGE)
    second_value: int = get_random_int_from_range(0, __RANGE)

    question: str = f"{first_value} {second_value}"
    expected_answer: int = __get_gcd(first_value, second_value)

    return question, str(expected_answer)


def __get_gcd(first_value: int, second_value: int) -> int:
    i: int = 1
    result: int = 1
    while i <= min(first_value, second_value):
        if first_value % i == 0 and second_value % i == 0:
            result = i
        i += 1
    return result
