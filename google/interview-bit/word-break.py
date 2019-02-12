# import collections


# class Solution:
#     # @param A : string
#     # @param B : list of strings
#     # @return an integer
#     def wordBreak(self, A, B):
#         dp = self.get_dp(A, set(B))
#         queue = collections.deque([[len(A)]])
#         results = []
#         while queue:
#             breaks = queue.pop()
#             end = breaks[-1]
#             if end == 0:
#                 results.append(breaks[::-1])
#             for start in range(end):
#                 if dp[start][end]:
#                     queue.append(breaks + [start])
#         return sorted([self.format(A, result) for result in results])

#     def format(self, A, result):
#         return [A[result[i-1]:result[i]] for i in range(1, len(result))]

#     def get_dp(self, A, B):
#         dp = []
#         for i in range(len(A)):
#             dp.append([False] * (len(A) + 1))
#         for start in range(len(A)):
#             for end in range(start + 1, len(A) + 1):
#                 dp[start][end] = A[start: end] in B
#         return dp


class Solution:

    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        B = set(B)
        self.cache = {}
        return self.get_sentences(0, A, B)

    def get_sentences(self, i, s, B):
        if i not in self.cache:
            sentences = []
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in B:
                    if j == len(s):
                        sentences.append([s[i:j]])
                        continue
                    for tail in self.get_sentences(j, s, B):
                        sentences.append([s[i:j]] + tail)
            self.cache[i] = sentences
        return self.cache[i]


s = Solution()
A = 'catsanddog'
B = ["cat", "cats", "and", "sand", "dog"]
print s.wordBreak(A, B)


