class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A) < 1:
            return 0
        if len(A) < 4:
            return max(A) - min(A)
        left = self.get_left_maxmin(A)
        right = self.get_right_maxmin(A)
        _max = None
        for i in range(len(left) - 2):
            j = len(right) - i - 1 - 2
            left_diff = left[i][0] - left[i][1]
            right_diff = right[j][0] - right[j][1]
            if _max is None or _max < left_diff + right_diff:
                _max = left_diff + right_diff
        return _max

    def get_left_maxmin(self, A):
        maxmin = [(max(A[0], A[1]), min(A[0], A[1]))]
        for i in range(2, len(A)):
            value = A[i]
            previous_max, previous_min = maxmin[-1]
            maxmin.append([max(previous_max, value), min(previous_min, value)])
        return maxmin

    def get_right_maxmin(self, A):
        maxmin = [(max(A[-1], A[-2]), min(A[-1], A[-2]))]
        for i in range(-3, -len(A) - 1, -1):
            value = A[i]
            previous_max, previous_min = maxmin[-1]
            maxmin.append([max(previous_max, value), min(previous_min, value)])
        return maxmin

# s = Solution()
# print s.maxProfit([1, 2, 3, 5])

print [1, 2][0:0]
