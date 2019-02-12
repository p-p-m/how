import itertools


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        lines = []
        for i, c in enumerate(B[::-1]):
            lines.append(self._mult(A, c) + '0' * i)
        result = reduce(lambda x, y: self._sum(x, y), lines).lstrip('0')
        if not result:
            return '0'
        return result

    def _mult(self, A, c):
        c = int(c)
        remember = 0
        result = ''
        for a in A[::-1]:
            a = int(a)
            mult = a * c + remember
            remember = mult // 10
            result += str(mult % 10)
        if remember:
            result += str(remember)
        return result[::-1]

    def _sum(self, s1, s2):
        result = ''
        remember = 0
        for c1, c2 in itertools.izip_longest(s1[::-1], s2[::-1], fillvalue='0'):
            c1 = int(c1)
            c2 = int(c2)
            _sum = c1 + c2 + remember
            if _sum > 9:
                remember = 1
            else:
                remember = 0
            result += str(_sum % 10)
        if remember == 1:
            result += '1'

        return result[::-1].lstrip('0')


s = Solution()
print s.multiply('12332', '0')
