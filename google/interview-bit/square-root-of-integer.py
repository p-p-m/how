class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        step = A // 2
        x = 1
        while True:
            if x * x <= A and (x + 1) * (x + 1) > A:
                return x
            elif x * x <= A and (x + 1) * (x + 1) <= A:
                x += step
            elif x * x >= A and (x + 1) * (x + 1) >= A:
                x -= step
            step = max(step // 2, 1)


s = Solution()
print s.sqrt(4)
