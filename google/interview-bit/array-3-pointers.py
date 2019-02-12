class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        self.arrays = [A, B, C]
        indexes = [0, 0, 0]
        diffs = [self.get_diff(indexes)]
        while any([index < len(arr) - 1 for index, arr in zip(indexes, self.arrays)]):
            i = self.get_min_i(indexes)
            indexes[i] += 1
            diffs.append(self.get_diff(indexes))

        return min(diffs)

    def get_diff(self, indexes):
        A, B, C = self.arrays
        i, j, k = indexes
        return max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

    def get_min_i(self, indexes):
        _min = min_i = None
        for i, (index, arr) in enumerate(zip(indexes, self.arrays)):
            if index + 1 == len(arr):
                continue
            if _min is None or arr[index + 1] < _min:
                _min = arr[index + 1]
                min_i = i
        return min_i


s = Solution()
A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 12]
print s.minimize(A, B, C)

