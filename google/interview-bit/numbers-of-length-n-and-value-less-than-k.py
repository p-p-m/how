# import itertools


# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @param C : integer
#     # @return an integer
#     def solve(self, A, B, C):
#         if B > len(str(C)):
#             return 0
#         numbers = [str(a) for a in A]
#         result = 0
#         for number in itertools.product(numbers, repeat=B):
#             if number[0] == '0' and len(number) > 1:
#                 continue
#             if int(''.join(number)) < C:
#                 result += 1
#         return result


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if B > len(str(C)):
            return 0
        if B < len(str(C)):
            return len([v for v in A if v > 0]) * len(A) ** (B - 1)
        return self.count(A, C)


    def count(self, A, C):
        print A, C
        first_digit = int(str(C)[0])
        try:
            equal = next(a for a in A if a == first_digit)
        except StopIteration:
            return len([v for v in A if v != 0 and v < first_digit]) * len(A) ** (len(str(C)) - 1)
        else:
            result = len([v for v in A if v != 0 and v < first_digit]) * len(A) ** (len(str(C)) - 1)
            print result
            A.remove(equal)
            try:
                C = int(str(C)[1:])
            except ValueError:
                result += len([v for v in A])
            result += self.count(A, C)
            print 'result', result
            return result


s = Solution()
print s.solve([1, 2, 5], 3, 219)





# s = Solution()
# print s.solve([ 0, 1, 2, 3, 4, 5, 7, 8, 9 ], 5, 51822)