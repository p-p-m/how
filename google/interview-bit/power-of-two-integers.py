class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A == 1:
            return 1
        _max = int(A ** 0.5)
        _range = range(_max + 1)
        for number in _range:
            value = number
            if number < 2 or number is None:
                continue
            while A % value == 0:
                value = value * number
                if value == A:
                    return 1
                try:
                    _range[value] = None
                except IndexError:
                    pass

        return 0


s = Solution()
print s.isPower(536870912)

print 2 ** 29