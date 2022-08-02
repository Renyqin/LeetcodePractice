# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.kth = 0
        self.ans = None
        
    def helper(self, root, k):
        if root == None:
            return 
        
        self.helper(root.left, k)
        
        self.kth += 1
        if self.kth == k:
            self.ans = root.val
            return 
        
        self.helper(root.right, k)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root == None or k <= 0 :
            return 
        self.helper(root, k)
        return self.ans
        
        