class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        return [self.bs_left(A, B), self.bs_right(A, B)]

    def bs_left(self, A, B):
        if A[0] == B:
            return 0
        left = 0
        right = len(A) - 1
        while left <= right:
            middle = (left + right) // 2
            if A[middle] == B:
                if middle - 1 < 0 or A[middle - 1] != B:
                    return middle
                right = middle - 1
            if A[middle] > B:
                right = middle - 1
            if A[middle] < B:
                left = middle + 1
        return -1

    def bs_right(self, A, B):
        if A[-1] == B:
            return len(A) - 1
        left = 0
        right = len(A) - 1
        while left <= right:
            middle = (left + right) // 2
            if A[middle] == B:
                if middle + 1 >= len(A) or A[middle + 1] != B:
                    return middle
                left = middle + 1
            if A[middle] > B:
                right = middle - 1
            if A[middle] < B:
                left = middle + 1
        return -1

s = Solution()
print s.searchRange([1], 1)