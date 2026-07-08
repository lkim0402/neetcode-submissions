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

class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;
        ListNode slow = head;
        ListNode fast = head.next;

        // use slow & fast pointer to get half
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode head2 = slow.next;
        slow.next = null;

        // reverse 2nd half
        ListNode prev = null;
        while (head2 != null) {
            ListNode next = head2.next;
            head2.next = prev;
            prev = head2;
            head2 = next;
        }

        // merge 1st and 2nd halves
        ListNode temp1 = head;
        ListNode temp2 = prev; // should be prev because head2 will be null
        
        // while (temp1 != null && temp2 != null) {
        while (temp2 != null) { // check only for 2nd, it will always run out first
            ListNode next1 = temp1.next;
            ListNode next2 = temp2.next;
            temp1.next = temp2;
            temp2.next = next1;
            temp1 = next1;
            temp2 = next2;
        }

    }
}
