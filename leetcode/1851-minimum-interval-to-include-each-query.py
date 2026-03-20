# https://leetcode.com/problems/minimum-interval-to-include-each-query/
# Given a list of intervals and a list of queries, for each query find the size
# (right - left + 1) of the smallest interval containing that query. Return -1 if none.


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        pass


s = Solution()
assert s.minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]) == [3, 3, 1, 4]
assert s.minInterval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]) == [2, -1, 4, 6]
assert s.minInterval([[1, 10]], [5]) == [10]
assert s.minInterval([[1, 2]], [3]) == [-1]
print("All tests passed")
