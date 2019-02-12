import collections


class TCounter:

    def __init__(self, T):
        self.counter = collections.Counter(T)
        self.letters_count = len(T)

    def add(self, letter):
        if letter not in self.counter:
            return
        self.counter[letter] -= 1
        if self.counter[letter] >= 0:
            self.letters_count -= 1

    def remove(self, letter):
        if letter not in self.counter:
            return
        self.counter[letter] += 1
        if self.counter[letter] > 0:
            self.letters_count += 1

    def is_full(self):
        return self.letters_count == 0


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, A, B):
        _min = None
        tcounter = TCounter(B)
        start = end = 0
        while True:
            while end < len(A) and not tcounter.is_full():
                tcounter.add(A[end])
                end += 1
            if not tcounter.is_full():
                break
            while start < end and tcounter.is_full():
                tcounter.remove(A[start])
                start += 1
            substring = A[start-1: end]
            if _min is None or len(_min) > len(substring):
                _min = substring
        return '' if _min is None else _min


s = Solution()
A, B = 'ADOBECODEBANC', 'ABCG'
print s.minWindow(A, B)
