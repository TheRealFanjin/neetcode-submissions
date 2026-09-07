# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')
        def dfs(root):
            nonlocal max_path
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            max_path = max(max_path, root.val + l + r,
                        root.val + l,
                        root.val + r,
                        root.val,
                        l if root.left else root.val,
                        r if root.right else root.val)
            return max( root.val + l,
                        root.val + r,
                        root.val)
        return max(dfs(root), max_path)