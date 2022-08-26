class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [nums[0]]
        neg_dp = [nums[0]]
        for i in range(1, len(nums)):
            maximum = max([nums[i] * dp[i-1], nums[i] * neg_dp[i-1], nums[i]]) 
            minimum = min([nums[i] * dp[i-1], nums[i] * neg_dp[i-1], nums[i]]) 
            dp.append(maximum)
            neg_dp.append(minimum)
            
                
 
        return max(dp)