def isCryptSolution(crypt, solution):
    solution = {k: v for k, v in solution}

    class EncodeError(Exception):
        pass

    def encode(word):
        encoded = ''.join([solution[latter] for latter in word])
        if encoded.startswith('0') and len(encoded) > 1:
            raise EncodeError
        return int(encoded)

    a, b, c = crypt
    try:
        return encode(a) + encode(b) == encode(c)
    except EncodeError:
        return False


crypt = ["SEND", "MORE", "MONEY"]
solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]

assert isCryptSolution(crypt, solution)


crypt = ["TEN", "TWO", "ONE"]
solution = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]


assert not isCryptSolution(crypt, solution)
