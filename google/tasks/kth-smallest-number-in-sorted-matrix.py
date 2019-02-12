# https://www.lintcode.com/problem/kth-smallest-number-in-sorted-matrix/description

import functools
import heapq


@functools.total_ordering
class Element:

    def __init__(self, value, i, j):
        self.value, self.i, self.j = value, i, j

    def get_neighbours(self, matrix):
        i, j = self.i + 1, self.j
        try:
            value = matrix[i][j]
        except IndexError:
            pass
        else:
            yield Element(value, i, j)

        i, j = self.i, self.j + 1
        try:
            value = matrix[i][j]
        except IndexError:
            pass
        else:
            yield Element(value, i, j)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __hash__(self):
        return hash((self.i, self.j))


class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        heap = []
        element = Element(matrix[0][0], 0, 0)
        heapq.heappush(heap, element)
        visited = set([element])
        for i in range(k):
            _min = heapq.heappop(heap)
            for neighbour in _min.get_neighbours(matrix):
                if neighbour not in visited:
                    heapq.heappush(heap, neighbour)
                    visited.add(neighbour)
        return _min.value


s = Solution()
matrix = [
    [1,2,3,4,5],
    [2,3,4,5,6],
    [3,4,5,6,7],
    [4,5,6,7,8]
]
print(s.kthSmallest(matrix, 19))
