# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res = []
        level_count = 1
        curr_level = 0
        next_level = 0
        while q:
            node = q.popleft()
            curr_level += 1
            if node.left:
                q.append(node.left)
                next_level += 1
            if node.right:
                q.append(node.right)
                next_level += 1
            if curr_level == level_count:
                res.append(node.val)
                curr_level = 0
                level_count = next_level
                next_level = 0
        return res