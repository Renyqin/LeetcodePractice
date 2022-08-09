class Solution:
    
    def helper(self, nums, path, ans, visited):
        if len(path) == len(nums):
            ans.append(path)
        
        
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.helper(nums, path+[nums[i]], ans, visited)
                visited.remove(i)
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()
        self.helper(nums, [], ans, visited)
        return ans