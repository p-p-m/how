class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        return list(self._generate(A))

    def _generate(self, A):
        row = [1]
        for i in range(A):
            yield row
            row = [
                (row[j] if j < len(row) else 0) + (row[j - 1] if j > 0 else 0)
                for j in range(len(row) + 1)
            ]

s = Solution()
s.solve(0)
