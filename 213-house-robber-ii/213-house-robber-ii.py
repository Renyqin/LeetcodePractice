class Solution:
    def sub_rob(self, nums):
        dp = []
        for index, ele in enumerate(nums):
            if index == 0:
                dp.append(ele)
            elif index == 1:
                dp.append(max(ele, dp[index-1]))
            else:
                dp.append(max(dp[index-1], ele+dp[index-2]))
                
        return dp[-1]
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        first_rob = self.sub_rob(nums[:-1])
        second_rob = self.sub_rob(nums[1:])
        return max(first_rob, second_rob)