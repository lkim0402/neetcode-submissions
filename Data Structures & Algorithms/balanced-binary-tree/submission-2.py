# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # in all comparisons we compare the max of left subtree and right subtree
        # if diff > 1, then return false?
        return self.dfs(root) != -1

    def dfs(self, node):
        if node == None: return 0

        leftMax = self.dfs(node.left)
        rightMax = self.dfs(node.right)

        if leftMax == -1 or rightMax == -1: return -1
        if abs(leftMax - rightMax) > 1: return -1

        return max(leftMax, rightMax) + 1
    