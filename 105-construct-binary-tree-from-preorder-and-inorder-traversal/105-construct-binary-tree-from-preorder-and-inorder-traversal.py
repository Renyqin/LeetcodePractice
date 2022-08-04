# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildSubTree(self, preorder, inorder, in_map, pre_left, pre_right, in_left, in_right):
        if pre_left > pre_right or in_left > in_right:
            return 
        
        root = TreeNode(preorder[pre_left])
        root.left = self.buildSubTree(preorder, inorder, in_map, 
                                      pre_left+1, pre_left+in_map[preorder[pre_left]]-in_left, 
                                      in_left, in_map[preorder[pre_left]]-1)
        root.right = self.buildSubTree(preorder, inorder, in_map, 
                                       pre_left+in_map[preorder[pre_left]]-in_left+1, pre_right, 
                                       in_map[preorder[pre_left]]+1, in_right)
        
        return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map = {}
        for index, ele in enumerate(inorder):
            in_map[ele] = index
            
        return self.buildSubTree(preorder, inorder, in_map, 0, len(preorder)-1, 0, len(inorder)-1)
        
        
        