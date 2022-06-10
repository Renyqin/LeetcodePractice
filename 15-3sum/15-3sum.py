class Solution:
    def twoSum(self, nums, target, ans, i):
        another_num = set()
        for j, num in enumerate(nums):
            #if j==i:
            #    continue
            new_triplets = tuple([num, target-num, -target])
            if num in another_num:
                ans.add(new_triplets)
            another_num.add(target-num)
        return ans
            
            
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()
        if len(nums) < 3:
            return []

        for i, num in enumerate(nums):
            sum_num = self.twoSum(nums[i+1:], -num, ans, i)

        
        

        return list(ans)