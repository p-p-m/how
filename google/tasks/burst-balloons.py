# https://www.lintcode.com/problem/burst-balloons/description

class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def maxCoins(self, nums):
        self.cache = {}
        return self.get_max(tuple(nums))

    def get_max(self, nums):
        if nums in self.cache:
            return self.cache[nums]

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            self.cache[nums] = nums[0]
            return nums[0]

        values = []
        for i in range(len(nums)):
            value = self.get_value(nums, i)
            _max = self.get_max(tuple(el for index, el in enumerate(nums) if index != i))
            values.append(value + _max)
        self.cache[nums] = max(values)
        return self.cache[nums]

    def get_value(self, nums, index):
        left = nums[index - 1] if index > 0 else 1
        right = nums[index + 1] if index < len(nums) - 1 else 1
        return left * nums[index] * right


class Solution2:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def maxCoins(self, nums):
        if not nums:
            return 0

        # [4,1,5] => [1,4,1,5,1]
        nums = [1] + nums + [1]
        self.memo = {}
        return self.memo_search(nums, 0, len(nums) - 1, self.memo)

    def memo_search(self, nums, i, j, memo):
        if i == j:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        best = 0
        for k in range(i + 1, j):
            left = self.memo_search(nums, i, k, memo)
            print 'left', left, i, k
            right = self.memo_search(nums, k, j, memo)
            print 'right', right, k, j
            best = max(best, left + right + nums[i] * nums[k] * nums[j])

        memo[(i, j)] = best
        return best


class Solution3:

    def maxCoins(self, nums):
        if not nums:
            return 0

        nums = [1] + nums + [1]
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] +  dp[k][j] + nums[i] * nums[k] * nums[j])

        return dp[0][n - 1]


# s = Solution()
# print s.maxCoins([4, 1, 5, 9, 7])
# kvs = [(key, value) for key, value in s.cache.items()]
# for key, value in sorted(kvs, key=lambda el: len(el[0])):
#     print key, value

s = Solution2()
print s.maxCoins([4, 1, 5, 9, 7])
kvs = [(key, value) for key, value in s.memo.items()]
for key, value in sorted(kvs, key=lambda el: len(el[0])):
    print key, value


