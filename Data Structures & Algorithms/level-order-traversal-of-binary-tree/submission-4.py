# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        visited = deque([])
        if root != None: visited.append(root)

        while visited:
            lvl = []
            for i in range(len(visited)):
                node = visited.popleft()
                if node.left != None: visited.append(node.left)
                if node.right != None: visited.append(node.right)
                lvl.append(node.val)
            res.append(lvl)
        
        return res
                