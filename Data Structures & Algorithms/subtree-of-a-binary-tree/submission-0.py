# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        found_subroot = False
        def same(p, q):
            if p and not q or q and not p:
                return False
            if p and q and p.val != q.val:
                return False
            if not p and not q:
                return True
            if not same(p.left, q.left) or not same(p.right, q.right):
                return False
            return True
        stack = [root]
        while stack:
            if same(stack[-1], subRoot):
                return True
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False