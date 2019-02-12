class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        self.arrays = [A, B, C]
        indexes = [0, 0, 0]
        diffs = [self.get_diff(indexes)]
        while any([index < len(arr) - 1 for index, arr in zip(indexes, self.arrays)]):
            i = self.get_min_i(indexes)
            indexes[i] += 1
            diffs.append(self.get_diff(indexes))

        return min(diffs)

    def get_diff(self, indexes):
        values = [arr[index] for index, arr in zip(indexes, self.arrays)]
        return max(values) - min(values)

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
A = [1, 4, 5, 8, 9]
B = [6, 9, 15]
C = [2, 3, 6, 6]
print s.solve(A, B, C)
