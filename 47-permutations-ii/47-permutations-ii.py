class Solution:
    
    def backtrack(self, nums, ans, path, visited,  used):
        #print(path)
        if len(path) == len(nums):
            ans.append(path)
            
        for i in range(len(nums)):
            
            if i>0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            
            if i not in visited:
                visited.add(i)
                used[i] = True
                self.backtrack(nums, ans, path+[nums[i]], visited, used)
                visited.remove(i)
                used[i] = False
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()
        used = [False] * len(nums)
        self.backtrack(sorted(nums), ans, [], visited, used)
        return ans