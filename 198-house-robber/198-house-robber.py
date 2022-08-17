class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = []
        for index, ele in enumerate(nums):
            if index == 0:
                dp.append(ele)
            elif index == 1:
                dp.append(max(dp[0], ele))  
            else: 
                #print(index)
                #print("dp_val")
                #print(dp[index-2])
                new_ele = max(ele+dp[index-2], dp[index-1])
                dp.append(new_ele)
                
        #print(dp)
            
        return max(dp)