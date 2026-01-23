# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sumLeftLeaves = 0

        def traverse(curr: Optional[TreeNode]) -> None:
            if curr.left:
                traverse(curr.left)
                if not(curr.left.left or curr.left.right):
                    self.sumLeftLeaves += curr.left.val

            if curr.right:
                traverse(curr.right)
        
        traverse(root)
        return self.sumLeftLeaves