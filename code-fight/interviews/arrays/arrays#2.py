# my solution
def firstNotRepeatingCharacter(s):
    a = [None] * 26
    ord_a = ord('a')
    for index, l in enumerate(s):
        index_in_a = ord(l) - ord_a
        if a[index_in_a] is None:
            a[index_in_a] = index
        else:
            a[index_in_a] = -1
    a = [el for el in a if el is not None and el != -1]
    if a:
        return s[min(a)]
    else:
        return '_'


s = "absedab"
assert firstNotRepeatingCharacter(s) == 's'

s = "abacabad"
assert firstNotRepeatingCharacter(s) == 'c'

s = "abacabaabacaba"
assert firstNotRepeatingCharacter(s) == '_'
