class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        n = A + B - 2
        k = A - 1
        if n < k:
            return 1
        return self.C(n, k)

    def C(self, n, k):
        return self.f(n) / (self.f(k) * self.f(n - k))

    def f(self, n):
        r = 1
        s = 1
        while s < n:
            s += 1
            r *= s
        return r


s = Solution()
print s.uniquePaths(15, 9)
