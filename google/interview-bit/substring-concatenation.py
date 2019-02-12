import collections
import itertools


class MyCounter:

    def __init__(self, B):
        self.counter = collections.Counter(B)
        self.B = B
        self.l = len(B[0])

    def reset(self):
        self.counter = collections.Counter(self.B)

    def is_valid_substring(self, substring):
        start = 0
        for start in range(0, len(substring), self.l):
            if substring[start: start + self.l] not in self.counter:
                self.reset()
                return False
            self.counter[substring[start: start + self.l]] -= 1
            if self.counter[substring[start: start + self.l]] < 0:
                self.reset()
                return False
        self.reset()
        return True


class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        my_counter = MyCounter(B)
        length = len(B[0]) * len(B)
        start = 0
        end = length
        result = []
        while end <= len(A):
            if my_counter.is_valid_substring(A[start: end]):
                result.append(start)
            start += 1
            end += 1
        return result

s = Solution()
A, B = "barfoothefoobarman", ["foo", "bar"]
print s.findSubstring(A, B)

