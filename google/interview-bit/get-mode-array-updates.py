import collections
import functools


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def getMode(self, A, B):
        l = [None] * len(A)
        c = collections.Counter()
        for key, count in c.most_common():
            if l[count]:
                l[count].append(key)
            else:
                l[count] = [key]
        max_index = max(i for i, el in enumerate(l) if el is not None)
        result = []
        for swap in B:
            previous = A[swap[0] - 1]
            new = swap[1]



            c[previous] -= 1
            if new in c:
                c[new] += 1
            else:
                c[new] = 1


            result.append(self.get_mode(c))
            A[swap[0] - 1] = new
        return result

    def get_mode(self, c):
        _count = None
        _key = None
        for key, count in c.items():
            if count == _count and key < _key:
                _key = key
            if _count is None or count > _count:
                _count = count
                _key = key
        return _key

s = Solution()
A = [ 2, 2, 2, 2, 2 ]
B = [
  [4, 1],
  [3, 1],
  [3, 1],
  [2, 1],
  [4, 2]
]
print s.getMode(A, B)