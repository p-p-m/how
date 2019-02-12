class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        if not A:
            return 0
        n = len(A)
        m = len(A[0])
        self.cache = {}
        zeros = 0
        for i1 in range(n):
            for j1 in range(m):
                for i2 in range(i1 + 1, n + 1):
                    for j2 in range(j1 + 1, m + 1):
                        if self.calc(A, i1, j1, i2, j2) == 0:
                            zeros += 1
        return zeros

    def calc(self, A, i1, j1, i2, j2):
        key = (i1, j1, i2, j2)
        if key in self.cache:
            return self.cache[key]
        if i2 - i1 > 1:
            result = self.calc(A, i1, j1, i2 - 1, j2) + self.calc(A, i2 - 1, j1, i2, j2)
            self.cache[key] = result
            return result
        if j2 - j1 > 1:
            result = self.calc(A, i1, j1, i2, j2 - 1) + self.calc(A, i1, j2 - 1, i2, j2)
            self.cache[key] = result
            return result

        result = A[i1][j1]
        self.cache[key] = result
        return result


s = Solution()
A = [
    [-2, -1, 1, 2],
]
print s.solve(A)
print '---' * 3
