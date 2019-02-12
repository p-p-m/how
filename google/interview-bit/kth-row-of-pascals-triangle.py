class Solution:
    # @param A : integer
    # @return a list of list of integers
    def getRow(self, A):
        row = [1]
        for i in range(A):
            row = [
                (row[j] if j < len(row) else 0) + (row[j - 1] if j > 0 else 0)
                for j in range(len(row) + 1)
            ]
        return row


s = Solution()
print s.solve(5)
