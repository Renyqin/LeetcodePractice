class Solution:
    
    def helper(self, nums, subset, ans):
        ans.append(subset)
        for i in range(len(nums)):
            self.helper(nums[i+1:], subset+[nums[i]], ans)
        
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.helper(nums,[], ans)
        return ans
    
    