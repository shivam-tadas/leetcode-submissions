# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0
        self.bstToGstHelper(root)
        return root

    def bstToGstHelper(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.bstToGstHelper(root.right)
        self.sum += root.val
        root.val = self.sum
        self.bstToGstHelper(root.left)