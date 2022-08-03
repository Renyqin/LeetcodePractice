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
        q.append([root,0])
        while q:
            node, level = q.popleft()
            if (q and q[0][1] > level) or not q:
                self.ans.append(node.val)
            
            
            
            if node.left:
                q.append([node.left, level+1])
            if node.right:
                q.append([node.right, level+1])
        
        
    
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return self.ans
        self.bfs(root)
        return self.ans
        