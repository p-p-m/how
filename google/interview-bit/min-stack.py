import collections


class MinStack:

    def __init__(self):
        self.stack = collections.deque()
        self.min_stack = collections.deque()

    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(self.min_stack[-1], x))

    # @return nothing
    def pop(self):
        if not self.stack:
            return
        x = self.stack.pop()
        self.min_stack.pop()
        return x

    # @return an integer
    def top(self):
        if not self.stack:
            return -1
        return self.stack[-1]


    # @return an integer
    def getMin(self):
        if not self.stack:
            return -1
        return self.min_stack[-1]


s = MinStack()
s.pop()
print s.top()
print s.getMin()