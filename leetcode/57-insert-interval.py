# https://leetcode.com/problems/insert-interval/
# Given a sorted list of non-overlapping intervals and a new interval, insert
# the new interval and merge any overlapping intervals. Return the result.


class Interval:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_before(self, other):
        return self.end < other.start

    def is_after(self, other):
        return self.start > other.end

    def merge(self, other):
        return Interval(min(self.start, other.start), max(self.end, other.end))

    def as_list(self):
        return [self.start, self.end]


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals = [Interval(start, end) for start, end in intervals]
        new_interval = Interval(newInterval[0], newInterval[1])
        result = []
        new_interval_inserted = False
        for interval in intervals:
            if interval.is_before(new_interval):
                result.append(interval.as_list())
            elif interval.is_after(new_interval):
                if not new_interval_inserted:
                    result.append(new_interval.as_list())
                    new_interval_inserted = True
                result.append(interval.as_list())
            else:
                new_interval = interval.merge(new_interval)
        if not new_interval_inserted:
            result.append(new_interval.as_list())
        return result


s = Solution()
assert s.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]], s.insert([[1, 3], [6, 9]], [2, 5])
assert s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
assert s.insert([], [5, 7]) == [[5, 7]]
assert s.insert([[1, 5]], [2, 3]) == [[1, 5]]
assert s.insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
print("All tests passed")
