def sudoku2(grid):

    def has_dupes(l):
        e = [el for el in l if el != '.']
        return len(e) != len(set(e))

    def to_squares(a, b, c):
        return [
            a[0:3] + b[0:3] + c[0:3],
            a[3:6] + b[3:6] + c[3:6],
            a[6:9] + b[6:9] + c[6:9],
        ]

    def batch(iterable, n=1):
        _l = len(iterable)
        for ndx in range(0, _l, n):
            yield iterable[ndx:min(ndx + n, _l)]

    if any(has_dupes(l) for l in grid):
        return False

    if any(has_dupes(l) for l in zip(*grid)):
        return False

    for a, b, c in batch(grid, n=3):
        if any(has_dupes(l) for l in to_squares(a, b, c)):
            return False

    return True


grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]


assert sudoku2(grid)


grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]

assert not sudoku2(grid)
