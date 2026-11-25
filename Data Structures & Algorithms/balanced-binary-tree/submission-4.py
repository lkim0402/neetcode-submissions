# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.heightCheck(root) != -1
    
    # returns -1 if not balanced, height (int) if balanced
    def heightCheck(self, n):
        if not n: return 0
        
        heightl = self.heightCheck(n.left)
        heightr = self.heightCheck(n.right)

        # if any is -1 / current height is invalid, return -1
        if heightl == -1 or heightr == -1: return -1
        if abs(heightl - heightr) > 1: return -1

        return max(heightl, heightr) + 1



