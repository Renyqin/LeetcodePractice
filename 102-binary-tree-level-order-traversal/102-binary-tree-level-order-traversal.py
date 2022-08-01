# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def __init__(self):
        self.ans = []
        
    def bfs(self, root):
        q = deque()
        q.append([root, 0])
        prev_level = 0
        temp = []
        while q:
            ele = q.popleft()
            level = ele[1]
            node = ele[0]
            if level != prev_level:
                self.ans.append(temp)
                temp = [node.val]
                prev_level = level
            else:
                temp.append(node.val)
            if node.left:
                q.append([node.left, level+1])
            if node.right:
                q.append([node.right, level+1])
                
        self.ans.append(temp)
        return 
        
        
        
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return self.ans
        self.bfs(root)
        return self.ans