class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        self.cache = {}
        return self.dist(A, B, len(A) - 1, len(B) - 1)

    def dist(self, A, B, i, j):
        if i == 0 and j == 0:
            return 1
        if i == 0:
            return j
        if j == 0:
            return i
        key = (i, j)
        if key in self.cache:
            return self.cache[key]
        if A[i] == B[j]:
            result = self.dist(A, B, i - 1, j - 1)
        else:
            result = min(
                1 + self.dist(A, B, i - 1, j - 1),
                1 + self.dist(A, B, i, j - 1),
                1 + self.dist(A, B, i - 1, j),
            )
        self.cache[key] = result
        return result


s = Solution()
A, B = 'a', 'b'
print s.minDistance(A, B)
