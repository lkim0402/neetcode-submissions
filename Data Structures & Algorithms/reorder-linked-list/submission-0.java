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
        // get other half the linkedlist with slow/fast pointer
        ListNode slow = head;
        ListNode fast = head.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        System.out.println(slow.val);
        
        // Reverse the last half
        ListNode second = slow.next;
        slow.next = null;
        ListNode prev = null;
        while (second != null) {
            ListNode next = second.next;
            second.next = prev;
            prev = second;
            second = next;
        }

        // merging both
        ListNode first = head;
        second = prev;
        while (second != null) {
            ListNode tempFirst = first.next;
            ListNode tempSec = second.next;
            first.next = second;
            second.next = tempFirst;
            first = tempFirst;
            second = tempSec;
        }

    }
}
