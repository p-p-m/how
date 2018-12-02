def sumOfTwo(a, b, v):
    a = [v - el for el in a]
    b = set(b)
    for el in a:
        if el in b:
            return True
    return False


a = [1, 2, 3]
b = [10, 20, 30, 40]

print sumOfTwo(a, b, 44)
