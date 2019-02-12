class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        sign = -1 if A < 0 else 1
        A = str(A)[1:] if A < 0 else str(A)
        A = A[::-1]
        result = int(str(A))
        if result > 2147483647:
            return 0
        return result * sign


# s = Solution()
# print s.reverse(-65535), 53556
