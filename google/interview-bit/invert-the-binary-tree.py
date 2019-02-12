import collections

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        queue = collections.deque([A])
        while queue:
            node = queue.popleft()
            node.right, node.left = node.left, node.right
            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)
        return A
