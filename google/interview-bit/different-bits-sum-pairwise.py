class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        s = 0
        for column in self.get_columns(A):
            s += self.calculate(column)
        return s * 2

    def calculate(self, column):
        ones = zeros = 0
        for el in column:
            if el == 1:
                ones += 1
            else:
                zeros += 1
        return ones * zeros

    def get_columns(self, A):
        rbins = []
        max_l = 0
        for a in A:
            b = bin(a)[2:][::-1]
            rbins.append(b)
            if len(b) > max_l:
                max_l = len(b)

        for i in range(max_l):
            column = []
            for b in rbins:
                if i < len(b):
                    column.append(int(b[i]))
                else:
                    column.append(0)
            yield column


s = Solution()
print s.cntBits([1, 3, 5])