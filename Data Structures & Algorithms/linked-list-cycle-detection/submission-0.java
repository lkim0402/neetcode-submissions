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
    public boolean hasCycle(ListNode head) {
        ListNode curr = head;
        ListNode runner = head;

        if (head.next == null) {
            return false;
        }

        while (runner != null && runner.next != null) {
            curr = curr.next;
            runner = runner.next.next;
            if (runner == curr) {
                return true;
            }
        } 
        return false;
    }
}
