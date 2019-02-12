class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        if len(A) == 1:
            return [A]
        if len(A) == 2:
            return [[A[0], A[1]], [A[1], A[0]]]
        results = []
        for i in range(len(A)):
            for perm in self.permute(A[:i] + A[i+1:]):
                results.append([A[i]] + perm)
        return results


s = Solution()
print s.permute([1, 2, 3, 4])
