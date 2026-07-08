/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

public class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode ptr = head;
        int count = 0;
        while (ptr != null && count < k) {
            ptr = ptr.next;
            count++;
        }

        if (count == k) {
            ListNode reversedRest = reverseKGroup(ptr, k);
            ListNode prev = reversedRest;
            ListNode curr = head;
            
            while (count > 0) {
                ListNode nextTemp = curr.next;
                curr.next = prev;  
                prev = curr;       
                curr = nextTemp;
                count--;
            }
            return prev;
        }
        
        return head;
    }
}