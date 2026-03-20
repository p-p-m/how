# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
# Given a row of cards with points and integer k, take exactly k cards from
# the beginning or end of the row to maximize your total score.


class Window:

    def __init__(self, nums, k):
        self.left = 0
        self.right = k - 1
        self.sum = sum(nums[0: k])
        self.nums = nums

    def move(self):
        self.sum -= self.nums[self.right]
        self.right -= 1
        self.left -= 1
        self.sum += self.nums[self.left]


class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        window = Window(cardPoints, k)
        max_ = window.sum
        while window.right >= 0:
            window.move()
            if max_ < window.sum:
                max_ = window.sum
        return max_


s = Solution()
assert s.maxScore([1, 2, 3, 4, 5, 6, 1], 3) == 12
assert s.maxScore([2, 2, 2], 2) == 4
assert s.maxScore([9, 7, 7, 9, 7, 7, 9], 7) == 55
assert s.maxScore([1, 1000, 1], 1) == 1
print("All tests passed")
