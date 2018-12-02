import re

tree = "(2 (7 (2 () ()) (6 (5 () ()) (11 () ()))) (5 () (9 (4 () ()) ())))"

index = 0
for el in re.findall(r'\d+|\(|\)', tree):
    if el.isdigit():
        print el, index
    if el == '(':
        index += 1
    if el == ')':
        index -= 1

from collections import defaultdict

c = defaultdict(list)
