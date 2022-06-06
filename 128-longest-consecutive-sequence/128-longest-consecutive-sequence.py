class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hash_table = set()
        for num in nums:
            hash_table.add(num)
         
        maximum = 0 
        for num in nums:
            if num-1 not in hash_table:
                curr = 1
                while num+1 in hash_table:
                    curr += 1
                    num+=1
                    
                maximum = max(maximum, curr)

        return maximum
            
            
        