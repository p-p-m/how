import collections
import itertools


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        d = collections.defaultdict(list)
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                d[A[i] + A[j]].append((i, j))

        results = []
        for values in d.values():
            if len(values) < 2:
                continue
            results.append(values[0] + values[1])
        return min(results)


s = Solution()
A = [3, 4, 7, 1, 2, 9, 8]
print s.equal(A)

