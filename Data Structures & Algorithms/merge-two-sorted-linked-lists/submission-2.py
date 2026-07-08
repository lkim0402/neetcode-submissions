# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        cur = dummy_node
        cur1 = list1
        cur2 = list2

        while (cur1 != None and cur2 != None):
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        
        if (cur1 != None):
            cur.next = cur1
        if (cur2 != None):
            cur.next = cur2
        
        return dummy_node.next

