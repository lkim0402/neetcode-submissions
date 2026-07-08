# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None: return 0

        res = 0

        def dfs(root, upperVal):
            nonlocal res
            if root == None:
                return
            if root.val >= upperVal:
                res += 1
            
            dfs(root.left, max(root.val, upperVal))
            dfs(root.right, max(root.val, upperVal))
        
        dfs(root, root.val)
        return res
        