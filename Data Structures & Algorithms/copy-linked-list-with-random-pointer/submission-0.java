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
        // hashmap -> old node : copy (new) node
        Map<Node, Node> nodeMap = new HashMap<>();
        // edge case: any null pointer's copy is null
        nodeMap.put(null, null);
        Node cur = head;
        while (cur != null) {
            Node node = new Node(cur.val);
            nodeMap.put(cur, node);
            cur = cur.next;
        }

        // linking everything together
        cur = head;
        while (cur != null) {
            Node copy = nodeMap.get(cur); // copy
            Node next = nodeMap.get(cur.next); // next
            Node random = nodeMap.get(cur.random); // random
            copy.next = next;
            copy.random = random;
            cur = cur.next;
        }

        return nodeMap.get(head);

    }
}
