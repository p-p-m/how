patterns = [
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1)
]

class InvalidNumberError(Exception):
    pass


def substract_pattern(s, pattern):
    """
    Extract given pattern from the string start
    """
    count = 0
    substracted = s[:]
    while count <= 3:
        if substracted.startswith(pattern):
            substracted = substracted[len(pattern):]
            count += 1
        else:
            return substracted, count
    raise InvalidNumberError


def parse(s):
    result = 0
    for pattern, value in patterns:
        s, count = substract_pattern(s, pattern)
        result += count * value
    if s:
        raise InvalidNumberError
    return result


def solution(S):
    try:
        return parse(s)
    except InvalidNumberError:
        return 0

examples = [()]