# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def iter(root):
            
            if not root or root.val is None:
                return 0
            elif not (root.left or root.right):
                return 1
            
            left_height = iter(root.left)
            right_height = iter(root.right)

            diameter = left_height + right_height
            self.max_diameter = max(diameter, self.max_diameter)
            return max(left_height, right_height) + 1

        iter(root)
        return self.max_diameter
        