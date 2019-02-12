import collections


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        queue = collections.deque()
        saved = 1
        for digit in A[::-1]:
            if digit + saved < 10:
                queue.append(digit + saved)
                saved = 0
            else:
                queue.append(0)
                saved = 1
        if saved != 0:
            queue.append(saved)

        result = []
        while queue:
            digit = queue.pop()
            if digit == 0 and len(result) == 0:
                continue
            result.append(digit)

        return result


s = Solution()
print s.plusOne([0, 0, 9, 9, 9])