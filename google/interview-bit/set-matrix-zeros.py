# class Solution:
#     # @param A : list of list of integers
#     # @return the same list modified
#     def setZeroes(self, A):
#         if not A:
#             return A
#         n = self.n = len(A)
#         m = self.m = len(A[0])
#         for i in range(n):
#             for j in range(m):
#                 if A[i][j] == 0:
#                     self.set_twos(A, i, j)
#         for i in range(n):
#             for j in range(m):
#                 if A[i][j] == 2:
#                     A[i][j] = 0
#         return A

#     def set_twos(self, A, i, j):
#         for i2 in range(self.n):
#             if A[i2][j] == 1:
#                 A[i2][j] = 2
#         for j2 in range(self.m):
#             if A[i][j2] == 1:
#                 A[i][j2] = 2

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        if not A:
            return A
        n = self.n = len(A)
        m = self.m = len(A[0])
        first_column_has_zeros = any(A[i][0] == 0 for i in range(n))
        first_row_has_zeros = any(A[0][j] == 0 for j in range(m))

        for i in range(1, n):
            if any(A[i][j] == 0 for j in range(m)):
                A[i][0] = 2

        for j in range(1, m):
            if any(A[i][j] == 0 for i in range(n)):
                A[0][j] = 2

        for i in range(n):
            if A[i][0] == 2:
                for j in range(m):
                    A[i][j] = 0

        for j in range(m):
            if A[0][j] == 2:
                for i in range(n):
                    A[i][j] = 0

        if first_column_has_zeros:
            for i in range(n):
                A[i][0] = 0

        if first_row_has_zeros:
            for j in range(m):
                A[0][j] = 0

        return A

matrix = [
    [0, 0],
    [1, 0],
]
s = Solution()
print s.setZeroes(matrix)