# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        res = []

        def dfs(root, lvl):
            if root is None:
                return
            
            if len(res) == lvl:
                res.append(root.val)

            dfs(root.right, lvl + 1)
            dfs(root.left, lvl + 1)

        dfs(root, 0)
        return res