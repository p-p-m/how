# https://www.lintcode.com/problem/binary-tree-longest-consecutive-sequence-ii/description

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import collections


class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    _max = 0

    def longestConsecutive2(self, root):
        self.longest_subtree(root)
        return self._max

    def longest_subtree(self, root):
        if root is None:
            return 0, 0

        left_inc, left_dec = self.longest_subtree(root.left)
        right_inc, right_dec = self.longest_subtree(root.right)

        inc, dec = 1, 1
        if root.left is not None:
            if root.left.val == root.val + 1:
                inc = left_inc + 1
            if root.left.val == root.val - 1:
                dec = left_dec + 1
        if root.right is not None:
            if root.right.val == root.val + 1:
                inc = max(right_inc + 1)
            if root.right.val == root.val - 1:
                dec = max(dec, right_dec + 1)
        self._max = max(self._max, inc + dec - 1)
        return inc, dec

