# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.maxDepth(root)
        return self.diameter

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        left = self.maxDepth(root.left) if root.left else 0
        right = self.maxDepth(root.right) if root.right else 0
        self.diameter = max(self.diameter, left + right)
        return 1 + max(left, right)