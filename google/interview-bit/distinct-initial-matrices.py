import math


class Solution:
    # @param A : list of integers
    # @return an integer
    def cntMatrix(self, A):
        if not A:
            return 0
        if len(A) == 1:
            return 1
        result = 1
        for ph in self.get_possible_heights(A):
            print ph, self.fits(A, ph)
            if self.fits(A, ph):
                result += self.get_possibilities(len(A) // ph, ph)
        return result % (10 ** 9 + 7)

    def get_possibilities(self, columns_count, height):
        if height == 1:
            return 1
        return math.factorial(height) ** columns_count

    def get_possible_heights(self, A):
        return [i for i in range(2, (len(A) // 2) + 1) if len(A) % i == 0] + [len(A)]

    def fits(self, A, ph):
        i = 1
        while i*ph <= len(A):
            if not self.is_asc(A[(i-1) * ph: i * ph]):
                return False
            i += 1
        return True

    def is_asc(self, a):
        for i in range(1, len(a)):
            if a[i-1] > a[i]:
                return False
        return True


s = Solution()
A = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 46, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 25, 47, 48, 49, 50 ]
print s.cntMatrix(A)
