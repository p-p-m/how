# NOT SOLVED

class ValueFound(Exception):
    pass


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        pass

    def find(self, A, B, start, end):
        if end - start <= 5:
            for i in range(start, end - 1):
                if A[i] > A[i + 1]:
                    return i

        first = A[start]
        last = A[end]
        middle_index = (start + end) // 2 + 1
        middle = A[middle_index]

        if middle > last:
            return middle_index
        is_gap_left = first > middle
        is_gap_right = !is_gap_left
        if is_gap_left and B > middle:
            return rbs(A, B, middle)


    def simple_find(self, A, B, start, end):
        for i in range(start, end):
            if A[i] == B:
                return i
        return -1

    def rbs(self, A, B, start, end):
        if end - start <= 5:
            return self.simple_find(A, B, start, end)
        middle_index = (start + end) // 2 + 1
        middle = A[middle_index]
        if middle == B:
            raise ValueFound(middle_index)
        if middle > B:
            return self.rbs(A, B, start, middle_index)
        if middle < B:
            return self.rbs(A, B, middle_index, end)


s = Solution()
A = [0, 1, 2, 3, 4, 5, 6, 9]
print s.rbs(A, 9, 0, len(A))


6 7 0 1 2 4 5

