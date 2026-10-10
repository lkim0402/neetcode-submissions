# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.heightCheck(root) != -1
    
    def heightCheck(self, node: TreeNode) -> int:
        if not node: return 0

        l = self.heightCheck(node.left)
        r = self.heightCheck(node.right)

        if l == -1 or r == -1: return -1
        if abs(l - r) > 1: return -1

        return max(l, r) + 1