class Solution:
    """
    @param matrix: an integer matrix
    @return: the length of the longest increasing path
    """
    def longestIncreasingPath(self, matrix):
        self.matrix = matrix
        self.n = len(self.matrix)
        self.memo = {}

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                self.get_value(i, j)

        if not self.memo:
            return 0
        return max(self.memo.values())

    def get_value(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        value = 1
        for ni, nj in self.get_neighbours(i, j):
            neighbour = self.matrix[ni][nj]
            if neighbour > self.matrix[i][j]:
                value = max(value, 1 + self.get_value(ni, nj))
        self.memo[(i, j)] = value
        return value

    def get_neighbours(self, i, j):
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for move_i, move_j in moves:
            ni, nj = move_i + i, move_j + j
            if ni < 0 or nj < 0 or ni >= self.n or nj >= self.n:
                continue
            yield ni, nj


matrix = [
    [9, 9, 4],
    [6, 5, 8],
    [2, 1, 1],
]
s = Solution()
print s.longestIncreasingPath(matrix)
