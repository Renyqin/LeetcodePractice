# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:
    def __init__(self):
        self.empty_node = "*"
    
    def bfs_to_string(self, root):
        tree_string = ""
        q = deque()
        q.append(root)
        while q:
            ele = q.popleft()
            if not ele:
                tree_string += self.empty_node
            else:
                tree_string += str(ele.val) + ","
                
                if ele.left:
                    q.append(ele.left)
                else:
                    q.append(None)
                if ele.right:
                    q.append(ele.right)
                else:
                    q.append(None)
        #print(tree_string)
        return tree_string
        
        
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        return self.bfs_to_string(root)
    
    
    def find_int_range(self, index, string):
        end_index = index
        for i in range(index, len(string)):
            if string[i] == "," or string[i] == self.empty_node:
                end_index = i
                value = int(string[index:end_index])
                return end_index+1, value
    
    def bfs_to_tree(self, data):
        q = deque()
        index, value = self.find_int_range(0,data)
        root = tree = TreeNode(value)
        q.append(tree)
        while q and index < len(data):
            ele = q.popleft()
            if data[index] != self.empty_node:
                
                index, value= self.find_int_range(index,data)
                ele.left = TreeNode(value)
                q.append(ele.left)
            else:
                index += 1
            if data[index] != self.empty_node:
                
                index, value= self.find_int_range(index,data)
                ele.right = TreeNode(value)
                q.append(ele.right)
            else:
                index+=1
        
        return root
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data)<=0:
            return None
        
        tree = self.bfs_to_tree(data)
        return tree
        
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))