matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

matrix = [
    [1, 2, 3, 4],
    [6, 7, 8, 9],
    [11, 12, 13, 14],
    [16, 17, 18, 19],
]

n = len(matrix)


def print_matrix(matrix):
    """ Print matrix nicely """
    for row in matrix:
        for cell in row:
            print cell,
        print


def solution(matrix):
    """ To rotate matrix in-place lets define Move action.

        Move - position switch between four elements that takes each other
               place after rotation.
        For example in matrix
          1 2 3
          4 5 6
          7 8 9
        numbers 1, 7, 9, 3 are involved in one Move:
        1 moves to place where was 3
        7 moves to place where was 1
        9 moves to place where was 7
        7 moves to place where was 1

        To rate matrix we need to execute we need to execute Move for each
        element from left quarter of the matrix.
          x o o
          x x o (this one)
          x o o
        All other will be aligned automatically because each of them will be
        involved in the Move.
    """

    def get_move_indexes(i, j):
        """ Get indexes of the elements that should replace each other in one
            Move.
        """
        return (i, j), (j, n - 1 - i), (n - 1 - i, n - 1 - j), (n - 1 - j, i)

    m = matrix

    for i in range(n - 1):
        for j in range(min(i + 1, n - i - 1)):
            (a1, a2), (b1, b2), (c1, c2), (d1, d2) = get_move_indexes(i, j)
            m[b1][b2], m[c1][c2], m[d1][d2], m[a1][a2] =\
                m[a1][a2], m[b1][b2], m[c1][c2], m[d1][d2]


print 'Before'
print_matrix(matrix)

solution(matrix)

print 'After'
print_matrix(matrix)
