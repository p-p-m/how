class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        if A == 1:
            return [0, 1]
        results = []
        previous = [gc for gc in self.grayCode(A - 1)]
        for gc in previous:
            results.append(gc)
        for gc in previous[::-1]:
            results.append((1 << A - 1) + gc)
        return results


s = Solution()
print s.grayCode(3)
