class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def order(self, A, B):
        heights = A
        infronts = B
        indexes = range(len(A))
        results = [None] * len(A)

        for height, infront in sorted(zip(heights, infronts)):
            index = indexes.index(infront)
            for i in range(index, len(indexes)):
                if indexes[i] is not None:
                    indexes[i] -= 1
            indexes[index] = None
            results[index] = height

        return results


# s = Solution()
# A, B = [5, 3, 2, 6, 1, 4], [0, 1, 2, 0, 3, 2]
# print s.order(A, B)

print [1, 2, 3][1:2]
