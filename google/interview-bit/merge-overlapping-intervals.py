import operator


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '{}-{}'.format(self.start, self.end)


class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals = sorted(intervals, key=operator.attrgetter('start'))
        return list(self._gen_merged_intervals(intervals))

    def _gen_merged_intervals(self, intervals):
        intervals = iter(intervals)
        current = next(intervals)
        for interval in intervals:
            if interval.start <= current.end:
                current.end = max(interval.end, current.end)
            else:
                yield current
                current = interval
        yield current


s = Solution()
print s.merge(
    intervals=[
        Interval(1, 3),
        Interval(2, 6),
        Interval(8, 10),
        Interval(15, 18),
    ],
)