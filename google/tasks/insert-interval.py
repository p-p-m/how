# https://www.lintcode.com/problem/insert-interval/


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return '({}, {})'.format(self.start, self.end)


class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        return list(self.iter_intervals(intervals, newInterval))

    def iter_intervals(self, intervals, current):
        if not intervals:
            yield current
            return

        for interval in intervals:
            if current is None:
                yield interval
                continue

            if current.end <= interval.end and current.start >= interval.start:
                yield interval
                current = None
                continue

            if interval.end >= current.start and interval.end <= current.end:
                current.start = min(interval.start, current.start)
                continue
            elif interval.start >= current.start and interval.start <= current.end:
                current.end = max(interval.end, current.end)
                continue

            if current.end < interval.end:
                yield current
                yield interval
                current = None
            else:
                yield interval

        if current is not None:
            yield current


s = Solution()
print s.insert([Interval(1, 5)], Interval(5, 7))