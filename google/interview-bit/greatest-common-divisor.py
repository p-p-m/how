class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if A == 0:
            return B
        if B == 0:
            return A
        result = 1
        x = 2
        while x <= A and x <= B:
            if A % x == 0 and B % x == 0:
                A = A // x
                B = B // x
                result *= x
            else:
                x += 1
        return result


s = Solution()
print s.gcd(12, 8)
