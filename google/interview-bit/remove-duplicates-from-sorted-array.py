class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        current = A[0]
        i = 1
        while i < len(A):
            if A[i] == current:
                A[i] = None
            else:
                current = A[i]
                i += 1
        A = [a for a in A if a is not None]
        return len(A)


s = Solution()
s.removeDuplicates([1, 1, 2])
