# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, high):
            if node == None: return 0

            isValid = 1 if node.val >= high else 0
            
            leftValid = dfs(node.left, max(high, node.val))
            rightValid = dfs(node.right, max(high, node.val))
            return isValid + leftValid + rightValid 
            
        return dfs(root, float("-inf"))


            