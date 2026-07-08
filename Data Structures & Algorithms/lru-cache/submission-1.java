class Node { // for double linked list
    int key;
    int val;
    Node next;
    Node prev;
    
    public Node(int key, int val) {
        this.key = key;
        this.val = val;
    }
}

class LRUCache {

    int capacity;
    Map<Integer, Node> cache;
    Node left; // LRU
    Node right; // MRU

    public LRUCache(int capacity) {
        this.cache = new HashMap<>();
        this.capacity = capacity;

        // initializing dummy nodes
        this.left = new Node(0,0);
        this.right = new Node(0,0);
        this.left.next = this.right;
        this.right.prev = this.left; 
    }
    
    public int get(int key) {
        if (!cache.containsKey(key)) return -1;

        // remove Node and re-add to linkedlist (MRU)
        Node node = cache.get(key);
        remove(node);
        insert(node);
        return node.val;
    }
    
    public void put(int key, int value) {
        if (!cache.containsKey(key)) { // new element
            // 1) check capacity, 2) put new node
            if (cache.size() == capacity) {
                Node LRU = this.left.next;
                remove(LRU); // remove LRU
                cache.remove(LRU.key);
            }
            Node node = new Node(key, value);
            cache.put(key, node);
            insert(node);
            return;
        }
        
        // removing old node to dll
        Node node = cache.get(key);
        remove(node);
        // adding new node to dll
        Node newNode = new Node(key, value);
        cache.put(key, newNode);
        insert(newNode);
    }

    // ========= linkedlist remove, insert helper methods ==========

    public void remove(Node node) {
        Node next = node.next;
        Node prev = node.prev;
        prev.next = next;
        next.prev = prev;
        node.prev = null;
        node.next = null;
    }

    public void insert(Node node) {
        Node prev = right.prev;
        // left and node
        prev.next = node;
        node.prev = prev;
        // node and right
        node.next = right;
        right.prev = node;
    }
}
