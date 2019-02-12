class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        a = [x]
        i = 2
        while i <= n:
            a.append(a[-1] ** 2)
            i = i << 1
        result = 1
        for index, bit in enumerate(bin(n)[2:][::-1]):
            if bit == '0':
                continue
            result *= a[index]
        return result % d


class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        res = 1 % d  # Cover case d == 1
        while n > 0:
            if n % 2 == 1:   # Odd?
               res = (res * x) % d
            x = x ** 2 % d
            n >>= 1
        return res


s = Solution()
x = 6
n = 8
d = 13
print s.pow(x, n, d), (x ** n) % d

101
110

