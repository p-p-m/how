class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):

        def get_move_indexes(i, j):
            """ Get indexes of the elements that should replace each other in one
                Move.
            """
            return (i, j), (j, n - 1 - i), (n - 1 - i, n - 1 - j), (n - 1 - j, i)

        n = len(A)
        for i in range(n - 1):
            for j in range(min(i + 1, n - i - 1)):
                (a1, a2), (b1, b2), (c1, c2), (d1, d2) = get_move_indexes(i, j)
                A[b1][b2], A[c1][c2], A[d1][d2], A[a1][a2] =\
                    A[a1][a2], A[b1][b2], A[c1][c2], A[d1][d2]
        return A

A = [
    [1, 2],
    [3, 4]
]

s = Solution()
print s.rotate(A)
