import collections


def get_possible_positions(queens, row, size):
    positions = [True] * size
    for q_row, q_column in queens:
        positions[q_column] = False
        diff = row - q_row
        if q_column + diff < size:
            positions[q_column + diff] = False
        if q_column - diff >= 0:
            positions[q_column - diff] = False
    return [
        (row, index) for index, value
        in enumerate(positions) if value
    ]

class Board:
    def __init__(self, queens, row, size):
        self.queens = queens
        self.row = row
        self.size = size

    def get_next_boards(self):
        for position in get_possible_positions(self.queens, self.row + 1, self.size):
            yield Board(self.queens + [position], self.row + 1, self.size)

    def __repr__(self):
        return 'S{}:{}'.format(self.row, '>'.join([str(queen) for queen in self.queens]))


class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        queue = collections.deque([
            Board([position], 0, A) for position in get_possible_positions([], 0, A)
        ])
        results = []
        while queue:
            board = queue.pop()
            if len(board.queens) == A:
                results.append(board.queens)
                continue
            for b in board.get_next_boards():
                queue.append(b)
        return [self.format_result(r) for r in results]

    def format_result(self, result):
        formatted = []
        for _, column in result:
            formatted.append(''.join(['Q' if i == column else '.' for i in range(len(result))]))
        return formatted


s = Solution()
print s.solveNQueens(4)

