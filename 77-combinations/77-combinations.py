class Solution:
    
    def backtrack(self, n, k, path, ans, startIndex):
        #print(path)
        if len(path) == k:
            ans.append(path.copy())
        
        for i in range(startIndex, n+1):
            if i not in path:
                path.append(i)
                self.backtrack(n, k , path, ans, i)
                path.pop()
            
        
        
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.backtrack(n, k, [], ans, 1)
        return ans