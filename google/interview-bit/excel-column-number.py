import string


class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        _map = {l: index + 1 for index, l in enumerate(string.ascii_uppercase)}
        result = 0
        multiplier = 1
        for letter in A[::-1]:
            result += _map[letter] * multiplier
            multiplier *= 26
        return result


s = Solution()
print s.titleToNumber('AAZD')
