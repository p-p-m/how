class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        result = []
        for a in A:
            result = self.add(result, a)
        return self.to_number(result)

    def add(self, result, a):
        for i, bit in enumerate(bin(a)[2:][::-1]):
            try:
                result[i] = (result[i] + int(bit)) % 3
            except IndexError:
                result.append(int(bit))
        return result

    def to_number(self, result):
        number = 0
        mult = 1
        for a in result:
            if a == 1:
                number += mult
            mult *= 2
        return number


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        first = 0
        second = 0
        for n in A:
            # Set the bits to first, if the bits were already set,
            # they are going to get toggled, then we check if they aren't
            # in the second variable by doign a negation of the variable and
            # an and
            first = (first ^ n) & ~second
            # We do another xor in case the first one toggled the bits, and
            # After that we need to check that we don't have any bits set in
            # the first bitset.
            second = (second ^ n) & ~first
        return first

print bin(~3), bin(~5)

s = Solution()
print s.singleNumber([1, 1, 1, 4, 6, 6, 6, 7, 7, 7, 11, 11, 11])
