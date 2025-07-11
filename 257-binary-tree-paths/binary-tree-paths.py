# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        if root == None:
            return paths

        def DFS(node: TreeNode, currPath: str) -> None:
            if node.left == None and node.right == None:
                if currPath == '':
                    currPath += str(node.val)
                else:
                    currPath += '->' + str(node.val)
                paths.append(currPath)
                return

            if node.left:
                if currPath == '':
                    DFS(node.left, currPath + str(node.val))
                else:
                    DFS(node.left, currPath + '->' + str(node.val))

            if node.right:
                if currPath == '':
                    DFS(node.right, currPath + str(node.val))
                else:
                    DFS(node.right, currPath + '->' + str(node.val))

        DFS(root, '')
        return paths