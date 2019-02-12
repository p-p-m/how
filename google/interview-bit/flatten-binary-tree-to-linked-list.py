# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        root = A
        self.move(root)
        return A

    def is_leaf(self, node):
        return node.left is None and node.right is None

    def move(self, node):
        if self.is_leaf(node):
            return node, node

        if node.left and node.right:
            l_start, l_end = self.move(node.left)
            r_start, r_end = self.move(node.right)

            node.right = l_start
            node.left = None
            l_start.left = None

            l_end.right = r_start
            l_end.left = None
            r_start.left = None

            r_end.right = None
            r_end.left = None

            return node, r_end

        if node.left is None:
            r_start, r_end = self.move(node.right)
            return node, r_end

        if node.right is None:
            l_start, l_end = self.move(node.left)

            node.right = l_start
            node.left = None
            return node, l_end
