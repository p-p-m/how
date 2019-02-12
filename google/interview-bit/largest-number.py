import functools


@functools.total_ordering
class Element:

    def __init__(self, value):
        self.value = str(value)


    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value + other.value > other.value + self.value


class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        elements = [Element(value) for value in A]
        elements = sorted(elements, reverse=True)
        result = ''
        for element in elements:
            if result == '0' and element.value == '0':
                continue
            result += element.value
        return result


A = [ 931, 94, 209, 448, 716, 903, 124, 372, 462, 196, 715, 802, 103, 740, 389, 872, 615, 638, 771, 829, 899, 999, 29, 163, 342, 902, 922, 312, 326, 817, 288, 75, 37, 286, 708, 589, 975, 747, 743, 699, 743, 954, 523, 989, 114, 402, 236, 855, 323, 79, 949, 176, 663, 587, 322 ]

s = Solution()
print s.largestNumber(A)


a = '9999899759549494993192290390289987285582981780279771757477437437407167157086996636386155895875234624484023893737234232632332231229288286236209196176163124114103'
b = '9999899759549499493192290390289987285582981780279771757477437437407167157086996636386155895875234624484023893737234232632332231229288286236209196176163124114103'
c = '9999899759549499493192290390289987285582981780279771757477437437407167157086996636386155895875234624484023893737234232632332231229288286236209196176163124114103'

print c == b




