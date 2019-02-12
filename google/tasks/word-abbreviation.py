# https://www.lintcode.com/problem/word-abbreviation/description


class Solution:
    """
    @param dict: an array of n distinct non-empty strings
    @return: an array of minimal possible abbreviations for every word
    """
    def wordsAbbreviation(self, dict):
        self._dict = dict
        self._dict = [(self.to_abbr(word), word) for word in sorted(self._dict)]
        for i in range(1, len(self._dict)):
            first_abbr, first_word =

    def to_abbr(self, word, start=0, end=-1):
        return word[start] + str(len(word) - (start - end + 1)) + word[end]


