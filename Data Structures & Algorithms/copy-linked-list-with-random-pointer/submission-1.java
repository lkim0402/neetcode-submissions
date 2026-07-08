/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        Node dummy = new Node(0);
        /*
            originalToCopy -> { original : copy }

            while head != null
              - make new node & add to new linkedlist
              - map.put(originalNode, copyNode)

            while head != null 
              - assign the next and random of the copy using head
              - 
        */

        Map<Node, Node> originalToCopy = new HashMap<>();
        Node cur = head;
        while (cur != null) {
            Node copy = new Node(cur.val);
            originalToCopy.put(cur, copy);
            cur = cur.next;
        }
        cur = head;
        while (cur != null) {
            Node copy = originalToCopy.get(cur);
            copy.next = originalToCopy.get(cur.next); // copy of cur.next
            copy.random = originalToCopy.get(cur.random); // copy of cur.random
            cur = cur.next;
        }
        return originalToCopy.get(head);
    }
}
