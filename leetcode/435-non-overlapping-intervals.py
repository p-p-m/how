# https://leetcode.com/problems/non-overlapping-intervals/
# Given an array of intervals, return the minimum number of intervals to remove
# to make the rest non-overlapping. Intervals sharing an endpoint are not overlapping.


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        pass


s = Solution()
assert s.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
assert s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
assert s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
assert s.eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2
print("All tests passed")
