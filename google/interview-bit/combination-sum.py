class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        self.cache = {}
        results = self.diff(A, B)
        results = set([tuple(sorted(result)) for result in results])
        return sorted(results)

    def diff(self, candidates, target):
        results = []
        for candidate in candidates:
            if target - candidate == 0:
                results.append([candidate])
            elif target - candidate > 0:
                for r in self.diff(candidates, target - candidate):
                    results.append([candidate] + r)
        self.cache[target] = results
        return results


s = Solution()
print s.combinationSum([2, 3, 6, 7], 7)
