# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.array = []
        self.dfs(root)
        self.count = 0 
        
    def dfs(self, root):
        if not root:
            return None
        
        self.dfs(root.left)
        self.array.append(root.val)
        self.dfs(root.right)
        

    def next(self) -> int:
        ans = self.array[self.count]
        self.count += 1
        return ans
        

    def hasNext(self) -> bool:
        return self.count<len(self.array)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()