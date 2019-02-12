def pack_line(words, max_length):
    cur_line = []
    while words:
        next_word = words[0]
        if len(' '.join(cur_line + [next_word])) <= max_length:
            cur_line.append(next_word)
            words = words[1:]
        else:
            break
    return cur_line, words


def my_justify(words, max_length):
    res = []
    while words:
        res_line = ''
        next_line, words = pack_line(words, max_length)
        if len(next_line) == 1:
            pass
        spaces_num = len(next_line) - 1
        if spaces_num == 0 or not words:  # last line or single word line
            res_line += ' '.join(next_line)
            res_line += ' ' * (max_length - len(res_line))  # fill in right side with spaces
        else:
            spaces_len = max_length - len(''.join(next_line))
            single_space_len = spaces_len // spaces_num
            extra_spaces_num = spaces_len % spaces_num
            for i, word in enumerate(next_line):
                res_line += word
                if i < spaces_num:
                    res_line += ' ' * single_space_len
                if i < extra_spaces_num:
                    res_line += ' '
        res.append(res_line)
    return res


class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        return my_justify(A, B)




a = ["What", "must", "be", "shall", "be."]
l = 15

s = Solution()
print s.fullJustify(a, l)