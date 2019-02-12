# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '{}-{}'.format(self.start, self.end)

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        if not new_interval:
            return intervals
        if not intervals:
            return [new_interval]

        intervals = self.iter_intervals(intervals, new_interval)
        return list(self._gen_merged_intervals(intervals))

    def iter_intervals(self, intervals, new_interval):
        interval_added = False
        for interval in intervals:
            if interval_added:
                yield interval
                continue
            if interval.start >= new_interval.start:
                yield new_interval
                interval_added = True
            yield interval
        if not interval_added:
            yield new_interval

    def _gen_merged_intervals(self, intervals):
        current = next(intervals)
        for interval in intervals:
            if interval.start <= current.end:
                current.end = max(interval.end, current.end)
            else:
                yield current
                current = interval
        yield current


s = Solution()
print s.insert(
    intervals=[
        Interval(1, 2),
        Interval(3, 5),
        Interval(6, 7),
        Interval(8, 10),
        Interval(12, 16),
    ],
    new_interval=Interval(4, 9),
)
