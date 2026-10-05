# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        start_roots = []
        bfs = deque([root])
        while bfs:
            curr = bfs.popleft()
            if curr.val == subRoot.val:
                start_roots.append(curr)
            if curr.left:
                bfs.append(curr.left)
            if curr.right:
                bfs.append(curr.right)
        if not start_roots:
            return False
        def dfs(root_node, subroot_node):
            if root_node and not subroot_node or subroot_node and not root_node:
                return False
            if not root_node and not subroot_node:
                return True
            if root_node.val != subroot_node.val:
                return False
            return dfs(root_node.left, subroot_node.left) and dfs(root_node.right, subroot_node.right)
        for start in start_roots:
            if dfs(start, subRoot):
                return True
        return False
        