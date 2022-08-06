class Solution:
    def helper(self, nums, subset, ans):
        ans.append(sorted(subset))
        for i in range(len(nums)):
            if sorted(subset+[nums[i]]) not in ans:
                self.helper(nums[i+1:], subset+[nums[i]], ans)
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.helper(nums, [], ans)
        return ans
        