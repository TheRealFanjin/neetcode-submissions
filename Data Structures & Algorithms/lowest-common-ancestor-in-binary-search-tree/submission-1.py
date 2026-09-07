# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recur(root):
            nonlocal p
            nonlocal q
            largest = max(p.val, q.val)
            smallest = min(p.val, q.val)
            print(root.val)
            if smallest <= root.val <= largest:
                return root
            if largest < root.val:
                return recur(root.left)
            return recur(root.right)
        return recur(root)