# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bfs = deque([root])
        res = []
        while bfs:
            curr_level = []
            for _ in range(len(bfs)):
                curr_node = bfs.popleft()
                if curr_node:
                    curr_level.append(curr_node.val)
                    bfs.append(curr_node.left)
                    bfs.append(curr_node.right)
            if curr_level:
                res.append(curr_level)
        return res