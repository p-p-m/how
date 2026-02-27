class Solution:

    def combine(self, n, k):
        pointers = list(range(1, k + 1))
        results = []
        index = -1
        limit = n
        if k < 0 or n < 0:
            return []
        if k == n:
            return [pointers]
        if k > n:
            return []


        while True:

            if pointers[index] < limit:
                results.append(pointers[:])
                pointers[index] += 1
                continue

            if pointers[index] == limit:
                results.append(pointers[:])
                limit -= 1
                index -=1
                try:
                    pointers[index] += 1
                except IndexError:
                    break
                continue

        return results


s = Solution()
# print([1, 2, 3][-3])
print(s.combine(4, 2))


