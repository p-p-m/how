# class Solution:
#     # @param A : list of list of integers
#     # @return an integer
#     def findMedian(self, A):
#         n = len(A)
#         m = len(A[0])
#         pointers = [0] * len(A)
#         count = 0
#         while count < (n * m) // 2 + 1:
#             min_index = None
#             _min = None
#             for index, pointer in enumerate(pointers):
#                 if pointer == m:
#                     continue
#                 if _min is None or A[index][pointer] < _min:
#                     _min = A[index][pointer]
#                     min_index = index
#             pointers[min_index] += 1
#             count += 1
#         pointer = pointers[min_index]
#         return A[min_index][pointer - 1]

# s = Solution()
# A = [
#     [1, 3, 9],
#     [2, 6, 9],
#     [3, 6, 9],
# ]
# print s.findMedian(A)


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        _max = max([max(row) for row in A])
        _min = min([min(row) for row in A])
        step = (_max - _min) // 2
        value = _min
        median_index = (len(A) * len(A[0])) // 2 + 1
        while True:
            s_count, se_count = self.get_s_and_se_count(A, value)
            if s_count < median_index and se_count >= median_index:
                return value
            elif s_count < median_index and se_count < median_index:
                value += step
            elif s_count >= median_index:
                value -= step
            step = max(step // 2, 1)

    def get_s_and_se_count(self, A, value):
        s_count = 0
        se_count = 0
        for row in A:
            s_count += len([1 for el in row if el < value])
            se_count += len([1 for el in row if el <= value])
        return s_count, se_count


s = Solution()
A = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9],
]
print s.findMedian(A)
