# https://www.lintcode.com/problem/decode-string/description
import re


class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        while True:
            old_s = s[:]
            s = self.replace(s)
            if s == old_s:
                break
        return s

    def replace(self, s):
        match = re.search(r'(?P<repetitions>\d+)\[', s)
        if not match:
            return s
        repetitions = int(match.groups(0)[0])
        origin = self.get_inside_text(s[match.end(0):])
        text = self.replace(origin)
        new_s = s[0:match.start(0)] + text * repetitions + s[match.end(0) + len(origin) + 1:]
        return new_s

    def get_inside_text(self, s):
        count = 1
        inside = ''
        for c in s:
            inside += c
            if c == '[':
                count += 1
            if c == ']':
                count -= 1
            if count == 0:
                return inside[:-1]



s = Solution()
print s.expressionExpand('2[q]aa2[qw3[e]]aa')
# print(re.search(r'(?P<number>\d+)\[.+\]', 'asa4[wq]3[2[ad]3[pf]]xyz3[df]').groups())
