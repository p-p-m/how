# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
# Given an array nums and integer k, find the maximum sum of any subarray of length k
# where all elements are distinct. Return 0 if no such subarray exists.

import collections


class Window:

    def __init__(self, values: list, k: int):
        self.k = k
        self.state_dict = collections.defaultdict(int)
        for value in values:
            self.state_dict[value] += 1
        self.state_queue = collections.deque(values)
        self.sum_ = sum(values)

    def is_valid(self):
        return len(self.state_dict) == self.k

    def move(self, value):
        removed_value = self.state_queue.popleft()
        self.state_queue.append(value)
        self.sum_ += value
        self.sum_ -= removed_value
        self.state_dict[value] += 1
        self.state_dict[removed_value] -= 1
        if self.state_dict[removed_value] == 0:
            del self.state_dict[removed_value]

    def is_end(self):
        return self.index == len(self.nums)


class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        window = Window(nums[:k], k)
        max_ = window.sum_ if window.is_valid() else None
        for i in range(k, len(nums)):
            window.move(nums[i])
            if window.is_valid():
                if max_ is None or max_ < window.sum_:
                    max_ = window.sum_
        return max_ if max_ is not None else 0


s = Solution()
assert s.maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3) == 15
assert s.maximumSubarraySum([4, 4, 4], 3) == 0
assert s.maximumSubarraySum([1, 2, 3], 3) == 6
assert s.maximumSubarraySum([1], 1) == 1
print("All tests passed")
