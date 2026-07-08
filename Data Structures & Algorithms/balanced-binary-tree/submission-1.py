# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)
        return self.balanced
        
    def dfs(self, root):
        if not root or not self.balanced:
            return 0
        
        leftMax = self.dfs(root.left)
        rightMax = self.dfs(root.right)

        if abs(leftMax - rightMax) > 1: # invalid
            self.balanced = False
        
        return 1 + max(leftMax, rightMax)