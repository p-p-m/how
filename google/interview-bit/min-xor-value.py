class Solution:
    # @param A : list of integers
    # @return an integer
    # def findMinXor(self, A):
    #     r = [a ^ b for a, b in itertools.product(A, A)]
    #     return min(r)

    def findMinXor(self, A):
        A = sorted(A)
        for i in range(len(A)):
            value = A[i] ^ A[i - 1]
            if _min is None or _min > value:
                _min = value
        return _min

# print list(itertools.combinations([1, 2, 3], 2))
s = Solution()
s.findMinXor([2, 7, 8, 11, 18, 90])