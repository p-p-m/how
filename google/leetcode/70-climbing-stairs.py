class Solution:

    def climbStairs(self, n):
        return self.fib(n)

    def fib(self, n):
        if n <= 1:
            return 1
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b


s = Solution()
print(s.climbStairs(0))