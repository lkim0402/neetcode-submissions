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

 /*
  1 1
  4 6 8
+   7 7 
  5 4 5  

- go thru the linkedlist, add
 - if the number is > 10, then subtract 10 from the number & make it the current value
 - and have a carry that adds to the next iteration
 */


class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode first = l1;
        ListNode second = l2;
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        int carry = 0;

        while (first != null || second != null) {
            int firstVal = (first != null) ? first.val : 0;
            int secondVal = (second != null) ? second.val : 0;
            int add = firstVal + secondVal + carry;
            if (add >= 10) {
                add -= 10;
                carry = 1;
            } else {
                carry = 0;
            }
            cur.next = new ListNode(add);
            cur = cur.next;
            first = (first == null) ? null : first.next;
            second = (second == null) ? null : second.next;
        }

        if (second == null && first == null && carry == 1) {
            cur.next = new ListNode(carry);
        }
        return dummy.next;
    }
}
