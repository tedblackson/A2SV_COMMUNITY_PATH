class LRUCache:

    def __init__(self, capacity: int):
        
        self.left, self.right = ListNode(), ListNode()
        self.left.next, self.right.prev = self.right, self.left
        self.capacity = capacity
        self.cache = {}
        
        
        
        

    def get(self, key: int) -> int:
        if key in self.cache:
            cur = self.cache[key]
            self.remove(self.cache[key])
            self.insert(cur)
            return self.cache[key].val
        return -1

        
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            cur = self.cache[key]
            self.remove(cur)
            self.insert(cur)
            cur.val = value
        elif len(self.cache) < self.capacity:
            node = ListNode(key, value)
            self.insert(node)
        else:
            
            lru = self.right.prev
            node = ListNode(key, value)
            del self.cache[lru.key]
            self.remove(lru)
            self.insert(node)
            
            
    
    def insert(self, node):
        mru = self.left.next
        node.next = mru
        mru.prev = node
        self.left.next = node
        node.prev = self.left
        self.cache[node.key] = node
        
    
    def remove(self, node):
        prev , nxt = node.prev, node.next
        
        prev.next , nxt.prev = nxt, prev
        

        
        
        

class ListNode:
    def __init__(self, key=-1, val=-1):
        self.key, self.val = key, val
        self.prev = self.next = None
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)