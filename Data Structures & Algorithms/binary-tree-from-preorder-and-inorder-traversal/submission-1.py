# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_hash = {}
        for i in range(len(inorder)):
            inorder_hash[inorder[i]] = i
        self.pre_idx = 0
        def recur(l, r):
            if l > r:
                return None
            val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(val)
            mid = inorder_hash[val]
            root.left = recur(l, mid - 1)
            root.right = recur(mid + 1, r)
            return root
        return recur(0, len(preorder) - 1)
