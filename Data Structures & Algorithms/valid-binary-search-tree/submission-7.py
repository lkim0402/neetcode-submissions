# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, low, high):
            if not node: return True
            
            # 1. Check if the CURRENT node violates the low/high limits passed from above
            if not (low < node.val < high):
                return False
            
            # 2. Pass the CURRENT node's value as the new limit for children
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        # Initial call: use float('-inf') and float('inf') to represent no limits
        return dfs(root, float('-inf'), float('inf'))

        