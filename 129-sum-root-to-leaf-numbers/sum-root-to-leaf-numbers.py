# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.nums = []
        self.root = root
        self.sumNumbersDFS(root, str(root.val))
        return sum(self.nums)

    def sumNumbersDFS(self, node: Optional[TreeNode], currNum: str) -> None:
        if not (node.left or node.right):
            print("Added", currNum)
            self.nums.append(int(currNum))
            return

        if node.left:
            self.sumNumbersDFS(node.left, currNum + str(node.left.val))

        if node.right:
            self.sumNumbersDFS(node.right, currNum + str(node.right.val))