# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node: return
        if not node.left and not node.right: return node

        temp = node.left
        node.left = node.right
        node.right = temp

        self.invertTree(node.left)
        self.invertTree(node.right)

        return node
        
