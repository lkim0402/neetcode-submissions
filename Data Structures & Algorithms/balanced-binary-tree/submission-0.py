# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) != -1

    def dfs(self, root):
        if root == None:
            return 0

        leftMax = self.dfs(root.left)
        rightMax = self.dfs(root.right)

        if leftMax == -1 or rightMax == -1 : return -1
        if abs(leftMax - rightMax) > 1:
            return -1

        return 1 + max(leftMax, rightMax)

