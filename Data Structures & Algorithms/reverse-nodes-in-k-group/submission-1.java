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
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(0, head);
        ListNode groupPrev = dummy;

        while (true) {
            ListNode kth = getKth(groupPrev, k);
            if (kth == null) break;
            ListNode groupNext = kth.next;
            // shortcut: so that tail will connect immediately to 
            // next group head
            ListNode prev = kth.next; 
            ListNode cur = groupPrev.next; // head of cur group
            while (cur != groupNext) {
                ListNode tmp = cur.next;
                cur.next = prev;
                prev = cur;
                cur = tmp;
            }
            // updating groupPrev to new head
            // groupPrev is pointing to original head (1st iteration)!
            ListNode tmp = groupPrev.next;
            // update dummy.next to new head
            groupPrev.next = kth;
            // update groupPrev to original head, which is 
            // the node before our new group!
            groupPrev = tmp; 
        }
        return dummy.next;
    }

    private ListNode getKth(ListNode cur, int k) {
        while (cur != null && k > 0) {
            cur = cur.next;
            k--;
        }
        return cur;
    }
}
