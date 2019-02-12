from collections import defaultdict


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        if not N:
            return 0
        if len(A) == 1:
            return 1
        DP = defaultdict(int)
        for i in range(1, N):
            for j in range(i):
                df = abs(A[j]-A[i])
                DP[(i, df)] = max(DP[(j, df)] + 1, DP[(i, df)])
                print i, j, DP
        return max(DP.values()) + 1


s = Solution()
A = [9, 4, 7, 2, 10]
s.solve(A)
