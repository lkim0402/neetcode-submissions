class Node {
    int key;
    int val;
    Node prev;
    Node next;
    
    public Node(int key, int val) {
        this.key = key;
        this.val = val;
    }
}

class LRUCache {

    private int capacity;
    private HashMap<Integer, Node> cache;
    private Node left; //LRU
    private Node right;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        //dummy LRU and MRU Nodes
        this.left = new Node(0,0);
        this.right = new Node(0,0);
        this.left.next = this.right;
        this.right.prev = this.left;
    }
    
    public int get(int key) {
        if (cache.containsKey(key)) {
            Node node = cache.get(key);
            remove(node);
            insert(node);
            return node.val;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        // if exists in cache
        if (cache.containsKey(key)) {
            Node node = cache.get(key);
            node.val = value;
            // put it to the most recent
            remove(node);
            insert(node);
            return;
        }  
        
        if (cache.size() == capacity) {
            // if cache full, remove LRU
            Node LRU = this.left.next;
            remove(LRU);
            cache.remove(LRU.key);             
        }

        Node newNode = new Node(key, value);
        insert(newNode);
        cache.put(newNode.key, newNode);   
        
    }
    public void insert(Node node) {
        Node prev = right.prev;
        // node and prev
        prev.next = node;
        node.prev = prev;
        // node and right
        node.next = right;
        right.prev = node;
    }

    public void remove(Node node) {
        Node prev = node.prev;
        Node next = node.next;
        prev.next = next;
        next.prev = prev;
    }
}
