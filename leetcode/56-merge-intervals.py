# https://leetcode.com/problems/merge-intervals/
# Given an array of intervals, merge all overlapping intervals and return the
# resulting array of non-overlapping intervals covering all input intervals.



class Interval:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def merge(self, other: Interval):
        self.left = min(self.left, other.left)
        self.right = max(self.right, other.right)

    def can_merge(self, other):
        return self.right >= other.left


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        current = Interval(*intervals[0])
        result = []
        for i in range(1, len(intervals)):
            next_ = Interval(*intervals[i])
            if current.can_merge(next_):
                current.merge(next_)
            else:
                result.append([current.left, current.right])
                current = next_
        result.append([current.left, current.right])
        return result


s = Solution()
assert s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert s.merge([[1, 4], [4, 5]]) == [[1, 5]]
assert s.merge([[4, 7], [1, 4]]) == [[1, 7]]
assert s.merge([[1, 4]]) == [[1, 4]]
print("All tests passed")
