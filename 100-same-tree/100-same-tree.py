# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False
            
        
        p_queue = deque()
        q_queue = deque()
        p_queue.append(p)
        q_queue.append(q)
        
        while p_queue:
            if not q_queue:
                return False
            p_ele = p_queue.popleft()
            q_ele = q_queue.popleft()
            
            if p_ele.val != q_ele.val:
                return False
            
            if (p_ele.left and q_ele.left == None) or (p_ele.right and q_ele.right == None) or\
               (p_ele.left == None and q_ele.left) or (p_ele.right == None and q_ele.right):
                    return False
            
            if p_ele.left:
                p_queue.append(p_ele.left)
                q_queue.append(q_ele.left)
            if p_ele.right:
                p_queue.append(p_ele.right)
                q_queue.append(q_ele.right)

                
        if q_queue:
            return False
                
        return True
        
        