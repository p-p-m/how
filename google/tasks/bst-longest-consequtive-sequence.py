# https://www.lintcode.com/problem/binary-tree-longest-consecutive-sequence/description

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        nodes = [(root, 0)]
        for node, level in nodes:
            if node.left is not None:
                child_level = level + 1 if node.left.val == node.val + 1 else 0
                nodes.append((node.left, child_level))
            if node.right is not None and node.right.val == node.val + 1:
                child_level = level + 1 if node.right.val == node.val + 1 else 0
                nodes.append((node.right, child_level))
        return max(level for _, level in nodes)