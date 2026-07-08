# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        go thru each node
        if node is equal to subroot node, do dfs on it
        """

        if not subRoot:
            return True
        if not root:
            return False
        
        if self.dfs(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def dfs(self, cur1, cur2):
        if not cur1 and not cur2:
            return True
        elif cur1 and cur2 and cur1.val == cur2.val:
            return self.dfs(cur1.left, cur2.left) and self.dfs(cur1.right, cur2.right)
        else:
            return False


