# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        idea
        - just kep doing dfs while passing the current val to child
        - in child compare current val and the passed value, 
          - if val > cur then return false?
        """
        neg_inf = float('-inf')
        return self.dfs(root, neg_inf)

    def dfs(self, node: Treenode, val: int) -> int:
        if not node: return 0

        curval = node.val
        isValid = 0 if curval < val else 1

        leftValid = self.dfs(node.left, max(curval, val))
        rightValid = self.dfs(node.right, max(curval, val))

        return isValid + leftValid + rightValid
    