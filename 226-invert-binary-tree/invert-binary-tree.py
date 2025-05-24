# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node: TreeNode) -> None:
            if not node:
                return

            invert(node.right)
            invert(node.left)
            node.left, node.right = node.right, node.left

        invert(root)
        return root