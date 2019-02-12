# class Solution:
#     # @param A : string
#     # @param B : integer
#     # @return a strings
#     def convert(self, A, B):
#         result = ''
#         step = self.get_step(B)
#         for start in range(B):
#             result += self._next(A, start, step)
#         return result

#     def _next(self, A, start, step):
#         result = ''
#         index = start
#         while index < len(A):
#             result += A[index]
#             index += step
#         print result
#         return result

#     def get_step(self, B):
#         return (B - 1) * 2


class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        if B == 1:
            return A
        lines = [''] * B
        index = 0
        move = 1
        for i in range(len(A)):
            lines[index] += A[i]
            index += move
            if index == B - 1:
                move = -1
            elif index == 0:
                move = 1
        return ''.join(lines)

s = Solution()
print s.convert('Baaa', 1)
