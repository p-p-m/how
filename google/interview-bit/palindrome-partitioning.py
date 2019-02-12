import collections


class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        dp = self.build_dp(A)
        return list(self.split(result, A) for result in self.process_results(dp, A))

    def process_results(self, dp, A):
        queue = collections.deque([[0, j] for j in range(1, len(A) + 1) if dp[0][j]])
        while queue:
            result = queue.popleft()
            i = result[-1]
            if i == len(A):
                yield result
                continue
            for j in range(len(A), i, -1):
                if dp[i][j]:
                    queue.appendleft(result + [j])

    def split(self, result, A):
        return [A[result[i]:result[i+1]] for i in range(len(result) - 1)]

    def build_dp(self, A):
        dp = []
        for _ in range(len(A)):
            dp.append([False] * (len(A) + 1))

        for i in range(len(A)):
            for j in range(i + 1, len(A) + 1):
                dp[i][j] = self.is_palindrome(A, i, j)

        return dp

    def is_palindrome(self, A, i, j):
        return A[i:j] == A[i:j][::-1]


s = Solution()
print s.partition('efe')