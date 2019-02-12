import collections
import itertools


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def get_ab(self, x1, y1, x2, y2):
        if x1 == x2:
            return None, x1
        a = (y1 - y2) / (x1 - x2)
        b = y1 - a * x1
        return a, b

    def maxPoints(self, A, B):
        if not A or not B:
            return 0
        if len(A) == 1:
            return 1
        d = collections.defaultdict(set)
        points = [(x, y) for x, y in zip(A, B)]
        for (x1, y1), (x2, y2) in itertools.combinations(points, 2):
            a, b = self.get_ab(x1, y1, x2, y2)
            d[a, b].add((x1, y1))
            d[a, b].add((x2, y2))
        return max(len(_set) for _set in d.values())


s = Solution()
# A, B = [1, 2, 3, 3], [1, 2, 8, 3]
A, B = [1, 1, 1, 2], [2, 3, 4, 8]
print s.maxPoints(A, B)
