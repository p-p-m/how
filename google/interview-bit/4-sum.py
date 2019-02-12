import collections


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        d = self.to_d(A)
        results = set()
        for i, j, k, required in self.gen_triplets(A, B):
            if required not in d:
                continue
            try:
                g = next(index for index in d[required] if index not in (i, j, k))
            except StopIteration:
                continue
            results.add(tuple(sorted([A[i], A[j], A[k], A[g]])))
        return sorted(results)

    def to_d(self, A):
        d = collections.defaultdict(list)
        for index, value in enumerate(A):
            d[value].append(index)
        return d

    def gen_triplets(self, A, B):
        for i in range(len(A) - 2):
            for j in range(i + 1, len(A) - 1):
                for k in range(j + 1, len(A)):
                    yield i, j, k, B - A[i] - A[j] - A[k]

s = Solution()
A, B = [1, 0, -1, 0, -2, 2], 0
print s.fourSum(A, B)
