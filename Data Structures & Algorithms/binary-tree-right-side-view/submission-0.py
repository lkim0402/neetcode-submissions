# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        use bfs
        - per level, assign the "last" node to each node (so it keeps updating)
        - add the last nodes to result list
        """
        if root == None: return []

        q = deque([root])
        res = []

        while q:
            qLen = len(q)
            last = None
            for i in range(qLen):
                cur = q.popleft()
                last = cur.val
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            res.append(last)
        
        return res
            
