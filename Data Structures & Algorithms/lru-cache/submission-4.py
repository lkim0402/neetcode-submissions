class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # int : Node

        self.left, self.right = Node(0,0), Node(0,0) # LRU, MRU
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node : Node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def insert(self, node : Node):
        prev = self.right.prev
        prev.next, node.prev = node, prev
        node.next, self.right.prev = self.right, node

    def get(self, key: int) -> int:
        # update MRU
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        # check if capacity exceeded
        if len(self.cache) > self.cap:
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[lru_node.key]
