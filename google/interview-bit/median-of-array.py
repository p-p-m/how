# Not solved but idea is right


class Pointer:
    def __init__(self, array):
        self.array = array
        self.step = len(array) // 2
        self.index = self.step
        print len(array) // 2, self.index

    def get_value(self):
        return self.array[self.index]

    def get_next_value(self):
        return self.array[self.index + 1]

    def move_left(self, step=None):
        self.step = step or self.step // 2
        if self.step == 0:
            self.step = 1
        self.index = self.index - self.step
        return self.step

    def move_right(self, step=None):
        self.step = step or self.step // 2
        if self.step == 0:
            self.step = 1
        self.index = self.index + self.step
        return self.step

    def is_end(self):
        return self.index == len(self.array) - 1

    def pprint(self):
        return (
            ' '.join([str(e) for e in self.array[:self.index]]) + ' |>' +
            ' '.join([str(e) for e in self.array[self.index:]])
        )


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        if len(A) < len(B):
            A, B = B, A

        pointerA = Pointer(A)
        pointerB = Pointer(B)
        while True:
            print 'A', pointerA.pprint()
            print 'B', pointerB.pprint()
            _max = max(pointerA.get_value(), pointerB.get_value())
            print _max
            if pointerB.is_end():
                middle = (len(A) + len(B)) // 2
            if pointerA.get_next_value() < _max:
                step = pointerB.move_left()
                pointerA.move_right(step)
                continue
            if pointerB.get_next_value() < _max:
                step = pointerB.move_right()
                pointerA.move_left(step)
                continue
            a, b = pointerA.get_value(), pointerB.get_value()
            break
        if (len(A) + len(B)) % 2 == 1:
            return min(a, b)
        else:
            return (a + b) / 2.0


# 1 4 5 6 8 11 20
# 2 3 9 9 10 12

# 1 2 3 4 5 6 (8) 8 9 10 11 12 20

# 6 + 7 = 13
# index = 7

# first_median = 6
# first_index = 4

# elements_before_median = 2


# 1 4 5 6 8 11 (20) 2 3 8 9 10 12
# 1 4 5 6 8 11 (20) 2 3 8 (9) 10 12
# 1 4 5 6 8 11 (20) 2 3 8 (9) 10 12


# 1 4 5 6 | 8 11 20
# 2 3 9 | 9 10 12

# 1 4 5 6 8 11 | 20
# 2 | 3 9 9 10 12

# 1 4 5 6 8 | 11 20
# 2 3 | 9 9 10 12

A = [1, 2, 2, 2, 7, 8]
B = [2, 3, 9, 9, 10, 12]

# 1 2 2 2 2 3 7 8 9 9 10 12

s = Solution()
print s.findMedianSortedArrays(A, B)


