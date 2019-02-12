# https://www.lintcode.com/problem/sentence-screen-fitting/description



# class DoesNotFit(Exception):
#     pass


# class Solution:
#     """
#     @param sentence: a list of string
#     @param rows: an integer
#     @param cols: an integer
#     @return: return an integer, denote times the given sentence can be fitted on the screen
#     """
#     def wordsTyping(self, sentence, rows, cols):
#         row = 0
#         count = 0
#         col_index = 0
#         word_index = 0
#         while row < rows:
#             try:
#                 col_index = self.add_word(sentence[word_index], col_index, cols)
#             except DoesNotFit:
#                 if col_index == 0:
#                     return 0
#                 else:
#                     col_index = 0
#                     row += 1
#             else:
#                 word_index += 1
#                 if word_index == len(sentence):
#                     count += 1
#                     word_index = 0
#         return count

#     def add_word(self, word, col_index, cols):
#         if col_index + len(word) <= cols:
#             return col_index + len(word) + 1
#         else:
#             raise DoesNotFit

# s = Solution()
# print s.wordsTyping(["I", "had", "apple", "pie"], 4, 5)


# This solutions
class Solution:

    def wordsTyping(self, sentence, rows, cols):
        rx = 0
        count = 0
        index = 0
        while rx < rows:
            cx = 0
            while cx < cols:
                if cx + len(sentence[index])  <= cols:
                    cx += len(sentence[index]) + 1
                    index += 1
                else:
                    break
                if index == len(sentence):
                    count += 1
                    index = 0
            rx += 1
        return count


s = Solution()
print s.wordsTyping(["I", "had", "appleww", "pie"], 4, 5)