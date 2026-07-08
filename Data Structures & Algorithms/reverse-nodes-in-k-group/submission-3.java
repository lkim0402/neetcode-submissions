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
        // 1. THE SCOUT
        ListNode ptr = head;
        int count = 0;
        while (ptr != null && count < k) {
            ptr = ptr.next;
            count++;
        }

        // If we found k nodes, we process them
        if (count == k) {
            // 2. THE LEAP: Recursively reverse the rest of the list
            // 'ptr' is at the k+1 node. 
            // The result 'reversedRest' is the head of the already-processed rest of the list.
            ListNode reversedRest = reverseKGroup(ptr, k);
            
            // 3. THE REVERSE: Standard reversal logic
            // We use 'reversedRest' as the starting 'prev' value.
            // This connects the end of our current group to the start of the next group.
            ListNode prev = reversedRest;
            ListNode curr = head;
            
            while (count > 0) {
                ListNode nextTemp = curr.next;
                curr.next = prev;  // Connect to the previous node (or the rest of the list)
                prev = curr;       // Move pointers
                curr = nextTemp;
                count--;
            }
            // After the loop, 'prev' is the new head of this reversed group
            return prev;
        }
        
        // If we didn't have k nodes (base case), just return the head as is
        return head;
    }
}