class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A = sorted(A)
        for i in range(len(A) - 1):
            if (i % 2 == 0 and A[i] < A[i + 1]) or (i % 2 == 1 and A[i + 1] < A[i]):
                A[i], A[i + 1] = A[i + 1], A[i]
        return A


s = Solution()
print s.wave([6, 8, 2, 2, 3, 4, 5, 5, 5])

