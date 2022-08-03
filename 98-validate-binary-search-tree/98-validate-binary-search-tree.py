# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root, val_list):

        if not root:
            return 
        self.helper(root.left, val_list)
        val_list.append(root.val)
        self.helper(root.right, val_list)
        
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        val_list = []
        self.helper(root, val_list)
        #print(val_list)
        for i in range(len(val_list)-1):
            if val_list[i+1] <= val_list[i] :
                return False
            
        return True