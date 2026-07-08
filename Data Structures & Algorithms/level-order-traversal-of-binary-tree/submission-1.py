# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        res = []
    
        def dfs(root, lvl):
            if root == None:
                return
            
            # add list per level
            if len(res) == lvl:
                res.append([])
            
            res[lvl].append(root.val)
            dfs(root.left, lvl + 1)
            dfs(root.right, lvl + 1)
        
        dfs(root,0)
        return res
