# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        bfs_q = [root]
        res = [[]]
        curr_levels = 1
        next_levels = 0
        while bfs_q:
            curr = bfs_q.pop(0)
            res[-1].append(curr.val)
            curr_levels -= 1
            if curr.left:
                bfs_q.append(curr.left)
                next_levels += 1
            if curr.right:
                bfs_q.append(curr.right)
                next_levels += 1
            if not curr_levels and bfs_q:
                curr_levels = next_levels
                next_levels = 0
                res.append([])
                continue
        return res
