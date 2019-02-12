# https://www.lintcode.com/problem/sort-transformed-array/description


class Solution:
    """
    @param nums: a sorted array
    @param a:
    @param b:
    @param c:
    @return: a sorted array
    """
    def sortTransformedArray(self, nums, a, b, c):
        if not nums:
            return []
        self.a, self.b, self.c = a, b, c
        if a == 0:
            if b > 0:
                return list(self.merge(nums, []))
            if b < 0:
                return list(self.merge(nums[::-1], []))
            return [self.f(num) for num in nums]
        head = - b / (2 * a)
        if a > 0:
            before = [num for num in nums if num < head][::-1]
            after = [num for num in nums if num >= head]
            return list(self.merge(before, after))
        if a < 0:
            before = [num for num in nums if num < head]
            after = [num for num in nums if num >= head][::-1]
            return list(self.merge(before, after))

    def merge(self, before, after):
        i = j = 0

        if len(before) > 0:
            before_value = self.f(before[i])

        if len(after) > 0:
            after_value = self.f(after[j])

        while len(before) > 0 and len(after) > 0:
            if before_value < after_value:
                yield before_value
                i += 1
                if i >= len(before):
                    break
                before_value = self.f(before[i])
            else:
                yield after_value
                j += 1
                if j >= len(after):
                    break
                after_value = self.f(after[j])

        while i < len(before):
            yield before_value
            i += 1
            if i >= len(before):
                break
            before_value = self.f(before[i])

        while j < len(after):
            yield after_value
            j += 1
            if j >= len(after):
                break
            after_value = self.f(after[j])

    def f(self, x):
        return self.a * x ** 2 + self.b * x + self.c


s = Solution()
print s.sortTransformedArray([-4,-2,2,4], 0, -1, 5)