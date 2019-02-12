# not soled because of incomplete description of moves

# https://www.lintcode.com/problem/android-unlock-patterns/description


class Solution:
    """
    @param m: an integer
    @param n: an integer
    @return: the total number of unlock patterns of the Android lock screen
    """
    numbers = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
    ]

    def numberOfPatterns(self, m, n):
        return 1

    def get_next_variants(self, visited, current):
        moves = (
            (1, 0), (-1, 0),  # left and right
            (0, 1), (0, -1),  # up and down
            (1, 1), (-1, 1), (1, -1), (-1, -1),  # digonals

        )
        up = current - 3
        down = current + 3
        left = current - 1
        right = current + 1
        if left % 3 == 0:
            left = None
        if right % 3 == 1:
            right = None
