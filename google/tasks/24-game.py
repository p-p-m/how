

import collections


# Looks like this solution is right, however tests fails on corner
# cases where we have a lot of divisions.
class Solution:
    """
    @param nums: 4 cards
    @return: whether they could get the value of 24
    """
    def compute24(self, nums):
        self.memo = {}
        queue = collections.deque([nums])
        _min = 24
        while queue:
            nums = queue.pop()
            if len(nums) == 2:
                if 24 in self.all_variants(*nums):
                    return True
                continue
            for n in self.step(nums):
                queue.append(n)
        return _min

    def step(self, nums):
        if tuple(nums) in self.memo:
            return self.memo[tuple(nums)]
        a, b = nums[:2]
        results = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                copy = nums[:]
                a, b = nums[i], nums[j]
                del copy[j]
                del copy[i]
                for variant in self.all_variants(a, b):
                    results.append([variant] + copy)
        self.memo[tuple(nums)] = results
        return results

    def all_variants(self, a, b):
        variants = [a * b, a + b, a - b, b - a]
        if a != 0:
            variants.append(round(float(b) / a, 10))
        if b != 0:
            variants.append(round(float(a) / b, 10))
        return variants



s = Solution()
print s.compute24([1, 1, 5, 5])
