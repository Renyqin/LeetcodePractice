class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        sorted_nums = sorted(set(nums))
        max_consec = 1
        curr_consec = 1 
        i = 0
        j = i+1
        
        while j < len(sorted_nums):
            if sorted_nums[j] - sorted_nums[i] == 1:
                curr_consec += 1
            else:
                curr_consec = 1 
            
            max_consec = max(max_consec, curr_consec)
            
            i += 1
            j += 1
            
        return max_consec
            
            
        