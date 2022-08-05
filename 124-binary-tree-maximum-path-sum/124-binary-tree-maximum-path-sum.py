# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = float("-inf")
    
    def dfs(self, root):
        if not root:
            return 0
        
        current = root.val
        self.max_sum = max(current, self.max_sum)
        
        left_sum = self.dfs(root.left)
        self.max_sum = max(current + left_sum, self.max_sum)
        #self.max_sum = max(left_sum, self.max_sum)
        right_sum = self.dfs(root.right)
        self.max_sum = max(current + right_sum, self.max_sum)
        #self.max_sum = max(right_sum, self.max_sum)
        self.max_sum = max(current + left_sum + right_sum, self.max_sum)
        
        
        
        return max(current,  max(current+left_sum, current + right_sum))
        
    
    def maxPathSum(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        self.dfs(root)
        return self.max_sum