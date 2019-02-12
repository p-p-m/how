# https://www.lintcode.com/problem/coin-path/description


class Solution:
    """
    @param A: a list of integer
    @param B: an integer
    @return: return a list of integer
    """
    def cheapestJump(self, A, B):
        self.A = A
        self.B = B
        self.coins = [[None, None] for i in range(len(self.A))]
        self.coins[0][0] = self.A[0]
        for i in range(len(self.coins)):
            self.calculate(i)
        return list(self.go_back())[::-1]

    def calculate(self, start):
        print 'Start', start, 'coins', self.coins
        if self.coins[start][0] is None:
            return
        for i in range(start + 1, min(start + self.B + 1, len(self.A))):
            if self.A[i] == -1:
                continue
            if self.coins[i][0] is None or self.coins[start][0] + self.A[i] <= self.coins[i][0]:
                self.coins[i] = [self.coins[start][0] + self.A[i], start]

    def go_back(self):
        if self.coins[-1][1] is None:
            return
        yield len(self.coins)
        current = self.coins[-1]
        while current[1] is not None:
            yield current[1] + 1
            current = self.coins[current[1]]

s = Solution()
print s.cheapestJump([1, -1, -1, -1, 5], 2)
print s.coins

# Start 0 coins [[1, None], [1000, None], [1000, None], [1000, None], [1000, None]]
# Start 1 coins [[1, None], [3, 0], [100, 0], [1000, None], [1000, None]]
# Start 2 coins [[1, None], [3, 0], [100, 0], [7, 1], [1000, None]]
# Start 3 coins [[1, None], [3, 0], [100, 0], [7, 1], [105, 2]]
# Start 4 coins [[1, None], [3, 0], [100, 0], [7, 1], [12, 3]]
# [[1, None], [3, 0], [100, 0], [7, 1], [12, 3]]