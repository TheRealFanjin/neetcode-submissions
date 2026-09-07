# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def iter(root, depth_count):
            if not root or root.val is None or not (root.left or root.right):
                return depth_count
            return max(iter(root.left, depth_count + 1), iter(root.right, depth_count + 1))
        
        return iter(root, 1)
        