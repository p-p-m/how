s = "))((((())))(("
print len(s)

# digits = set([str(i) for i in range(10)])
# supported_operations = {'*', '+', '-', '/'}


# def _is_valid(expression, begin, end):
#     opened_brackets = 0
#     operation_in_begin = False
#     has_digits = False
#     for i in range(begin, end):
#         if expression[i] == ' ':
#             continue
#         elif expression[i] in digits:
#             if not operation_in_begin: return False
#             has_digits = True
#         elif expression[i] in supported_operations:
#             if operation_in_begin: continue
#             if not has_digits and opened_brackets:
#                 operation_in_begin = True
#             else:
#                 return False
#         elif expression[i] == '(':
#             opened_brackets += 1
#         elif expression[i] == ')':
#             opened_brackets -= 1
#             if opened_brackets < 0: return False
#         else: return False

#     return opened_brackets == 0 and has_digits and operation_in_begin


# def _eval(expression, begin, end):
#     if not _is_valid(expression, begin, end): raise ValueError("Wrong format.")

#     operation = None
#     numbers = []

#     was_first_bracket = False

#     i = begin
#     while i < end:
#         if expression[i] == ' ': pass
#         if expression[i] == '(':
#             if not was_first_bracket:
#                 was_first_bracket = True
#             else:
#                 open_brackets = 1
#                 j = i + 1
#                 while open_brackets != 0:
#                     if expression[j] == '(': open_brackets += 1
#                     if expression[j] == ')': open_brackets -= 1
#                     j += 1

#                 numbers.append(_eval(expression, i, j))
#                 i = j
#                 continue

#         elif expression[i] in supported_operations and operation is None:
#             operation = expression[i]
#         elif expression[i] in digits:
#             j = i
#             while expression[j] in digits:
#                 j += 1

#             numbers.append(int(expression[i:j]))
#             i = j
#             continue

#         i += 1

#     if operation == '+':
#         return sum(numbers)
#     elif operation == '*':
#         prod = 1
#         for value in numbers:
#             prod *= value
#         return prod


# def calculate_expression(expr):
#     return _eval(expr, 0, len(expr))


# if __name__ == '__main__':
#     expr = "(+1 2)"
#     v = calculate_expression(expr)
#     print(v)
