class Node:
    def __init__(self, key=None, value=None, nxt=None, prev=None):
        self.key = key
        self.value = value
        self.nxt = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.prev = self.tail
        self.tail.next = self.head
        self.node_dict = {}
        
    def insert_to_head(self, node):
        node.prev = self.head.prev
        node.next = self.head
        self.head.prev.next = node
        self.head.prev = node
        
    
    def remove_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        #node.next = None
        #node.prev = None
      

    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)

        if key not in self.node_dict:

            self.node_dict[key] = new_node
            self.insert_to_head(new_node)
            
            if len(self.node_dict) > self.capacity:
                tail_node = self.tail.next
                self.remove_node(tail_node)
                self.node_dict.pop(tail_node.key)
            
        else:
            node = self.node_dict[key]
            node.value = value
            self.remove_node(node)
            self.insert_to_head(node)
            


    def get(self, key: int) -> int:
        if key in self.node_dict:
            node = self.node_dict[key]
            value = node.value
            self.remove_node(node)
            self.insert_to_head(node)
            return value
            
        else:
            return -1
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)