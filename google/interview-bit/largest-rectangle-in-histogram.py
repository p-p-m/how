class Group:

    def __init__(self, A):
        self._min = min(A)
        self.size = len(A)
        self.elements = A

    def divide(self):
        a = []
        for element in self.elements:
            if element > self._min:
                a.append(element)
            else:
                if a:
                    yield Group(a)
                a = []
        if a:
            yield Group(a)

    def get_area(self):
        return self._min * self.size

    def __repr__(self):
        return '{} ({})'.format(self.get_area(), ', '.join([str(e) for e in self.elements]))


class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        groups = [Group(A)]
        max_area = 0
        for group in groups:
            if max_area < group.get_area():
                max_area = group.get_area()
            for g in group.divide():
                groups.append(g)
        return max_area


s = Solution()
print s.largestRectangleArea([2, 1, 5, 6, 2, 3])
