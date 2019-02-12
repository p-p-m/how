class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        if not B or not A:
            return -1
        return self.search(A, B)

    def search(self, s, p):
        lps = self.get_lps(p)
        i = j = 0
        while i < len(s):
            if s[i] == p[j]:
                i += 1
                j += 1
                if j == len(p):
                    return i - j
            elif j > 0:
                j = lps[j - 1]
            elif j == 0:
                i += 1
        return -1

    def get_lps(self, s):
        result = [0]
        for i in range(1, len(s)):
            j = result[i - 1]
            while s[i] != s[j] and j > 0:
                j = result[j - 1]
            if s[i] == s[j]:
                result.append(j + 1)
            else:
                result.append(j)
        return result


s = Solution()
print s.strStr('a', '')