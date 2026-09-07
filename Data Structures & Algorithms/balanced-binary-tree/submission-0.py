# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def recur(root):
            if not root:
                return 0
            l_height = recur(root.left)
            r_height = recur(root.right)
            if abs(l_height - r_height) > 1:
                nonlocal balanced
                balanced = False
            return 1 + max(l_height, r_height)
        recur(root)
        return balanced