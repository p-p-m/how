# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def hammingDistance(self, A):
#         _max = max(A)
#         mask = 1
#         result = 0
#         while mask <= _max:
#             zeros = 0
#             ones = 0
#             for value in A:
#                 if value & mask > 0:
#                     ones += 1
#                 else:
#                     zeros += 1
#             result += zeros * ones
#             mask *= 2
#         return result * 2


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        A = [bin(value)[2:][::-1] for value in A]
        max_length = max([len(value) for value in A])
        result = 0
        for i in range(max_length):
            zeros = 0
            ones = 0
            for value in A:
                try:
                    digit = value[i]
                except IndexError:
                    digit = '0'

                if digit == '1':
                    ones += 1
                else:
                    zeros += 1
            result += 2 * zeros * ones
        return result



s = Solution()
print s.hammingDistance([16, 0, 1, 0, 0, 16, 0, 0, 0, 0, 9, 4, 0, 0, 0, 0, 0, 0, 2, 8, 0])

# print bin(9 ^ 4).count('1')
# print bin(9 ^ 12).count('1')

# 1001
# 1100

# 001 1
# 010 2
# 101 5
# 011 3

# 3 * 1
# 2 * 2
# 3 * 1