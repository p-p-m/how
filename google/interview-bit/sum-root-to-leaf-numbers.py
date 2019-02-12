# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, A):
        _sum = 0
        for number in self.bfs(A):
            _sum += number
        return _sum % 1003

    def bfs(self, A):
        A.number = str(A.val)
        queue = collections.deque([A])
        while queue:
            node = queue.popleft()
            number = node.number
            if node.left is not None:
                node.left.number = number + str(node.left.val)
                queue.append(node.left)
            if node.right is not None:
                node.right.number = number + str(node.right.val)
                queue.append(node.right)
            if node.left is None and node.right is None:
                yield int(number)

s = Solution()
s.sumNumbers()


