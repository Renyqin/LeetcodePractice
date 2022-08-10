class Solution:
    
    def helper(self, nums, path, ans):
        #print(path)
        if len(path) == len(nums):
            ans.append(path.copy())
        
        for i in range(len(nums)):
            if nums[i] not in path:
                path.append(nums[i])
                self.helper(nums, path, ans)
                path.remove(nums[i])
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()
        path = []
        self.helper(nums, path, ans)
        return ans