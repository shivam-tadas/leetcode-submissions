# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
            
        path = []

        def paths(currSum: int, currPath: List[int], currNode: TreeNode) -> None:
            if not (currNode.left or currNode.right):
                if currSum == targetSum:
                    path.append(currPath)
                return

            if currNode.left:
                newNode = currNode.left
                paths(currSum + newNode.val, currPath + [newNode.val], newNode)

            if currNode.right:
                newNode = currNode.right
                paths(currSum + newNode.val, currPath + [newNode.val], newNode)

        paths(root.val, [root.val], root)
        return path