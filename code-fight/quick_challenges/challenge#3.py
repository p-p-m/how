# textJustification(words, l) = ["This    is    an",
#                                "example  of text",
#                                "justification.  "]

words = ["This", "is", "an", "example", "of", "text", "justification."]
l = 16

ms = 7
words = ["This", "is", "an", "example"]
for i in range(ms):
    words[i % (len(words) - 1)] += ' '
print words
