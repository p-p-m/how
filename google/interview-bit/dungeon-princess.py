class Solution:
    # @param A : list of list of integers
    # @return an integer
    def calculateMinimumHP(self, A):
        if not A:
            return 0
        self.cache = {}
        return self.get_cost(A, len(A) - 1, len(A[0]) - 1)

    def _calc_cost(self, A, i, j):
        cost = - A[i][j]
        if i == 0 and j == 0:
            return cost, cost
        if i == 0:
            cost_before, _min = self.get_cost(A, i, j-1)
        elif j == 0:
            cost_before, _min = self.get_cost(A, i-1, j)
        else:
            cost_before = min(self.get_cost(A, i-1, j), self.get_cost(A, i, j-1))
        if cost_before >= 0 and cost >= 0:
            return cost + cost_before
        if cost_before >= 0 and cost < 0:
            return cost_before
        return cost_before - cost

    def get_cost(self, A, i, j):
        key = (i, j)
        if key in self.cache:
            return self.cache[key]
        cost = self._calc_cost(A, i, j)
        self.cache[key] = cost
        return cost


s = Solution()
A = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5],
]
print s.calculateMinimumHP(A)
