class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if not A:
            return 0

        palindrome_end = start = end = 0
        while end < len(A) - 1:
            end += 1
            if self.is_palindrome(A, start, end):
                palindrome_end = end

        return len(A) - 1 - palindrome_end

    def is_palindrome(self, A, start, end):
        while start < end:
            if A[start] != A[end]:
                return False
            start += 1
            end -= 1
        return True


s = Solution()
print s.solve('BACEC')
