class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        n = 2 * A - 1
        start = 0
        end = n - 1
        matrix = []
        for _ in range(n):
            matrix.append([None] * n)

        while start <= end:
            for i in range(start, end + 1):
                matrix[start][i] = A
                matrix[end][i] = A
                matrix[i][start] = A
                matrix[i][end] = A
            A = A - 1
            start = start + 1
            end = end - 1

        return matrix


s = Solution()
print s.prettyPrint(3)

