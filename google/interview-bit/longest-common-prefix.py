class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        prefix = ''
        for i in range(len(A[0])):
            letter = A[0][i]
            try:
                if any(A[j][i] != letter for j in range(1, len(A))):
                    break
                else:
                    prefix += letter
            except IndexError:
                break
        return prefix


s = Solution()
A = [
  "abcefgh",
  "abce",
  "abcefgh"
]
print s.longestCommonPrefix(A)
