import pdb


class Node:
    def __init__(self, key=None, nxt=None, prev=None):
        self.key = key
        self.next = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # the format of key_dict shoud be {key: [value, count]}
        self.key_dict = {}
        self.head = Node()
        self.tail = self.head
        self.dict_len = 0
        
    def add_head(self, key):
        self.head.prev = Node(key, self.head)
        self.head = self.head.prev
        
        return 
    
    def remove_tail(self):
        self.tail = self.tail.prev
        return 
        
    
        
    def get(self, key: int) -> int:

        if key in self.key_dict:
            self.add_head(key)
            self.key_dict[key][1] += 1
            return self.key_dict[key][0]
        else:
            return -1
        
    
        
        
    def put(self, key: int, value: int) -> None:
        
        self.add_head(key)
        if self.tail.key == None:
            self.tail = self.head
         
        
        
        if key not in self.key_dict:

            while self.dict_len >= self.capacity:
                tail_key = self.tail.key
                self.remove_tail()
                self.key_dict[tail_key][1] -= 1

                if self.key_dict[tail_key][1] == 0:
                    self.key_dict.pop(tail_key)
                    self.dict_len -= 1


            
            self.key_dict[key] = [value, 1]
            self.dict_len += 1
        else:
            self.key_dict[key] = [value, self.key_dict[key][1]+1]
     
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)