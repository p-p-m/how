# https://www.lintcode.com/problem/binary-search-tree-iterator/description

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.root = root

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        return bool(self.root)

    """
    @return: return next node
    """
    def next(self):
        while self.root.left:
            self.root = self.rotate_right(self.root)
        result = self.root.val
        self.root = self.root.right
        return result

    def rotate_right(self, root):
        if not root.left:
            raise Exception('cannot rotate right without left element')
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        return new_root
