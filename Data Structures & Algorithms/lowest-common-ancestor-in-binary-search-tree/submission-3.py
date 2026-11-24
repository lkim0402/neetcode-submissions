# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        cur = root
        while cur:
            curVal = cur.val
            if p.val <= curVal <= q.val or q.val <= curVal <= p.val:
                return cur
            elif curVal < max(p.val, q.val):
                cur = cur.right
            else:
                # curVal > min(p.val, q.val)
                cur = cur.left
        
        return cur