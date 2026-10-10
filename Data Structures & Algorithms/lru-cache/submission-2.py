class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.LRU, self.MRU = Node(0,0), Node(0,0)
        self.LRU.next, self.MRU.prev = self.MRU, self.LRU
    
    def remove(self, node: Node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node: Node):
        prev = self.MRU.prev
        prev.next, node.prev = node, prev
        self.MRU.prev, node.next = node, self.MRU

    def get(self, key: int) -> int:
        if key in self.cache:   
            self.remove(self.cache[key]) #LRU
            self.insert(self.cache[key]) #MRU
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # if key exists, update
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru_node = self.LRU.next
            self.remove(lru_node)
            del self.cache[lru_node.key]

        
