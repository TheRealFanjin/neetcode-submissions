class Node:
    def __init__(self, val, key, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.node_map = {}
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, node):
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
    
    def remove(self, node):
        if node != self.head:
            node.prev.next = node.next
        else:
            if node.next:
                node.next.prev = None
            self.head = self.head.next
        if node != self.tail:
            node.next.prev = node.prev
        else:
            if node.prev:
                node.prev.next = None
            self.tail = self.tail.prev
    
    def update(self, node):
        self.remove(node)
        self.append(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            self.update(self.node_map[key])
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.update(self.node_map[key])
        else:
            self.cache[key] = value
            node = Node(value, key)
            self.node_map[key] = node
            self.append(node)
            self.size += 1
            if self.size > self.capacity:
                lru = self.head
                self.cache.pop(lru.key)
                self.node_map.pop(lru.key)
                self.remove(lru)
                del lru
                
