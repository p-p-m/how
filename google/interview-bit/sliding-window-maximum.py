import collections


class Window:

    def __init__(self, elements):
        self._max = max(elements)
        self.stack = collections.deque(elements)
        self.max_stack = collections.deque([self._max] * len(elements))

    def append(self, value):
        self.stack.append(value)
        self.max_stack

    def move(self, element):
        self.stack.popleft()
        self.stack.append(element)
        result = []
        while self.stack[0] < element:
            result.append(element)
            self.stack.popleft()

            if el < element:
                result.append(elements)
                self.stack.popleft()
            else:
                result.append.
        while self.stack[-1] < element:
            self.stack.popleft()
            self.stack.append(element)

        self._max = max(self.stack)


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        window = Window(A[:B])
        result = [window._max]
        for i in range(len(A) - B):
            window.move(A[i + B])
            result.append(window._max)
        return result

s = Solution()
print s.slidingMaximum([1, 3, -1, -3, 1, 5, 3, 6, 7], 3)
