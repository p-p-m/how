
def gcd(x, y):
    while y:
       x, y = y, x % y
    return x



class Node:
    def __init__(self, c3, c2):
        if c3 != 0 and c2 != 0:
            _gcd = gcd(c3, c2)
            c3 = c3 / _gcd
            c2 = c2 / _gcd
        self.c3 = c3
        self.c2 = c2

    def multiply_p(self, p):
        return (3 * self.c3 * p + 2 * self.c2 * p) / (self.c3 + self.c2)

    def __repr__(self):
        return '{}-{}'.format(self.c3, self.c2)


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        dp = []
        first_row = [None]
        for i in range(1, A):
            first_row.append(Node(c3=1, c2=0))
        dp.append(first_row)
        second_row = [Node(c3=1, c2=0)]
        for i in range(1, A):
            second_row.append(self.get_node(second_row[i-1], dp[0][i]))
        dp.append(second_row)
        third_row = [Node(c3=1, c2=0)]
        for i in range(1, A):
            third_row.append(self.get_node(third_row[i-1], dp[1][i]))
        dp.append(third_row)
        return self.mult(dp)

    def _c3(self, l3, l2, u3, u2):
        return 2 * l3 * u3 + 2 * l3 * u2 + 2 * l2 * u3 + 3 * l2 * u2

    def _c2(self, l3, l2, u3, u2):
        return 4 * l3 * u3 + 4 * l3 * u2 + 4 * l2 * u3 + 3 * l2 * u2

    def get_node(self, lnode, unode):
        return Node(
            c3=self._c3(lnode.c3, lnode.c2, unode.c3, unode.c2),
            c2=self._c2(lnode.c3, lnode.c2, unode.c3, unode.c2),
        )

    def mult(self, dp):
        p = 4
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == j == 0:
                    continue
                node = dp[i][j]
                p = node.multiply_p(p)
        return p

s = Solution()
print s.solve(2)
