class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        start = 0
        end = len(A) - 1
        has_symbol = False
        self.symbols = ['*', '/', '+', '-']
        while start < end:
            start, start_has_symbol = self.go_forward(start, end, A)
            end, end_has_symbol = self.go_back(start, end, A)
            if not start_has_symbol and not end_has_symbol and start < end:
                return 1

    def go_forward(self, start, end, A):
        has_symbol = False
        while A[start] != '(' and start < end:
            if A[start] in self.symbols:
                has_symbol = True
            start += 1
        return start + 1, has_symbol

    def go_back(self, start, end, A):
        has_symbol = False
        while A[end] != ')' and start < end:
            if A[start] in self.symbols:
                has_symbol = True
            start += 1
        return start + 1, has_symbol



import collections


class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = collections.deque([])
        symbols = ['*', '/', '+', '-']
        for c in A:
            if c == '(':
                stack.append('(')
            if c in symbols:
                if stack and stack[-1] == '+':
                    continue
                stack.append('+')
            if c == ')':
                removed = stack.pop()
                if removed == '(':
                    return 1
                else:
                    stack.pop()
            print stack
        if not stack:
            return 1
        return 0


s = Solution()
print s.braces('()')





