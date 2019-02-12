# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def maxProduct(self, A):
#         dp = []
#         n = len(A)
#         for _ in range(n):
#             dp.append([1] * (n+1))
#         _max = None
#         for i in range(n):
#             for j in range(i + 1, n + 1):
#                 dp[i][j] = self.calc(A, i, j, dp)
#                 if _max is None or _max < dp[i][j]:
#                     _max = dp[i][j]
#         # print dp
#         return _max

#     def calc(self, A, i, j, dp):
#         return dp[i][j-1] * A[j-1]


# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def maxProduct(self, A):
#         best = A[0]
#         lp = ln = 0
#         for i,x in enumerate(A):
#             if x == 0:
#                 lp = ln = 0
#             elif x > 0:
#                 lp, ln = x*max(1,lp), x*ln
#             else:
#                 lp, ln = x*ln, x*max(1,lp)
#             best = max(best, lp)
#         return best


# s = Solution()
# A = [2, 2, -1, -2, 3]
# print s.maxProduct(A)

s = 'asdf'