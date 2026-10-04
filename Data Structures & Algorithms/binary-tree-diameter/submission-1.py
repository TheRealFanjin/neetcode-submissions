# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            diam = left + right
            nonlocal max_diam
            if diam > max_diam:
                max_diam = diam
            return max(1 + left, 1 + right)
        dfs(root)
        return max_diam
            
        