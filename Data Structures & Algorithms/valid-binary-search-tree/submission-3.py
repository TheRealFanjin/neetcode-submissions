# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True
        def recur(node, upper, lower):
            if not node:
                return
            if node.left and node.val <= node.left.val or node.right and node.val >= node.right.val or node.val >= upper or node.val <= lower:
                nonlocal valid
                valid = False
            else:
                recur(node.left, node.val, lower)
                recur(node.right, upper, node.val)
        recur(root, 1001, -1001)
        return valid
