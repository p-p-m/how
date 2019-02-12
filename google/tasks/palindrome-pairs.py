# https://www.lintcode.com/problem/palindrome-pairs/description

class Solution:
    """
    The most important part is to think about break a word apart.
    If part of the word is palindromic, then all we need is to look for the reversed version of the other part
    in the word list.

    @param words: a list of unique words
    @return: all pairs of distinct indices
    """
    def palindromePairs(self, words):
        # Write your code here
        if not words:
            return []

        table = dict()
        for idx, word in enumerate(words):
            table[word] = idx

        ans = []
        for idx, word in enumerate(words):
            size = len(word)

            for i in range(size + 1):
                leftSub = word[:i]
                rightSub = word[i:]

                if self.isPalindrome(leftSub):
                    reversedRight = rightSub[::-1]
                    if reversedRight in table and table[reversedRight] != idx:
                        ans.append([table[reversedRight], idx])

                if len(rightSub) > 0 and self.isPalindrome(rightSub):
                    reversedLeft = leftSub[::-1]
                    if reversedLeft in table and table[reversedLeft] != idx:
                        ans.append([idx, table[reversedLeft]])
        return ans

    def isPalindrome(self, word):
        if not word:
            return True

        left = 0
        right = len(word) - 1

        while left <= right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1

        return True