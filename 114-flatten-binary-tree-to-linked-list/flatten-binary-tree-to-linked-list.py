# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        preorder = []

        def traversePreOrder(node: TreeNode) -> None:
            if not node:
                return

            preorder.append(node.val)
            traversePreOrder(node.left)
            traversePreOrder(node.right)

        traversePreOrder(root)

        root.right = None
        root.left = None
        curr = root

        for i in range(1, len(preorder)):
            curr.right = TreeNode(preorder[i])
            curr = curr.right