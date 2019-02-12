import collections
import itertools


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        combs = itertools.combinations(A, 2)
        counter = collections.Counter(A)
        _set = set(A)
        result = set([])
        for a, b in combs:
            _sum = - a - b
            if _sum not in _set:
                continue
            if _sum == a and counter[a] < 2:
                continue
            if _sum == b and counter[b] < 2:
                continue
            if _sum == a == b and counter[b] < 3:
                continue
            result.add(tuple(sorted([a, b, _sum])))
        return list(result)


s = Solution()
print s.threeSum([-4, 2, 2])