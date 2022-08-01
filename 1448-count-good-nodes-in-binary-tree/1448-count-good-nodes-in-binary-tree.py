# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.good_nodes = 0
    
    def helper(self, root, prev_max_val):
        if root == None:
            return 
        if root.val >= prev_max_val:
            self.good_nodes += 1
            prev_max_val = root.val
        
        self.helper(root.left, prev_max_val)
        self.helper(root.right, prev_max_val)
        
        
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        prev_max_val = root.val
        self.helper(root, prev_max_val)
        return self.good_nodes