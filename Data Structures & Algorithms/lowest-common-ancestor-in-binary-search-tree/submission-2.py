# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recur(node):
            if not node:
                return
            if node.val < p.val and node.val < q.val:
                return recur(node.right)
            elif node.val > p.val and node.val > q.val:
                return recur(node.left)
            else:
                return node
        return recur(root)