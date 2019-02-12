# Not soled fully

class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        value = 0
        operation = '+'
        for index, el in enumerate(s):
            if el == ' ':
                continue
            if el.isdigit():
                value = self._add(value, el, operation)
            if el == '+' or el == '-':
                operation = el
        return value

    def _add(self, a, b, operation):
        print a, b, operation
        if operation == '+':
            return a + int(b)
        if operation == '-':
            return a - int(b)
        raise Exception('Invalid operation')

    def find_inside_braces(self, s):
        open_count = 1
        new_s = ''
        for el in s:
            if el == ')':
                open_count -= 1
            if el == '(':
                open_count += 1
            if open_count == 0:
                return new_s
            new_s += el
        raise Exception('String is not valid')

print '+'.isdigit()
s = Solution()
print s.calculate('1 + 2 - 10')