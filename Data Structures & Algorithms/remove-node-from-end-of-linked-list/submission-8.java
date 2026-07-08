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
    public ListNode removeNthFromEnd(ListNode head, int n) {

        ListNode curr = head;
        ListNode runner = head;
        int num = 0;
        while (num < n) {
            runner = runner.next;
            num++;
        }
        // removing head
        if (runner == null) {
            return head.next;
        }

        // starting the loop
        while (runner.next != null) {
            runner = runner.next;
            curr = curr.next;
        }
        curr.next = curr.next.next;
        return head;


        // // get the length of list
        // ListNode temp = head;
        // int length = 1;
        // while (temp.next != null) {
        //     temp = temp.next;
        //     length++;
        // }

        // // removing node
        // int removeIndex = length - n;
        // if (length == 1) {
        //     head = null;
        // } else if (removeIndex == 0) {
        //     ListNode prevHead = head;
        //     ListNode newHead = head.next;
        //     prevHead.next = null;
        //     head = newHead;
        // } else {
        //     ListNode before = head; 
        //     int beforeIndex = removeIndex - 1;
        //     int start = 0;
        //     while (start < beforeIndex) {
        //         before = before.next;
        //         start++;
        //     }
        //     ListNode toRemove = before.next;
        //     ListNode after = toRemove.next;
        //     before.next = after;
        //     toRemove.next = null;
        // }
        // return head;
    }
}
