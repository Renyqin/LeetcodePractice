class Solution:
    
    def helper(self, candidates, target, path, ans):
        for i in range(len(candidates)):
            
            if target <0:
                return 
            
            if target == 0:
                ans.append(path)
                return

            self.helper(candidates[i:], target-candidates[i], path+[candidates[i]], ans)
            
                    
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.helper(candidates, target, [], ans)
        return ans
        