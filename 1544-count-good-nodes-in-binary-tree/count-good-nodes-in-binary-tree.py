# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNode = 0

        def goodNodesHelper(node: TreeNode, path: List[int], maxPathVal: int) -> None:
            if not node:
                return

            if node.val >= maxPathVal:
                self.goodNode += 1
        
            if node.left:
                newMaxPathVal = maxPathVal if node.left.val <= maxPathVal else node.left.val
                goodNodesHelper(node.left, path + [node.val], newMaxPathVal)
            
            if node.right:
                newMaxPathVal = maxPathVal if node.right.val <= maxPathVal else node.right.val
                goodNodesHelper(node.right, path + [node.val], newMaxPathVal)

        goodNodesHelper(root, [], root.val)
        return self.goodNode