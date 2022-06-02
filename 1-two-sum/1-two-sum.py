class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        another_num = {}
        for index, num in enumerate(nums):
            if num in another_num:
                return [another_num[num], index]
            
            another_num[target - num] = index 
            
            
        