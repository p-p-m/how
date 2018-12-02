# Best solution
# def firstDuplicate(A):
#     for x in A:
#         A[abs(x) - 1] *= -1
#         if A[abs(x) - 1] > 0:
#             return abs(x)
#     return -1


# My solution
# def firstDuplicate(a):
#     reviewed = set()
#     for el in a:
#         if el in reviewed:
#             return el
#         reviewed.add(el)
#     return -1


# a = [1, 2, 3, 3, 4, 5]
# print(firstDuplicate(a))
