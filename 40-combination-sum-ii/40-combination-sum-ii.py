class Solution:
    
    def helper(self, candidates, target, path, ans):
        if target < 0:
            return 
        if target == 0:
            ans.append(path)
        
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue

            self.helper(candidates[i+1:], target-candidates[i], path+[candidates[i]], ans)
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates = sorted(candidates)
        self.helper(candidates, target, [], ans)
        return ans