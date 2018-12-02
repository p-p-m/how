# coding: utf-8
"""
In chess, queens can move any number of squares vertically, horizontally, or
diagonally. The n-queens puzzle is the problem of placing n queens on an
n × n chessboard so that no two queens can attack each other.

Given an integer n, print all possible distinct solutions to the n-queens
puzzle. Each solution contains distinct board configurations of the placement
of the n queens, where the solutions are arrays that contain permutations of
[1, 2, 3, .. n]. The number in the ith position of the results array
indicates that the ith column queen is placed in the row with that number.
In your solution, the board configurations should be returned in
lexicographical order.
"""


# class Board(object):

#     def __init__(self, n):
#         self.n = n
#         self.data = [[False] * n for _ in range(n)]
#         self.row = 0

#     def add_queen(self, column):
#         if self.data[self.row][column]:
#             raise ValueError
#         for i in range(self.n):
#             self.data[self.row][i] = True
#         for i in range(self.n):
#             self.data[i][column] = True
#         for i in range(self.n):
#             try:
#                 self.data[i][column + i] = True
#             except IndexError:
#                 pass
#         self.row += 1

#     def visualize(self):
#         for r in self.data:
#             for el in r:
#                 print 'x' if el else '0',
#             print ''


# def try_one(column, n):


# n = 4
# b = Board(n)
# for i in range(n):
#     for j in range(n)
#         b.add_queen(i)
# b.add_queen(0)
# b.visualize()

# xqxxxx
# xxxqxx
# 0xxxx0

def get_places(exist, n):
    data = [True] * n
    current_row = len(exist)
    for index, el in enumerate(exist):
        data[el] = False
        i = el + current_row - index
        if -1 < i < n:
            data[i] = False
        i = el - current_row + index
        if -1 < i < n:
            data[i] = False
    return [ind for ind, el in enumerate(data) if el]


def q(existing, n):
    new = []
    for e in existing:
        places = get_places(e, n)
        new += [e[:] + [place] for place in places]

    return new


def nQueens(n):
    existing = [[p] for p in get_places([], n)]
    for i in range(n - 1):
        existing = q(existing, n)
    return [[el + 1 for el in l] for l in sorted(existing)]


n = 4
print nQueens(n)
