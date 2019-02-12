class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        l = [el.strip() for el in A.strip().split(' ') if el.strip()]
        return ' '.join(l[::-1])


s = Solution()
print s.reverseWords('  asd  ')
