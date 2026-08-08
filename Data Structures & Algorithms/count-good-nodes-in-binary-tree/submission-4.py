# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, high:int): 
            if not node: return 0
            curVal = node.val

            # current node check
            isValid = 1 if curVal >= high else 0

            maxHigh = max(high, curVal)
            # left node check
            leftValid = dfs(node.left, maxHigh)
            # right node check
            rightValid = dfs(node.right, maxHigh)

            return isValid + leftValid + rightValid
        
        return dfs(root, float("-inf"))



            