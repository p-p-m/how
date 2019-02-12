import collections
import operator


class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        if len(A) == 1:
            return A[0]
        stack = collections.deque([])
        result = None
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.floordiv,
        }
        for a in A:
            try:
                a = int(a)
            except ValueError:
                if a not in operations:
                    raise Exception('Invalid {}'.format(a))
                right = stack.pop()
                left = stack.pop()
                result = operations[a](left, right)
                stack.append(result)
            else:
                stack.append(int(a))

        return result


s = Solution()
A = ["-500", "-10", "/"]
print s.evalRPN(A)

2 - 1 // 3
