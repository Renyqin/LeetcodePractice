class Solution:
    def helper(self, nums, subset, ans):
        ans.append(subset)
        for i in range(len(nums)):
            if i>0 and nums[i] ==nums[i-1]:
                continue
            
            self.helper(nums[i+1:], subset+[nums[i]], ans)
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        self.helper(nums, [], ans)
        return ans
        