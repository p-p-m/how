def rotateImage(a):
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
    n = len(a)

    def get_move_indexes(i, j):
        """ Get indexes of the elements that should replace each other in one
            Move.
        """
        return (i, j), (j, n - 1 - i), (n - 1 - i, n - 1 - j), (n - 1 - j, i)

    for i in range(n - 1):
        for j in range(min(i + 1, n - i - 1)):
            (a1, a2), (b1, b2), (c1, c2), (d1, d2) = get_move_indexes(i, j)
            a[b1][b2], a[c1][c2], a[d1][d2], a[a1][a2] =\
                a[a1][a2], a[b1][b2], a[c1][c2], a[d1][d2]

    return a
