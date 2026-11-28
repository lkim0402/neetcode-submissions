class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.keyNode = {} # hashmap
        self.cap = capacity

        # initializing the dll
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        # get the value from keyNode Map
        if key in self.keyNode:
            n = self.keyNode[key]
            val = n.value
            # update the LRU (head)
            self.remove(n)
            self.insert(n)
            # return the value
            return val
        return -1
    
    def remove(self, n):
        prev, next = n.prev, n.next
        prev.next, next.prev = next, prev

    def insert(self, n):
        # adding next to end
        prev = self.tail.prev
        prev.next, n.prev = n, prev
        # updating LFU (tail)
        self.tail.prev, n.next = n, self.tail

    def put(self, key: int, value: int) -> None:
        # if key exists alr
        if key in self.keyNode:
            n = self.keyNode[key]
            # update the value
            n.value = value
            self.remove(n)
            self.insert(n)
            return
        
        n = Node(key, value)
        # if capacity is full
        if len(self.keyNode) == self.cap:
            # remove head (LRU)
            toRemove = self.head.next
            self.remove(toRemove) # remove from ll
            del self.keyNode[toRemove.key] # remove from dict

        # update tail
        self.insert(n)
        self.keyNode[key] = n



        
