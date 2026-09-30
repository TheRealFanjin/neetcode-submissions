# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recur(curr, min_value, max_value):
            if not curr:
                return True
            if not (min_value < curr.val < max_value):
                return False
            l = recur(curr.left, min_value, curr.val)
            r = recur(curr.right, curr.val, max_value)
            if l and r:
                return True
            return False
        return recur(root, -inf, inf)