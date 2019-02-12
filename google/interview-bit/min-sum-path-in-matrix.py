class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        if not A:
            return 0
        self.cache = {}
        return self.get_cost(A, len(A) - 1, len(A[0]) - 1)

    def _calc_cost(self, A, i, j):
        cost = A[i][j]
        if i == 0 and j == 0:
            return cost
        if i == 0:
            return cost + self.get_cost(A, i, j-1)
        if j == 0:
            return cost + self.get_cost(A, i-1, j)
        return cost + min(self.get_cost(A, i-1, j), self.get_cost(A, i, j-1))

    def get_cost(self, A, i, j):
        key = (i, j)
        if key in self.cache:
            return self.cache[key]
        cost = self._calc_cost(A, i, j)
        self.cache[key] = cost
        return cost


s = Solution()
A = [
    [1, 3, 2],
    [4, 3, 1],
    [5, 6, 1],
]
print s.minPathSum(A)
